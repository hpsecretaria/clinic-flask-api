from mypy_extensions import TypedDict


class PatientInterface(TypedDict, total=False):
    patient_id: int
    first_name: str
    last_name: str
    address: str
    city: str
    province: str
