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
import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Location', '-l' )
	_.switches.register( 'Shrine', '-sh' )
	_.switches.register( 'Trial', '-t' )
	_.switches.register( 'Print', '-p' )
	_.switches.register( 'Done', '-d,-done' )
	_.switches.register( 'ToDo', '-todo' )
	_.switches.register( 'Completed', '-did' )
	_.switches.register( 'NoAsk', '-noask' )
	
def trigger_plus(data):
	# return data
	# _.pr(data)
	# sys.exit()
	return data.replace("'",'')

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'botw.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'The Legend of Zelda: Breath of the Wild, Shrine Tool',
	'categories': [
						'entertainment',
						'ent',
						'personal',
						'game',
						'gaming',
						'shrine',
						'botw',
						'zelda',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p botw -todo - side quest'),
						_.hp(''),
						_.hp('NOTE: green=done, yellow=todo'),
						_.hp(''),
						_.hp('p botw'),
						_.hp(''),
						_.hp('p botw -todo'),
						_.hp('p botw -did'),
						_.hp(''),
						_.hp('p botw -p 0'),
						_.hp('p botw + Naag'),
						_.hp('p botw  -t  + test strength'),
						_.hp('p botw  -l  + Hateno'),
						_.hp(''),
						_.hp('p botw -sh + Dagah Keek Shrine -p 0123'),
						_.hp(''),
						_.hp('p botw -todo -l + hyrule - side quest'),
						_.hp(''),
						_.hp('p botw -done -sh + kachta'),
						_.hp('p botw -did'),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	_.default_switch_trigger('Plus', trigger_plus)
	# _.switches.trigger( 'Plus', trigger_plus )
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


def load():
	global data
	global done
	done=_.getTableDB('botw.list')
	done=list(set(done))
	data = [
	{
		"Akkala": [
			{
				"Shrine": "Dah Hesho Shrine",
				"Trial": "A Minor Test of Strength",
				"Treasure": "Giant Ancient Core"
			},
			{
				"Shrine": "Katosa Aug Shrine",
				"Trial": "Katosa Aug Apparatus",
				"Treasure": "Great Frostblade"
			},
			{
				"Shrine": "Ke'nai Shakah Shrine",
				"Trial": "A Modest Test of Strength",
				"Treasure": "Sapphire"
			},
			{
				"Shrine": "Ritaag Zumo Shrine",
				"Trial": "Ritaag Zumo's Blessing / Into the Vortex",
				"Treasure": "Giant Ancient Core"
			},
			{
				"Shrine": "Tu Ka'loh Shrine",
				"Trial": "Lomei Labyrinth Island / Trial of the Labyrinth",
				"Treasure": "Ancient Core"
			},
			{
				"Shrine": "Tutsuwa Nima Shrine",
				"Trial": "A Major Test of Strength / The Spring of Power",
				"Treasure": "Flamespear"
			},
			{
				"Shrine": "Ze Kasho Shrine",
				"Trial": "Ze Kasho Apparatus",
				"Treasure": "Silverscale Spear"
			},
			{
				"Shrine": "Zuna Kai Shrine",
				"Trial": "Zuna Kai's Blessing / The Skull's Eye",
				"Treasure": "Flame Blade"
			}
		]
	},
	{
		"Central Hyrule": [
			{
				"Shrine": "Dah Kaso Shrine",
				"Trial": "A Minor Test of Strength",
				"Treasure": "Ancient Core"
			},
			{
				"Shrine": "Kaam Ya'tak Shrine",
				"Trial": "Trial of Power",
				"Treasure": "Edge of Duality\nSilver Rupee\nDiamond"
			},
			{
				"Shrine": "Katah Chuki Shrine",
				"Trial": "A Minor Test of Strength",
				"Treasure": "Royal Halberd"
			},
			{
				"Shrine": "Namika Ozz Shrine",
				"Trial": "A Modest Test of Strength",
				"Treasure": "Frostspear"
			},
			{
				"Shrine": "Noya Neha Shrine",
				"Trial": "A Minor Test of Strength",
				"Treasure": "Royal Shield"
			},
			{
				"Shrine": "Rota Ooh Shrine",
				"Trial": "Passing of the Gates",
				"Treasure": "Feathered Edge"
			},
			{
				"Shrine": "Saas Ko'sah Shrine",
				"Trial": "A Major Test of Strength",
				"Treasure": "Flameblade"
			},
			{
				"Shrine": "Wahgo Katta Shrine",
				"Trial": "Metal Connections",
				"Treasure": "Amber"
			}
		]
	},
	{
		"Dueling Peaks": [
			{
				"Shrine": "Bosh Kala Shrine",
				"Trial": "The Wind Guides You",
				"Treasure": "Soldier's Claymore\nAmber"
			},
			{
				"Shrine": "Ha Dahamar Shrine",
				"Trial": "The Water Guides",
				"Treasure": "Purple Rupee"
			},
			{
				"Shrine": "Hila Rao Shrine",
				"Trial": "Shrine Quest - Watch out for the Flowers\nDrifting",
				"Treasure": "Opal\nIce Arrows (x5)Opal"
			},
			{
				"Shrine": "Lakna Rokee Shrine",
				"Trial": "Shrine Quest - The Stolen Heirloom\nLanka Rokee's Blessing",
				"Treasure": "Edge of Duality"
			},
			{
				"Shrine": "Ree Dahee Shrine",
				"Trial": "Timing is Critical",
				"Treasure": "Climber's Bandana"
			},
			{
				"Shrine": "Shee Vaneer Shrine",
				"Trial": "Twin Memories",
				"Treasure": "Eightfold Longblade"
			},
			{
				"Shrine": "Shee Venath Shrine",
				"Trial": "Twin Memories",
				"Treasure": "Serpentine Spear"
			},
			{
				"Shrine": "Ta'loh Naeg Shrine",
				"Trial": "Ta'loh Naeg's Teaching",
				"Treasure": "Eightfold Longblade\nOpal\nShield of the Mind's EyeOpal"
			},
			{
				"Shrine": "Toto Sah Shrine",
				"Trial": "Toto Sah Apparatus",
				"Treasure": "Shield of the Mind's Eye"
			}
		]
	},
	{
		"Eldin": [
			{
				"Shrine": "Daqa Koh Shrine",
				"Trial": "Stalled Flight",
				"Treasure": "Silver Rupee"
			},
			{
				"Shrine": "Gorae Torr Shrine",
				"Trial": "Shrine Quest - The Gut Check Challenge\nGorae Torr's Blessing",
				"Treasure": "Great Frostblade"
			},
			{
				"Shrine": "Kayra Mah Shrine",
				"Trial": "Shrine Quest - A Brother's Roast\nGreedy Hill",
				"Treasure": "Ruby"
			},
			{
				"Shrine": "Mo'a Keet Shrine",
				"Trial": "Metal Makes a Path",
				"Treasure": "Knight's Broadsword"
			},
			{
				"Shrine": "Qua Raym Shrine",
				"Trial": "A Balanced Approach",
				"Treasure": "Knight's Claymore"
			},
			{
				"Shrine": "Sah Dahaj Shrine",
				"Trial": "Power of Fire",
				"Treasure": "Knight's Bow"
			},
			{
				"Shrine": "Shae Mo'sah Shrine",
				"Trial": "Swinging Flames",
				"Treasure": "Stone Smasher\nRuby\nIce Arrows x10"
			},
			{
				"Shrine": "Shora Hah Shrine",
				"Trial": "Blue Flame",
				"Treasure": "Giant Ancient Core\nGreat Flameblade\nSilver Rupee\nIce Arrows"
			},
			{
				"Shrine": "Tah Muhl Shrine",
				"Trial": "Shrine Quest - A Landscape of a Stable\nPassing The Flame",
				"Treasure": "Cobble Crusher\nOpal\nRuby"
			}
		]
	},
	{
		"Faron": [
			{
				"Shrine": "Kah Yah Shrine",
				"Trial": "Shrine Quest - A Fragmented Monument\nQuick Thinking",
				"Treasure": "Royal Claymore"
			},
			{
				"Shrine": "Korgu Chideh Shrine",
				"Trial": "Shrine Quest - Stranded on Eventide\nKorgu Chideh's Blessing",
				"Treasure": "Gold Rupee"
			},
			{
				"Shrine": "Muwo Jeem Shrine",
				"Trial": "A Modest Test of Strength",
				"Treasure": "Royal Bow"
			},
			{
				"Shrine": "Qukah Nata Shrine",
				"Trial": "Shrine Quest - Song of Storms\nQukah Nata's Blessing",
				"Treasure": "Rubber Tights"
			},
			{
				"Shrine": "Shai Utoh Shrine",
				"Trial": "Halt the Tilt",
				"Treasure": "Traveler's Sword\nAncient Core"
			},
			{
				"Shrine": "Shoda Sah Shrine",
				"Trial": "Impeccable Timing",
				"Treasure": "Ice Arrow x5"
			},
			{
				"Shrine": "Tawa Jinn Shrine",
				"Trial": "Shrine Quest - The Three Giant Brothers\nTawa Jinn's Blessing",
				"Treasure": "Great Thunderblade"
			},
			{
				"Shrine": "Yah Rin Shrine",
				"Trial": "A Weighty Decision",
				"Treasure": "Knight's Broadsword\nOpal"
			}
		]
	},
	{
		"Gerudo Highlands": [
			{
				"Shrine": "Joloo Nah Shrine",
				"Trial": "Shrine Quest - Test of Will\nJoloo Nah Apparatus",
				"Treasure": "Golden Claymore\nGerudoSpear "
			},
			{
				"Shrine": "Keeha Yoog Shrine",
				"Trial": "Shrine Quest - Cliffside Etchings\nKeeha Yoog's Blessing",
				"Treasure": "Diamond"
			},
			{
				"Shrine": "Kema Kosassa Shrine",
				"Trial": "A Major Test of Strength",
				"Treasure": "Silver Rupee"
			},
			{
				"Shrine": "Kuh Takkar Shrine",
				"Trial": "Melting Ice Hazard",
				"Treasure": "Frostblade"
			},
			{
				"Shrine": "Sasa Kai Shrine",
				"Trial": "Shrine Quest - Sign of the Shadow\nA Modest Test of Strength",
				"Treasure": "Frostblade"
			},
			{
				"Shrine": "Sho Dantu Shrine",
				"Trial": "Two Bombs",
				"Treasure": "Silver Rupee"
			}
		]
	},
	{
		"Gerudo Wasteland": [
			{
				"Shrine": "Dako Tah Shrine",
				"Trial": "Electric Path",
				"Treasure": "Moonlight Scimitar\nAncient Core\nSilver Rupee\nRadiant Shield"
			},
			{
				"Shrine": "Daqo Chisay Shrine",
				"Trial": "The Whole Picture",
				"Treasure": "Thunderblade"
			},
			{
				"Shrine": "Dila Maag Shrine",
				"Trial": "Shrine Quest - South Lomei Labyrinth\nDila Maag's Blessing",
				"Treasure": "Barbarian Armor Piece"
			},
			{
				"Shrine": "Hawa Koth Shrine",
				"Trial": "The Current Solution",
				"Treasure": "Ancient Core\nGold Rupee\nSapphire"
			},
			{
				"Shrine": "Jee Noh Shrine",
				"Trial": "On the Move",
				"Treasure": "Opal"
			},
			{
				"Shrine": "Kay Noh Shrine",
				"Trial": "Power of Electricity",
				"Treasure": "Gerudo Scimitar"
			},
			{
				"Shrine": "Kema Zoos Shrine",
				"Trial": "A Delayed Puzzle",
				"Treasure": "Moonlight Scimitar"
			},
			{
				"Shrine": "Korsh O'hu Shrine",
				"Trial": "Shrine Quest - The Seven Heroines\nKorsh O'hu's Blessing",
				"Treasure": "Flamespear"
			},
			{
				"Shrine": "Misae Suma Shrine",
				"Trial": "Shrine Quest - The Perfect Drink\nMisae Suma's Blessing",
				"Treasure": "Diamond"
			},
			{
				"Shrine": "Raqa Zunzo Shrine",
				"Trial": "Shrine Quest - The Undefeated Champ\nRaqa Zunzo's Blessing",
				"Treasure": "Radiant Shield"
			},
			{
				"Shrine": "Suma Sahma Shrine",
				"Trial": "Snow Shrine",
				"Treasure": "Moonlight Scimitar"
			},
			{
				"Shrine": "Tho Kayu Shrine",
				"Trial": "Tho Kayu's Blessing",
				"Treasure": "Golden Bow"
			}
		]
	},
	{
		"Great Hyrule Forest": [
			{
				"Shrine": "Daag Chokah Shrine",
				"Trial": "Shrine Quest - The Lost Pilgrimage\nDaag Chokah's Blessing",
				"Treasure": "Ancient Core"
			},
			{
				"Shrine": "Keo Ruug Shrine",
				"Trial": "Fateful Stars",
				"Treasure": "Knight's Claymore"
			},
			{
				"Shrine": "Ketoh Wawai Shrine",
				"Trial": "Side Quest - Shrouded Shrine\nKetoh Wawai's Blessing",
				"Treasure": "Ancient Core"
			},
			{
				"Shrine": "Kuhn Sidajj Shrine",
				"Trial": "Side Quest - Trial of Second Sight\nKuhn Sidajj's Blessing",
				"Treasure": "Giant Ancient Core"
			},
			{
				"Shrine": "Maag Halan Shrine",
				"Trial": "Side Quest - The Test of Wood\nMaag Halan's Blessing",
				"Treasure": "Giant Ancient Core"
			},
			{
				"Shrine": "Mirro Shaz Shrine",
				"Trial": "Tempered Power",
				"Treasure": "(2) Iron Sledgehammer\nGiant Ancient Core"
			},
			{
				"Shrine": "Monya Toma Shrine",
				"Trial": "Drawing Parabolas",
				"Treasure": "Thunderblade"
			},
			{
				"Shrine": "Rona Kachta Shrine",
				"Trial": "Rona Kachta's Blessing",
				"Treasure": "Great Flameblade"
			}
		]
	},
	{
		"Great Plateau": [
			{
				"Shrine": "Ja Baij Shrine",
				"Trial": "Bomb Trial",
				"Treasure": "Remote Bombs Rune\nTraveler's Claymore\nAmber"
			},
			{
				"Shrine": "Keh Namut Shrine",
				"Trial": "Cryonis Trial",
				"Treasure": "Cryonis Rune\nTraveler's Spear"
			},
			{
				"Shrine": "Oman Au Shrine",
				"Trial": "Magnesis Trial",
				"Treasure": "Magnesis Rune\nTraveler's Bow"
			},
			{
				"Shrine": "Owa Daim Shrine",
				"Trial": "Stasis Trial",
				"Treasure": "Stasis Rune\nTraveler's Shield\nIron Sledgehammer"
			}
		]
	},
	{
		"Hateno": [
			{
				"Shrine": "Chaas Qeta Shrine",
				"Trial": "Major Test of Strength",
				"Treasure": "Climbing Gear"
			},
			{
				"Shrine": "Dow Na'eh Shrine",
				"Trial": "Three Boxes",
				"Treasure": "Zora SwordZora Sword\nZora SwordAmber\nOpal"
			},
			{
				"Shrine": "Jitan Sa'mi Shrine",
				"Trial": "Shrine Quest - The Spring of Wisdom",
				"Treasure": "Frostspear"
			},
			{
				"Shrine": "Kam Urog Shrine",
				"Trial": "Shrine Quest - A Cursed Statue\nTrial of Passage",
				"Treasure": "Soldier's Spear\nOpal"
			},
			{
				"Shrine": "Mezza Lo Shrine",
				"Trial": "Shrine Quest - The Crowned Beast\nAncient Trifecta",
				"Treasure": "Thunderblade"
			},
			{
				"Shrine": "Myahm Agana Shrine",
				"Trial": "Myahm Agana Apparatus",
				"Treasure": "Phrenic Bow"
			},
			{
				"Shrine": "Tahno O'ah Shrine",
				"Trial": "Shrine Quest - Secret of the Cedars\nTahno O'ah's Blessing",
				"Treasure": "Climbing Boots"
			}
		]
	},
	{
		"Hebra": [
			{
				"Shrine": "Dunba Taag Shrine",
				"Trial": "Build and Release",
				"Treasure": "Falcon Bow\nGreat Thunderblade"
			},
			{
				"Shrine": "Gee Ha'rah Shrine",
				"Trial": "Tandem",
				"Treasure": "Diamond"
			},
			{
				"Shrine": "Goma Asaagh Shrine",
				"Trial": "A Major Test of Strength",
				"Treasure": "Royal Claymore"
			},
			{
				"Shrine": "Hia Miu Shrine",
				"Trial": "A Major Test of Strength",
				"Treasure": "Sapphire"
			},
			{
				"Shrine": "Lanno Kooh Shrine",
				"Trial": "Lanno Kooh's Blessing",
				"Treasure": "Gold Rupee"
			},
			{
				"Shrine": "Maka Rah Shrine",
				"Trial": "Steady Thy Heart",
				"Treasure": "10 Bomb Arrows\nAncient Core\nDiamond"
			},
			{
				"Shrine": "Mozo Shenno Shrine",
				"Trial": "Shrine Quest - The Bird in the Mountain\nA Major Test of Strength",
				"Treasure": "Diamond"
			},
			{
				"Shrine": "Qaza Tokki Shrine",
				"Trial": "Shrine Quest - Trial on the Cliff\nQaza Tokki's Blessing",
				"Treasure": "Barbarian Armor Piece"
			},
			{
				"Shrine": "Rin Oyaa Shrine",
				"Trial": "Directing the Wind",
				"Treasure": "Ancient Core"
			},
			{
				"Shrine": "Rok Uwog Shrine",
				"Trial": "Power of Reach",
				"Treasure": "Drillshaft"
			},
			{
				"Shrine": "Sha Gehma Shrine",
				"Trial": "Shift and Lock",
				"Treasure": "Royal Broadsword"
			},
			{
				"Shrine": "Shada Naw Shrine",
				"Trial": "Red Giveaway",
				"Treasure": "Great Frostblade"
			},
			{
				"Shrine": "To Quomo Shrine",
				"Trial": "To Quomo's Blessing",
				"Treasure": "Royal Claymore"
			}
		]
	},
	{
		"Lake": [
			{
				"Shrine": "Ishto Soh Shrine",
				"Trial": "Bravery's Grasp",
				"Treasure": "Topaz\nAncient Core"
			},
			{
				"Shrine": "Ka'o Makagh Shrine",
				"Trial": "Metal Doors Open the Way",
				"Treasure": "Traveler's Bow\nGold Rupee\nOpal"
			},
			{
				"Shrine": "Pumaag Nitae Shrine",
				"Trial": "A Minor Test of Strength",
				"Treasure": "Boomerang"
			},
			{
				"Shrine": "Shae Katha Shrine",
				"Trial": "Side Quest - The Serpent's Jaw\nShae Katha's Blessing",
				"Treasure": "Thunderspear"
			},
			{
				"Shrine": "Shoqa Tatone Shrine",
				"Trial": "A Modest Test of Strength",
				"Treasure": "Royal Broadsword"
			},
			{
				"Shrine": "Ya Naga Shrine",
				"Trial": "Shatter the Heavens",
				"Treasure": "Eightfold Blade"
			}
		]
	},
	{
		"Lanayru": [
			{
				"Shrine": "Dagah Keek Shrine",
				"Trial": "Shrine Quest - The Ceremonial Song\nDagah Keek's Blessing",
				"Treasure": "Silver Rupee"
			},
			{
				"Shrine": "Daka Tuss Shrine",
				"Trial": "Sunken Scoop",
				"Treasure": "Silver Longsword"
			},
			{
				"Shrine": "Kaya Wan Shrine",
				"Trial": "Shields From Water",
				"Treasure": "Ancient Core\nKnight's Broadsword"
			},
			{
				"Shrine": "Kah Mael Shrine",
				"Trial": "Drop and Rise",
				"Treasure": "Diamond"
			},
			{
				"Shrine": "Ne'ez Yohma Shrine",
				"Trial": "Pushing Power",
				"Treasure": "Zora Spear"
			},
			{
				"Shrine": "Rucco Maag Shrine",
				"Trial": "The Five Torches",
				"Treasure": "Opal\nSilver Bow"
			},
			{
				"Shrine": "Shai Yota Shrine",
				"Trial": "Shrine Quest - Master of the Wind\nShai Yota's Blessing",
				"Treasure": "Great Flameblade"
			},
			{
				"Shrine": "Sheh Rata Shrine",
				"Trial": "Speed of Light",
				"Treasure": "Opal\nGiant Boomerang"
			},
			{
				"Shrine": "Soh Kofi Shrine",
				"Trial": "A Minor Test of Strength",
				"Treasure": "Knight's Bow"
			}
		]
	},
	{
		"Ridgeland": [
			{
				"Shrine": "Mijah Rokee Shrine",
				"Trial": "Shrine Quest - Under a Red Moon\nA Modest Test of Strength",
				"Treasure": "Frostblade"
			},
			{
				"Shrine": "Maag No'rah Shrine",
				"Trial": "Maag No'rah's Blessing",
				"Treasure": "Silver Rupee"
			},
			{
				"Shrine": "Mogg Latan Shrine",
				"Trial": "Synced Swing",
				"Treasure": "Forest Dweller's Spear\nForest Dweller's Bow\nGold Rupee"
			},
			{
				"Shrine": "Shae Loya Shrine",
				"Trial": "Aim for the Moment",
				"Treasure": "Topaz\nFalcon Bow"
			},
			{
				"Shrine": "Sheem Dagoze Shrine",
				"Trial": "Shrine Quest - The Two Rings\nMoving in Parallel",
				"Treasure": "Great Thunderblade"
			},
			{
				"Shrine": "Toh Yahsa Shrine",
				"Trial": "Shrine Quest - Trial of Thunder\nBuried Secrets",
				"Treasure": "Rubber Armor\nOpalRubber Armor"
			},
			{
				"Shrine": "Zalta Wa Shrine",
				"Trial": "Two Orbs to Guide You",
				"Treasure": "Knight's Bow"
			}
		]
	},
	{
		"Tabantha": [
			{
				"Shrine": "Akh Va'quot Shrine",
				"Trial": "Windmills",
				"Treasure": "Ancient Core\nSapphire\nFeathered Spear"
			},
			{
				"Shrine": "Bareeda Naag Shrine",
				"Trial": "Shrine Quest - The Ancient Rito Song\nCannon",
				"Treasure": "Falcon Bow\nDiamond"
			},
			{
				"Shrine": "Kah Okeo Shrine",
				"Trial": "Wind Guide",
				"Treasure": "Korok Leaf\nGold Rupee\nForest Dweller's Sword\nThunderspear"
			},
			{
				"Shrine": "Sha Warvo Shrine",
				"Trial": "Path of Hidden Flights",
				"Treasure": "Purple Rupee\nKnight's Bow"
			},
			{
				"Shrine": "Tena Ko'sah Shrine",
				"Trial": "A Major Test of Strength",
				"Treasure": "Knight's Halberd"
			},
			{
				"Shrine": "Voo Lota Shrine",
				"Trial": "Shrine Quest - Recital at Warbler's Nest\nThe Winding Route",
				"Treasure": "Flameblade"
			}
		]
	}
]


last_loc=''

xXx = 'Shrine'
if 'ia' in _.switches.value('Print').lower() or '2' in _.switches.value('Print'):
	xXx += 'Trial'
if 'ea' in _.switches.value('Print').lower() or '3' in _.switches.value('Print'):
	xXx += 'Treasure'
if 'id' in _.switches.values('Print') or '0' in _.switches.value('Print'):
	xXx += 'ID'
if _.switches.isActive('Trial'):
	xXx += 'Trial'

printed=0
completed=0
loc_tally=0

def display(a,b):
	global done
	global completed
	global data
	global last_loc
	global xXx
	global printed
	global loc_tally

	loc=list(data[a].keys())[0]
	ID=data[a][loc][b]['id']
	shrine=data[a][loc][b]['Shrine']
	trial=data[a][loc][b]['Trial']
	treasure=data[a][loc][b]['Treasure']


	if _.switches.isActive('Minus'):
		if not _.showLine(str(data[a][loc][b]),plus=None,minus=_.switches.values('Minus')):
			return None

	if ID in done:
		completed+=1
		color='green'
	else:
		color='yellow'


	if _.switches.isActive('Done'):
		done.append( ID )
	if _.switches.isActive('ToDo'):
		if ID in done:
			return None

	if _.switches.isActive('Completed'):
		if not ID in done:
			return None


	# _.pv(data[a][loc])
	# sys.exit()
	if not loc == last_loc:
		if loc_tally:
			_.cp(loc_tally,'darkcyan')
		loc_tally=0
		last_loc=loc
		_.pr()
		_.pr()
		_.cp(loc,'darkcyan')
	if 'ID' in xXx:
		_.pr( '\t', _.cp( ID, 'white', p=0 ), _.cp( shrine, color, p=0 ) )     
	else:
		_.cp( [ '\t', shrine ], color )
	if 'Trial' in xXx:
		_.cp( [ '\t\t', trial.replace('\n',', ') ], 'cyan' )
	if 'Treasure' in xXx:
		_.cp( [ '\t\t', treasure.replace('\n',', ') ], 'purple' )
	printed+=1
	loc_tally+=1
	



def action():
	load()
	global done
	global data
	global printed

	if _.switches.isActive('Done') and len(_.switches.value('Done')):
		for d in _.switches.values('Done'):
			done.append( int(d) )
		_.saveTableDB(list(set(done)),'botw.list')
		_.cp('Saved','green')
		return None


	cnt=0
	for a,lo in enumerate(data):
		loc=list(data[a].keys())[0]
		for b,sh in enumerate(data[a][loc]):
			cnt+=1
			data[a][loc][b]['id']=cnt



	if _.switches.isActive('Location'):
		for a,lo in enumerate(data):
			loc=list(data[a].keys())[0]
			if _.showLine(loc):
				for b,sh in enumerate(data[a][loc]):
					display(a,b)
	elif _.switches.isActive('Trial'):
		for a,lo in enumerate(data):
			loc=list(data[a].keys())[0]
			for b,sh in enumerate(data[a][loc]):
				shrine=data[a][loc][b]['Shrine']
				trial=data[a][loc][b]['Trial']
				treasure=data[a][loc][b]['Treasure']
				if _.showLine(trial):
					display(a,b)
	elif _.switches.isActive('Shrine'):

		for a,lo in enumerate(data):
			loc=list(data[a].keys())[0]
			for b,sh in enumerate(data[a][loc]):
				shrine=data[a][loc][b]['Shrine']
				trial=data[a][loc][b]['Trial']
				treasure=data[a][loc][b]['Treasure']
				if _.showLine(shrine.replace("'",'')):
					display(a,b)

	else:

		for a,lo in enumerate(data):
			loc=list(data[a].keys())[0]
			for b,sh in enumerate(data[a][loc]):
				if _.showLine(str(data[a][loc][b])):
					display(a,b)
	global loc_tally
	if loc_tally:
		_.cp(loc_tally,'darkcyan')


	if printed == 120:
		_.pr('',printed)
	else:
		_.pr('',printed,'of',120)

	if _.switches.isActive('Done'):

		if printed == completed:
			_.cp('already in data set','red')
			sys.exit()

		if printed==0:
			_.cp('null set','red')
			sys.exit()
		if printed == 1:

			if _.switches.isActive('NoAsk'):
				_.saveTableDB(list(set(done)),'botw.list')
				_.cp('Saved','green')                
			else:
				ask=input('  Save? Y/n: ')
				_.pr()
				if not 'n' in ask.lower():
					_.saveTableDB(list(set(done)),'botw.list')
					_.cp('Saved','green')
				else:
					_.cp('did not save','red')

		elif not printed == 1:

			ask=input('  Save? y/N: ')
			_.pr()
			if 'y' in ask.lower():
				_.saveTableDB(list(set(done)),'botw.list')
				_.cp('Saved','green')
			else:
				_.cp('did not save','red')
	pass
	done=list(set(done))
	_.pr()
	_.cp( [ 'completed:', str(len(done))+',', 120-len(done), 'left' ], 'Background.light_blue' )
	_.pr()

# googled: zelda breath of the wild wiki shrines map
# https://www.ign.com/wikis/the-legend-of-zelda-breath-of-the-wild/Shrines#Lanayru

# def load():

'''
Plate with missing shrine:

Shoqa Tatone Shrine


'''



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()