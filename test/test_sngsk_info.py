#!/bin/env python

import requests
import unittest


class TestSngskInfo(unittest.TestCase):
    def test_sngsk_info(self):
        status_code = requests.get("https://sngsk.info").status_code
        self.assertEqual(status_code, 200)

    def test_sngsk_info_aboutme(self):
        status_code = requests.get("https://sngsk.info/aboutme").status_code
        self.assertEqual(status_code, 200)

    def test_mastodon_sngsk_info(self):
        status_code = requests.get("https://mastodon.sngsk.info").status_code
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()
