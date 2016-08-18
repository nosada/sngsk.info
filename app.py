#!/usr/bin/python

import argparse
import flask
import random
from lorem_ipsum import LoremIpsum

app = flask.Flask(__name__)


class LoremIpsumBody(object):
    def __init__(self, word_source):
        self.li = LoremIpsum(word_source)
        self.text = self.li.generate_text()
        self.rate_emphasis = 80
        self.emphasis = [" <b>{}</b> ", " <i>{}</i> "]

    def generate_html_body(self):
        paragraphs = self.text.split("\n\n")
        html_paragraphs = set()
        for paragraph in paragraphs:
            html_paragraph = ''
            for word in paragraph.split(' '):
                if random.randint(1, 100) > self.rate_emphasis:
                    html_paragraph += random.choice(self.emphasis).format(word)
                else:
                    html_paragraph += " {} ".format(word)
            html_paragraphs.add("<p>" + html_paragraph + "</p>")
        self.html_body = '\n'.join(html_paragraphs)
        return self.html_body


@app.route('/')
def return_html():
    lib = LoremIpsumBody(word_source)
    html_body = lib.generate_html_body()
    return flask.render_template("index.html.tmpl", body=html_body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates and serves html with \
                random pseudo-sentences like Lorem ipsum.")
    parser.add_argument(
        "word_source",
        metavar="<word source>",
        type=str,
        help="list of words for generating pseudo-sentences")
    args = parser.parse_args()

    global word_source
    word_source = args.word_source

    app.run("::", port=8080)
