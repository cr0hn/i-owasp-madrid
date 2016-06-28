# -*- coding: utf-8 -*-

from flask import Flask, request

import logging

app = Flask("logi")

# --------------------------------------------------------------------------
# Config log
# --------------------------------------------------------------------------
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
log = logging.getLogger("my_log")

log_console = logging.StreamHandler()
log_console.setFormatter(formatter)

# File
log_file = logging.FileHandler("log_injection.logs")
log_file.setFormatter(formatter)

log.addHandler(log_file)
log.addHandler(log_console)
log.setLevel(logging.DEBUG)


@app.route("/")
def home():
	return "heeello world"


@app.route("/info", methods=["POST"])
def logi():

	data = request.form['id']

	log.debug("[*] Tried to get info '" + data + "' from the user.")

	return "got info!"


if __name__ == '__main__':
	app.run()
