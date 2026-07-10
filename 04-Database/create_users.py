from flaskblog import app, db, User

with app.app_context():

    if User.query.count() == 0:
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

        print("Users added successfully!")
    else:
        print("Users already exist.")