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
parser.add_argument('maritalStatus', action='append')
parser.add_argument('regionCode')
parser.add_argument('taxAgent', action='append')
parser.add_argument('salaryWages')

class TaxProcess(Resource):
    def get(self):
        # dir = os.path.dirname(__file__)
        pred = get_model.prediction_backend([1, 10, 200000])
        cl = get_model.clustering_backend([1, 10, 200000])

        return {'pred' : pred, 'cl' : cl}

    # receive the post request from front end
    def post(self):
        # getting the arguments
        args = parser.parse_args()
        # doing machine learning magic and returning result to the front end
        pred = get_model.prediction_backend(np.array(args['taxAgent'],dtype='float32'))
        cl = get_model.clustering_backend(np.array(args['maritalStatus'], dtype='float32'))#[1, 10, 200000])

        # return pred
        # return args['taxAgent']
        return {'pred': pred, 'cl': cl}


api.add_resource(TaxProcess, '/process')
