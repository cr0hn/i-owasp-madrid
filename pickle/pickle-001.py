# -*- coding: utf-8 -*-

import base64
import pickle


class MyLittleBastard(object):
	def __reduce__(self):
		print("WoooooooW")

		return self.__class__, tuple(),


def main():
	base64.b64encode(pickle.dumps(MyLittleBastard()))


if __name__ == '__main__':
	main()
