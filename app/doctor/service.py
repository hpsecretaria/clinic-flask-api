from app import db
from typing import List
from .model import Doctor
from .interface import DoctorInterface


class DoctorService:
    @staticmethod
    def get_all() -> List[Doctor]:
        return Doctor.query.all()

    @staticmethod
    def get_by_id(doctor_id: int) -> Doctor:
        return Doctor.query.get(doctor_id)

    @staticmethod
    def update(doctor: Doctor, Doctor_change_updates: DoctorInterface) -> Doctor:
        doctor.query.update(Doctor_change_updates)
        db.session.commit()
        return doctor

    @staticmethod
    def delete_by_id(doctor_id: int) -> List[int]:
        doctor = Doctor.query.filter(Doctor.doctor_id == doctor_id).first()
        if not doctor:
            return []
        db.session.delete(doctor)
        db.session.commit()
        return [doctor_id]

    @staticmethod
    def create(new_attrs: DoctorInterface) -> Doctor:
        new_doctor = Doctor(**new_attrs)

        db.session.add(new_doctor)
        db.session.commit()

        return new_doctor
