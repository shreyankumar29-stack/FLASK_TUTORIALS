# Flask Templates — A Detailed Explanation

## What are Flask Templates?

Flask uses the **Jinja2** templating engine to generate dynamic HTML. Instead of hardcoding data into HTML files, you write templates with placeholders that Flask fills in with Python data at request time. This lets you separate your application logic (Python) from your presentation layer (HTML).

---

## Basic Setup

Flask looks for templates in a folder named `templates/` by default, and static assets (CSS/JS/images) in a folder named `static/`:

```
your_project/
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Yassu", marks=85)
```

---

## Jinja2 Syntax Basics

Jinja2 has three main delimiter types:

| Syntax | Purpose |
|---|---|
| `{{ ... }}` | Print a variable or expression |
| `{% ... %}` | Control structures (if, for, blocks, etc.) |
| `{# ... #}` | Comments (not rendered in output) |

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head><title>Attendance Calculator</title></head>
<body>
    <h1>Hello, {{ name }}!</h1>

    {% if marks >= 75 %}
        <p style="color:green;">Attendance is sufficient.</p>
    {% else %}
        <p style="color:red;">Attendance is below required threshold.</p>
    {% endif %}

    <ul>
    {% for subject in subjects %}
        <li>{{ subject }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

Passing a list from the view function:
```python
@app.route('/subjects')
def subjects():
    subject_list = ["DBMS", "Python", "Discrete Math"]
    return render_template('index.html', subjects=subject_list, name="Yassu", marks=80)
```

---

## Template Inheritance

Instead of repeating the same navbar/footer in every page, create a **base template** that other pages extend.

**templates/base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>My Attendance App</nav>

    <div class="content">
        {% block content %}{% endblock %}
    </div>

    <footer>© 2026 Yassu</footer>
</body>
</html>
```

**templates/dashboard.html**
```html
{% extends "base.html" %}

{% block title %}Dashboard{% endblock %}

{% block content %}
    <h2>Welcome back, {{ name }}</h2>
    <p>Your current attendance: {{ attendance }}%</p>
{% endblock %}
```

Any page that extends `base.html` automatically gets the shared layout — you only fill in the `{% block %}` sections.

---

## Linking Static Files

Always use `url_for()` instead of hardcoding paths, so links don't break if the folder structure changes:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/app.js') }}"></script>
<img src="{{ url_for('static', filename='images/logo.png') }}">
```

## Linking Between Routes

```html
<a href="{{ url_for('home') }}">Home</a>
<a href="{{ url_for('subjects') }}">Subjects</a>
```

This generates the correct URL for the route function name (`home`, `subjects`) — so if the URL rule changes later, the links update automatically without editing every template.

---

## Useful Jinja2 Filters

Filters transform a variable's output using the pipe `|` symbol:

```html
{{ name | upper }}            <!-- YASSU -->
{{ attendance | round(2) }}   <!-- rounds a number -->
{{ subjects | length }}       <!-- count of a list -->
{{ description | truncate(50) }}
{{ "" if attendance is none else attendance }}
```

Common built-in filters: `upper`, `lower`, `title`, `length`, `round`, `default`, `truncate`, `join`, `first`, `last`, `safe` (marks a string as trusted HTML).

---

## Passing Dictionaries / Objects

```python
@app.route('/student/<int:roll_no>')
def student_profile(roll_no):
    student = {"name": "Yassu", "roll": roll_no, "attendance": 82}
    return render_template('profile.html', student=student)
```

```html
<h2>{{ student.name }}</h2>
<p>Roll No: {{ student.roll }}</p>
<p>Attendance: {{ student.attendance }}%</p>
```

---

## Macros (Reusable Template Snippets)

Macros work like functions for templates — useful when the same HTML block repeats with different data.

**templates/_macros.html**
```html
{% macro render_card(title, value) %}
<div class="card">
    <h3>{{ title }}</h3>
    <p>{{ value }}</p>
</div>
{% endmacro %}
```

**templates/dashboard.html**
```html
{% extends "base.html" %}
{% from "_macros.html" import render_card %}

{% block content %}
    {{ render_card("Attendance", "82%") }}
    {{ render_card("Total Classes", "120") }}
{% endblock %}
```

---

## Practical Example: Attendance Calculator Pattern

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    total_classes = int(request.form['total'])
    attended = int(request.form['attended'])
    percentage = (attended / total_classes) * 100
    return render_template('result.html', percentage=round(percentage, 2))

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/result.html**
```html
{% extends "base.html" %}
{% block content %}
    <h2>Your Attendance: {{ percentage }}%</h2>
    {% if percentage < 75 %}
        <p class="warning">You need to attend more classes!</p>
    {% else %}
        <p class="success">You're meeting the attendance requirement.</p>
    {% endif %}
{% endblock %}
```

---

## Best Practices

- Keep templates focused on presentation — avoid heavy logic in Jinja2; compute values in your Flask view functions instead.
- Use template inheritance (`base.html`) to avoid repeating layout code.
- Always use `url_for()` for static files and route links.
- Escape user input by default (Jinja2 auto-escapes HTML); only use the `| safe` filter when you fully trust the content.
- Organize templates into subfolders for larger apps (e.g., `templates/auth/login.html`, `templates/dashboard/index.html`).

---

## Summary

Flask's templating system, powered by Jinja2, allows Python data to be rendered dynamically inside HTML using `{{ }}`, `{% %}`, and `{# #}` syntax. Combined with template inheritance, filters, macros, and `url_for()`, it enables clean, DRY, and maintainable web application front-ends — making it a natural fit for projects like a Flask-based Smart Class Attendance Calculator.

---

*Reference: [flask.palletsprojects.com/en/stable/templating](https://flask.palletsprojects.com/en/stable/templating/)*
