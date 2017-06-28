#!/usr/bin/python


"""Tiny application for sngsk.info"""


import configparser
import os
import random
import flask

from lorem_ipsum import LoremIpsum


SCRIPT_LOCATION = os.path.dirname(os.path.abspath(__file__))
CONFIG_LOCATION = os.path.join(
    SCRIPT_LOCATION, "config", "sngsk.info.conf")
CONF = configparser.ConfigParser(allow_no_value=True)
CONF.read(CONFIG_LOCATION)
SECTION = "app"

DOMAIN = CONF.get(SECTION, "domain")
CSS = CONF.get(SECTION, "common_css")
FAVICON = CONF.get(SECTION, "favicon")

APP = flask.Flask(__name__)


class GenerateBody(object):
    """Generate Lorem Ipsum content and put it into page body"""

    def __init__(self):
        """Constructor of LoremIpsumBody"""

        section = "lorem_ipsum"
        word_list = CONF.get(section, "word_source")
        word_source = os.path.join(
            SCRIPT_LOCATION, "files", word_list)

        self.lorem_ipsum = LoremIpsum(word_source)
        self.text = self.lorem_ipsum.generate_text()
        self.emphasis = [" <b>{}</b> ", " <i>{}</i> "]
        self.rate_emphasis = int(CONF.get(section, "rate_emphasis"))

    def generate_html_body(self):
        """Create page body; generate Lorem Ipsum and put it into page body"""

        paragraphs = self.text.split("\n\n")
        html_paragraphs = []
        for paragraph in paragraphs:
            html_paragraph = ''
            for word in paragraph.split(' '):
                if random.randint(1, 100) > self.rate_emphasis:
                    html_paragraph += random.choice(self.emphasis).format(word)
                else:
                    html_paragraph += " {} ".format(word)
            html_paragraphs.append("<p>" + html_paragraph + "</p>")
        html_body = '\n'.join(html_paragraphs)
        return html_body


@APP.route('/')
def return_lorem_ipsum_html():
    """Generate Lorem Ipsum page and return it"""
    lib = GenerateBody()
    html_body = lib.generate_html_body()
    return flask.render_template("index.html.tmpl",
                                 body=html_body,
                                 domain=DOMAIN,
                                 css=CSS,
                                 favicon=FAVICON)


@APP.route('/aboutme')
def return_aboutme_html():
    """Generate aboutme page and return it"""
    return flask.render_template("aboutme.html.tmpl",
                                 domain=DOMAIN,
                                 css=CSS,
                                 favicon=FAVICON)


APP.run("::", port=8080)
