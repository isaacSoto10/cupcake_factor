"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, session, jsonify 
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY']= "isaacsoto"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']= True
connect_db(app)


@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    serializer = [Cupcake.serializer_cupcakes(c)for c in cupcakes]
    return jsonify(cupcakes=cupcakes.serializer_cupcakes())

@app.route('/api/cupcakes/<int:id>', methods=['GET'])
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serializer_cupcakes())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    data = request.json
    flavor = data['flavor']
    size = data['size']
    rating = data['rating']
    image = data['image']
    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serializer_cupcakes()), 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def create_cupcake(id):
    data = request.json
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serializer_cupcakes())

 

@app.route('/api/cupcakes/<int:id>', methods=[])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="cupcake DELETED")



 




