import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Entertainment', '-e,-ent,-movie,-show', 'Inception' )
	_.switches.register( 'Person', '-p,-person', 'Leonardo DiCaprio' )
	_.switches.register( 'All', '-a,-all' )
_._default_settings_()

_.appInfo[focus()] = {
	'description': 'Movie and Show research tool',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


import requests
from bs4 import BeautifulSoup
import re
import os

def is_number(s):
    pattern = r'^-?\d+(\.\d+)?$'
    return bool(re.match(pattern, s))

def fi(input_string):
	sanitized = re.sub(r'[^\w\-\.]', '_', input_string)
	return sanitized

def titleDB(title): return 'imdb'+os.sep+'ent-'+fi(title)

def peopleDB(title): return 'imdb'+os.sep+'people-'+fi(title)

def extractID(url):
	for part in url.split('/'):
		if part.startswith('tt'): return part
		if part.startswith('nm'): return part

def google_cache_person(query): return _v.tt+os.sep+'imdb'+os.sep+'google-person-'+fi(query)
def google_cache_title(query): return _v.tt+os.sep+'imdb'+os.sep+'google-title-'+fi(query)

import requests
from bs4 import BeautifulSoup
import re
import sys

def get_imdb_person_id(query):
	# print(google_cache_person(query));sys.exit();
	if os.path.isfile(google_cache_person(query)): return _.getText2(google_cache_person(query),'text').strip()

	# Append ' imdb' to the search query
	search_query = query + ' imdb'
	google_url = f"https://www.google.com/search?q={search_query}"

	# Make a request to Google Search
	response = requests.get(google_url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		# Find the first link that contains 'www.imdb.com/name/nm'
		link = soup.find('a', href=re.compile("www.imdb.com/name/nm"))
		if link:
			# Extract the IMDb person ID
			imdb_id_match = re.search("/name/(nm\\d+)/", link['href'])
			if imdb_id_match:
				_.saveText(imdb_id_match.group(1),google_cache_person(query))
				return imdb_id_match.group(1)
	else:
		print(f"Failed to get a response from Google, status code: {response.status_code}")
	return None



def get_imdb_title_id(query):
	if os.path.isfile(google_cache_title(query)): return _.getText2(google_cache_title(query),'text').strip()
	# Append ' imdb' to the search query
	search_query = query + ' imdb'
	google_url = f"https://www.google.com/search?q={search_query}"

	# Make a request to Google Search
	response = requests.get(google_url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		# Find the first link that contains 'www.imdb.com/title/tt'
		link = soup.find('a', href=re.compile("www.imdb.com/title/tt"))
		if link:
			# Extract the IMDb ID
			imdb_id_match = re.search("/title/(tt\\d+)/", link['href'])
			if imdb_id_match:
				_.saveText(imdb_id_match.group(1),google_cache_title(query))
				return imdb_id_match.group(1)
	else:
		print(f"Failed to get a response from Google, status code: {response.status_code}")
	return None


def get_actors(imdb_id):
	"""
	Extracts the list of actors from the IMDB page of a movie given its IMDB ID.
	Returns a list of dictionaries containing the actor's name and their IMDb URL.
	"""
	actors = []
	url = f"https://www.imdb.com/title/{imdb_id}/fullcredits"

	# Make a request to the IMDb page
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	response = requests.get(url, headers=headers)
	# response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		# Find all links that start with '/name/nm'
		characters = []
		for link in soup.find_all('a', href=re.compile("^.*/characters/nm")):
			character = link.get_text(strip=True)
			if character:
				characters.append(character)
		i=0
		for link in soup.find_all('a', href=re.compile("^/name/nm")):
			actor_url = "https://www.imdb.com" + link['href'].split('?')[0]  # Clean the URL
			actor_name = link.get_text(strip=True)
			if actor_name:
				i+=1
				try:
					character = characters[i]
				except:
					character = ''
				actors.append({"name": actor_name, "url": actor_url, "id": extractID(actor_url), 'character': character})
	return actors

def get_movie_info1(title, api_key):
	movie_info = _.getTable(titleDB(title))
	if not movie_info:
		title_query = title.replace(' ', '+')
		url = f"http://www.omdbapi.com/?t={title_query}&apikey={api_key}"
		response = requests.get(url)
		if response.status_code != 200:
			return "Request to OMDB API failed."
		movie_info = response.json()
		movie_info['Actors'] = get_actors(movie_info['imdbID'])
		if movie_info['Response'] == 'False':
			return "Movie not found."
		_.saveTable(movie_info,titleDB(title))
	return movie_info

def get_movie_info(title, api_key):
	info = _.getTable(titleDB(title))
	if not info:
		imdb_id = get_imdb_title_id(title)
		if not imdb_id: _.e("Unable to find person's imdbID",'No imdb google results')
		url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
		response = requests.get(url)
		if response.status_code != 200:
			return "Request to OMDB API failed."
		info = response.json()
		info['Actors'] = get_actors(info['imdbID'])
		if info['Response'] == 'False':
			return "Movie not found."
		_.saveTable(info,titleDB(title))
	return info

def get_actor_filmography1(person, imdb_id):
	info = _.getTable(peopleDB(person))
	if not info:
		url = f"https://www.imdb.com/name/{imdb_id}/?ref_=ttfc_fc_cl_t1"
		# print(url)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
		response = requests.get(url, headers=headers)

		print(response.status_code)
		if response.status_code != 200:
			return {"error": "Failed to retrieve data from IMDb."}

		soup = BeautifulSoup(response.text, 'html.parser')
		filmography = []

		for item in soup.find_all("a", href=lambda href: href and href.startswith('/title/tt')):
			film_title = item.get_text().strip()
			film_url = "https://www.imdb.com" + item.get('href')
			filmography.append({"title": film_title.strip(), "url": film_url, "id": extractID(film_url)})

		info = {
			"imdbID": imdb_id,
			"url": url,
			"filmography": filmography
		}
	_.saveTable(info,peopleDB(person))
	return info

def get_actor_filmography(person,imdb_id=None):
	info = _.getTable(peopleDB(person))

	if not info:
		if imdb_id is None:
			imdb_id = get_imdb_person_id(person)
			if not imdb_id: _.e("Unable to find person's imdbID",'No imdb google results')


		url = f"https://www.imdb.com/name/{imdb_id}/?ref_=ttfc_fc_cl_t1"
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
		}
		response = requests.get(url, headers=headers)

		if response.status_code != 200:
			return {"error": "Failed to retrieve data from IMDb."}

		soup = BeautifulSoup(response.text, 'html.parser')
		filmography = []

		# Find all elements with the class 'sc-6703147-3', and select the second instance
		elements = soup.find_all(class_='sc-6703147-3')
		if len(elements) > 1:
			filmography_section = elements[1]  # Select the second instance
			years=[]
			for item in filmography_section.find_all("span", class_="ipc-metadata-list-summary-item__li"):
				year = item.get_text().strip()
				years.append(year)
			# Find all <a> tags with the specified class within this section
			i=-1
			for item in filmography_section.find_all("a", class_="ipc-metadata-list-summary-item__t", href=lambda href: href and href.startswith('/title/tt')):
				i+=1
				film_title = item.get_text().strip()
				film_url = "https://www.imdb.com" + item.get('href').split('?')[0]
				filmography.append({"title": film_title, "url": film_url, "id": extractID(film_url)})
			filmography.reverse()
			years.reverse()
			for i,rec in enumerate(filmography):
				try:
					filmography[i]['year']=years[i]
				except:
					filmography[i]['year']=''

			filmography.reverse()

		info = {
			"imdbID": imdb_id,
			"url": url,
			"filmography": filmography
		}
		if info:
			_.saveTable(info, peopleDB(person))
	return info

def printTitles(info):
	_.pr(info['Title'],c='green')
	meta = [{'Year': info['Year'], 'Rated': info['Rated'], 'Released': info['Released'], 'Runtime': info['Runtime']}]; _.pt(meta);
	meta = [{'Genre': info['Genre'], 'Awards': info['Awards'], 'Director': info['Director'], 'Writer': info['Writer']}]; _.pt(meta);
	_.pr('Plot:',info['Plot'],c='cyan')
	_.pr('Awards:',info['Awards'],c='cyan')
	_.pr('Rating:',info['imdbRating'],c='cyan')
	all = _.switches.isActive('All')
	people = []
	data = []
	spent = []
	ii=-1
	for i,person in enumerate(info['Actors']):
		if  not all:
			ii+=1
			if ii < 20:
				# if not person['id'] in spent:
				spent.append(person['id'])
				people.append({'i':ii, 'name': person['name'], 'character': person['character']})
				data.append({'i':ii, 'name': person['name'], 'character': person['character'], 'id': person['id']})
		else:
			# if not person['id'] in spent:
				# ii+=1
			spent.append(person['id'])
			people.append({'i':ii, 'name': person['name'], 'character': person['character']})
			data.append({'i':ii, 'name': person['name'], 'character': person['character'], 'id': person['id']})
	_.pt(people)
	choose = input(' : ')
	if is_number(choose):
		person = get_actor_filmography(data[int(choose)]['name'],data[int(choose)]['id'])
		printPerson(person)
def printPerson(info):
	# _.pv(info); sys.exit();
	ii=-1
	titles = []
	data = []
	spent = []
	all = _.switches.isActive('All')
	for i,filmography in enumerate(info['filmography']):
		if not filmography['id'] in spent:
			ii+=1
			spent.append(filmography['id'])
			titles.append({'i':ii, 'title': filmography['title'], 'year': filmography['year']})
	_.pt(titles)
	choose = input(' : ')
	if is_number(choose):
		info = get_movie_info(titles[int(choose)]['title'], _v.fig['imdb'])
		printTitles(info)
def action():
	if _.switches.isActive('Entertainment'):
		title = ' '.join(_.switches.values('Entertainment'))
		info = get_movie_info(title, _v.fig['imdb'])
		# del info['Actors']
		# _.pv(info)
		printTitles(info)
	if _.switches.isActive('Person'):
		person = ' '.join(_.switches.values('Person'))
		info = get_actor_filmography(person)
		# _.pv(info)
		printPerson(info)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);