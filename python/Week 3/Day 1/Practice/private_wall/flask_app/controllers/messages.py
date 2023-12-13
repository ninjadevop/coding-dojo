from flask_app import app
from flask import render_template,session,redirect,request,flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message



@app.route('/send', methods=['post'])
def send():
        data={'r_user_id':request.form['r_user_id'],'s_user_id':session['user_id'],'message':request.form['message']}
        Message.create_message(data)
        return redirect('/dashboard')
        

@app.route('/delete/<int:id>', methods=['post'])
def delete(id):
        data={'id':id}
        Message.delete_message(data)
        return redirect('/dashboard')
