from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

App=Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/CRUD'

db=SQLAlchemy(App)

# Creating Class:-
class crud(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)

@App.route("/",methods=['GET','POST'])
def index():
    posts=crud.query.all()
    if request.method=='POST':
        text=request.form.get('text')
        entry=crud(text=text)
        db.session.add(entry)
        db.session.commit()
        return redirect("/")
    return render_template("index.html",posts=posts)

@App.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    delete_data=crud.query.filter_by(sno=sno).first()
    db.session.delete(delete_data)
    db.session.commit()
    return redirect("/")


@App.route("/edit/<string:sno>",methods=['GET','POST'])
def edit(sno):
    posts=crud.query.filter_by(sno=sno).first()
    text=request.form.get("edit_text")
    if request.method=='POST':
        text=request.form.get("text")
        edit=crud.query.filter_by(sno=sno).first()
        edit.text=text
        db.session.commit()
        return redirect("/")
    return render_template("edit.html",posts=posts)

App.run(debug=True)