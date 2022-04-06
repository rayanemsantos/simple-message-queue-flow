# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from .urls import resources, api_prefix

app = Flask(__name__)
CORS(app)
api = Api(app, prefix=api_prefix)

# all routes
for view_class, url in resources:
    api.add_resource(view_class, url)