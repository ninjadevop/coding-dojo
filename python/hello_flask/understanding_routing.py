from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return ("hello world!")

@app.route("/dojo")
def dojo():
    return ("Dojo!")

@app.route("/say/<smthg>")
def say(smthg):
    print(smthg)
    return "say ," + smthg
    
@app.route('/repeat/<int:num>/<string:word>') 
def repeat_word(num, word):
    repeat_word = word * num
    return f"{repeat_word}\n"




if __name__ == "__main__" :
    app.run(debug=True)
