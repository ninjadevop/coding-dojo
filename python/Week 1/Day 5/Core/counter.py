from flask import Flask ,render_template , session,redirect,url_for
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route("/")
def index():
    session['view_count'] = session.get('view_count', 0) + 1
    return render_template('index.html', view_count=session['view_count'])


@app.route('/click', methods=['POST'])
def click():
    session['view_count'] = session.get('view_count', 0) + 1
    return redirect(url_for('index'))
@app.route('/destroy_session')
def destroy_session():
    # Clear the session
    session.clear()
    return redirect(url_for('index'))
        
if __name__ == '__main__':
    app.run(debug=True)