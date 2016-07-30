from mainapp import mainapp, api
from flask import render_template, flash, redirect, url_for, request, jsonify
import forms
from flask_restful import reqparse, abort, Api, Resource
import predstuff

@mainapp.route('/')
def index():
    form = forms.UserInputForm()
    return render_template('index.html', title='GovHack 2016') #, form=form)

parser = reqparse.RequestParser()
parser.add_argument('userdata')

class TaxProcess(Resource):
    def get(self):
        return 'there is nothing in here, use post'

    def post(self):
        args = parser.parse_args()
        return magic(args)

def magic(data):
    return jsonify({'hey': 1, 'how': 3, 'data': data})

api.add_resource(TaxProcess, '/process')