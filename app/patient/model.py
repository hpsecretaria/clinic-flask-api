from app import db


class Patient(db.Model):
    __tablename__ = 'patient'

    patient_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(128))
    city = db.Column(db.String(50))
    province = db.Column(db.String(50))
    state = db.Column(db.String(50))
