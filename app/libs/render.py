"""Render Lorem Ipsum HTML body"""

import random
from libs.lorem_ipsum import LoremIpsum
from libs.conf import Conf


class GenerateLoremIpsum(object):
    """Generate Lorem Ipsum content and put it into page body"""

    def __init__(self):
        """Constructor of LoremIpsumBody"""
        self.conf = Conf()
        self.emphasis = [" <b>{}</b> ", " <i>{}</i> "]
        self.word_list, rate_emphasis = \
            self.conf.read_lorem_ipsum_config()
        self.rate_emphasis = int(rate_emphasis)

    def _get_lorem_ipsum_paragraphs(self):
        lorem_ipsum = LoremIpsum(self.word_list)
        return lorem_ipsum.generate_text().split("\n\n")

    def _generate_html_body(self):
        """Create page body; generate Lorem Ipsum and put it into page body"""
        paragraphs = self._get_lorem_ipsum_paragraphs()
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
