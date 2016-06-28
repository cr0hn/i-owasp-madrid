# -*- coding: utf-8 -*-
import re

from flask import Flask, request

import logging

app = Flask("logi")


@app.route("/")
def home():
	return "heeello world"


@app.route("/mailme/<mail>", methods=["GET"])
def logi(mail=None):

	if re.match(r'^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$', mail):
		return "mail sent to: %s" % mail
	else:
		return "mail forma invalid"


if __name__ == '__main__':
	app.run()
