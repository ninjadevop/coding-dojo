from flask import Flask , render_template , request,redirect, session
app=Flask(__name__)
app.secret_key="don't try that at home"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/result", methods=['POST'])
def result():
    session["your_name"] = request.form['your_name']
    session["dojo_location"]= request.form['dojo_location']
    session["favourite_language"]= request.form['favourite_language']
    session["comments"]=request.form['comments']
    return redirect("/display")

@app.route("/display")
def display():
    data={
        "your_name": session["your_name"],
        "dojo_location":session["dojo_location"],
        "favourite_language":session["favourite_language"],
        "comments":session["comments"]
    }
    return render_template("resultat.html",data=data)





if __name__ == '__main__' :
    app.run(debug=True)