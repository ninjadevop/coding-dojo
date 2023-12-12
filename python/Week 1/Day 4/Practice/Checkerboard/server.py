from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def check():
    return   render_template("index.html",x=8,y=8)


@app.route('/<int:x>')          # The "@" decorator associates this route with the function immediately following
def check1(x):
    return   render_template("index.html",x=x,y=8)

@app.route('/<int:x>/<int:y>')          # The "@" decorator associates this route with the function immediately following
def check2(x,y):
    return   render_template("index.html",x=x,y=y)


@app.route('/<int:x>/<int:y>/<color1>/<color2>')          # The "@" decorator associates this route with the function immediately following
def check3(x,y,color1,color2):
    return   render_template("index.html",x=x,y=y,color1=color1,color2=color2)











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.