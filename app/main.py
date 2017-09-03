#!/usr/bin/python

"""Tiny application for sngsk.info"""

import flask
from libs.conf import Conf
from libs.view import GetLoremIpsumView, GetAboutMeView

APP = flask.Flask(__name__)
CONF = Conf()

APP.add_url_rule(
    "/",
    view_func=GetLoremIpsumView.as_view("lorem_ipsum",
                                        template_name="index.html.tmpl"))
APP.add_url_rule(
    "/aboutme",
    view_func=GetAboutMeView.as_view("aboutme",
                                     template_name="aboutme.html.tmpl"))
APP.run("::", port=CONF.get_port_number())
