from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import PatientSchema
from .service import PatientService
from .model import Patient
from .interface import PatientInterface

api = Namespace("Patient")  # noqa


@api.route('')
class PatientResource(Resource):
    """Patients"""

    @responds(schema=PatientSchema, many=True)
    def get(self) -> List[Patient]:
        """Get all Patients"""

        return PatientService.get_all()

    @accepts(schema=PatientSchema, api=api)
    @responds(schema=PatientSchema)
    def post(self) -> Patient:
        """Create a Single Patient"""

        return PatientService.create(request.parsed_obj)


@api.route("/<int:patientId>")
@api.param("patientId", "Patient database ID")
class PatientIdResource(Resource):
    @responds(schema=PatientSchema)
    def get(self, patientId: int) -> Patient:
        """Get Single Patient"""

        return PatientService.get_by_id(patientId)

    def delete(self, patientId: int) -> Response:
        """Delete Single Patient"""
        from flask import jsonify

        id = PatientService.delete_by_id(patientId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PatientSchema, api=api)
    @responds(schema=PatientSchema)
    def put(self, patientId: int) -> Patient:
        """Update Single Patient"""

        changes: PatientInterface = request.parsed_obj
        Patient = PatientService.get_by_id(patientId)
        return PatientService.update(Patient, changes)
