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

# Date: Mon 24 Jun 2019 17:37:37 CEST
# Author: Nicolas Flandrois
# Description: The Compute class regroup all necessary computing functions,
# needed in stardate.

# import _rightThumb._stardate as _sd

# https://github.com/NicolasFlandrois/Stardate
	# sdcompute.py

import _rightThumb._base3 as _
import _rightThumb._date as _date

import datetime
import json
import sys


class Compute(object):
	"""
	The Compute class regroup all necessary computing functions.
	"""

	def config():

		return {
					"earthdate": 2019,
					"stardate": 96601.20
		}

		"""
		Returns a Tuple from config.json reference points:
		(Earthdate, Stardate)
		"""
		# with open("sdconfig.json") as f:
		#     return json.load(f)

	def ask_integer(message: str, range, error_message: str = ""):
		"""
		This function's purpose is to ask and verify an Integer.
		"""
		var = None
		while True:
			try:
				var = int(input(message))
				if var in range:
					return var
					raise

			except KeyboardInterrupt:
				break

			except:
				_.pr(error_message)

	def leapyr(year: int):
		""""
		This function defines if the year is
		a Leap year (366 days)
		or a Normal year (365 days).
		Then it will to the variable n the value of 366 or 365, accordingly.
		"""
		if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
			n = 366
			# _.pr("The year is a Leap year.\n")

		else:
			n = 365
			# _.pr("The year is a normal year.\n")

		return n

	def nowearthdate():
		"""Will generate automaticaly a tuple datetime object, for now time"""
		nowdate = datetime.datetime.now()
		return nowdate.timetuple(), nowdate.strftime('%A, %Y %B %d. %H:%M:%S')

	def sdconvert(tt=None,pp=None):

		if not tt is None:
			res_date = datetime.datetime.fromtimestamp( _.autoDate(tt) )

		if not pp is None:

			if len(pp) == 19 and pp.count('-') == 2 and pp.count(':') == 2:
				res_date = datetime.datetime.strptime( pp , "%Y-%m-%d %H:%M:%S")
			elif len(pp) == 16 and pp.count('-') == 2 and pp.count(':') == 1:
				res_date = datetime.datetime.strptime( pp , "%Y-%m-%d %H:%M")
			# elif len(pp) == 21 and pp.count('-') == 4:
			#      res_date = datetime.datetime.strptime(  pp  ,  '%Y-%m-%d'  )
			elif len(pp) == 10 and pp.count('-') == 2:
				res_date = datetime.datetime.strptime(  pp  ,  '%Y-%m-%d'  )

			# _.pr(res_date)
			# sys.exit()
			# datetime.datetime.strptime('0001-01-01T00:00:00', "%Y-%m-%dT%H:%M:%S")



		# res_date = datetime.datetime.strptime(dstring, '%Y %m %d %H %M')

		# t = res_date.timetuple(), res_date.strftime('%A, %Y %B %d. %H:%M:%S')
		t = res_date.timetuple()


		# _.pr( t )
		# sys.exit()

		# fd = _.friendlyDate( _.autoDate(tt) )
		# _.pr( fd )
		# y = int(fd.split(' ')[0].split('-')[0])
		# # m = int(fd.split(' ')[0].split('-')[1])
		# d = int(fd.split(' ')[0].split('-')[2])
		# m = int(fd.split(' ')[1].split(':')[0])
		# h = int(fd.split(' ')[1].split(':')[1])

		# _.pr( y, m, d, m, h )


		# sys.exit()

		"""
		Stardate calculator
		t = Time  (cf 'datetime.datetime.now().timetuple()' format)
		Compute.config()["earthdate"] = Earthdate Year reference point
		Compute.config()["stardate"] = Stardate Yaer reference point
		Compute.leapyr(t.tm_year) = number of days leap year/not (365 or 366)
		"""

		return float(format(((Compute.config()["stardate"] +
								(1000*(t.tm_year - Compute.config()["earthdate"]))) +
							((1000/((Compute.leapyr(t.tm_year))*1440.0))*(((
									t.tm_yday - 1.0)*1440.0) +
								(t.tm_hour*60.0) + t.tm_min))), '.2f'))

		# return format(((Compute.config()["stardate"] +
		#                 (1000*(y - Compute.config()["earthdate"]))) +
		#               ((1000/((Compute.leapyr(y))*1440.0))*(((
		#                     d - 1.0)*1440.0) +
		#                 (h*60.0) + m))), '.2f')

	def sdtranslate(sd):

		"""
		Stardate translator
		sd = Stardate Time  (cf float, stardate format)
		Compute.config()["earthdate"] = Earthdate Year reference point
		Compute.config()["stardate"] = Stardate Yaer reference point
		Compute.leapyr(t.tm_year) = number of days leap year/not (365 or 366)
		"""
		# _.pr("Stardate  : ", sd, type(sd))

		dlist = []
		ed_year = int(((sd - Compute.config()["stardate"]) // 1000) +
					Compute.config()["earthdate"])
		ey = str(ed_year)
		if int(ed_year) < 1000:
			ey = str(ed_year)
			if len(ey) == 3:
				ey = '0'+ey
			if len(ey) == 2:
				ey = '00'+ey
			if len(ey) == 1:
				ey = '000'+ey
		dlist.append(ey)
		ed_time = (((sd - Compute.config()["stardate"]) % 1000) /
				(1000 / (1440*Compute.leapyr(ed_year))))
		ed_day = (ed_time//1440)+1
		dlist.append(int(ed_day))
		ed_hour = (ed_time-((ed_day-1)*1440))//60
		dlist.append(int(ed_hour))
		ed_min = ed_time % 60
		dlist.append(int(ed_min))
		# NOTE: This calculation has 2 min leap from real date
		dstring = " ".join([str(i) for i in dlist])
		# _.pr(dstring)
		# _.pr( dstring )
		# dt = datetime.datetime.strptime(dstring, '%Y %j %H %M')
		# res = datetime.datetime.strptime(dstring, '%Y %j %H %M').strftime('%Y-%m-%d %H:%M:%S')
		return str(datetime.datetime.strptime(dstring, '%Y %j %H %M').strftime('%Y-%m-%d %H:%M:%S'))
		# return dt
		# return datetime.datetime.strptime(dstring, '%Y %j %H %M').strftime('%Y-%m-%d %H:%M:%S')
		try:
			return datetime.datetime.timestamp(dt)
		except Exception as e:
			return str(datetime.datetime.strptime(dstring, '%Y %j %H %M').strftime('%Y-%m-%d %H:%M:%S'))

def gen(tt=None,pp=None):
	return Compute.sdconvert(tt,pp)

def resolve(sd):
	return Compute.sdtranslate(sd)




