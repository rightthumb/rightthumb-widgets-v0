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


##################################################
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################


def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

_._default_settings_()
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def time_for_air(people, cubic_feet):
	# Assumes each person consumes 0.5 cubic feet of air per minute
	air_per_person_per_minute = 0.5
	total_air_consumed_per_minute = people * air_per_person_per_minute
	total_time_in_minutes = cubic_feet / total_air_consumed_per_minute
	hours = total_time_in_minutes / 60  # Convert minutes to hours
	return hours

def air_needed(people, time_str):
	# Assumes each person consumes 0.5 cubic feet of air per minute
	air_per_person_per_minute = 0.5
	
	# Parsing time_str to get total time in minutes
	total_minutes = 0
	time_units = {"sec": 1/60, "min": 1, "hr": 60}
	
	time_parts = time_str.split()
	for i in range(0, len(time_parts), 2):
		value = int(time_parts[i])
		unit = time_parts[i+1]
		total_minutes += value * time_units[unit]
	
	total_air_needed = people * air_per_person_per_minute * total_minutes
	return total_air_needed


def sequestration_needs(people, hours, cubic_feet):
	# Assumes each person produces 0.04 cubic feet of CO2 per minute
	co2_per_person_per_minute = 0.04
	total_co2_per_minute = people * co2_per_person_per_minute
	
	# Total time in minutes
	total_minutes = hours * 60
	
	# Total CO2 produced in cubic feet
	total_co2_produced = total_co2_per_minute * total_minutes
	
	# Calculate sequestration needs in cubic feet
	sequestration_needed = total_co2_produced
	
	return sequestration_needed

def sodium_bicarbonate_needed(people, hours, cubic_feet):
	# Constants
	co2_per_person_per_minute = 0.04  # Cubic feet of CO2 produced per person per minute
	molar_volume_co2 = 0.79  # Cubic feet per mole of CO2 at STP
	molar_mass_nahco3 = 84  # Grams per mole of NaHCO3
	
	# Total CO2 produced in cubic feet
	total_minutes = hours * 60
	total_co2_produced = people * co2_per_person_per_minute * total_minutes
	
	# Moles of CO2 produced
	moles_co2 = total_co2_produced / molar_volume_co2
	
	# Moles of NaHCO3 needed (2 moles of NaHCO3 per mole of CO2)
	moles_nahco3 = 2 * moles_co2
	
	# Mass of NaHCO3 needed in grams
	mass_nahco3_needed = moles_nahco3 * molar_mass_nahco3
	
	return mass_nahco3_needed

def oxygen_needed(people, hours):
	# Assumes each person consumes 0.84 cubic feet of oxygen per hour
	oxygen_per_person_per_hour = 0.84
	
	# Total oxygen needed in cubic feet
	total_oxygen_needed = people * oxygen_per_person_per_hour * hours
	
	return total_oxygen_needed

def oxygen_needed2(people, hours, cubic_feet):
	# Assumes each person consumes 0.84 cubic feet of oxygen per hour
	oxygen_per_person_per_hour = 0.84
	
	# Total oxygen needed in cubic feet
	total_oxygen_needed = people * oxygen_per_person_per_hour * hours
	
	# Calculate the oxygen deficit if the cubic feet available is less than needed
	oxygen_deficit = max(0, total_oxygen_needed - cubic_feet)
	
	return total_oxygen_needed, oxygen_deficit

# people = 5
# cubic_feet = 1500
# print(f"Air will last for {time_for_air(people, cubic_feet):.2f} hours.")

# time_str = "2 hr 30 min"
# print(f"Air needed: {air_needed(people, time_str):.2f} cubic feet.")


# people = 5
# cubic_feet = 1500
# hours = 10  # Duration for which the air needs to be breathable
# print(f"Sequestration needed: {sequestration_needs(people, cubic_feet, hours):.2f} cubic feet of CO2.")


# people = 5
# cubic_feet = 1500
# hours = 10  # Duration for which the air needs to be breathable
# print(f"Sodium bicarbonate needed: {sodium_bicarbonate_needed(people, cubic_feet, hours):.2f} grams.")


# people = 5
# hours = 10  # Duration for which oxygen needs to be calculated
# print(f"Oxygen needed: {oxygen_needed(people, hours):.2f} cubic feet.")


