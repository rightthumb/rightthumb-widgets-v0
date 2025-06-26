import sys

args = list(sys.argv)
if (args[0].endswith('.py')):
	args.pop(0)
if (args[0] == 'args'):
	args.pop(0)

# print(' '.join(args))

test='start'
while test:
	test=input(': ')
	print(test)