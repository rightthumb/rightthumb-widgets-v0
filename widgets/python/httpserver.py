#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import cgi

# ip and port of server
HOST_NAME = '127.0.0.1'

# by default http server port is 8085
PORT_NUMBER = '8080'

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
	""" Create custom HTTPRequestHandler class """


	def _set_headers(self):
		""" set HTTP headers """

		# send code 200 response
		self.send_response(200)
		# send header first
		self.send_header('Content-type', 'text/html')
		self.send_header('Last-Modified',
						self.date_time_string(time.time()))
		# send file content to client
		self.end_headers()

	def _set_headers_json(self):
		""" set HTTP headers """

		# send code 200 response
		self.send_response(200)
		# send header first
		self.send_header('Content-type', 'application/json')
		# self.send_header('Last-Modified',
		#                  self.date_time_string(time.time()))
		# send file content to client
		self.end_headers()

	def do_HEAD(self):
		""" do the HTTP HEAD """

		# set HTTP headers
		self._set_headers()


	def do_GET(self):
		""" handle GET command """

		rootdir = os.path.dirname(__file__) # file location
		# self.path = self.path.replace('/','')
		# if self.path.endswith('.html'):
		if 1:
			f = open(rootdir + self.path) # open requested file
			# set headers
			self._set_headers()
			# send file content to client
			self.wfile.write(bytes(f.read(), "utf-8"))
			f.close()
			return
		try:
			pass
		except IOError:
			self.send_error(404, 'file not found')


	def do_POST(self):
		""" handle POST command """

		# set HTTP headers
		self._set_headers()

		# Create instance of FieldStorage
		# for parse the form data posted

		# print('________________________________________________')
		# print('rfile')
		# print( dir(self.rfile) )
		# # print( self.rfile.readlines() )
		# print('headers')
		# print( self.headers )
		# print('________________________________________________')
		form = cgi.FieldStorage(
			fp=self.rfile,
			headers=self.headers,
			environ={'REQUEST_METHOD':'POST',
					'CONTENT_TYPE':self.headers['Content-Type'],
					})

		# Begin the response
		# self._set_headers()
		# self._set_headers_json()
		
		# Get data from fields
		message = form.getvalue('message')

		html_response = """
<html>
  <body>
	<h1>POST verb demo</h1>
	<p>The message is '%s'.</p>
	<br />
	<p>This is a POST verb!</p>
  </body>
</html>
		""" % (message)

		
		html_response = message

		self.wfile.write(bytes(html_response, "utf-8"))


def run():
	try:
		print('HTTP Server is starting...')
		server_address = (HOST_NAME, int(PORT_NUMBER))
		server = HTTPServer(server_address, MyHTTPRequestHandler)
		print ("HTTP Server running on http://{0}:{1}/ use <Ctrl-C> to stop.".format(HOST_NAME, PORT_NUMBER))
		server.serve_forever()
	except KeyboardInterrupt:
		print (" o <Ctrl-C> entered, stopping web server....")
		server.socket.close()


if __name__ == '__main__':
	""" Starting Python program """
	run()
else:
	print('error')


# https://gist.github.com/macagua/58f85dc8905cec78dfa085eab2b15bfb
# python server form fields site:github.com
# simple python web server send form


"""

https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
https://en.wikipedia.org/wiki/Media_type


"""




