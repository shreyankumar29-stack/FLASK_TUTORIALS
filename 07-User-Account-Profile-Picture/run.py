from flaskblog import app, db


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database Created Successfully!")

    app.run(debug=True)