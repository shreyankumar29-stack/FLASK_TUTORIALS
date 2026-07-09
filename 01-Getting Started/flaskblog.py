from flask import Flask
app = Flask(__name__) #setting an instance of flask class

@app.route("/") # shows the information for the routes
@app.route("/home") # shows the information for the routes
def Home():    
    return "<h1>Home Page</h1>" #returning a string

@app.route("/about") # shows the information for the routes
def About():    
    return "<h1>About Page</h1>" #returning a string


if __name__ == "__main__":
    app.run(debug=True)   #running the app in debug mode