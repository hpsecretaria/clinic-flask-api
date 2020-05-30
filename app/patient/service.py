from app import db
from typing import List
from .model import Patient
from .interface import PatientInterface


class PatientService:
    @staticmethod
    def get_all() -> List[Patient]:
        return Patient.query.all()

    @staticmethod
    def get_by_id(patient_id: int) -> Patient:
        return Patient.query.get(patient_id)

    @staticmethod
    def update(patient: Patient, Patient_change_updates: PatientInterface) -> Patient:
        patient.query.update(Patient_change_updates)
        db.session.commit()
        return patient

    @staticmethod
    def delete_by_id(patient_id: int) -> List[int]:
        patient = Patient.query.filter(Patient.patient_id == patient_id).first()
        if not patient:
            return []
        db.session.delete(patient)
        db.session.commit()
        return [patient_id]

    @staticmethod
    def create(new_attrs: PatientInterface) -> Patient:
        new_patient = Patient(**new_attrs)

        db.session.add(new_patient)
        db.session.commit()

        return new_patient
