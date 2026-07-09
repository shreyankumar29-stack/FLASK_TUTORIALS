from flask import Flask, render_template #importing the flask class and render_template function
app = Flask(__name__) #setting an instance of flask class

posts = [
    {
        'author': 'Shreyansh Kumar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2026'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2026'
    }
]
    
@app.route("/") # shows the information for the routes
@app.route("/home") # shows the information for the routes
def Home():    
    return render_template("home.html", posts=posts) #returning the home.html template

@app.route("/about") # shows the information for the routes
def About():    
    return render_template("about.html") #returning the about.html template


if __name__ == "__main__":
    app.run(debug=True)   #running the app in debug mode