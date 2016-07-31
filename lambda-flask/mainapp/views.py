from mainapp import mainapp, api
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response, Response
import forms
from flask_restful import reqparse, abort, Api, Resource
import numpy as np
import sys
import os

from predstuff import get_model

@mainapp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        # form = forms.UserInputForm()
        return render_template('index.html', title='GovHack 2016') #, form=form)
    else:
        return 'hello'
    # else:
    #     return request.get_data()

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

        result = {'pred': pred, 'cl': cl}

        # resp = Response({'pred': pred}, mimetype='application/json')
        return result


    # receive the post request from front end
    def post(self):
        # getting the arguments
        args = parser.parse_args()
        pred_arg = np.array([args['isMale'],
                            args['ageRange'],
                            args['occupationCode']], dtype='int32')
        # doing machine learning magic and returning result to the front end
        pred = get_model.prediction_backend(pred_arg)
        cl = get_model.clustering_backend(pred_arg)#[1, 10, 200000])

        # return pred
        # return args['taxAgent']
        args['pred'] = pred
        args['cl'] = cl
        return args


api.add_resource(TaxProcess, '/process')
