from mypy_extensions import TypedDict


class DoctorInterface(TypedDict, total=False):
    doctor_id: int
    first_name: str
    last_name: str
