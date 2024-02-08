"""Classes for rendering HTML content on sngsk.info"""

from flask import render_template
from flask.views import View
from libs.conf import Conf
from libs.render import GenerateLoremIpsum


class GetLoremIpsumView(GenerateLoremIpsum, View):
    """Generate Lorem Ipsum HTML"""

    def __init__(self, template_name):
        """Read conf and set template name for given template_name"""

        super(GetLoremIpsumView, self).__init__()
        self.conf = Conf()
        self.domain, self.favicon = self.conf.read_app_config()
        self.template_name = template_name

    def dispatch_request(self):
        """Generate Lorem Ipsum page and return it
        - args: none
        - returns: render_template object"""

        html_body = self.generate_html_body()
        return render_template(self.template_name,
                               body=html_body,
                               domain=self.domain,
                               favicon=self.favicon)


class GetAboutMeView(View):
    """Generate Lorem Ipsum HTML"""

    def __init__(self, template_name):
        """Read conf and set template name for given template_name"""

        super(GetAboutMeView, self).__init__()
        self.conf = Conf()
        self.domain, self.favicon = self.conf.read_app_config()
        self.template_name = template_name

    def dispatch_request(self):
        """Generate aboutme page and return it
        - args; none
        - returns: render_template object"""

        return render_template(self.template_name,
                               domain=self.domain,
                               favicon=self.favicon)
