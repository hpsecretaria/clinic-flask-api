from .model import Patient  # noqa
from .schema import PatientSchema  # noqa

BASE_ROUTE = "patients"


def register_routes(api, app):
    from .controller import api as patient_api

    api.add_namespace(patient_api, path=f"/{BASE_ROUTE}")
