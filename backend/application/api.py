from pymongo import MongoClient, ReturnDocument
from uuid import uuid4
from bson.objectid import ObjectId
# from app_config import url

url = "mongodb+srv://senjenathaniel:4BXBpEdw9Fmf@blogcluster.b9rhq.mongodb.net/blog?ssl=true&ssl_cert_reqs=CERT_NONE"

patient_id = uuid4()
client = MongoClient(url)
patients = client.operations.patients


def get_single_patient():
    patient = patients.find_one()
    return patient


def get_patients():
    data = []
    for x in patients.find():
        data.append(x)

    return data


def get_patient(patient_id):
    patient = patients.find_one({"_id": ObjectId(patient_id)})
    return patient


def add_patients(patients):
    patients.insert_many(patients)
    return


def add_patient(patient):
    patient = patients.insert_one(patient)
    return patient


def delete_patient(val):
    patient = patients.find_one_and_delete({'_id': ObjectId(val)})
    return patient


print(get_patients())

print(get_single_patient())
