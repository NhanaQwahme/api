from  flask import Flask,request,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
import os



app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'THEPASSCODE'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'ticket.sqlite')
db=SQLAlchemy(app)

class Ticket(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        email=db.Column(db.String(50),unique=True)
        name=db.Column(db.String(50))
        ticket_type=db.Column(db.String(50))
        ticket_message=db.Column(db.String(120))
        def __init__(self,email,name,ticket_type,ticket_message):
            self.name=name
            self.email=email
            self.ticket_type=ticket_type
            self.ticket_message=ticket_message

@app.route('/')
def index():
    return render_template('index.html'),200

								
@app.route('/customer/create-ticket/',methods=['POST','GET'])
def get_new_tickets():
    ticket_type=request.form.get('type')
    email=request.form.get('form')
    name=request.form.get('name')
    ticket_message=request.form.get('reply')

    ticket=Ticket(email=email,name=name,ticket_type=ticket_type,ticket_message=ticket_message)
    db.session.add(ticket)
    db.session.commit()
    

    print(type(ticket_type))


    
    return jsonify({
    "status":"200",
    "message":"created"
    

    }),200

@app.route('/member/create-ticket/',methods=['GET'])
def message():
   
    new_tickets=Ticket.query.all()
    
    New_ticket=[]
    for data in new_tickets:
        
        
       
        new_ticket={}
        new_ticket['id'] = data.id
        new_ticket[' email']= data. email
        new_ticket['name']= data.name
        new_ticket['ticket_type']= data.ticket_type
        new_ticket['ticket_message']= data.ticket_message
        New_ticket.append(new_ticket)


    ticket_type=New_ticket[-1]["ticket_type"]
    if (ticket_type =='5' ):
        return jsonify({
        "Ticket owner":"Sherifa",
        "Image":"Sherifa"

            }),200
    elif(ticket_type == '12' or ticket_type == '2' or ticket_type == '16' or ticket_type == '3' or ticket_type =='4' ):
        return jsonify({
        "Ticket owner":"Manuel",
        "Image":"manuel"

            }),200
    elif(ticket_type == '1' ):
        return jsonify({
    "Ticket owner":"Theophilus",
    "Image":"theo"

        }),200
    elif(ticket_type == '10' ):
        return jsonify({
    "Ticket owner":"Michael",
    "Image":"mic"

        }),200
    elif(ticket_type == '26'):
        return jsonify({
"Ticket owner":"Farida",
"Image":"farida"

    }),200

    elif(ticket_type == '18'):
        return jsonify({
"Ticket owner":"Ann",
"Image":"Ann"
}),200
    

        
   

if "__main__" =="__name__":
    app.run(debug=True,host="0.0.0.0", port=5050)