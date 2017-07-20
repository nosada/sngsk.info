"""Return HTML"""

from flask import render_template
from flask.views import View
from libs.conf import Conf
from libs.render import GenerateLoremIpsum


class GetLoremIpsumView(GenerateLoremIpsum, View):
    def __init__(self, template_name):
        super(GetLoremIpsumView, self).__init__()
        self.conf = Conf()
        self.domain, self.css, self.favicon = self.conf.read_app_config()
        self.template_name = template_name

    def dispatch_request(self):
        """Generate Lorem Ipsum page and return it"""
        html_body = self._generate_html_body()
        return render_template(self.template_name,
                               body=html_body,
                               domain=self.domain,
                               css=self.css,
                               favicon=self.favicon)


class GetAboutMeView(View):
    def __init__(self, template_name):
        super(GetAboutMeView, self).__init__()
        self.conf = Conf()
        self.domain, self.css, self.favicon = self.conf.read_app_config()
        self.template_name = template_name

    def dispatch_request(self):
        """Generate aboutme page and return it"""
        return render_template(self.template_name,
                               domain=self.domain,
                               css=self.css,
                               favicon=self.favicon)
