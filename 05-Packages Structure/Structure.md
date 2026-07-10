# Flask Tutorial - Part 5: Package Structure

These are my notes while learning **Package Structure in Flask** from the **Corey Schafer Flask Tutorial Series**.

---

# 📚 Topics Covered

- Why Package Structure is Important
- Converting a Flask Project into a Package
- Creating `__init__.py`
- Separating Routes, Models and Forms
- Creating `run.py`
- Package Imports
- Organizing Flask Applications

---

# ❓ Why Package Structure?

Initially, the Flask application was written inside a single file:

```text
flaskblog.py
```

As the project grows, keeping everything inside one file becomes difficult.

Problems:

- Difficult to maintain
- Hard to read
- Mixing routes, models and forms
- Poor scalability

To solve this, the application is converted into a **Python Package**.

---

# 📦 What is a Python Package?

A package is simply a folder containing an

```text
__init__.py
```

file.

The `__init__.py` file tells Python that this folder should be treated as a package.

Example:

```text
flaskblog/
    __init__.py
```

---

# 📂 New Project Structure

```text
05-Packages Structure/

│── run.py
│
└── flaskblog/
    │── __init__.py
    │── routes.py
    │── models.py
    │── forms.py
    │
    ├── static/
    │   └── main.css
    │
    └── templates/
        ├── about.html
        ├── home.html
        ├── layout.html
        ├── login.html
        └── register.html
```

---

# 📄 Purpose of Each File

## run.py

Entry point of the application.

Used to start the Flask server.

```python
from flaskblog import app

if __name__ == "__main__":
    app.run(debug=True)
```

Run application:

```bash
python run.py
```

---

## __init__.py

Initializes the Flask application.

Responsibilities:

- Create Flask app
- Configure SECRET_KEY
- Configure Database
- Initialize SQLAlchemy
- Import routes

Example:

```python
app = Flask(__name__)

db = SQLAlchemy(app)
```

---

## routes.py

Contains all Flask routes.

Example:

```python
@app.route("/")
def home():
    return render_template("home.html")
```

Responsibilities:

- Home Route
- About Route
- Register Route
- Login Route

---

## models.py

Contains database models.

Example:

```python
class User(db.Model):
```

```python
class Post(db.Model):
```

Responsibilities:

- Define Database Tables
- Relationships
- Primary Keys
- Foreign Keys

---

## forms.py

Contains all Flask-WTF forms.

Example:

```python
class RegistrationForm(FlaskForm):
```

```python
class LoginForm(FlaskForm):
```

---

## templates/

Contains HTML templates.

Examples:

- layout.html
- home.html
- about.html
- register.html
- login.html

---

## static/

Contains static files.

Examples:

- CSS
- Images
- JavaScript

---

# 🔄 Code Separation

Old Structure

```text
flaskblog.py

- Routes
- Models
- Forms
- Configurations
```

↓

New Structure

```text
__init__.py
    ↓

routes.py

models.py

forms.py
```

Everything now has its own responsibility.

---

# 📥 Package Imports

Instead of writing:

```python
from forms import RegistrationForm
```

Use:

```python
from flaskblog.forms import RegistrationForm
```

or

```python
from .forms import RegistrationForm
```

Similarly,

```python
from flaskblog.models import User, Post
```

or

```python
from .models import User, Post
```

Relative imports (`.`) are commonly used inside a package.

---

# 🚀 Running the Application

Instead of

```bash
python flaskblog.py
```

the application is started using

```bash
python run.py
```

because the Flask app is now inside the `flaskblog` package.

---

# ✅ Benefits of Package Structure

- Cleaner project
- Easier to maintain
- Better organization
- Easy to scale
- Reusable code
- Follows Flask best practices
- Suitable for large applications

---

# 📌 Files Moved

| Old File | New Location |
|----------|--------------|
| flaskblog.py | Split into multiple files |
| Routes | routes.py |
| Models | models.py |
| Forms | forms.py |
| App Initialization | __init__.py |
| Templates | templates/ |
| CSS | static/ |

---

# 📝 Important Commands

Run Flask Application

```bash
python run.py
```

Display Folder Structure (Windows)

```powershell
tree /F
```

---

# 📖 Concepts Learned

- Python Packages
- Package Structure
- `__init__.py`
- Flask Package Organization
- Code Separation
- Package Imports
- Relative Imports
- Absolute Imports
- Entry Point (`run.py`)
- Project Scalability

---

# 💡 Key Takeaways

- Large Flask projects should be organized into packages instead of a single file.
- `__init__.py` initializes the Flask application and extensions.
- Routes, models, and forms should be placed in separate modules.
- `run.py` is used as the application's entry point.
- Organizing code into packages makes Flask projects easier to manage, maintain, and extend.

---