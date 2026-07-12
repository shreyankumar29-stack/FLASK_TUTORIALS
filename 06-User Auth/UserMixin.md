## UserMixin

`UserMixin` is a helper class provided by Flask-Login.

Instead of manually implementing authentication-related methods, the `User` model inherits from `UserMixin`.

```python
from flask_login import UserMixin

class User(UserMixin, db.Model):
    ...
```

### UserMixin provides:

- `is_authenticated`
- `is_active`
- `is_anonymous`
- `get_id()`

### Benefits

- Reduces boilerplate code.
- Integrates the User model with Flask-Login.
- Enables session-based authentication.


## Modern SQLAlchemy Change

### Corey's Code

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

### Modern Code (SQLAlchemy 2.x)

```python
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
```

### Reason

`Query.get()` is deprecated in SQLAlchemy 2.x.

The recommended approach is to use `Session.get()` via `db.session.get()`.