# people = 5
# hours = 10  # Duration for which oxygen needs to be calculated
# cubic_feet = 30  # Available cubic feet of air
# total_oxygen, oxygen_deficit = oxygen_needed2(people, hours, cubic_feet)

# print(f"Total oxygen needed: {total_oxygen:.2f} cubic feet.")
# if oxygen_deficit > 0:
#     print(f"Oxygen deficit: {oxygen_deficit:.2f} cubic feet.")
# else:
#     print("The available air is sufficient.")



def action2():
	people = 5
	cubic_feet = 1500
	result = time_for_air(people, cubic_feet)
	result = _.addComma2(result)
	print(f"{time_for_air(people, cubic_feet):.2f}")
	print(f"Air will last for {result} hours.")

	print()
	print()

	time_str = "2 hr 30 min"
	result = air_needed(people, time_str)
	result = _.addComma2(result)
	print(f"Air needed: {result} cubic feet.")

	print()
	print()

	people = 5
	cubic_feet = 1500
	hours = 10  # Duration for which the air needs to be breathable
	result = sequestration_needs(people, hours, cubic_feet)
	result = _.addComma2(result)
	print(f"{sequestration_needs(people, cubic_feet, hours):.2f}")
	print(f"Sequestration needed: {result} cubic feet of CO2.")

	print()
	print()

	people = 5
	cubic_feet = 1500
	hours = 10  # Duration for which the air needs to be breathable
	result = sodium_bicarbonate_needed(people, hours, cubic_feet)
	result = _.addComma2(result)
	print(f"{sodium_bicarbonate_needed(people, hours, cubic_feet):.2f}")
	print(f"Sodium bicarbonate needed: {result} grams.")

	print()
	print()

	people = 5
	hours = 10  # Duration for which oxygen needs to be calculated
	result = oxygen_needed(people, hours)
	result = _.addComma2(result)
	print(f"{oxygen_needed(people, hours):.2f}")
	print(f"Oxygen needed: {result} cubic feet.")

	print()
	print()

	people = 5
	hours = 10  # Duration for which oxygen needs to be calculated
	cubic_feet = 30  # Available cubic feet of air
	total_oxygen, oxygen_deficit = oxygen_needed2(people, hours, cubic_feet)

	print(f"{total_oxygen:.2f}")
	print(f"Total oxygen needed: {total_oxygen} cubic feet.")
	if oxygen_deficit > 0:
		print()
		print()
		print(f"{oxygen_deficit:.2f}")
		print(f"Oxygen deficit: {oxygen_deficit} cubic feet.")
	else:
		print("The available air is sufficient.")

def action():
	people = 5
	cubic_feet = 1500
	print(f"Air will last for {time_for_air(people, cubic_feet):.2f} hours.")

	print()
	print()

	time_str = "2 hr 30 min"
	print(f"Air needed: {air_needed(people, time_str):.2f} cubic feet.")

	print()
	print()

	people = 5
	cubic_feet = 1500
	hours = 10  # Duration for which the air needs to be breathable
	print(f"Sequestration needed: {sequestration_needs(people, cubic_feet, hours):.2f} cubic feet of CO2.")

	print()
	print()

	people = 5
	cubic_feet = 1500
	hours = 10  # Duration for which the air needs to be breathable
	print(f"Sodium bicarbonate needed: {sodium_bicarbonate_needed(people, cubic_feet, hours):.2f} grams.")

	print()
	print()

	people = 5
	hours = 10  # Duration for which oxygen needs to be calculated
	print(f"Oxygen needed: {oxygen_needed(people, hours):.2f} cubic feet.")

	print()
	print()

	people = 5
	hours = 10  # Duration for which oxygen needs to be calculated
	cubic_feet = 30  # Available cubic feet of air
	total_oxygen, oxygen_deficit = oxygen_needed2(people, hours, cubic_feet)

	print()
	print()
	
	print(f"Total oxygen needed: {total_oxygen:.2f} cubic feet.")
	if oxygen_deficit > 0:
		print()
		print()
		print(f"Oxygen deficit: {oxygen_deficit:.2f} cubic feet.")
	else:
		print("The available air is sufficient.")

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action(); _.isExit(__file__);

