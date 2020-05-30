from .model import Doctor  # noqa
from .schema import DoctorSchema  # noqa

BASE_ROUTE = "doctors"


def register_routes(api, app):
    from .controller import api as doctor_api

    api.add_namespace(doctor_api, path=f"/{BASE_ROUTE}")
