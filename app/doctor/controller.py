from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import DoctorSchema
from .service import DoctorService
from .model import Doctor
from .interface import DoctorInterface

api = Namespace("Doctor")  # noqa


@api.route('')
class DoctorResource(Resource):
    """Doctors"""

    @responds(schema=DoctorSchema, many=True)
    def get(self) -> List[Doctor]:
        """Get all Doctors"""

        return DoctorService.get_all()

    @accepts(schema=DoctorSchema, api=api)
    @responds(schema=DoctorSchema)
    def post(self) -> Doctor:
        """Create a Single Doctor"""

        return DoctorService.create(request.parsed_obj)


@api.route("/<int:doctorId>")
@api.param("doctorId", "Doctor database ID")
class DoctorIdResource(Resource):
    @responds(schema=DoctorSchema)
    def get(self, doctorId: int) -> Doctor:
        """Get Single Doctor"""

        return DoctorService.get_by_id(doctorId)

    def delete(self, doctorId: int) -> Response:
        """Delete Single Doctor"""
        from flask import jsonify

        id = DoctorService.delete_by_id(doctorId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=DoctorSchema, api=api)
    @responds(schema=DoctorSchema)
    def put(self, doctorId: int) -> Doctor:
        """Update Single Doctor"""

        changes: DoctorInterface = request.parsed_obj
        Doctor = DoctorService.get_by_id(doctorId)
        return DoctorService.update(Doctor, changes)
