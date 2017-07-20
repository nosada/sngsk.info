"""Config parser for app on sngsk.info"""

import configparser
import os


class Conf(object):
    """Read app config and return parameters"""

    def __init__(self):
        """Dettermine conf path and load cofig"""
        script_location = os.path.dirname(os.path.abspath(__file__))
        config_location = os.path.join(
            script_location, "..", "config", "sngsk.info.conf")
        self.conf = configparser.ConfigParser(allow_no_value=True)
        self.conf.read(config_location)

    def read_lorem_ipsum_config(self):
        """Get location of word list which is source for
        generating lorem ipsum"""
        section = "lorem_ipsum"
        word_list = self.conf.get(section, "word_source")
        rate_emphasis = self.conf.get(section, "rate_emphasis")
        return word_list, rate_emphasis

    def read_app_config(self):
        """Return static files location for rendering html"""
        section = "app"
        domain = self.conf.get(section, "domain")
        css = self.conf.get(section, "common_css")
        favicon = self.conf.get(section, "favicon")
        return domain, css, favicon
