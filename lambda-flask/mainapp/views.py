from mainapp import mainapp, api
from flask import render_template, flash, redirect, url_for, request, jsonify
import forms
from flask_restful import reqparse, abort, Api, Resource
import numpy as np
import sys
import os

from predstuff import get_model

@mainapp.route('/')
def index():
    form = forms.UserInputForm()
    return render_template('index.html', title='GovHack 2016') #, form=form)

parser = reqparse.RequestParser()
parser.add_argument('isMale')
parser.add_argument('ageRange')
parser.add_argument('occupationCode')
parser.add_argument('maritalStatus')
parser.add_argument('regionCode')
parser.add_argument('taxAgent')
parser.add_argument('salaryWages')

class TaxProcess(Resource):
    def get(self):
        # doing relative path
        # not working on windows the pickle file
        dir = os.path.dirname(__file__)
        mdl = get_model.load_model\
            (os.path.join(dir, 'reg_baseline.p'))
        return get_model.predict(mdl, np.random.random_sample((35, 2)))

    # receive the post request from front end
    def post(self):
        # getting the arguments
        args = parser.parse_args()
        # doing machine learning magic and returning result to the front end
        return magic(args)

def magic(data):
    return jsonify(dict({'hey': 1, 'how': 3 }.items() + data.items()))

api.add_resource(TaxProcess, '/process')