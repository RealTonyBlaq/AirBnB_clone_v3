#!/usr/bin/python3
""" Amenity module """

from api.v1.views import app_views
from flask import abort, jsonify
from models.amenity import Amenity


@app_views.route('')