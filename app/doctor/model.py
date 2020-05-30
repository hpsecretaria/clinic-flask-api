from app import db


class Doctor(db.Model):
    __tablename__ = 'doctor'

    doctor_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
