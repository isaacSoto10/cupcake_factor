"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, session, jsonify 
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY']= "isaacsoto"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']= True
connect_db(app)


@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    all_cupcakes = Cupcake.query.all()
    serializer = (serializer_cupcakes(c)for c in all_cupcakes)
    return jsonify(cupcakes=serializer)

@app.route('/api//cupcakes/<int:id>', methods=['GET'])
def get_cupcake(id):
    cupcake = Cupcake.query.get(id)
    serializer = (serializer_cupcake(cupcake))
    return jsonify(cupcake=serializer)


@app.route('/cupcake', methods=['POST'])
def create_cupcake():
    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json.get('image')
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    serialized = serializer_cupcake(new_cupcake)
    return (jsonify(dessert=serialized), 201)





