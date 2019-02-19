from flask import flash,redirect,url_for,render_template

from sayhello import app,db
from sayhello.models import Message
from sayhello.forms import HelloForm

@app.route('/',methods=['GET','POST'])
def index():
    #加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        sender = form.sender.data
        content = form.content.data
        message = Message(sender=sender,content=content)
        db.session.add(message)
        db.session.commit()
        flash('留言发表成功')
        return redirect(url_for('index'))
    return render_template('index.html',form=form, messages=messages)
