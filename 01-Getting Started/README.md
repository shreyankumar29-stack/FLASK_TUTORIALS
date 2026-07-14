# 🚀 Flask Tutorial by Corey Schafer – Part 1: Getting Started

## 📌 Objective

In this part, we learn the fundamentals of Flask and build our first web application.

---

## 📖 What is Flask?

Flask is a **lightweight (micro) web framework** written in Python that helps developers build web applications quickly and efficiently.

It provides essential features such as:

- URL Routing
- HTTP Request Handling
- Template Rendering
- Session Management
- Error Handling

Additional features can be added using extensions like:

- Flask-SQLAlchemy (Database)
- Flask-WTF (Forms)
- Flask-Login (Authentication)
- Flask-Bcrypt (Password Hashing)

---

## 🔹 Why is Flask called a Micro Framework?

The term **Micro** does **not** mean Flask is limited.

It means Flask only includes the core functionality required for web development while allowing developers to choose additional libraries based on project requirements.

### Built-in Features

- Routing
- Request & Response Handling
- Jinja2 Template Engine
- Sessions
- Cookies

---

## 📦 Installation

Install Flask using pip:

```bash
pip install flask
```

Verify the installation:

```bash
pip show flask
```

---

## 🏗️ Creating a Flask Application

```python
from flask import Flask

app = Flask(__name__)
```

### Explanation

- `Flask` is a class.
- `app` is an instance (object) of the Flask application.

---

## ❓ Why do we use `__name__`?

```python
app = Flask(__name__)
```

The `__name__` variable tells Flask where the application is located.

Flask uses this information to locate:

- Templates
- Static files
- Configuration files
- Other project resources

---

## 🌐 Routing

Routing maps a URL to a Python function.

Example:

```python
@app.route("/")
def home():
    return "Hello World"
```

When a user visits:

```
http://127.0.0.1:5000/
```

Flask executes the `home()` function and returns its response.

---

## 🎯 Multiple Routes

A single function can respond to multiple URLs.

```python
@app.route("/")
@app.route("/home")
def home():
    return "Home Page"
```

Both URLs call the same function.

---

## 🎨 Decorators

```python
@app.route("/")
```

`@app.route()` is a **decorator**.

A decorator modifies or extends the behavior of a function without changing its original implementation.

Flask uses decorators to register routes.

---

## 🔄 Request Flow

```text
Browser
    │
    ▼
HTTP Request
    │
    ▼
Flask Application
    │
    ▼
Route Matching
    │
    ▼
Python Function
    │
    ▼
Response
    │
    ▼
Browser
```

---

## ▶️ Running the Application

```python
if __name__ == "__main__":
    app.run(debug=True)
```

### Why use `if __name__ == "__main__"`?

It ensures that the Flask server starts **only when the file is executed directly**, not when it is imported into another Python module.

---

## 🐞 Debug Mode

```python
app.run(debug=True)
```

### Benefits

- Automatically reloads the server after code changes.
- Displays detailed error messages.
- Speeds up development.

> **Note:** Never enable Debug Mode in production.

---

## 📂 Project Structure

```text
project/
│
├── app.py
└── venv/
```

---

## 💻 Final Code

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ⚠️ Common Beginner Mistakes

### 1. Forgetting `@app.route()`

```python
def home():
```

The function will never be accessible through the browser.

---

### 2. Forgetting `return`

```python
def home():
    print("Hello")
```

Flask expects every route to return a response.

---

### 3. Incorrect Route

❌ Wrong

```python
@app.route("home")
```

✅ Correct

```python
@app.route("/home")
```

---

### 4. Running without Debug Mode

Without Debug Mode, every code change requires manually restarting the server.

---

## 🎤 Interview Questions

### What is Flask?

Flask is a lightweight Python web framework used to develop web applications.

---

### Why is Flask called a Micro Framework?

Because it provides only the core functionality required for web development while allowing additional features through extensions.

---

### What is Routing?

Routing maps URLs to Python functions.

---

### What is a Decorator?

A decorator modifies or extends the behavior of a function. In Flask, decorators are used to register URL routes.

---

### Why do we use `__name__`?

It helps Flask locate templates, static files, and other project resources.

---

### Why do we use Debug Mode?

Debug Mode automatically reloads the application after code changes and displays detailed error messages during development.

---

## 📝 Key Takeaways

- Learned what Flask is and why it is called a micro framework.
- Created the first Flask application.
- Understood routing and decorators.
- Learned the purpose of `__name__`.
- Explored the request-response cycle.
- Used Debug Mode for development.

---

## 📌 Modern Flask Notes

✅ Corey Schafer's Part 1 code is fully compatible with **Flask 3.x**.

No code changes are required in this part.