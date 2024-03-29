from python_backend.db import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    note = db.relationship("NoteModel", back_populates="category", lazy="dynamic")
