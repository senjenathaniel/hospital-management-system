from flask import current_app as app
from flask import render_template, redirect, request, url_for, flash
from . api import get_patients, get_patient, delete_patient, add_patient, get_single_patient

"""
    APPLICATION ROUTES
"""


@ app.route("/create", methods=["GET", "POST"])
def create():
    patient = {}
    return patient


@ app.route("/patients")
def index():
    data = get_patients()
    print(type(data))
    return data


@ app.route("/latest_patient")
def latest_patient():
    patient = get_single_patient()
    return patient


@ app.route("/patient/<_id>")
def patient(patient_id):
    patient = get_patient(patient_id)
    return patient


@ app.route("/delete/<_id>")
def delete(_id):
    patient = delete_patient(_id)
    return patient
