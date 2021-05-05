"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


db = SQLAlchemy()

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(50),
                     nullable=False,
                     )
    size = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    image = db.Column(db.String, nullable=False, default=" https://tinyurl.com/demo-cupcake")
    def serializer_cupcakes(self):
            return {
                "id": self.id,
                "flavor": self.flavor,
                "size": self.size,
                "rating": self.rating,
                "image": self.image
            }


    











def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
