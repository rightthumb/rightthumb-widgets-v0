https://roll20.net/compendium/dnd5e/Spells%20List#content

$('.dropdown-toggle').click();

listResult booktemplate list open
subtitle redsubtitle




hackTool.hack.instructions = [
	{
		"name": "spells",
		"location": {
			"parent": ".listResult",
			"children": [
				{
					"name": "spell",
					"location": "h1",
					"type": "single",
					"settings": {}
				},
				{
					"name": "level",
					"location": ".redsubtitle :nth-child(1)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "fields",
					"location": ".single-list ul li",
					"type": "list",
					"settings": {}
				}
			]
		},
		"type": "records",
		"settings": {}
	}
]
hackTool.autoHack();
copy(  hackTool.payload.spells  )






hackTool.hack.instructions = [
	{
		"name": "spells",
		"location": {
			"parent": ".listResult",
			"children": [
				{
					"name": "Spell",
					"location": "h1",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Level",
					"location": ".redsubtitle :nth-child(1)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Casting_Time",
					"location": ".single-list ul li  :nth-child(1)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Range",
					"location": ".single-list ul li  :nth-child(2)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Components",
					"location": ".single-list ul li  :nth-child(3)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Duration",
					"location": ".single-list ul li  :nth-child(4)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Classes",
					"location": ".single-list ul li  :nth-child(5)",
					"type": "single",
					"settings": {}
				},
				{
					"name": "Classes",
					"location": ".single-list ul li :nth-child(6)",
					"type": "single",
					"settings": {}
				},
			]
		},
		"type": "records",
		"settings": {}
	}
]
hackTool.autoHack();
copy(  hackTool.payload.spells  )
