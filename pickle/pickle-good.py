# -*- coding: utf-8 -*-

import pickle


class ImSoHappy(object):

	def __init__(self):
		self.my_var = []


def main():
	pickle.dump(ImSoHappy(), open("my_info.db", "wb"))


if __name__ == '__main__':
	main()
