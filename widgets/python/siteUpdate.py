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

#A1695618-Converted
# check for an update on a web-page, and email the user
import http.client
import sys
import pickle
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import yaml

address, url_path = sys.argv[2].split('/', 1)
url_path = '/' + url_path
print("Checking {} on {} for updates...".format(url_path, address))
c = http.client.HTTPConnection(address)
c.request('GET', url_path)
r = c.getresponse()

# get the date into a datetime object
lmd = r.getheader('last-modified')
if lmd != None:
   cur_data = { url: datetime.strptime(lmd, '%a, %d %b %Y %H:%M:%S %Z') }
else:
   print("Hmmm, no last-modified data was returned from the URL.")
   print("Returned header:")
   print("----------------")
   print(yaml.dump(dict(r.getheaders()), default_flow_style=False))
   print("----------------")
   exit()
print(cur_data)

# def email_user(cur_data, email_from, email_to):
#    msg = MIMEText("The URL you've been watching has been modified!\n{}".format(
#       yaml.dump(cur_data, default_flow_style=False)))
#    msg['Subject'] = 'Site Update Notification'
#    msg['From'] = email_from
#    msg['To'] = email_to
#    server = smtplib.SMTP('localhost')
#    server.sendmail(email_from, email_to, msg.as_string())
#    server.quit()

# # we must have a URL to check!
# if len(sys.argv) < 2:
#    print('Please submit a URL as the first argument!')
#    exit()

# url = sys.argv[2]

# if len(sys.argv) > 3:
#    email_from = sys.argv[3]

# if len(sys.argv) > 4:
#    email_to = sys.argv[4]

# # load any previous data from the data file.
# data_file = '.check4update'
# lm_data = {}
# try:
#    lm_data = pickle.load(open(data_file, 'rb'))
# except IOError as e:
#    print("Couldn't open {}: {}".format(data_file, e.strerror))
# except EOFError:
#    print("File loaded, but it's empty")

# separate the IP address from the URL path, then make the call...

# check to see if we have any previous last-modified data for this URL.
# if url in lm_data:
#    # is the current last-modified time newer than the stored time?
#    if(cur_data[url] != lm_data[url]):
#       print("Last-modified time has changed!\n   old: {}\n   new: {}".format(lm_data[url], cur_data[url]))
#       lm_data[url] = cur_data[url]
#       email_user(cur_data)
#    else:
#       print("Last-modified time is the same: {}.".format(lm_data[url]))
#       email_user(cur_data)
# else:
#    # this is a new URL, so just add it to the stored data.
#    print('Adding new URL data:\n   URL: {}\n   last-modified: {}'.format(url, cur_data[url]))
#    lm_data.update(cur_data)

# # save the current data to the data file...
# try:
#    pickle.dump(lm_data, open(data_file, 'wb'))
# except:
#    print("Couldn't save data file!")


