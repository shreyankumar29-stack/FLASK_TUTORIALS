# 🚀 Flask Tutorial by Corey Schafer – Part 7: User Account & Profile

## 📌 Objective

In this part, we create an **Account Page** where logged-in users can:

- View their profile information.
- Update their username and email.
- Prevent duplicate usernames and email addresses.
- Learn how to use `current_user` provided by Flask-Login.

---

# 📖 Why Do We Need an Account Page?

After implementing authentication in Part 6, users can now log in.

The next logical step is allowing users to **manage their account information**.

Typical features include:

- View profile
- Update username
- Update email
- Change password
- Upload profile picture (next part)

---

# 📂 Files Modified

```text
flaskblog/
│
├── forms.py
├── routes.py
├── templates/
│      └── account.html
```

---

# 🧾 UpdateAccountForm

A new form is created specifically for updating account information.

```python
class UpdateAccountForm(FlaskForm):
    username = StringField(...)
    email = StringField(...)
    submit = SubmitField("Update")
```

Unlike the Registration Form, this form only updates existing user information.

---

# 🔑 current_user

Flask-Login provides a special object called:

```python
current_user
```

It always represents the currently authenticated user.

Example:

```python
current_user.username
current_user.email
```

Instead of querying the database again, we can directly access the logged-in user's data.

---

# 🛡️ Protecting the Route

The Account page should only be accessible to logged-in users.

```python
@app.route("/account")
@login_required
def account():
    ...
```

If a user is not logged in, Flask automatically redirects them to the login page.

---

# 📥 Pre-populating Form Fields

When opening the Account page for the first time, the form should already contain the user's existing information.

```python
form.username.data = current_user.username
form.email.data = current_user.email
```

This improves the user experience because they don't need to re-enter unchanged values.

---

# ✏️ Updating User Information

When the form is submitted:

```python
current_user.username = form.username.data
current_user.email = form.email.data

db.session.commit()
```

`current_user` is already connected to the database session, so updating its attributes and committing saves the changes.

---

# 🚫 Preventing Duplicate Username

Suppose the user updates only their email.

Their username remains unchanged.

Without additional validation:

```python
User.query.filter_by(username=username.data).first()
```

the query would find the same user and incorrectly report:

```
Username already exists.
```

To prevent this:

```python
if username.data != current_user.username:
```

Only check the database if the username has actually changed.

The same logic applies to email.

---

# 📷 Displaying Profile Picture

The profile image URL is generated using:

```python
image_file = url_for(
    "static",
    filename="profile_pics/" + current_user.image
)
```

The image is then passed to the template:

```python
return render_template(
    "account.html",
    image_file=image_file,
    form=form
)
```

Inside the template:

```html
<img src="{{ image_file }}">
```

At this stage, every user still uses the default profile picture.

Actual image uploads are implemented in the next part.

---

# 🔄 Request Flow

```text
User
   │
   ▼
/account
   │
   ▼
@login_required
   │
   ▼
Load current_user
   │
   ▼
Populate Form
   │
   ▼
User edits data
   │
   ▼
Validate Form
   │
   ▼
Update current_user
   │
   ▼
db.session.commit()
   │
   ▼
Flash Success Message
   │
   ▼
Redirect to Account Page
```

---

# 📂 Project Structure

```text
flaskblog/
│
├── forms.py
├── routes.py
├── models.py
├── templates/
│      └── account.html
├── static/
│      └── profile_pics/
│             └── default.jpg
```

---

# ⚠️ Common Beginner Mistakes

## 1. Forgetting `@login_required`

Without it:

```python
@app.route("/account")
```

Anyone can access the page.

---

## 2. Not Using `current_user`

Incorrect:

```python
user = User.query.first()
```

Correct:

```python
current_user
```

Always use the currently authenticated user.

---

## 3. Forgetting `db.session.commit()`

Updating values without committing means nothing is saved to the database.

---

## 4. Duplicate Validation

Incorrect:

```python
user = User.query.filter_by(username=username.data).first()
```

Correct:

```python
if username.data != current_user.username:
```

Only validate when the value changes.

---

## 5. Passing Wrong Variable to Template

Incorrect:

```python
image=image
```

Correct:

```python
image_file=image_file
```

---

## 6. Bootstrap Flash Category

Incorrect:

```python
flash("Updated!", "Success")
```

Correct:

```python
flash("Updated!", "success")
```

Bootstrap alert classes are lowercase.

---

# 🎤 Interview Questions

### What is `current_user`?

`current_user` is an object provided by Flask-Login that represents the currently authenticated user.

---

### Why do we use `@login_required`?

It restricts access to authenticated users only.

---

### Why don't we query the database every time?

Because Flask-Login already provides the logged-in user through `current_user`.

---

### Why compare with `current_user.username` before validation?

To avoid detecting the user's own username as a duplicate.

---

### Why is `db.session.commit()` necessary?

It permanently saves changes to the database.

---

### Why use `url_for()` for profile pictures?

It generates the correct URL to static files regardless of the application's location.

---

# 📝 Key Takeaways

- Created an Account page.
- Learned how to use `current_user`.
- Updated user information.
- Protected routes using `@login_required`.
- Displayed profile information.
- Prevented duplicate usernames and email addresses.
- Used flash messages after successful updates.
- Displayed the default profile image.

---

# 📌 Modern Flask Notes (2026)

Corey Schafer's Part 7 is **mostly compatible** with Flask 3.x.

### Modern Recommendations

### ✅ Use lowercase Bootstrap categories

```python
flash("Profile updated!", "success")
```

---

### ✅ Modern SQLAlchemy

Whenever loading by primary key, prefer:

```python
db.session.get(User, user_id)
```

instead of:

```python
User.query.get(user_id)
```

(Used in the user loader from Part 6.)

---

### ✅ Keep using `current_user`

The `current_user` API has not changed and remains the recommended approach.

---

## ✅ Conclusion

By the end of Part 7, the application now supports authenticated user profiles. Users can securely view and update their account information while Flask-Login manages authentication and SQLAlchemy persists the changes.