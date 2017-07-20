#!/usr/bin/python

"""Tiny application for sngsk.info"""

import flask
from libs.app import GetLoremIpsumView, GetAboutMeView

APP = flask.Flask(__name__)

APP.add_url_rule(
    "/",
    view_func=GetLoremIpsumView.as_view("lorem_ipsum",
                                        template_name="index.html.tmpl"))
APP.add_url_rule(
    "/aboutme",
    view_func=GetAboutMeView.as_view("aboutme",
                                     template_name="aboutme.html.tmpl"))
APP.run("::", port=8080)
