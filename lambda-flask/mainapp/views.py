from mainapp import mainapp, api
from flask import render_template, flash, redirect, url_for, request, jsonify
import forms
from flask_restful import reqparse, abort, Api, Resource
import numpy as np
import sys

sys.path.insert(0, 'D:\GovHackGitHub\predstuff')
print(sys.path)
import predstuff

from predstuff import get_model

@mainapp.route('/')
def index():
    form = forms.UserInputForm()
    return render_template('index.html', title='GovHack 2016') #, form=form)

parser = reqparse.RequestParser()
parser.add_argument('userdata')

class TaxProcess(Resource):
    def get(self):
        # return 'there is nothing in here, use post'
        mdl = get_model.load_model\
            ('D:\\GovHackGitHub\\predstuff\\models\\reg_baseline.p')
        get_model.predict(mdl, np.random.random_sample((35,)))

    def post(self):
        args = parser.parse_args()
        return magic(args)

def magic(data):
    return jsonify({'hey': 1, 'how': 3, 'data': data})

api.add_resource(TaxProcess, '/process')
