import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-file,-files,-i,-in,-input','file.txt', isData='name', description='Files', isRequired=True, group='Files: Input / Output' )
	_.switches.register( 'SaveTo', '-save,-o,-out,-output', isRequired=False, group='Files: Input / Output' )
	_.switches.register( 'Repair', '-r,-repair,-fix', isRequired=False, group='Actions' )
	_.switches.register( 'Flush', '-flush', isRequired=False, group='Actions' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'named.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p named -f  sds.sh.db_bk -r -save sds.sh.db -flush'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start



import time
import dns.zone
import dns.rdatatype
from dns.exception import DNSException

def format_zone_file(input_file, domain, output_file=None):
	try:
		# Load the DNS zone file
		zone = dns.zone.from_file(input_file, origin=domain)

		# Header to match your cPanel format
		header = (
			f"; cPanel first:118.0.0 (update_time):{int(time.time())} Cpanel::ZoneFile::VERSION:1.3 hostname:teth.{domain}\n"
			f"; Zone file for {domain}\n"
			"$TTL 14400\n"
		)

		formatted_lines = [header]

		# Iterate through all records in the zone
		for name, node in zone.nodes.items():
			for rdataset in node.rdatasets:
				# Normalize TTL to 14400 for consistency
				rdataset.ttl = 14400

				# Filter and fix CNAME records
				if rdataset.rdtype == dns.rdatatype.CNAME and len(rdataset) > 1:
					rdataset = rdataset[:1]  # Keep only the first CNAME record

				for rdata in rdataset:
					# Format each DNS record
					record = f"{name}.{domain}.\t{rdataset.ttl}\tIN\t{dns.rdatatype.to_text(rdataset.rdtype)}\t{rdata}"
					formatted_lines.append(record)

		# Footer
		formatted_lines.append('; ----')
		formatted_lines.append('; EOF')
		formatted_lines.append('; ----')
		formatted_lines.append(';')
		formatted_lines.append("; ----------------------------------------------------------------------------")
		formatted_lines.append("; Repaired by: named.py")
		formatted_lines.append("; ----------------------------------------------------------------------------")
		formatted_lines.append(';')

		if output_file:
			# Save the formatted zone file
			with open(output_file, 'w') as f:
				f.write("\n".join(formatted_lines))
			print(f"Zone file formatted and saved to {output_file}")
		else:
			# Print the output if no file is specified
			print("\n".join(formatted_lines))

	except DNSException as e:
		print(f"Error processing zone file: {e}")








def flush_and_restart_named():
	import subprocess
	from os import path
	# Execute the rndc flush and reload commands
	try:
		subprocess.run(['sudo', 'rndc', 'flush'], check=True)
		subprocess.run(['sudo', 'rndc', 'reload'], check=True)
		print("rndc flush and reload completed successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Error occurred during rndc flush/reload: {e}")
	except Exception as e:
		print(f"Unexpected error: {e}")

	# Check and clear cache directories
	cache_dirs = [
		'/var/named/cache/*',
		'/var/named/ns_parse_cache/*',
		'/var/named/parse_cache/*',
		'/etc/bind/cache/*',
		'/etc/bind/ns_parse_cache/*',
		'/etc/bind/parse_cache/*',
	]

	for cache_dir in cache_dirs:
		if path.exists(path.dirname(cache_dir)):
			try:
				subprocess.run(['sudo', 'rm', '-rf', cache_dir], check=True)
				print(f"Cleared cache: {cache_dir}")
			except subprocess.CalledProcessError as e:
				print(f"Error clearing cache {cache_dir}: {e}")
			except Exception as e:
				print(f"Unexpected error clearing cache {cache_dir}: {e}")

	# Restart the named service
	try:
		subprocess.run(['sudo', 'systemctl', 'restart', 'bind9'], check=True)
		print("BIND service (bind9) restarted successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Error restarting BIND service: {e}")
	except Exception as e:
		print(f"Unexpected error restarting BIND service: {e}")










# sds.sh.db
def action():
	if _.switches.isActive('Repair'):
		for i,path in enumerate(_.isData(r=0)):
			if '/' in path:
				file = path.split('/')[-1]
			else:
				file = path
			ext = file.split('.')[-1]
			zone = file.replace('.'+ext,'')
			# fix_cname_records(path, zone)
			try:
				output_file = _.switches.values('SaveTo')[i]
			except:
				output_file = None
			format_zone_file(path, zone, output_file)
	if _.switches.isActive('Flush'): flush_and_restart_named()

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);