import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
    pass
    _.switches.register( 'DomainOrIP', '-d,-domain,-domains,-ip,-ips,-i', 'domain.com 1.1.1.1', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'WhoisXML.py',
    'description': 'Domain or IP whois',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p WhoisXML -file file.txt'),
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

if 'WhoisXML' in _v.fig:
    API_KEY = _v.fig['WhoisXML']
else:
     _.e('No API Key',['Run: p config','or add to:','\tLinux: $HOME/.rt/.config.hash','\tWindows: %USERPROFILE%/.rt/.config.hash'])

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "DNT": "1",  # Do Not Track request header
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com/",
}

def get_domain_whois(domain_name):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={API_KEY}&domainName={domain_name}&outputFormat=JSON"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        pass # print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        pass # print(f"Request error occurred: {req_err}")
    except ValueError:
        pass # print("Invalid JSON response received.")
    return None

def get_ip_netblocks(ip_address):
    url = f"https://ip-netblocks.whoisxmlapi.com/api/v1?apiKey={API_KEY}&ip={ip_address}&outputFormat=JSON"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        pass # print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        pass # print(f"Request error occurred: {req_err}")
    except ValueError:
        pass # print("Invalid JSON response received.")
    return None

def get_ip_geolocation(ip_address):
    url = f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={API_KEY}&ipAddress={ip_address}&outputFormat=JSON"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        pass # print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        pass # print(f"Request error occurred: {req_err}")
    except ValueError:
        pass # print("Invalid JSON response received.")
    return None

def get_domain_reputation(domain_name):
    url = f"https://domain-reputation.whoisxmlapi.com/api/v1?apiKey={API_KEY}&domainName={domain_name}&outputFormat=JSON"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        pass # print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        pass # print(f"Request error occurred: {req_err}")
    except ValueError:
        pass # print("Invalid JSON response received.")
    return None

def get_ssl_cert_info(domain_name):
    url = f"https://ssl-certificates.whoisxmlapi.com/api/v1?apiKey={API_KEY}&domainName={domain_name}&outputFormat=JSON"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        pass # print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        pass # print(f"Request error occurred: {req_err}")
    except ValueError:
        pass # print("Invalid JSON response received.")
    return None

def get_dns_lookup(domain_name):
    url = f"https://dns-lookup.whoisxmlapi.com/api/v1?apiKey={API_KEY}&domainName={domain_name}&outputFormat=JSON"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        pass # print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        pass # print(f"Request error occurred: {req_err}")
    except ValueError:
        pass # print("Invalid JSON response received.")
    return None

def fetch_domain_info(domain_name):
    whois_info = get_domain_whois(domain_name)
    reputation_info = get_domain_reputation(domain_name)
    ssl_info = get_ssl_cert_info(domain_name)
    dns_info = get_dns_lookup(domain_name)
    
    return {
        "whois_info": whois_info,
        "reputation_info": reputation_info,
        "ssl_info": ssl_info,
        "dns_info": dns_info
    }

def fetch_ip_info(ip_address):
    netblocks_info = get_ip_netblocks(ip_address)
    geolocation_info = get_ip_geolocation(ip_address)
    
    return {
        "netblocks_info": netblocks_info,
        "geolocation_info": geolocation_info
    }



def clean(data):
    if 'ssl_info' in data:
        if 'certificates' in data['ssl_info']:
            for certificate in data['ssl_info']['certificates']:
                if 'pem' in certificate:
                    del certificate['pem']
                if 'publicKey' in certificate:
                    del certificate['publicKey']
    return data

def Domain(input_value):
    cache = _.getTable('WhoisXML-'+input_value+'.json')
    if cache:
        return clean(cache)
    pass # print(f"Fetching information for domain: {input_value}")
    domain_info = fetch_domain_info(input_value)
    _.saveTable(domain_info,'WhoisXML-'+input_value+'.json')
    pass # print("Domain Information:")
    return clean(domain_info)

def IP(input_value):
    cache = _.getTable('WhoisXML-'+input_value+'.json')
    if cache:
        return cache
    pass # print(f"Fetching information for IP address: {input_value}")
    ip_info = fetch_ip_info(input_value)
    _.saveTable(ip_info,'WhoisXML-'+input_value+'.json')
    pass # print("IP Information:")
    return ip_info

def action():
    DomainOrIPs = _.switches.values('DomainOrIP')
    for DomainOrIP in DomainOrIPs:
        input_value = DomainOrIP
        
        if any(c.isalpha() for c in input_value):

        else:


########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__);