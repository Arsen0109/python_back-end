from python_backend.db import db


class CurrencyModel(db.Model):
    __tablename__ = "currency"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    note = db.relationship("NoteModel", back_populates="currency", lazy="dynamic")
