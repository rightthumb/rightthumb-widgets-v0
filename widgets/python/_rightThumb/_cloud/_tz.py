import datetime as ddatetime

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import pytz
import time


def convert( epoch, tz_src, tz_to ):
	global index
	source_date = ddatetime.datetime.fromtimestamp( epoch )
	source_time_zone = pytz.timezone( index[tz_src]['name'] )
	source_date_with_timezone = source_time_zone.localize(source_date)
	target_time_zone = pytz.timezone( index[tz_to]['name'] )
	target_date_with_timezone = source_date_with_timezone.astimezone(target_time_zone)
	out = time.mktime(target_date_with_timezone.timetuple())
	return out

index = {
	"+0000": {
		"country": "CI",
		"name": "Africa/Abidjan",
		"offset": "+00:00",
		"offset2": "+0000",
		"status": "Canonical",
		"py": True
	},
	"+0300": {
		"country": "ET",
		"name": "Africa/Addis_Ababa",
		"offset": "+03:00",
		"offset2": "+0300",
		"status": "Alias",
		"py": True
	},
	"+0100": {
		"country": "DZ",
		"name": "Africa/Algiers",
		"offset": "+01:00",
		"offset2": "+0100",
		"status": "Canonical",
		"py": True
	},
	"+0200": {
		"country": "MW",
		"name": "Africa/Blantyre",
		"offset": "+02:00",
		"offset2": "+0200",
		"status": "Alias",
		"py": True
	},
	"-1000": {
		"country": "US",
		"name": "America/Adak",
		"offset": "-10:00",
		"offset2": "-1000",
		"status": "Canonical",
		"py": True
	},
	"-0900": {
		"country": "US",
		"name": "America/Anchorage",
		"offset": "-09:00",
		"offset2": "-0900",
		"status": "Canonical",
		"py": True
	},
	"-0400": {
		"country": "AI",
		"name": "America/Anguilla",
		"offset": "-04:00",
		"offset2": "-0400",
		"status": "Alias",
		"py": True
	},
	"-0300": {
		"country": "BR",
		"name": "America/Araguaina",
		"offset": "-03:00",
		"offset2": "-0300",
		"status": "Canonical",
		"py": True
	},
	"-0500": {
		"country": "CA",
		"name": "America/Atikokan",
		"offset": "-05:00",
		"offset2": "-0500",
		"status": "Canonical",
		"py": True
	},
	"-0600": {
		"country": "MX",
		"name": "America/Bahia_Banderas",
		"offset": "-06:00",
		"offset2": "-0600",
		"status": "Canonical",
		"py": True
	},
	"-0700": {
		"country": "US",
		"name": "America/Boise",
		"offset": "-07:00",
		"offset2": "-0700",
		"status": "Canonical",
		"py": True
	},
	"-0800": {
		"country": "MX",
		"name": "America/Ensenada",
		"offset": "-08:00",
		"offset2": "-0800",
		"status": "Deprecated",
		"py": True
	},
	"-0200": {
		"country": "BR",
		"name": "America/Noronha",
		"offset": "-02:00",
		"offset2": "-0200",
		"status": "Canonical",
		"py": True
	},
	"-0100": {
		"country": "GL",
		"name": "America/Scoresbysund",
		"offset": "-01:00",
		"offset2": "-0100",
		"status": "Canonical",
		"py": True
	},
	"-0330": {
		"country": "CA",
		"name": "America/St_Johns",
		"offset": "-03:30",
		"offset2": "-0330",
		"status": "Canonical",
		"py": True
	},
	"+1100": {
		"country": "AQ",
		"name": "Antarctica/Casey",
		"offset": "+11:00",
		"offset2": "+1100",
		"status": "Canonical",
		"py": True
	},
	"+0700": {
		"country": "AQ",
		"name": "Antarctica/Davis",
		"offset": "+07:00",
		"offset2": "+0700",
		"status": "Canonical",
		"py": True
	},
	"+1000": {
		"country": "AQ",
		"name": "Antarctica/DumontDUrville",
		"offset": "+10:00",
		"offset2": "+1000",
		"status": "Canonical",
		"py": True
	},
	"+0500": {
		"country": "AQ",
		"name": "Antarctica/Mawson",
		"offset": "+05:00",
		"offset2": "+0500",
		"status": "Canonical",
		"py": True
	},
	"+1200": {
		"country": "AQ",
		"name": "Antarctica/McMurdo",
		"offset": "+12:00",
		"offset2": "+1200",
		"status": "Alias",
		"py": True
	},
	"+0600": {
		"country": "AQ",
		"name": "Antarctica/Vostok",
		"offset": "+06:00",
		"offset2": "+0600",
		"status": "Canonical",
		"py": True
	},
	"+0400": {
		"country": "AZ",
		"name": "Asia/Baku",
		"offset": "+04:00",
		"offset2": "+0400",
		"status": "Canonical",
		"py": True
	},
	"+0800": {
		"country": "BN",
		"name": "Asia/Brunei",
		"offset": "+08:00",
		"offset2": "+0800",
		"status": "Canonical",
		"py": True
	},
	"+0530": {
		"country": "IN",
		"name": "Asia/Calcutta",
		"offset": "+05:30",
		"offset2": "+0530",
		"status": "Deprecated",
		"py": True
	},
	"+0900": {
		"country": "RU",
		"name": "Asia/Chita",
		"offset": "+09:00",
		"offset2": "+0900",
		"status": "Canonical",
		"py": True
	},
	"+0430": {
		"country": "AF",
		"name": "Asia/Kabul",
		"offset": "+04:30",
		"offset2": "+0430",
		"status": "Canonical",
		"py": True
	},
	"+0545": {
		"country": "NP",
		"name": "Asia/Kathmandu",
		"offset": "+05:45",
		"offset2": "+0545",
		"status": "Canonical",
		"py": True
	},
	"+0630": {
		"country": "MM",
		"name": "Asia/Rangoon",
		"offset": "+06:30",
		"offset2": "+0630",
		"status": "Deprecated",
		"py": True
	},
	"+0330": {
		"country": "IR",
		"name": "Asia/Tehran",
		"offset": "+03:30",
		"offset2": "+0330",
		"status": "Canonical",
		"py": True
	},
	"+0930": {
		"country": "AU",
		"name": "Australia/Adelaide",
		"offset": "+09:30",
		"offset2": "+0930",
		"status": "Canonical",
		"py": True
	},
	"+0845": {
		"country": "AU",
		"name": "Australia/Eucla",
		"offset": "+08:45",
		"offset2": "+0845",
		"status": "Canonical",
		"py": True
	},
	"+1030": {
		"country": "AU",
		"name": "Australia/LHI",
		"offset": "+10:30",
		"offset2": "+1030",
		"status": "Deprecated",
		"py": True
	},
	"-1100": {
		"country": "",
		"name": "Etc/GMT+11",
		"offset": "-11:00",
		"offset2": "-1100",
		"status": "Canonical",
		"py": True
	},
	"-1200": {
		"country": "",
		"name": "Etc/GMT+12",
		"offset": "-12:00",
		"offset2": "-1200",
		"status": "Canonical",
		"py": True
	},
	"+1300": {
		"country": "",
		"name": "Etc/GMT-13",
		"offset": "+13:00",
		"offset2": "+1300",
		"status": "Canonical",
		"py": True
	},
	"+1400": {
		"country": "",
		"name": "Etc/GMT-14",
		"offset": "+14:00",
		"offset2": "+1400",
		"status": "Canonical",
		"py": True
	},
	"+1245": {
		"country": "NZ",
		"name": "NZ-CHAT",
		"offset": "+12:45",
		"offset2": "+1245",
		"status": "Deprecated",
		"py": True
	},
	"-0930": {
		"country": "PF",
		"name": "Pacific/Marquesas",
		"offset": "-09:30",
		"offset2": "-0930",
		"status": "Canonical",
		"py": True
	}
}

