## 📅 Formatting Dates with `strftime()`

In this part, Corey uses Python's `strftime()` method to display dates in a more readable format.

### Syntax

```python
datetime.strftime(format)
```

Example:

```python
post.date_posted.strftime('%Y-%m-%d')
```

Output:

```text
2026-07-15
```

---

### Common Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit Year | 2026 |
| `%y` | 2-digit Year | 26 |
| `%m` | Month (01-12) | 07 |
| `%B` | Full Month Name | July |
| `%b` | Short Month Name | Jul |
| `%d` | Day of Month | 15 |
| `%A` | Full Weekday | Wednesday |
| `%a` | Short Weekday | Wed |
| `%H` | Hour (24-hour) | 18 |
| `%I` | Hour (12-hour) | 06 |
| `%M` | Minutes | 30 |
| `%S` | Seconds | 45 |
| `%p` | AM / PM | PM |

---

### Example Used in the Project

```html
{{ post.date_posted.strftime('%Y-%m-%d') }}
```

Output:

```text
2026-07-15
```

Another example:

```html
{{ post.date_posted.strftime('%B %d, %Y') }}
```

Output:

```text
July 15, 2026
```

This format is more user-friendly and is commonly used in blogs.

---

### Why do we use `strftime()`?

Dates stored in the database are `datetime` objects.

Example:

```python
2026-07-15 18:42:37.235812
```

Displaying this directly is not user-friendly.

Using `strftime()` converts it into a readable format like:

```text
July 15, 2026
```

or

```text
15-07-2026
```

depending on the desired format.

---

### Interview Question

**Q. What is `strftime()` in Python?**

**Answer:**

`strftime()` (String Format Time) is a method of Python's `datetime` object that converts a date and time into a formatted string based on the specified format codes.

---

### Key Takeaway

- `strftime()` converts a `datetime` object into a formatted string.
- It is commonly used to display dates in a readable format.
- Flask templates can directly call `strftime()` on `datetime` objects.