# -*- coding: utf-8 -*-

import yaml

YAML = '''
hello: world
how:
 - are
 - you
'''


def main():
	print(yaml.load(YAML))


if __name__ == '__main__':
	main()
