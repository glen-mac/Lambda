from flask import Flask
from flask_restful import Resource, Api

mainapp = Flask(__name__)
api = Api(mainapp)

mainapp.config.from_object('config')

from mainapp import views