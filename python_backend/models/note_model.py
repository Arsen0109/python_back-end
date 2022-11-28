from sqlalchemy import func

from python_backend.db import db


class CategoryModel(db.Model):
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user_id"),
        unique=False,
        nullable=False
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category_id"),
        unique=False,
        nullable=False
    )
    date_of_creating = db.Column(db.TIMESTAMP, server_default=func.now())
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="note")
    category = db.relationship("CategoryModel", back_populates="note")