from marshmallow import fields, Schema


class DoctorSchema(Schema):

    doctorId = fields.Number(attribute='doctor_id', dump_only=True)
    firstName = fields.String(attribute='first_name')
    lastName = fields.String(attribute='last_name')
