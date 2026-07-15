# 📝 NOTES – (Part 8)

# 📌 Topic
Displaying Individual Posts & Dynamic Routes

---

# 1. Dynamic Routes

Until now, every route in our application was static.

Example:

```python
@app.route("/")
def home():
    ...
```

The URL never changes.

Dynamic routes allow Flask to capture values directly from the URL.

Example:

```python
@app.route("/post/<int:post_id>")
def post(post_id):
    ...
```

Now URLs like:

```
/post/1
/post/2
/post/3
```

all point to the same route.

---

# 2. URL Converters

Flask supports different URL converters.

Example:

```python
<int:id>
```

Only integers are accepted.

Common converters:

```python
<string:name>
```

Accepts text.

```python
<int:id>
```

Accepts integers.

```python
<float:value>
```

Accepts floating-point numbers.

```python
<path:file_path>
```

Accepts complete file paths.

Using converters makes routes safer by validating URL parameters automatically.

---

# 3. Receiving Route Parameters

Example:

```python
@app.route("/post/<int:post_id>")
def post(post_id):
```

Flask automatically passes the value from the URL into the function parameter.

Example:

```
/post/5
```

becomes

```python
post_id = 5
```

---

# 4. Querying the Database

Corey uses:

```python
post = Post.query.get_or_404(post_id)
```

This searches for a post using its primary key.

If the post exists:

✔ Return the post.

If the post doesn't exist:

✔ Automatically display a 404 Not Found page.

---

# 5. Why use get_or_404()?

Without it:

```python
post = db.session.get(Post, post_id)
```

If the record doesn't exist:

```python
post = None
```

Accessing

```python
post.title
```

would raise an error.

Using

```python
get_or_404()
```

makes the application safer because Flask immediately returns a proper 404 page.

---

# 6. Rendering the Post Page

Example:

```python
return render_template(
    "post.html",
    title=post.title,
    post=post
)
```

The complete post object is passed to the template.

---

# 7. Accessing Object Attributes in Jinja

Inside the template:

```html
{{ post.title }}
```

```html
{{ post.author.username }}
```

```html
{{ post.content }}
```

Jinja can directly access model attributes.

---

# 8. SQLAlchemy Relationships

Because of the relationship defined in the models:

```python
author = db.relationship(
    "User",
    backref="posts",
    lazy=True
)
```

Flask automatically connects:

```
Post
   │
   ▼
User
```

Therefore,

```html
{{ post.author.username }}
```

works without writing another database query.

---

# 9. Rendering HTML Dynamically

The same template displays every blog post.

Example:

```
/post/1
```

shows

```
First Post
```

while

```
/post/2
```

shows

```
Second Post
```

The HTML file never changes.

Only the data changes.

---

# 10. Request Flow

```
Browser
      │
      ▼
/post/5
      │
      ▼
Dynamic Route
      │
      ▼
Database Query
      │
      ▼
Post Object
      │
      ▼
render_template()
      │
      ▼
post.html
      │
      ▼
Browser
```

---

# 11. Common Beginner Mistakes

### Forgetting the URL converter

Incorrect:

```python
@app.route("/post/<post_id>")
```

Recommended:

```python
@app.route("/post/<int:post_id>")
```

---

### Using the wrong variable name

Incorrect:

```python
post = Post.query.get_or_404(id)
```

Correct:

```python
post = Post.query.get_or_404(post_id)
```

---

### Forgetting to pass the object

Incorrect:

```python
return render_template("post.html")
```

Correct:

```python
return render_template(
    "post.html",
    post=post
)
```

---

### Forgetting relationships

Incorrect:

```html
{{ author.username }}
```

Correct:

```html
{{ post.author.username }}
```

---

# 12. Modern Flask / SQLAlchemy Note

Corey's code:

```python
Post.query.get_or_404(post_id)
```

works correctly in modern Flask-SQLAlchemy.

Unlike `Query.get()`, **`get_or_404()` is not deprecated** and is still recommended for Flask applications when you want to return a 404 page if the object is not found.

---

# 🎤 Interview Questions

### What is a dynamic route?

A dynamic route allows parts of the URL to be treated as variables and passed to the route function.

---

### Why do we use `<int:post_id>`?

It ensures only integer values are accepted and automatically converts the URL value to an integer.

---

### What does `get_or_404()` do?

It retrieves an object from the database using its primary key. If the object doesn't exist, Flask automatically returns a **404 Not Found** response.

---

### Why do we use relationships?

Relationships connect database tables so related data can be accessed easily, such as:

```python
post.author.username
```

without writing additional SQL queries.

---

# ✅ Key Takeaways

- Learned how to create dynamic routes.
- Used URL converters like `<int:post_id>`.
- Retrieved database records using `get_or_404()`.
- Rendered individual blog posts.
- Accessed related objects using SQLAlchemy relationships.
- Understood how Flask passes URL parameters to view functions.