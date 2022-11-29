from sqlalchemy import func

from python_backend.db import db


class NoteModel(db.Model):
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        unique=False,
        nullable=False
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id"),
        unique=False,
        nullable=False
    )
    currency_id = db.Column(
        db.Integer,
        db.ForeignKey("currency.id"),
        unique=False,
        nullable=False
    )
    date_of_creating = db.Column(db.TIMESTAMP, server_default=func.now())
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="note")
    category = db.relationship("CategoryModel", back_populates="note")
    currency = db.relationship("CurrencyModel", back_populates="note")
