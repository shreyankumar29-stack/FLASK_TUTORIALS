# Flask Database with SQLAlchemy

These are my notes while learning **Database Integration in Flask** from the **Corey Schafer Flask Tutorial Series**.

---

# 📚 Topics Covered

- Flask-SQLAlchemy
- SQLite Database
- SQLAlchemy ORM
- Database Models
- Primary Key
- Foreign Key
- Relationships
- Creating Tables
- Inserting Data
- Querying Data
- Updating Data
- Deleting Data
- Application Context

---

# 📦 Installing Flask-SQLAlchemy

```bash
pip install flask-sqlalchemy
```

---

# 📥 Import SQLAlchemy

```python
from flask_sqlalchemy import SQLAlchemy
```

---

# ⚙️ Database Configuration

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

---

# 📂 Project Structure

```text
04-Database/

│── flaskblog.py
│── forms.py
│── create_users.py
│── create_posts.py
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── about.html
│   ├── register.html
│   └── login.html
│
├── static/
│   └── main.css
│
└── instance/
    └── site.db
```

---

# 🗂 Database Models

## User Model

```python
class User(db.Model):
```

Columns:

- id
- username
- email
- image
- password

---

## Post Model

```python
class Post(db.Model):
```

Columns:

- id
- title
- content
- date_posted
- user_id

---

# 🔗 Relationship

```python
author = db.relationship(
    'User',
    backref='posts',
    lazy=True
)
```

```python
user_id = db.Column(
    db.Integer,
    db.ForeignKey('user.id'),
    nullable=False
)
```

Relationship:

```
One User
     │
     │
     ▼
Many Posts
```

---

# 🏗 Creating Database

```python
with app.app_context():
    db.create_all()
```

---

# 👤 create_users.py

Used to insert sample users.

```python
from flaskblog import app, db, User

with app.app_context():

    user_1 = User(
        username="Shreyansh",
        email="c@demo.com",
        password="password"
    )

    user_2 = User(
        username="JohnDoe",
        email="jd@demo.com",
        password="password"
    )

    db.session.add(user_1)
    db.session.add(user_2)

    db.session.commit()
```

Run:

```bash
python create_users.py
```

---

# 📝 create_posts.py

Used to insert sample posts.

```python
from flaskblog import app, db, User, Post

with app.app_context():

    user = db.session.get(User, 1)

    post_1 = Post(
        title="Blog 1",
        content="First Post Content!",
        user_id=user.id
    )

    post_2 = Post(
        title="Blog 2",
        content="Second Post Content!",
        user_id=user.id
    )

    db.session.add(post_1)
    db.session.add(post_2)

    db.session.commit()
```

Run:

```bash
python create_posts.py
```

---

# 🔥 Important SQLAlchemy Queries

## Create Database

```python
with app.app_context():
    db.create_all()
```

---

## Add Single Record

```python
db.session.add(user)
db.session.commit()
```

---

## Add Multiple Records

```python
db.session.add(user_1)
db.session.add(user_2)

db.session.commit()
```

---

## Get All Users

```python
User.query.all()
```

---

## Get First User

```python
User.query.first()
```

---

## Get Last User

```python
User.query.order_by(User.id.desc()).first()
```

---

## Get User by ID (Modern)

```python
db.session.get(User, 1)
```

---

## Filter by Username

```python
User.query.filter_by(username="Shreyansh").all()
```

---

## Filter by Email

```python
User.query.filter_by(email="c@demo.com").first()
```

---

## Filter Using Conditions

```python
User.query.filter(User.username == "Shreyansh").all()
```

---

## Count Records

```python
User.query.count()
```

---

## Check if User Exists

```python
User.query.filter_by(username="Shreyansh").first()
```

---

## Get All Posts

```python
Post.query.all()
```

---

## Get First Post

```python
Post.query.first()
```

---

## Access User Information

```python
user = db.session.get(User, 1)

print(user.id)
print(user.username)
print(user.email)
```

---

## Access All Posts of a User

```python
user.posts
```

---

## Print Post Titles

```python
for post in user.posts:
    print(post.title)
```

---

## Update Record

```python
user.username = "New Username"

db.session.commit()
```

---

## Delete Record

```python
db.session.delete(user)

db.session.commit()
```

---

## Delete All Posts

```python
Post.query.delete()

db.session.commit()
```

---

## Rollback Transaction

```python
db.session.rollback()
```

---

# 📌 Common Session Methods

```python
db.session.add()

db.session.commit()

db.session.delete()

db.session.rollback()

db.session.flush()
```

---

# 💻 Commands Used

Activate virtual environment

```bash
venv\Scripts\activate
```

Install Flask-SQLAlchemy

```bash
pip install flask-sqlalchemy
```

Run Flask App

```bash
python flaskblog.py
```

Create Database

```python
with app.app_context():
    db.create_all()
```

Insert Users

```bash
python create_users.py
```

Insert Posts

```bash
python create_posts.py
```

---

# 📖 Concepts Learned

- Flask-SQLAlchemy
- SQLite
- ORM (Object Relational Mapper)
- Database Models
- Primary Key
- Foreign Key
- Relationships
- One-to-Many Relationship
- SQLAlchemy Session
- CRUD Operations
- Database Queries
- Application Context

---

# 📝 Summary

In this section, I learned how to integrate SQLite with Flask using Flask-SQLAlchemy. I created database models (`User` and `Post`), established a one-to-many relationship between them, created the database, inserted sample records, queried data using SQLAlchemy ORM, and performed basic CRUD operations. I also learned how to use SQLAlchemy sessions and application contexts when working with modern versions of Flask.