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

from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
from urllib.parse import urlparse
import sys

url = sys.argv[2]

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):

	# This is a function that HTMLParser normally has
	# but we are adding some functionality to it
	def handle_starttag(self, tag, attrs):
		# We are looking for the begining of a link. Links normally look
		# like <a href="www.someurl.com"></a>
		if tag == 'a':
			for (key, value) in attrs:
				if key == 'href':
					# We are grabbing the new URL. We are also adding the
					# base URL to it. For example:
					# www.netinstructions.com is the base and
					# somepage.html is the new URL (a relative URL)
					#
					# We combine a relative URL with the base URL to create
					# an absolute URL like:
					# www.netinstructions.com/somepage.html
					newUrl = parse.urljoin(self.baseUrl, value)
					# And add it to our colection of links:
					self.links = self.links + [newUrl]

	# This is a new function that we are creating to get links
	# that our spider() function will call
	def getLinks(self, url):
		self.links = []
		# Remember the base URL which will be important when creating
		# absolute URLs
		self.baseUrl = url
		# Use the urlopen function from the standard Python 3 library
		response = urlopen(url)
		# Make sure that we are looking at HTML and not other things that
		# are floating around on the internet (such as
		# JavaScript files, CSS, or .PDFs for example)
		if response.getheader('Content-Type')=='text/html':
			htmlBytes = response.read()
			# Note that feed() handles Strings well, but not bytes
			# (A change from Python 2.x to Python 3.x)
			try:
				htmlString = htmlBytes.decode("utf-8")
			except Exception as e:
				htmlString = htmlBytes.decode("iso-8859-1")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "",[]

# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url, word, maxPages): 
	pagesToVisit = [url]
	numberVisited = 0
	foundWord = False
	# The main loop. Create a LinkParser and get all the links on the page.
	# Also search the page for the word or string
	# In our getLinks function we return the web page
	# (this is useful for searching for the word)
	# and we return a set of links from that web page
	# (this is useful for where to go next)
	while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
		numberVisited = numberVisited +1
		# Start from the beginning of our collection of pages to visit:
		url = pagesToVisit[0]
		pagesToVisit = pagesToVisit[1:]
		foundWord = False
		try:
			print("Searching:", urlparse(url).path)
			parser = LinkParser()
			data, links = parser.getLinks(url)
			if data.find(word)>-1:
				foundWord = True
				# Add the pages that we visited to the end of our collection
				# of pages to visit:
				pagesToVisit = pagesToVisit + links
				print("\n\t** Success! **")
		except:
			print(" **Failed!**")
	if foundWord:
		print("\t\tThe word", word, "was found at", url)
	else:
		pass
		# print("Word never found")
	return foundWord

def urlList(rows):
	result = []
	for r in rows:
		try:
			if not 'javascript' in r:
				# result = result + r.split('#')[0]
				result.append(r.split('#')[0])
				# result.append(r)
		except Exception as e:
			pass
	result = [i for i in set(tuple(result))]
	return result

def urlListRefine(base,rows,ext):
	b = urlparse(base).netloc
	result = []
	for r in rows:
		rb = urlparse(r).netloc
		if ext:
			result.append(r)
		elif b == rb:
			result.append(r)
	return result
test = 2
if test == 0:
	spider(url,'Love',10)

if test == 1:
	parser = LinkParser()
	result = parser.getLinks(url)[1]
	result = urlList(result)
	result = urlListRefine(url,result,False)
	
	# print(result)
	for r in result:
		print(r)
if test == 2:
	parser = LinkParser()
	result = parser.getLinks(url)[1]
	result = urlList(result)
	result = urlListRefine(url,result,False)
	if not spider(url,'Love',5):
		for r in result:
			if not url == r:
				if spider(r,'Love',5):
					break

if test == 3:
	print(urlparse(url))