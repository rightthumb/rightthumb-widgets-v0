# Variables

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# import _rightThumb._vars as _v


from pathlib import Path
import os
import _rightThumb._string as _str

# import md5

class myVars:

	def __init__(self):

		self.home = str(Path.home())
		self.computername = os.getenv('COMPUTERNAME')
		self.computername2 = self.computername.replace(' ','_')
		fileName = self.home + _v.slash+'.tk421'
		# print(computername,'HOME:',fileName)
		self.techDrive = open( fileName, 'r' ).read()
		self.techDrive = _str.totalStrip(self.techDrive)
		self.techFolder =  self.techDrive + ':\\tech'
		print()
		# scriptsFolder =  techFolder + _v.slash+'scripts'
		self.myHome =  self.techFolder + _v.slash+'hosts' + _v.slash + self.computername2
		self.thisHost =  'hosts' + _v.slash + self.computername2
		self.myIndexes = self.myHome + _v.slash+'indexes'
		self.myTables = self.myHome + _v.slash+'tables'

		self.stmp = self.myHome + _v.slash+'temp'
		self.tmpbat = self.stmp + _v.slash+'44E28BDF-8269-EEAE-D1DC-9B05B63E5F93.bat'
		self.tmpf = self.stmp + _v.slash+'{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}'
		self.tmpf0 = self.stmp + _v.slash+'{B820137A-79B8-45E3-BCBD-A6CAC50892D0}'
		self.tmpf1 = self.stmp + _v.slash+'{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}'
		self.tmpf2 = self.stmp + _v.slash+'{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}'
		self.tmpf3 = self.stmp + _v.slash+'{F139D191-FA1A-44D5-855C-7E5141B30E0D}'
		self.tmpf4 = self.stmp + _v.slash+'{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}'
		self.tmpf5 = self.stmp + _v.slash+'{201D82D6-2DC0-4552-A598-54F5481399A1}'
		self.tmpf6 = self.stmp + _v.slash+'{26B3B9C6-0A59-432A-9386-D432B53001CB}'
		self.tmpf7 = self.stmp + _v.slash+'{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}'
		self.tmpf8 = self.stmp + _v.slash+'{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}'
		self.tmpf9 = self.stmp + _v.slash+'{DF1D4EBC-838E-419C-9C58-943C1767391A}'
		self.myTemp = self.stmp
		self.tempFile = self.tmpf
		# self.tmpfb = self.tmpbat
		# indexFolder = indexRoot + _v.slash + self.computername + _v.slash+'index'+_v.slash
		self.myBookmarks = self.myHome + _v.slash+'bookmarks'
		# bookmarksFolder = techFolder + _v.slash+'scripts\\script-bookmarks\\MSI'+_v.slash
	def getUserProfile():
	# machineID = _v.getMachineID()
		os.system("echo %userprofile% >" + tempFile)
		output = open( tempFile, 'r' ).read()
		os.remove(tempFile)
		output = output.replace('\n','')
		output = output.replace('\r','')
		return output

	def getMachineID():
	# machineID = _v.getMachineID()
		import _rightThumb._md5 as _md5
		global tempFile
		os.system("wmic useraccount where (name='administrator' and domain='%computername%') get name,sid | find \"admin\" >" + tempFile)
		output = open( tempFile, 'r' ).read()
		os.remove(tempFile)
		output = _str.replaceAll(output, ' ','')
		output = _str.totalStrip(output)
		output = output.replace('administrator','')
		# print(output)
		md5 = _md5.md5(output)
		guid = _md5.md52GUID(md5,True)
		self.machineID = guid
		return guid

	def getDriveID(driveLetter):
		idFile = driveLetter + ':\drive.id.sys'
		# print(idFile)
		result = False
		if os.path.isfile(idFile) == True:
			driveID = open( idFile, 'r' ).read()
			driveID = driveID.replace(' ','')
			driveID = driveID.replace('\n','')
			driveID = driveID.replace('\r','')
			result = driveID
		return result

	def filePath(path):
		return 'file://' + os.path.realpath(path)

v = myVars()


