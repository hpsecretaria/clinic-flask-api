from marshmallow import fields, Schema


class PatientSchema(Schema):

    patientId = fields.Number(attribute='patient_id', dump_only=True)
    firstName = fields.String(attribute='first_name')
    lastName = fields.String(attribute='last_name')
    address = fields.String(attribute='address')
    city = fields.String(attribute='city')
    province = fields.String(attribute='province')
