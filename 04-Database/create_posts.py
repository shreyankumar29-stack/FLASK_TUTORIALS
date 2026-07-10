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

    print(user.posts)

    for post in user.posts:
        print(post.title)

print("Posts added successfully!")