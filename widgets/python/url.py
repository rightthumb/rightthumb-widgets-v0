from urllib.parse import urlparse, parse_qs

def vars():
	vars = {}
	parts = urlparse(window.location.href)
	for key, value in parse_qs(parts.query).items():
		vars[key] = value[0]
	return vars

def var(parameter, defaultvalue):
	urlparameter = defaultvalue
	if parameter in vars():
		urlparameter = vars()[parameter]
	return urlparameter

def addParam(url, param, value):
	parts = urlparse(url)
	params = parse_qs(parts.query)
	params[param] = [value]
	parts = parts._replace(query='&'.join([f"{k}={v[0]}" for k,v in params.items()]))
	return parts.geturl()

def dic(url):
	parts = urlparse(url)
	port = parts.port or ('443' if parts.scheme == 'https' else '80')
	params = {}
	for key, value in parse_qs(parts.query).items():
		params[key] = value[0]
	result = {
		'href': url,
		'origin': f"{parts.scheme}://{parts.hostname}",
		'domain': parts.hostname.replace('www.','').lower(),
		'host': parts.hostname,
		'protocol': parts.scheme,
		'folder': '',
		'path': parts.path.replace('//','/').replace('www.','').lower(),
		'port': port,
		'param': parts.query,
		'params': params,
		'username': parts.username,
		'password': parts.password,
	}
	result['path'] = result['path'].replace(result['domain'], '')
	temp = result['path'].split('/')
	temp.pop()
	result['folder'] = '/'.join(temp).replace('//','/')
	return result

info=dic
url=dic
URL=dic

