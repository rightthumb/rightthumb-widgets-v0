#!/usr/bin/python


import sys
import json
import argparse
import os


try:
	from urlparse import urlparse
except ImportError:
	from urllib.parse import urlparse


def get_terminal_size():
	import os
	env = os.environ
	def ioctl_GWINSZ(fd):
		try:
			import fcntl, termios, struct, os
			cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
		'1234'))
		except:
			return
		return cr
	cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
	if not cr:
		try:
			fd = os.open(os.ctermid(), os.O_RDONLY)
			cr = ioctl_GWINSZ(fd)
			os.close(fd)
		except:
			pass
	if not cr:
		cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

	return int(cr[1]), int(cr[0])


def color(color):
	if color:
		sys.stdout.write('\033[%sm' % (30 + color));
	else:
		sys.stdout.write('\033[0m')


def text_wrap(s, cols=72, ident=4, ident_first=True):
	"""
	Hard-wrap a string on chars, not words. Returns a string with the newlines
	places in the correct positions.
	"""
	new_s = ''
	if ident_first:
		new_s += ' ' * ident
	pos = 0
	for i in range(len(s)):
		c = s[i]
		if pos == cols - ident:
			# Text is about to run off the right side.
			new_s += '\n' + ' ' * ident + c
			pos = 0
		elif c == '\n':
			# Naturally occuring newline in text.
			new_s += '\n'
			if i != len(s) - 1:
				new_s += ' ' * ident
			pos = 0
		else:
			new_s += c
		pos += 1
	return(new_s)

def should_output_entry(entry, url_filter, grep_req, grep_res):
	"""
	Inspects the entry (request) and determines if it needs to be displayed.
	"""
	url = urlparse(entry['request']['url'])
	fname, ext = os.path.splitext(url.path)
	if ext in url_filter:
		return False

	if grep_req is not None:
		for header in entry['request']['headers']:
			full_header = '%s: %s' % (header['name'], header['value'])
			if grep_req in full_header:
				return True
		else:
			return False

	if grep_res is not None:
		for header in entry['response']['headers']:
			full_header = '%s: %s' % (header['name'], header['value'])
			if grep_res in full_header:
				return True
		else:
			return False

	return True

def output_entry(entry, show_color, verbose):
	if entry['response']['status'] == 0:
		status_code = '  0'
	else:
		status_code = str(entry['response']['status'])

	if show_color is True:
		if status_code[0] in ['4', '5']: # Client / Server error
			color(1)
		elif status_code[0] == '2': # OK reponses
			color(2)
		elif status_code == '  0':
			color(5)
		else: # Other responses
			color(3)

	sys.stdout.write(status_code)

	if show_color is True:
		color(None)

	sys.stdout.write(' %s %s\n' % (
			entry['request']['method'],
			entry['request']['url']
		)
	)

	if verbose > 0:
		# Print headers
		sys.stdout.write('    Request headers\n')
		for header in entry['request']['headers']:
			ident = len('        %s: ' % (header['name']))
			sys.stdout.write('        %s: %s\n' % (
					header['name'],
					text_wrap(header['value'], cols=cols, ident=ident, ident_first=False)
				)
			)

		if verbose > 1:
			# Print request body
			if entry['request']['method'] == 'POST':
				sys.stdout.write('    POST data (%s)\n' % (entry['request']['postData']['mimeType']))
				sys.stdout.write(text_wrap(entry['request']['postData']['text'] + '\n',  cols=cols, ident=8))

		sys.stdout.write('    Response headers (status = %s)\n' % (entry['response']['status']))
		for header in entry['response']['headers']:
			sys.stdout.write('        %s: %s\n' % (
				header['name'], header['value']
				)
			)

		if verbose > 1:
			# Print response body
			if 'text' in entry['response']['content']:
				sys.stdout.write('    Response data (%s)\n' % (entry['response']['content']['mimeType']))
				try:
					sys.stdout.write(text_wrap(entry['response']['content']['text'] + '\n',  cols=cols, ident=8))
				except:
					sys.stderr.write('Response data can not be displayed\n')


		sys.stdout.write('\n')

if __name__ == "__main__":
	global options

	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--verbose', action='count', default=0, help="Show more. Can be used multiple times")
	parser.add_argument('--filter-img', action='store_true', help="Filter out requests for images")
	parser.add_argument('--filter-refs', action='store_true', help="Filter out requests for CSS, JS, etc")
	parser.add_argument('--filter-all', action='store_true', help="All filters")
	parser.add_argument('--grep-req', action='store', help="Only show requests where Request headers contain GREP_REQ.")
	parser.add_argument('--grep-res', action='store', help="Only show requests where Response headers contain GREP_RES.")
	parser.add_argument('--nocolor', action='store_true', default=False)
	parser.add_argument('har_file')
	args = parser.parse_args()

	url_filter = set()
	if args.filter_refs or args.filter_all:
		url_filter.update(('.js', '.css', '.woff', '.otf'))
	if args.filter_img or args.filter_all:
		url_filter.update(('.png', '.jpg', '.jpeg', '.gif', '.svg'))

	cols, lines = get_terminal_size()

	try:
		har = json.load(open(args.har_file, 'r'))
	except IndexError:
		sys.stderr.write("Usage: %s <file.har>\n" % (sys.argv[0]))
		sys.exit(1)
	except ValueError as e:
		sys.stderr.write("Invalid .har file: %s\n" % (str(e)))
		sys.exit(2)

	for entry in har['log']['entries']:
		if should_output_entry(entry, url_filter, args.grep_req, args.grep_res):
			output_entry(entry, not args.nocolor, args.verbose)
