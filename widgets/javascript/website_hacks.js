
$(this).click(function() {});
$(document).ready(function() {});
throw new Error('Error');
try {} catch (err) {}
setTimeout(function() {}, 500);
setInterval(checkStuff, 1000);
for (var i = 0; i < data.length; i++) {}
$.each( data, function( key, val ) { });
Foo.caller.name Foo.caller.arguments
var keys = Object.keys(record);
JSON.stringify( data , null, '\t');
JSON.parse( data );
document.querySelector('#content-container')
document.querySelectorAll('.content-container')[0].remove()
document.getElementsByClassName('box')[0].getAttribute('rid')
document.getElementById('box-1').classList.contains('note')
document.getElementById('box-1').classList.remove('dragging');
document.getElementsByTagName('body')

$=document.querySelectorAll
////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////
ns0 = undefined;
ns0 = [];
ns0.g = [];
ns0.b = [];
var getKeys = function(name) { var obj = eval(name); var keys = []; for (var key in obj) { keys.push(name + '.' + key); } if (keys.length > 0) { for (var i = 0; i < keys.length; i++) { if (!keys[i].includes("$")) { eval("setTimeout(function(){try{getKeys(\"" + keys[i] + "\");} catch(e) { getKeysError(name); }},10);"); } else { getKeysError(name); } } } else { getKeysSuccess(name); } };
var getKeysSuccess = function(name) { var err = false; for (var i = 0; i < ns0.g.length; i++) { if (ns0.g[i] == name) { var err = true; } } if (!err) { ns0.g.push(name); } ns0.g.sort(); };
var getKeysError = function(name) { var err = false; for (var i = 0; i < ns0.g.length; i++) { if (ns0.g[i] == name) { var err = true; } } for (var i = 0; i < ns0.b.length; i++) { if (ns0.b[i] == name) { var err = true; } } if (!err) { ns0.b.push(name); } ns0.b.sort(); };
var getKeysError2 = function(name) { getKeysSuccess(name); };

function globals() { return this; }
var names = [];
for (var name in globals()) { names.push(name); } copy(names.toString().replace(/,/g, "\n"));
////////////////////////////////////////////////////////////////////////////////////
jQuery().jquery
window.open('http://rightthumb.com/projects/john/js/jquery.copycss.js', 'new')
window.open('http://www.pillerbeauty.com/js/jquery-1.11.3.js', 'new')
window.open('https://code.jquery.com/jquery-1.10.2.js', 'new')
//////////////////////////////////////
hackData = [];
document.querySelectorAll( '.random_word' ).forEach(function(item) {
    hackData.push( item.innerText );
});
//////////////////////////////////////
$('#random_words_count').val('3');
randomWordGenerator();
hackData = [];
document.querySelectorAll( '.random_word' ).forEach(function(item) {
    hackData.push( item.innerText );
});
console.log(hackData.join('-'));
copy(hackData.join('-'))
https://wordcounter.net/random-word-generator
//////////////////////////////////////
var array = []
var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')

for (var i = 0; i < checkboxes.length; i++) {
  array.push(checkboxes[i].value)
}
copy(array)
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
$('li').each(function() {
    $(this).attr('draggable', 'true');
    $(this).attr('ondragstart', 'dragStarted(event)');
    $(this).attr('ondragover', 'draggingOver(event)');
    $(this).attr('ondrop', 'dropped(event)');
});
//////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
hackData = '';
$('.stat--box h2')[1].innerText
$('.stat--box h2').each(function() {
    hackData += $(this).html();
});
copy(hackData)
//////////////////////////////////////
hackData = '';
$('table').each(function() {
	hackData += $(this).html();
});
copy(hackData)
//////////////////////////////////////
hackData = []
$('tr').each(function() {
    window.count = 0;
    $(this).find('td').each(function() {
        if ( !window.count ) {
            hackData.push( $(this).text() );
        }
        window.count++;
    });
});
copy(hackData)
//////////////////////////////////////
// https://docs.python.org/3/library/os.html
hackData = []
$('.sig-name.descname').each(function() {
    hackData.push($(this).text());
});
copy(hackData)
////////////////////////////////////// //////////////////////////////////////
hackData = []
$('h3').each(function() {
    hackData.push($(this).text());
});
copy(hackData)
////////////////////////////////////// //////////////////////////////////////
hackData = []
$('.data').each(function() {
	var test = $(this).text().toLowerCase();
	if ( test.indexOf('set ') && test.indexOf('creat') ) {
    	hackData.push($(this).text());
	}
});
copy(hackData)
//////////////////////////////////////
hackData = []
$('time').each(function() {
	hackData.push($(this).attr('datetime'));
});
copy(hackData)


//////////////////////////////////////
hackData = []
$('article').each(function() {
    var title = $(this).find('a').attr('title')
    var date = $(this).find('time').attr('datetime')
    hackData.push({ 'title': title, 'date': date });
});
copy(hackData)
//////////////////////////////////////
hackData = []
$('li').each(function() {
    var verse = $(this).find('h2').text();
    var text = $(this).find('.scripture').text();
    if ( verse.length && text.length )
        hackData.push({ 'verse': verse, 'text': text });
});
copy(hackData)
//////////////////////////////////////
hackData = 0;
$('tr').each(function() {
	hackData++;
});
console.log( 'count:', hackData );
//////////////////////////////////////

// https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512/item/seven-samurai-hollywoods-100-favorite-818479
https://www.listchallenges.com/top-1000-greatest-movies-of-all-time-by-imdb
function cleanSpaces(data) {
    var done = false;
    var incap = '9CE9B7A1-6BCE-1D46-FCA6-5CA95A8B13A4';
    data = incap + data + incap;
    while (!done) {
        data = data.replace('\n', ' ');
        data = data.replace('\t', ' ');
        data = data.replace('  ', ' ');

        if (!data.includes('  ') && !data.includes('\t') && !data.includes('\n') )
            done = true;

        if (data === ' ')
            data = '';

    }
    data = data.replace(incap + ' ', '');
    data = data.replace(' ' + incap, '');
    data = data.replace(incap, '');
    data = data.replace(incap, '');
    return data;
}
hackData = '';
$('.item-name').each(function() {
    hackData += cleanSpaces( $(this).text() )+'\n';
});
copy(hackData)

//////////////////////////////////////
const getMethods = (obj) => {
	let properties = new Set()
	let currentObj = obj
	do {
	Object.getOwnPropertyNames(currentObj).map(item => properties.add(item))
	} while ((currentObj = Object.getPrototypeOf(currentObj)))
	return [...properties.keys()].filter(item => typeof obj[item] === 'function')
}


function objToString (obj) {
	var str = '';
	for (var p in obj) {
		if (obj.hasOwnProperty(p)) {
			str += p + '::' + obj[p] + '\n';
		}
	}
	return str;
}
//////////////////////////////////////
hack_i = 0;
function hackChildren(that) {
	$(that).attr( 'hackID', hack_i );
	$(that).children().each(function() {
		hack_i++;
		hackChildren( $(this) );
	});
}
hackChildren('body');
console.log('Done',hack_i);
//////////////////////////////////////
hackData = []
hackSpent = []
$('a').each(function() {
	var thisTXT = $(this).text();
	var thisHREF = $(this).attr('href');
	if ( thisHREF !== '#' && !hackSpent.includes(thisHREF) ) {
		hackData.push({ 'label': thisTXT, 'href': thisHREF });
		hackSpent.push(thisHREF);
	}
});
copy(hackData)
//////////////////////////////////////   //////////////////////////////////////



$('div').mouseup(function() {
	var data=getSelectedLocation();
	console.log(data);
});

function getSelectedLocation() {
	return window.getSelection;
}​
window.getSelection().getRangeAt(0).startContainer.parentNode.getAttribute('profileid')

/////////////////////
window.getSelection().toString();


$('div').mouseup(function() {
	var text=getSelectedText();
	if (text!='') alert(text);
});

function getSelectedText() {
	if (window.getSelection) {
		return window.getSelection().toString();
	} else if (document.selection) {
		return document.selection.createRange().text;
	}
	return '';
}​

//////////////////////////////////////   //////////////////////////////////////

// Front End HTML AUDIT


hackData = {
		v: {},

		IDs: [],
		classes: [],
		attributes: [],
		indexes: {},
		records: [],
		temp: {
				'nextID': 0,
		},

		cleanSpaces: function(data) {
			var done = false;
			var incap = '9CE9B7A1-6BCE-1D46-FCA6-5CA95A8B13A4';
			data = incap + data + incap;
			while (!done) {
				data = data.replace('\n', ' ');
				data = data.replace('\t', ' ');
				data = data.replace('  ', ' ');

				if (!data.indexOf('  ') > -1 )
					done = true;

				if (data === ' ')
					data = '';

				if (data.indexOf('\n') > -1 )
					done = false;

				if (data.indexOf('\t') > -1 )
					done = false;

				if (data.indexOf('  ') > -1 )
					done = false;

			}
			data = data.replace(incap + ' ', '');
			data = data.replace(' ' + incap, '');
			data = data.replace(incap, '');
			data = data.replace(incap, '');
			return data;
			// hackData.cleanSpaces();
		}, //==============================================
		processChildren: function(that) {

			try {
				var theText = $(that).contents().get(0).nodeValue;
			} catch (err) {
				var theText = '';
			}

			var attibs = [];
			var attibsNames = [];
			var theKeys = [];
			var theID = '';
			var theClasses = [];

			theKeys = Object.keys( $(that)[0].attributes );
			for (var i = 0; i < theKeys.length; i++) {
				var thisAttr = $(that)[0].attributes[theKeys[i]];
				attibs.push({ 'name': thisAttr.name, 'value': thisAttr.value });
			}
			for (var i = 0; i < attibs.length; i++) {

				if ( !hackData.attributes.indexOf(attibs[i].name) > -1 ) {
					hackData.attributes.push( attibs[i].name );
				}

				if ( attibs[i].name === 'id' ) {
					theID = attibs[i].value;
					if ( !hackData.IDs.indexOf(attibs[i].value) > -1 ) {
						hackData.IDs.push( attibs[i].value );
					}
				} else if ( attibs[i].name === 'class' ) {
					theClasses = attibs[i].value.split(' ');
					for (var i = 0; i < theClasses.length; i++) {
						if ( !hackData.classes.indexOf(theClasses[i]) > -1 ) {
							hackData.classes.push( theClasses[i] );
						}
						
					}
				} else {
					attibsNames.push( attibs[i].name );
				}


			}


			var record = {
								'recordID': hackData.temp.nextID,
								'tag': $(that).prop('tagName'),
								'text': hackData.cleanSpaces(theText),
								'attrID': theID,
								'attrClasses': theClasses,
								'attributes': attibsNames,
								'attributesRecords': attibs,
								'childIDs': [],
								'childRecords': [],
								'parentID': null,
								'parentIDs': [],
			};
			hackData.temp.nextID++;
			var childRecords = [];


			$(that).children().each(function() {
				childRecords.push( hackData.processChildren(this) );
			});

			var childIDs = [];
			if ( childRecords.length ) {
				for (var ii = 0; ii < childRecords.length; ii++) {
					childIDs.push( childRecords[ii].recordID ); 
				}
			}
			record.childIDs = childIDs;
			hackData.records.push( record );
			return record;

			// hackData.processChildren();
		}, //==============================================
		findParent: function(theID) {
			for (var i = 0; i < hackData.records.length; i++) {
				if ( hackData.records[i].childIDs.indexOf( theID ) > -1 ) {
					return hackData.records[i].recordID;
				}
			}
			for (var i = 0; i < hackData.records.length; i++) {
				if ( hackData.records[i].childIDs.includes( theID ) ) {
					return hackData.records[i].recordID;
				}
			}

			for (var i = 0; i < hackData.records.length; i++) {
				for (var ii = 0; ii < hackData.records[i].childIDs.length; ii++) {
					if ( hackData.records[i].childIDs[ii] === theID ) {
						return hackData.records[i].recordID;
					}
				}

			}

			return null;
		}, //==============================================
		sort: function( arr, key, direction ) {
			direction = direction.toLowerCase();
			// var exec = 'a.'+key+' - b.'+key+';';
			var exec = 'arr.sort((a, b) => (a.'+key+' > b.'+key+') ? 1 : -1)'
			var data =  eval( exec );
			if ( direction.indexOf('d') > -1 ) {
				data.reverse();
			}
			return data;
		}, //==============================================
		process: function() {

			hackData.processChildren( 'body' );

			for (var i = 0; i < hackData.records.length; i++) {
				var theParent = hackData.findParent( hackData.records[i].recordID );
				hackData.records[i].parentID = theParent;

				var parentList = [];
				// parentList.push( theParent );
				var theParent = hackData.records[i].recordID;
				while ( typeof theParent === 'number' ) {
					theParent = hackData.findParent( theParent );
					if ( typeof theParent === 'number' ) { parentList.push( theParent ); }
				}



				// if ( typeof theParent === 'number' ) { parentList.push( theParent ); }
				// while ( typeof theParent === 'number' ) {
				//  theParent = hackData.findParent( parentList );
				//  if ( typeof theParent === 'number' ) { parentList.push( theParent ); }
				// }



				hackData.records[i].parentIDs = parentList;
			}

			hackData.records = hackData.sort( hackData.records, 'recordID', 'asc' );

			for (var i = 0; i < hackData.records.length; i++) {
				hackData.indexes[ hackData.records[i].recordID ] = i;
			}
			

			return hackData.records;
		}, //==============================================
		search: function(data) {
			data = data.toLowerCase();
			var records = [];

			for (var i = 0; i < hackData.records.length; i++) {
				var record = hackData.records[i];
				var text = record.text.toLowerCase();
				if ( text.indexOf(data) > -1 ) {
					records.push({ 'id': record.recordID, 'len': text.length })
				}
			}
			records = hackData.sort( records, 'len', 'asc' );

			if (!records.length)
				return null

			var subject = hackData.records[  hackData.indexes[ records[0].id ]  ];

			return subject;
		}, //==============================================
		nullFunction: function(data) {
			console.log(data);
			// hackData.three();
		} //==============================================
};


copy( hackData.process() )
copy( hackData.search('556601') )


//////////////////////////////////////   //////////////////////////////////////

hSelect = document.querySelectorAll('.VfPpkd-vQzf8d')

for (var i = hSelect.length - 1; i >= 0; i--) {
	var text = hSelect[i].outerText
    if ( text === 'Save' ) {
    	console.log(text);
    	simulateClick(hSelect[i]);
    }
}

//////////////////////////////////////
window.$ = function(selector) {
	var selectorType = 'querySelectorAll';

	if (selector.indexOf('#') === 0) {
		selectorType = 'getElementById';
		selector = selector.substr(1, selector.length);
	}

	return document[selectorType](selector);
};
var simulateClick = function(elem) {
	// Create our event (with options)
	var evt = new MouseEvent('click', {
		bubbles: true,
		cancelable: true,
		view: window
	});
	// If cancelled, don't dispatch our event
	var canceled = !elem.dispatchEvent(evt);
};
//////////////////////////////////////
hSelect = $('.VfPpkd-LgbsSe-OWXEXe-k8QpJ');

for (var i = hSelect.length - 1; i >= 0; i--) {
	var text = hSelect[i].outerText
	console.log(text);
	simulateClick(hSelect[i]);
}
simulateClick()
//////////////////////////////////////   //////////////////////////////////////
//////////////////////////////////////
hackData = {};
$('td.value').each(function() {
	hackData[$(this).text()] = 0;
});
$('td.value').each(function() {
	hackData[$(this).text()]++;
});
copy(hackData)
//////////////////////////////////////
// insert after comment
$(function() {
	$('#content-wrapper').contents().filter(function() {
		return this.nodeType == 8;
	}).each(function(i, e) {
		console.log($.trim(e.nodeValue));
		if ($.trim(e.nodeValue) == 'End of Main Content') {
			$('<div>here</div>').insertAfter(e);
			return false;
		}
	});
});
//////////////////////////////////////
// check certificate email log
// smtp2go.com

hackData = []

function lookupTimes(searchEmail) {
	searchEmail = searchEmail.toLowerCase();
	hackData = []
	$('tr').each(function(index) {
		if (index) {
			var datetime = $(this).find('.datetime').text();
			var email = $(this).find('.cell-recipient').text();
			email = email.toLowerCase();
			if (email.indexOf(searchEmail) > -1) {
				hackData.push(datetime);
				console.log(datetime);
			}

		}
	});

}
lookupTimes('Emerly75@gmail.com');
copy(hackData);







//////////////////////////////////////




$('.card').remove();
$('.row').remove();
$('<div>here</div>').insertAfter('.container-fluid');

$('.fa-laugh-wink').remove();
$('.sidebar-brand-icon').remove();
$('.sidebar-brand-text').remove();

$('.sidebar-brand').prepend('<img src="../images/logo.jpg" style="width:188px">');
$('h1').next().remove();
$('h1').text('Spreadsheet');
$('#content-wrapper .navbar-nav').remove();





$('.nav-item').each(function(index) {
	// if ( index === 0 ) {
	//     $(this).text( '0' );
	// }
	if (index === 1) {
		$(this).find('span').text('Columns');
	}
});




'#accordionSidebar ul li:nth-child(1n)'




$('').remove();



//////////////////////////////////////
// insert after comment
var url = "bla.css";
$(function() {
	$("head").contents().filter(function() {
		return this.nodeType == 8;
	}).each(function(i, e) {
		if ($.trim(e.nodeValue) == " End of Main Content ") {
			$('<link>', {
				rel: 'stylesheet',
				href: url
			}).insertAfter(e);
			return false; // stop immediately - remove if f.ex. url is an array of css
		}
	});
});
//////////////////////////////////////


hackData = [];

function setResults(data) {
	hackData = data;
	console.log(data);
}
$.ajax({
	url: 'https://api.duckduckgo.com/?q=DuckDuckGo&format=json',
	// data: { g: 'test', format: 'json' },
	dataType: 'jsonp',
	success: function(data) {
		setResults(data);

	}
});

// wait a sec then copy again
copy(hackData)




//////////////////////////////////////
found = false;

function textClean(text, oText, nText) {
	while (text.indexOf(oText) > -1) {
		text = text.replace(oText, nText);
	}
	return text;
}

$('td').each(function() {
	if (!found) {
		var thisTXT = $(this).text();
		if (thisTXT.indexOf('common name') > -1 && thisTXT.length < 200) {
			found = true;
			thisTXT = thisTXT.replace('common name(s)', '');
			thisTXT = textClean(thisTXT, '\n', ' ');
			thisTXT = textClean(thisTXT, '  ', ' ');
			console.log(thisTXT, thisTXT.length);
		}
	}
});

//////////////////////////////////////
$('h4 a').each(function() {
	var thisTXT = $(this).text();
	if (thisTXT.includes('Conquer')) {
		console.log(thisTXT);
		$(this).click();
	}
});
//////////////////////////////////////
$('a').each(function() {
	var thisTXT = $(this).text();
	var thisHREF = $(this).attr('href');
	if (thisHREF.indexOf('https://en.wikipedia.org/wiki/') > -1) {
		console.log({ 'label': thisTXT, 'href': thisHREF });
	}
});
//////////////////////////////////////
// https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9615&lvl=3&keep=1&srchmode=1&unlock&mod=1&log_op=modifier_toggle#modif
function hasNumber(myString) {
	return /\d/.test(myString);
}
hackData = []
hackDataAll = []
$('td').each(function() {
	var txt = $(this).text()
	hackDataAll.push(txt);
	if (txt.includes(' [')) {
		var txtX = txt.split(' [');
		var txtNew = txtX[0];
		if (!hasNumber(txtNew) && txtNew.length > 3 && !txtNew.includes('(')) {
			hackData.push(txtNew);
		}
	}
});
console.log('Good:', hackData.length, 'Total:', hackDataAll.length, 'Removed:', hackDataAll.length - hackData.length)
copy(hackData)
//////////////////////////////////////
hackData = []
$('p').each(function() {
	var txt = $(this).text();
	if (txt.includes('#') && txt.includes(')') && txt.includes(':')) {
		var txtX = txt.split(':');
		hackData.push(txtX[0]);
	}
});
copy(hackData)

////////////////////////////////////////////////////////////////////////////////////
$('h3').each(function() {
	console.log($(this).text());
});
////////////////////////////////////////////////////////////////////////////////////
hackData = []
$('.wikitable tr').each(function() {
	hackData.push({ 'move': $(this).find('td:nth-child(1)').text(), 'year': $(this).find('td:nth-child(2)').text() });
});
copy(hackData)
////////////////////////////////////////////////////////////////////////////////////
// https://www.complex.com/life/the-100-best-old-school-nintendo-games-dex/ring-king?utm_source=kw_fb&kwp_0=1375067&kwp_4=4349107&kwp_1=1829379
hackData = []
$('.article-list__slide').each(function() {
	hackData.push({ 'label': $(this).find('h2').text(), 'img': $(this).find('img').attr('src') });
});
copy(hackData)

////////////////////////////////////////////////////////////////////////////////////
hackData = []
$('table tr').each(function() {
	hackData.push({ 'ext': $(this).find('td:nth-child(1)').text(), 'description': $(this).find('td:nth-child(2)').text() });
});
copy(hackData)
////////////////////////////////////////////////////////////////////////////////////

// copyCSS

hackSelection = 'td';
$(hackSelection).copyCSS(hackSelection);
$(hackSelection + 'div').each(function() {
	$(this).copyCSS(this);
	$(this).children().each(function() {
		$(this).copyCSS(this);
	});
});
$(hackSelection).children().each(function() {
	$(this).copyCSS(this);
});

copy($(hackSelection)[0].outerHTML)

	**
	** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
	https: //uimagine.edu.au/cssout/
	**
	** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
	////////////////////////////////////////////////////////////////////////////////////
	hackSelection = '.js-cookie-banner-terminal';
hackCustom = '[hack=1]'
$(hackSelection).copyCSS(hackSelection);
$(hackSelection).attr('hack', '1');

$(hackCustom).removeAttr('id');
$(hackCustom).removeAttr('class');
$(hackCustom).children().each(function() {
	$(this).copyCSS(this);
	$(this).removeAttr('id');
	$(this).removeAttr('class');
});

copy($(hackCustom)[0].outerHTML)
////////////////////////////////////////////////////////////////////////////////////
var hackSelection = '.skins';
// $(hackSelection).copyCSS(hackSelection);
function processChildren(that) {
	that.children().each(function() {
				appName = {};
				appName.v = {};
				$.fn.listHandlers = function(events, outputFunction) {
					return this.each(function(i) {
						var elem = this,
							dEvents = $(this).data('events');
						if (!dEvents) { return; }
						$.each(dEvents, function(name, handler) {
							if ((new RegExp('^(' + (events === '*' ? '.+' : events.replace(',', '|').replace(/^on/i, '')) + ')$', 'i')).test(name)) {
								$.each(handler, function(i, handler) {
									appName.v.handler = handler;
									// handler.constructor.constructor.name
									outputFunction(elem, 'n' + i + ': [' + name + '] : ' + handler + ' objKeys: ' + Object.keys(handler));
								});
							}
						});
					});
				};

				// var hackSelection = '.tabsWidget';
				var hackAudit = 'onclick';

				function processChildren(that) {
					that.children().each(function() {
						$(this).listHandlers(hackAudit, console.info);
						processChildren($(this));
					});
				}
				$(hackSelection).listHandlers(hackAudit, console.info);
				processChildren($(hackSelection));





				// $('a').listHandlers('onclick', console.info);
				// $('#whatever').listHandlers('click',function(element,data){
				//     $('body').prepend('<br />' + element.nodeName + ': <br /><pre>' + data + '');
				// });
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				hack = {};
				hack.v = {};
				hack.form = {};
				hack.form.fields = {
					activate: 0,
					toHTML: {},
					asdf: function() {}, //==============================================
					audit: function(selection) {

						hack.v.field_profile = [];
						$(selection).each(function() {
							console.log('parent:', parent);
							if (parent !== 0) {
								hack.form.fields.thisChildren(this, $(this).attr('data-id'));
							}
						});
						var data = hack.v.field_profile;
						return data;
						// hack.form.fields.audit( '5a4a0974-dbeb-41b0-a010-34486fd28879' );
						// copy( hack.v.field_profile )
					}, //==============================================
					thisChildren: function(e, dID) {
						var profile = [];
						$(e).children().each(function() {
							// this.value
							var result = hack.form.fields.thisChild(this, dID);

							if (typeof result !== "boolean") {
								hack.v.field_profile.push(result);
							}

							hack.form.fields.thisChildren(this, dID);
						});
						return profile;
					}, //==============================================
					thisChild: function(e, dID) {
						var hasParent = false;
						var theID = '';
						var label = '';
						var theName = '';
						var exclude = ['DIV', 'SPAN', 'LI', 'OL', 'BUTTON'];
						var inc = ['INPUT', 'OPTION'];
						var tag = $(e).prop("tagName");
						var p0 = $(e).parent().attr('data-id');
						var p1 = $(e).parent().parent().parent().attr('data-id');
						// var parent = $( e ).parent().parent().attr( 'data-id' );
						var parent = '';
						console.log('X:', tag, parent, dID, p0, p1);
						if (!exclude.includes(tag) && inc.includes(tag)) {
							console.log(tag);
							var theType = '';
							var theValue = '';
							var theName = '';
							var isSelected = 0;

							if (tag === 'INPUT') {
								theType = $(e).attr('type');
								if (typeof $(e).attr('label') === 'undefined') { label = $(e).attr('name'); } else { label = $(e).attr('label'); }
							}

							try {
								if ($(e).val().length) {
									theValue = $(e).val();
								}
							} catch (error) {}

							if (theType === 'text' || theType === 'checkbox' || theType === 'radio') {

							}

							if (theType === 'checkbox' || theType === 'radio') {
								if ($(e).is(':checked')) {
									isSelected = 1;
								}
								if (typeof $(e).attr('label') === 'undefined') { label = $(e).attr('name'); } else { label = $(e).attr('label'); }
							}
							if (tag === 'OPTION') {
								hasParent = true;
								var parentID = parent = $(e).parent().attr('id');
								if ($(e).is(':selected ')) {
									isSelected = 1;
								}
								if (typeof $(e).attr('label') === 'undefined') { label = $(e).val(); } else { label = $(e).attr('label'); }
							}

							if (tag === 'SELECT') {
								theType = $(e).attr('type');
								if (typeof $(e).attr('label') === 'undefined') { label = $(e).val(); } else { label = $(e).attr('label'); }
							}


							if (typeof $(e).attr('id') !== 'undefined') { theID = $(e).attr('id'); }
							if (typeof $(e).attr('name') !== 'undefined') { theName = $(e).attr('name'); }



							if (hasParent) {
								return { 'tag': tag, 'name': theName, 'type': theType, 'value': theValue, 'isSelected': isSelected, 'label': label, 'id': theID, 'parentID': parentID };
							} else {
								return { 'tag': tag, 'name': theName, 'type': theType, 'value': theValue, 'isSelected': isSelected, 'label': label, 'id': theID };
							}

						} else {

							return false;
						}
						// hack.form.fields.thisChild();
					}, //==============================================
					restoreSingle: function(record, method) {

						if (record['tag'] === 'INPUT') {
							if (record['type'] === 'text') {
								$(hack.form.fields.findSelector(record)).val(record['value']);
							} else if (record['type'] === 'radio') {
								if (record['isSelected']) {
									$(hack.form.fields.findSelector(record)).attr('checked', true);
								} else {
									$(hack.form.fields.findSelector(record)).attr('checked', false);
								}
							} else if (record['type'] === 'checkbox') {
								if (record['isSelected']) {
									if (method === 'click') {
										if ($(hack.form.fields.findSelector(record)).is(':checked')) {} else {
											$(hack.form.fields.findSelector(record)).click();
										}
									} else {
										$(hack.form.fields.findSelector(record)).attr('checked', true);
									}
								} else {
									if (method === 'click') {
										if ($(hack.form.fields.findSelector(record)).is(':checked')) {
											$(hack.form.fields.findSelector(record)).click();
										} else {}
									} else {
										$(hack.form.fields.findSelector(record)).attr('checked', false);
									}
								}
							}
						} else if (record['tag'] === 'OPTION') {
							if (record['isSelected']) {
								$(hack.form.fields.findSelector(record)).attr('selected', 'selected');
							} else {
								$(hack.form.fields.findSelector(record)).attr('selected', '');
							}
						}




					}, //==============================================
					restore: function(records, method) {
						for (var i = records.length - 1; i >= 0; i--) {
							try {
								hack.form.fields.restoreSingle(records[i], method);
							} catch (err) {
								console.log('Error restore:', records[i]);
							}
						}
					}, //==============================================
					findSelector: function(record) {
						var selector = '';
						try {

							if (record['id'] === '') {
								if (record['tag'] === 'INPUT') {
									if (record['type'] === 'text') {} else if (record['type'] === 'radio') {} else if (record['type'] === 'checkbox') {}
								} else if (record['tag'] === 'OPTION') {}
							} else {
								selector = '#' + record['id'];
							}
						} catch (err) {
							console.log('Error findSelector:', record);
							return false;
						}
						// {
						//   "tag": "INPUT",
						//   "name": "",
						//   "type": "checkbox",
						//   "value": "on",
						//   "isSelected": 0,
						//   "id": "letter-zmq_checkbox"
						// }  
						console.log(selector);
						return selector;
						// hack.form.fields.findSelector( record )
					}, //==============================================
					null: function() {} //==============================================
				}
				// copy( hack.form.fields.audit( '.lvemanager-setting-item' ) );
				hack.form.fields.restore(hack.v.field_profile, 'click')
				// copy( hack.v.field_profile )
				// hack.form.fields.restore( hack.v.field_profile, 'click' )
				// $('#letter-bcmath').click();
				// $( '#letter-bcmath' ).is(':checked')
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				p savePages - i links.json

				hackData = []
				$('.season-episode-title a').each(function() {
					var data = {
						'label': cleanSpaces($(this).text()),
						'href': $(this).attr('href')
					}
					hackData.push(data);
				});

				function cleanSpaces(data) {
					var done = false;
					var incap = '9CE9B7A1-6BCE-1D46-FCA6-5CA95A8B13A4';
					data = incap + data + incap;
					while (!done) {
						data = data.replace('\n', ' ');
						data = data.replace('\t', ' ');
						data = data.replace('  ', ' ');

						if (!data.includes('  '))
							done = true;

						if (data === ' ')
							data = '';

					}
					data = data.replace(incap + ' ', '');
					data = data.replace(' ' + incap, '');
					data = data.replace(incap, '');
					data = data.replace(incap, '');
					return data;
				}
				copy(hackData)
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				////////////////////////////////////////////////////////////////////////////////////
				encodeURIComponent(uri);
				decodeURIComponent(uri_enc);
				try {} catch (err) {}
				document.getElementById('login-passwd').value
				setTimeout(function() { alert("Hello"); }, 3000);
				new Array()
				////////////////////////////////////////////////////////////////////////////////////
				hack = {}
				hack.v = {}
				hack.acquire = {
					data: [],
					spent: [],
					test: function() {
						$('.yg-list-title [data-rapid_p]').each(function() {
							console.log($(this).text());
						});
					}, //==============================================
					audit: function() {
						hack.acquire.data = [];
						hackData = []
						$('.yg-list-title [data-rapid_p]').each(function() {
							var href = hack.acquire.thisChildren(this, $(this).text());
							var data = { 'label': $(this).text(), 'href': $(this).attr('href'), 'children': [] };
							hack.acquire.data.push(data);
						});
						var result = hack.acquire.data;
						return result
						// copy( hack.acquire.audit() )
					}, //==============================================
					thisChildren: function(e, thePar) {
						$(e).children().each(function() {
							console.log($(this).prop("tagName"));
							// this.value
							var result = hack.acquire.thisChild(this, thePar);

							if (typeof result !== "boolean") {

								if (!hack.acquire.spent.includes(thePar)) {
									hack.acquire.spent.push(thePar);
									return result;
								}
							}

							hack.acquire.thisChildren(this, thePar);
						});

					}, //==============================================
					thisChild: function(e, thePar) {
						var tag = $(e).prop("tagName");
						console.log(tag);
						if (tag === 'A') {
							return $(e).attr('href');
						} else {
							return false;
						}
					} //==============================================
				}
				hack.acquire.test()
				copy(hack.acquire.audit())

				////////////////////////////////////////////////////////////////////////////////////















/*

    instructions:

        name: is the name of the field in the payload variable
        location: h1, #id, .class

        types:  recordDelim single list table tables

        settings per type:
            recordDelim
                no settings is NOT ok
                must have record
                delim is optional
                example { 'record': '\n' }
                example { 'delim': ':', 'record': '\n' }
                    \n is return carriage

            table
                no settings is ok
                can have nth
                    nth is what table number if multiple tables
                example { 'nth': '2' }
                example { 'nth': '2,3' }
                requires plugin: http://tools.rightthumb.com/js/hack/jquery.tabletojson.min.js
    
jQuery: http://tools.rightthumb.com/js/jquery-1.11.3.js
jQuery MIN (smaller size): http://tools.rightthumb.com/js/hack/jquery-3.4.1.min.js

app is configured to the below page to show you how it works
https://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/

*/



hack = {
    'data': {},
    'instructions': [
        {
            'name': 'recipe',
            'location': 'h1',
            'type': 'single',
            'settings': {}
        },
        {
            'name': 'meta',
            'location': '.two-subcol-content-wrapper',
            'type': 'recordDelim',
            'settings': { 'delim': ':', 'record': '\n' }
        },
        {
            'name': 'ingredients',
            'location': '.checkbox-list-checkmark',
            'type': 'list',
            'settings': {}
        },
    ]

};

function autoHack( hack ) {

    for (var iy = 0, len = hack['instructions'].length; iy < len; iy++) {
        try {
            var n = hack['instructions'][iy]['name'];
            var t = hack['instructions'][iy]['type'];
            var l = hack['instructions'][iy]['location'];
            var s = hack['instructions'][iy]['settings'];
            if (t === 'recordDelim') {
                preData = _str.cleanWhiteSpace( $(l).text() );

                if ( Object.keys(s).indexOf( 'delim' ) > -1 ) {
                    preData = _str.replaceAll( preData, s['delim']+s['record'], s['delim'] );
                    var prepData = preData.split(s['record']);
                    var field = {};
                    for (var i = 0; i < prepData.length; i++) {
                        var pre = prepData[i].split(s['delim']);
                        field[pre[0]] = pre[1];
                    }
                    hack['data'][n] = field;
                } else {
                    var prepData = preData.split(s['record']);
                    hack['data'][n] = [];
                    for (var i = 0; i < prepData.length; i++) {
                        if ( prepData[i].length )
                            hack['data'][n].push( prepData[i] );

                    }
                }
            }

            if (t === 'single') {
                hack['data'][n] = _str.removeWhiteSpace($(l).text());
            }

            if (t === 'list') {
                window.preDataX = [];
                $(l).each(function() {
                    window.preDataX.push( _str.removeWhiteSpace( $(this).text() ) );
                });

                hack['data'][n] = window.preDataX;
                delete window.preDataX;
            }

            if (t === 'table') {
                hack['data'][n] = [];

                if ( Object.keys(s).indexOf( 'nth' ) > -1 ) {
                    console.log( 'nth' )
                    window.myTables = [];
                    $('table').each(function() {
                        window.myTables.push( $(this).tableToJSON() );
                    });

                    for (var i = 0; i < window.myTables.length; i++) {
                        if ( s['nth'].split(',').indexOf( i.toString() ) > -1 ) {
                            console.log( s['nth'].split(','), i )
                            hack['data'][n].push( window.myTables[i] );
                        }
                    }
                } else {
                    console.log( 'NOT nth' )
                    $(l).each(function() {
                        hack['data'][n].push( $(this).tableToJSON() );
                    });
                }

            }

        } catch (err) { console.log(err); }
    }
}



_str = {
    records: [],
    tempID: '9CE9B7A1-6BCE-1D46-FCA6-5CA95A8B13A4',
    printable: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
    cleanWhiteSpace: function( data ) {
        data = _str.replaceAll( data, '\r', '\n' );
        data = _str.replaceAll( data, '\t', ' ' );
        data = _str.replaceAll( data, '  ', ' ' );
        data = _str.replaceAll( data, '\n ', '\n' );
        data = _str.replaceAll( data, '  ', ' ' );
        data = _str.replaceAll( data, '\n ', '\n' );
        data = _str.replaceAll( data, '\n\n', '\n' );
        data = _str.cleanBE( data, ' ' );
        data = _str.cleanBE( data, '\n' );
        data = _str.cleanBE( data, ' ' );
        data = _str.cleanBE( data, '\n' );
        return data;
    },
    replaceAll: function( data, what, to ) {
        while ( data.indexOf(what) > -1 ) {
            data = data.replace( what, to );
        }
        return data
    },
    cleanBE: function( data, what ) {
        data = _str.replaceAll( data, _str.tempID + what, '' );
        data = _str.replaceAll( data, what + _str.tempID, '' );
        data = _str.replaceAll( data, _str.tempID, '' );
        return data;
    },
    cleanCharBE: function( data ) {
        if ( _str.printable.indexOf( data[0] ) < 1 )
            data = data.substr(1);
        if ( _str.printable.indexOf( data[ data.length-1 ] ) < 1 )
            data = data.substring(0, data.length - 1);
        return data
    },
    removeWhiteSpace: function( data ) {
        data = _str.replaceAll( data, '\n', '' );
        data = _str.replaceAll( data, '\t', ' ' );
        data = _str.replaceAll( data, '  ', ' ' );
        data = _str.cleanBE( data, ' ' );
        data = _str.cleanBE( data, ' ' );
        data = _str.cleanCharBE( data );
        return data;
    },
    nullFunction: function( data ) {},
    //==============================================
};

autoHack(hack);
copy(hack['data'])



















				////////////////////////////////////////////////////////////////////////////////////

                    class cleanJob {
                        constructor( data ) {
                            this.data = data;
                            this.tempID = '9CE9B7A1-6BCE-1D46-FCA6-5CA95A8B13A4';
                            this.printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~';
                        }
                        isValid() {
                            if ( this.data.length ) {
                                return true;
                            } else {
                                return false;
                            }
                        }
                        payload() {
                            return this.data;
                        }
                        cleanWhiteSpace() {
                            this.replaceAll( '\r', '\n' );
                            this.replaceAll( '\t', ' ' );
                            this.replaceAll( '  ', ' ' );
                            this.replaceAll( '\n ', '\n' );
                            this.replaceAll( '  ', ' ' );
                            this.replaceAll( '\n ', '\n' );
                            this.replaceAll( '\n\n', '\n' );
                            this.cleanBE( ' ' );
                            this.cleanBE( '\n' );
                            this.cleanBE( ' ' );
                            this.cleanBE( '\n' );
                            return this.data;
                        }
                        replaceAll( what, to ) {
                            while ( this.data.indexOf(what) > -1 ) {
                                this.data.replace( what, to );
                            }
                            return this.data;
                        }
                        cleanBE( what ) {
                            this.replaceAll( this.tempID + what, '' );
                            this.replaceAll( what + this.tempID, '' );
                            this.replaceAll( this.tempID, '' );
                            return this.data;
                        }
                        cleanCharBE() {
                            if ( this.printable.indexOf( this.data[0] ) < 1 )
                                this.data = this.data.substr(1);
                            if ( this.printable.indexOf( this.data[ this.data.length-1 ] ) < 1 )
                                this.data = this.data.substring(0, this.data.length - 1);
                            return this.data;
                        }
                        removeWhiteSpace() {
                            this.replaceAll( '\n', '' );
                            this.replaceAll( '\t', ' ' );
                            this.replaceAll( '  ', ' ' );
                            this.cleanBE( ' ' );
                            this.cleanBE( ' ' );
                            this.cleanCharBE();
                            return this.data;
                        }
                    }

                        verse = new cleanJob( $(this).find('h2').text() );
                        if ( verse.isValid() )
                            hackData.push({ 'verse': verse.removeWhiteSpace() });
                        delete verse

                ////////////////////////////////////////////////////////////////////////////////////
				// hack title 



				function acquirePayload() {
					console.log('acquirePayload');
					hackElements = [];
					$('.card').each(function(index) {
						theLink = ''
						$(this).find('a').each(function(index) {
							var testLink = $(this).attr('href');
							if (testLink.includes('/store/')) { theLink = testLink; }
						});

						var thisName = $(this).find('.title').text().trim();
						var thisURL = 'https://play.google.com' + theLink;

						var thisDescription = $(this).find('.description').text().trim();
						var ts = $(this).find('.tiny-star').attr('aria-label').trim();
						try {
							var tss = ts.split(' ');
							var thisStars = tss[1];
						} catch (err) {
							var thisStars = '';
						}


						hackElements.push({ 'name': thisName, 'url': thisURL, 'description': thisDescription, 'stars': thisStars });
					});
					// copy( hackElements )

					console.log('');
					console.log('Done');
					console.log('');
					console.log('Execute:    copy( hackElements );');

				}

				function scrollEnd() {
					console.log('scrollEnd');
					setTimeout(function() {
						$('html, body').scrollTop($(document).height());
						setTimeout(function() {
							$('html, body').scrollTop($(document).height() - 1000);
							setTimeout(function() {
								$('html, body').scrollTop($(document).height());
								setTimeout(function() {

									if ($('#show-more-button').css('display') !== 'none') {
										$('#show-more-button').click();
										setTimeout(function() { scrollEnd(); }, 1500);
									} else {
										if (checkLen()) {
											setTimeout(function() { acquirePayload(); }, 1500);
										} else {
											setTimeout(function() { scrollEnd(); }, 1500);
										}
									}

								}, 1500);
							}, 1500);

						}, 1500);

					}, 1500);


				}


				function checkLen() {
					hackElements = [];
					$('.id-card-list .title').each(function(index) {
						hackElements.push($(this).text());
					});
					if (lastLength == hackElements.length) {
						return true;
					} else {
						lastLength = hackElements.length
						return false;
					}
				}



				lastLength = 0;

				setTimeout(function() { scrollEnd(); }, 800);

				// acquirePayload();
				// copy( hackElements );





				///////////////////////////////////
				hackElements = [];
				$('.id-card-list .title').each(function(index) {
					hackElements.push($(this).text())
				});
				copy(hackElements)



				////////////////////////////////////////////////////////////////////////////////////
				hackElements = [];

				function getOverflow(data) {
					hackElements.push(data + ' - ' + $(data).css('overflow'));

				}

				getOverflow('.body-content');

				copy(hackElements)
				////////////////////////////////////////////////////////////////////////////////////
				//google assistant save all pictures
				function saveAllPictures() {
					var test = document.getElementsByClassName('z4bHUc');
					test[test.length - 1].scrollIntoView();
					var buttons = document.getElementsByTagName('button');
					var ii = 0;
					for (var i = 0, len = buttons.length; i < len; i++) {
						if (buttons[i].textContent.includes('Save')) {
							buttons[i].click();
							ii++;
							console.log(ii);
						}
					}
					setTimeout(function() { saveAllPictures(); }, 800);

				}
				saveAllPictures();



				WpHeLc

				////////////////////////////////////////////////////////////////////////////////////
				jQuery().jquery
				window.open("http://www.pillerbeauty.com/js/jquery-1.11.3.js", "new")
				////////////////////////////////////////////////////////////////////////////////////

				hackElements = [];
				$('code').each(function(index) {
					hackElements.push($(this).text())
				});
				copy(hackElements)
				////////////////////////////////////////////////////////////////////////////////////

				hackElements = [];
				$('a').each(function(index) {
					hackElements.push($(this).text() + ' - ' + $(this).attr('href'))
				});
				copy(hackElements)

				////////////////////////////////////////////////////////////////////////////////////

				function acquirePayload() {
					var genre = '';
					var company = '';

					var links = document.querySelectorAll('a');
					for (var i = 0; i < links.length; i++) {
						if (links[i].href.includes('https://play.google.com/store/apps/dev?id=') || links[i].href.includes('https://play.google.com/store/apps/developer?id=')) {
							console.log(links[i].text.trim());
							company = links[i].text.trim();
							if (company.length > 0) {
								break
							}
						}
					};
					var links = document.querySelectorAll('a[itemprop="genre"]');
					genre = links[0].text.trim();

					return { 'g': genre, 'c': company }
				}
				copy(JSON.stringify(acquirePayload()) + '\n');

				////////////////////////////////////////////////////////////////////////////////////
				hackElements = [];
				$('a').each(function(index) {
					hackElements.push($(this.href).text())
				});


				hackElements = [];
				$('.actor-name').each(function(index) {
					hackElements.push($(this).text())
				});


				hackElements = [];
				$('.search-result__result-link').each(function(index) {
					hackElements.push({ 'name': $(this).find('.actor-name').text(), 'link': $(this).href })
				});
				////////////////////////////////////////////////////////////////////////////////////
				//LinkedIn people hack


				Things = []
				hackElements = [];

				function hackRegisterThing(name) {
					result = true
					for (var i = Things.length - 1; i >= 0; i--) {
						if (Things[i] === name) {
							result = false
						}
					}
					if (name === 'LinkedIn Member' || name === '') {
						result = false
					}
					if (result) {
						Things.push(name)
					}
					return result
				}

				function hackProcessPage() {
					$('.search-result').each(function(index) {
						if (hackRegisterThing($(this).find('.actor-name').text())) {
							hackElements.push({ 'name': $(this).find('.actor-name').text(), 'link': $(this).find('a').attr('href') })
						}
					});
				}

				function hackStart() {
					hackProcessPage();
					setTimeout(function() { hackNext(); }, 900);
				}

				function hackNext() {
					if ($('.next-text').length) {
						$('.next-text').click();
						setTimeout(function() { hackStart(); }, 900);
					}
				}
				hackStart()





				copy(hackElements)

				////////////////////////////////////////////////////////////////////////////////////
				var images = $$('img');
				for (each in images) {
					console.log(images[each].src);
				}
				////////////////////////////////////////////////////////////////////////////////////

				window.open("http://www.pillerbeauty.com/js/jquery-1.11.3.js", "new")

				////////////////////////////////////////////////////////////////////////////////////

				////////////////////////////////////// SCROLL TO BOTTOM OF PAGE


				done = false;

				function goToBottom() {
					window.scrollTo(0, document.body.scrollHeight);
					if (!done) {
						setTimeout(function() { goToBottom(); }, 800);
					}
				}
				goToBottom();


				done = true;

				////////////////////////////////////////////////////////////////////////////////////

				hackElements = [];

				function goGetem() {
					$('[draggable]').each(function(index) {
						hackElements.push({ 'name': $(this).find('._sd').text(), 'count': $(this).find('span').text() });
					});
					// goGetemAgain();
				}
				goGetem()
				console.log(hackElements.length)
				copy(hackElements)

				////////////////////////////////////////////////////////////////////////////////////
				$('.pinWrapper').each(function(index) {
					console.log($(this).text())
				})
				////////////////////////////////////////////////////////////////////////////////////
				// pinterest boards

				window.open("http://www.pillerbeauty.com/js/jquery-1.11.3.js", "new")


				hackElements = [];
				hackElementsTitles = [];
				$('.Hsu').each(function(index) {
					var title = '';
					var data = '';
					if ($(this).find('[title]').attr('class') === 'tBJ dyH iFc SMy SNs pBj DrD IZT mWe z-6') {
						if (!hackElements.includes($(this).find('[title]').attr('title'))) {
							var title = $(this).find('[title]').attr('title');


						}
					}
					if (!hackElementsTitles.includes(title) && title.length > 0) {
						hackElementsTitles.push(title)
						var data = $(this).text();
						if (data.includes('Secret')) {
							var status = 'Secret'
						} else {
							var status = 'Public'
						}

						var pinRaw = data.split('board');
						var pins0 = pinRaw[1];
						var pins = "0";
						try {
							var pins1 = pins0.split(' Pin');
							var pins = pins1[0];

						} catch (err) {
							var pins = pins0;
						}
						// pins = typeof pins;
						if (typeof pins === "string" && pins.includes('section')) {
							pins0 = pins.split('section');
							pins = pins0[1];
						}
						if (status === 'Public') {
							var pins0 = $(this).text();
							var pins1 = pins0.split(title);
							var pins2 = pins1[1];
							var pins3 = pins2.split(' Pin');
							var pins = pins3[0]


						}
						if (typeof pins === "string" && pins.includes('section')) {
							pins0 = pins.split('sections');
							pins = pins0[1];
						}
						// var pins = pinRaw[1].split(' Pins');

						hackElements.push({ 'title': title, 'status': status, 'pins': pins })
					}
				})
				copy(hackElements)





				////////////////////////////////////////////////////////////////////////////////////
				// test area

				function addStuff(string, howMany) {
					var result = ''
					var i = 0;
					while (i < howMany) {
						result += string
						i++;
					}
					return result;
				}

				$('.pinWrapper').each(function(index) {
					if (index === 0) {
						var i = 0;
						while (i < 50) {
							var thingToDo = "var test = $('.pinWrapper')[index]." + addStuff("children[0].", i) + "srcset;";
							try { eval(thingToDo) } catch (e) { var test = ""; }
							if (test !== "" && test !== undefined) {
								console.log(thingToDo);
								break
							}
							i++;
						}
					}
				});
				$('.pinWrapper')[index].children[0].children[0].children[0].children[0].children[0].children[0].children[0].srcset
				$('.pinWrapper')[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].srcset;

				// test area END
				////////////////////////////////////////////////////////////////////////////////////
				//////////////////////////////////////////////////////////////////////////////////// START NEW
				////////////////////////////////////////////////////////////////////////////////////

				https: //www.pinterest.com/n0tech/-programming/
					https: //www.pinterest.com/n0tech/-rel/
					window.open("http://www.pillerbeauty.com/js/jquery-1.11.3.js", "new")


				// pinterest pins *********************************************** NEW START

				// try {}catch (e) {}

				////////////////////////////////////// START COPY

				__thisID_FAMILY_TREE = 0;
				__link_FAMILY_TREE = 0;
				__imgSRC_FAMILY_TREE = 0;
				__imgSRCSET_FAMILY_TREE = 0;

				__NULL_SET_IN_A_ROW = 0;

				hackElements = [];
				hackElementsPinIDs = [];

				function addStuff(string, howMany) {
					var result = ''
					var i = 0;
					while (i < howMany) {
						result += string
						i++;
					}
					return result;
				}

				function goGetem() {
					if ($('.pinWrapper').length === 0) {
						__NULL_SET_IN_A_ROW++;
					} else {
						__NULL_SET_IN_A_ROW = 0;
					}

					if (__NULL_SET_IN_A_ROW > 4) {
						console.log('');
						console.log('');
						console.log('__NULL_SET_IN_A_ROW: ' + __NULL_SET_IN_A_ROW);
						console.log('');
						console.log('hackElements: ' + hackElements.length);
						console.log('');
						console.log('');
					}

					$('.pinWrapper').each(function(index) {

						if (__imgSRCSET_FAMILY_TREE === 0) {
							generateFamilyTree();
						}


						var __thisID = '';
						var __link = '';
						var __img = '';
						var __imgSRCSET = '';

						// __thisID
						var thingToDo = "__thisID = $('.pinWrapper')[index]." + addStuff("children[0].", __thisID_FAMILY_TREE) + "href.replace('https://www.pinterest.com/pin/','').replace('/','');";
						try { eval(thingToDo) } catch (e) { var test = ""; }

						// __link
						var thingToDo = "__link = $('.pinWrapper')[index]." + addStuff("children[0].", __link_FAMILY_TREE) + "href;";
						try { eval(thingToDo) } catch (e) { var test = ""; }

						// __img
						var thingToDo = "__img = $('.pinWrapper')[index]." + addStuff("children[0].", __imgSRC_FAMILY_TREE) + "src;";
						try { eval(thingToDo) } catch (e) { var test = ""; }

						// __imgSRCSET
						var thingToDo = "__imgSRCSET = $('.pinWrapper')[index]." + addStuff("children[0].", __imgSRCSET_FAMILY_TREE) + "srcset;";
						try { eval(thingToDo) } catch (e) { var test = ""; }


						try {
							var __imgSRCSET1 = __imgSRCSET.split(' ');
							var __img1 = __imgSRCSET1[0];
							var __img2 = __imgSRCSET1[2];
							var __img3 = __imgSRCSET1[4];
							var __img4 = __imgSRCSET1[6];
						} catch (e) {
							var __img1 = '';
							var __img2 = '';
							var __img3 = '';
							var __img4 = '';
						}


						__description = $(this).text().replace(',', '_-_')

						if (!hackElementsPinIDs.includes(__thisID)) {
							console.log(__thisID);
							hackElementsPinIDs.push(__thisID);
							hackElements.push({ '_id': __thisID, 'link': __link, 'description': __description, 'img': __img, 'img1': __img1, 'img2': __img2, 'img3': __img3, 'img4': __img4 });
							try { $('.pinWrapper')[index].remove(); } catch (e) {}

						}
						scrollDownJustABitAndExecute();


					});
					// goGetem END
				}

				function generateFamilyTree() {

					var __thisID = '';
					var __link = '';
					var __img = '';
					var __imgSRCSET = '';

					// __thisID
					var i = 0;
					while (i < 50) {
						var thingToDo = "__thisID = $('.pinWrapper')[0]." + addStuff("children[0].", i) + "href.replace('https://www.pinterest.com/pin/','').replace('/','');";
						try { eval(thingToDo) } catch (e) { var test = ""; }
						if (__thisID !== "" && __thisID !== undefined) {
							__thisID_FAMILY_TREE = i;
							console.log('__thisID_FAMILY_TREE: ' + __thisID_FAMILY_TREE);
							console.log('__thisID: ' + __thisID);
							break
						}
						i++;
					}


					// __link
					var i = 0;
					while (i < 50) {
						var thingToDo = "__link = $('.pinWrapper')[0]." + addStuff("children[0].", i) + "href;";
						try { eval(thingToDo) } catch (e) { var test = ""; }
						if (__link !== "" && __link !== undefined) {
							__link_FAMILY_TREE = i;
							console.log('__link_FAMILY_TREE: ' + __link_FAMILY_TREE);
							break
						}
						i++;
					}

					// __img
					var i = 0;
					while (i < 50) {
						var thingToDo = "__img = $('.pinWrapper')[0]." + addStuff("children[0].", i) + "src;";
						try { eval(thingToDo) } catch (e) { var test = ""; }
						if (__img !== "" && __img !== undefined) {
							__imgSRC_FAMILY_TREE = i;
							console.log('__imgSRC_FAMILY_TREE: ' + __imgSRC_FAMILY_TREE);
							break
						}
						i++;
					}

					// __imgSRCSET
					var i = 0;
					while (i < 50) {
						var thingToDo = "__imgSRCSET = $('.pinWrapper')[0]." + addStuff("children[0].", i) + "srcset;";
						try { eval(thingToDo) } catch (e) { var test = ""; }
						if (__imgSRCSET !== "" && __imgSRCSET !== undefined) {
							__imgSRCSET_FAMILY_TREE = i;
							console.log('__imgSRCSET_FAMILY_TREE: ' + __imgSRCSET_FAMILY_TREE);
							break
						}
						i++;
					}
					// generateFamilyTree END
				}

				function goGetemCheck(id) {
					result = true
					try {
						for (var ii = hackElements.length - 1; ii >= 0; ii--) {
							if (hackElements[ii].id = id) {
								result = false
							}
						}
					} catch (e) {}
					return result
				}

				function goGetemAgain() {
					var answer = confirm("Again?")
					if (answer) {
						copy(hackElements);
					} else {
						$(window).scrollTop($(document).height());
						var delay = 2000; // milliseconds
						var before = Date.now();

						while (Date.now() < before + delay) {};
						goGetem();
						// settimeout(function(){goGetem();},2000);
					}
				}

				function scrollDownJustABitAndExecute() {
					var scroll = $(window).scrollTop();
					var scrollto = scroll + 500;
					$("html, body").animate({ scrollTop: scrollto });
					var duration = 5000;
					$({ to: 0 }).animate({ to: 1 }, duration, function() {
						goGetem();
					});
				}

				////////////////////////////////////// END COPY


				goGetem();
				copy(hackElements);

				////////////////////////////////////// PAGE DOWN ON INTERVAL


				goGetem();

				var interval = null;
				$(function() {
					interval = setInterval(scrollDownJustABit, 1500);
				});


				///// THIS FUNCTION IS IN THE PAST AREA - START

				function scrollDownJustABit() {
					var scroll = $(window).scrollTop();
					var scrollto = scroll + 500;
					$("html, body").animate({ scrollTop: scrollto });
					goGetem();
				}

				///// THIS FUNCTION IS IN THE PAST AREA - END

				// pinterest pins *********************************************** NEW END 


				////////////////////////////////////////////////////////////////////////////////////
				//////////////////////////////////////////////////////////////////////////////////// END NEW
				////////////////////////////////////////////////////////////////////////////////////
				https: //www.pinterest.com/n0tech/-programming/
					https: //www.pinterest.com/n0tech/-rel/
					window.open("http://www.pillerbeauty.com/js/jquery-1.11.3.js", "new")

				// pinterest pins ***********************************************  OLD START

				// try {}catch (e) {}



				hackElements = [];
				hackElementsPinIDs = [];

				function addStuff(string, howMany) {
					var result = ''
					var i = 0;
					while (i < howMany) {
						result += string
						i++;
					}
					return result;
				}

				function goGetem() {
					$('.pinWrapper').each(function(index) {
						// __thisID = $('.pinWrapper')[index].children[0].children[0].children[0].href
						var __thisID = '';

						// __thisID
						var i = 0;
						while (i < 50) {
							var thingToDo = "__thisID = $('.pinWrapper')[index]." + addStuff("children[0].", i) + "href.replace('https://www.pinterest.com/pin/','').replace('/','');";
							try { eval(thingToDo) } catch (e) { var test = ""; }
							if (test !== "" && test !== undefined) {
								// console.log(thingToDo);
								break
							}
							i++;
						}


						// theLink
						var i = 0;
						while (i < 50) {
							var thingToDo = "theLink = $('.pinWrapper')[index]." + addStuff("children[0].", i) + "href;";
							try { eval(thingToDo) } catch (e) { var test = ""; }
							if (test !== "" && test !== undefined) {
								// console.log(thingToDo);
								break
							}
							i++;
						}

						try {
							theLink = $('.pinWrapper')[index].children[0].children[0].href
						} catch (e) {}

						__description = $(this).text().replace(',', '_-_')

						// __img
						var i = 0;
						while (i < 50) {
							var thingToDo = "__img = $('.pinWrapper')[index]." + addStuff("children[0].", i) + "src;";
							try { eval(thingToDo) } catch (e) { var test = ""; }
							if (test !== "" && test !== undefined) {
								// console.log(thingToDo);
								break
							}
							i++;
						}

						// __imgTMP
						var i = 0;
						while (i < 50) {
							var thingToDo = "__imgTMP = $('.pinWrapper')[index]." + addStuff("children[0].", i) + "srcset;";
							try { eval(thingToDo) } catch (e) { var test = ""; }
							if (test !== "" && test !== undefined) {
								// console.log(thingToDo);
								break
							}
							i++;
						}
						try {
							__imgTMP1 = __imgTMP.split(' ')
						} catch (e) {}

						try { __img1 = __imgTMP1[0] } catch (e) { __img1 = '' }
						try { __img2 = __imgTMP1[2] } catch (e) { __img2 = '' }
						try { __img3 = __imgTMP1[4] } catch (e) { __img3 = '' }
						try { __img4 = __imgTMP1[6] } catch (e) { __img4 = '' }
						if (!hackElementsPinIDs.includes('__thisID')) {
							console.log(__thisID);
							hackElementsPinIDs.push(__thisID);
							hackElements.push({ '_id': __thisID, 'link': theLink, 'description': __description, 'img': __img, 'img1': __img1, 'img2': __img2, 'img3': __img3, 'img4': __img4 });
						}
						// if (goGetemCheck(__thisID) || index === 0) {
						// } else {
						//     console.log('nope')
						// }

					});
					// goGetemAgain();
				}

				function goGetemCheck(id) {
					result = true
					try {
						for (var ii = hackElements.length - 1; ii >= 0; ii--) {
							if (hackElements[ii].id = id) {
								result = false
							}
						}
					} catch (e) {}
					return result
				}

				function goGetemAgain() {
					var answer = confirm("Again?")
					if (answer) {
						copy(hackElements);
					} else {
						$(window).scrollTop($(document).height());
						var delay = 2000; // milliseconds
						var before = Date.now();

						while (Date.now() < before + delay) {};
						goGetem();
						// settimeout(function(){goGetem();},2000);
					}
				}



				//////////////////////////////////////



				goGetem();

				copy(hackElements);



				////////////////////////////////////// PAGE DOWN ON INTERVAL


				goGetem();
				var interval = null;

				$(function() {
					interval = setInterval(callFunc, 1500);
				});

				function callFunc() {
					var scroll = $(window).scrollTop();
					var scrollto = scroll + 500;
					$("html, body").animate({ scrollTop: scrollto });
					goGetem();
				}

				// pinterest pins *********************************************** OLD END

				////////////////////////////////////////////////////////////////////////////////////








				// <div class="pinWrapper" data-test-id="pinWrapper">
				//    <div data-test-id="" class="XiG zI7 iyn Hsu">
				//       <a data-force-refresh="1" href="/pin/AWIgq3nf23vPeL8Z-8qHdP1opMQMR56mlJ0d8b2v0RAWXmJxMWpUJmc/" rel="" style="cursor: zoom-in; display: block; position: relative;">
				//          <div class="Pj7 sLG XiG ZKv mix">
				//             <div class="zI7 iyn Hsu" style="min-height: 55px;">
				//                <div class="XiG zI7 iyn Hsu">
				//                   <div data-pwt="true">
				//                      <div>
				//                         <div class="XiG zI7 iyn Hsu" style="background-color: rgb(239, 239, 239); padding-bottom: 100%;">
				//                            <img alt=" " class="hCL kVc L4E MIw" src="https://i.pinimg.com/236x/e7/64/0f/e7640f6738bf5904f08b2012fbb9073f.jpg?b=t" srcset="https://i.pinimg.com/236x/e7/64/0f/e7640f6738bf5904f08b2012fbb9073f.jpg?b=t 1x, https://i.pinimg.com/474x/e7/64/0f/e7640f6738bf5904f08b2012fbb9073f.jpg?b=t 2x, https://i.pinimg.com/736x/e7/64/0f/e7640f6738bf5904f08b2012fbb9073f.jpg?b=t 3x, https://i.pinimg.com/originals/e7/64/0f/e7640f6738bf5904f08b2012fbb9073f.jpg 4x">
				//                         </div>
				//                      </div>
				//                   </div>
				//                </div>
				//             </div>
				//             <div class="KPc MIw ojN Rym p6V QLY"></div>
				//          </div>
				//          <div class="MIw QLY Rym ojN p6V zI7 iyn Hsu"></div>
				//       </a>
				//    </div>
				//    <div class="Jea hDW hs0 zI7 iyn Hsu">
				//       <div class="ujU wYR zI7 iyn Hsu" style="width: 100%;"></div>
				//       <div class="zI7 iyn Hsu"></div>
				//    </div>
				// </div>

				////////////////////////////////////////////////////////////////////////////////////

				////////////////////////////////////////////////////////////////////////////////////
				// http://rephrecruiting.com/profile/docs/test/test21.php
				// $('*').unbind();

				$('.mid').html('<center style="color:white;font-weight:bolder;"></center>');
				$('.mid center').append('<div id="theX" style="display:inline-block;padding:10px;"></div>');
				$('.mid center').append('<div id="theY" style="display:inline-block;padding:10px;"></div>');
				$('.mid center').append('<div id="theText" style="display:inline-block;padding:10px;"></div>');

				// $('.contactTopItem ').css( 'margin', '25px' );
				// $('.contactTopItem ').css( 'padding', '0px' );
				// $('.contactTopItem ').css( 'width', '50px' );
				// $('.contactTopItem ').css( 'height', '50px' );

				$('.contactTopItem ').css('margin', '10px');
				$('.contactTopItem ').css('padding', '0px');
				$('.contactTopItem ').css('width', '200px');
				$('.contactTopItem ').css('height', '25px');
				$('#contacts_top_item_0_0_0').css('width', '25px');
				$('#contacts_top_item_0_0_3').css('width', '25px');
				$('#contacts_top_item_1_0_0').css('width', '25px');
				$('#contacts_top_item_1_0_3').css('width', '25px');

				$('#contacts_top_item_0_0_4').css('width', '245px');
				$('#contacts_top_item_1_0_4').css('width', '245px');


				$('body').mousemove(function(event) {
					$('#theX').text('X:' + event.clientX);
					$('#theY ').text('Y:' + event.clientY);
				});
				$('.contactTopItem').click(function(event) {

					hackData = [];
					hack = {};
					hack.selection = '';
					$('.contactTopItem').each(function() {
						var off = $(this).offset();
						off.bottom = off.top + $(this).height();
						off.right = off.left + $(this).width();
						off.text = $(this).text();
						off.id = $(this).attr('id');
						// console.log( off );
						hackData.push(off);
					});

					for (var ii = 0; ii < hackData.length; ii++) {
						rec = hackData[ii];
						// console.log( rec );
						if (event.pageX < rec.right && event.pageX > rec.left && event.pageY > rec.top && event.pageY < rec.bottom) {
							hack.selection = rec.id;
							hack.lastWidth = $('#' + rec.id).css('width');
							$('#theText').html('');
							$('#theText').append(rec.text);
							$('#theText').append('<input type="text" id="editField" value="' + $('#' + rec.id).css('width').replace('px', '') + '">');
							$('#theText').append(' width');
							$('#editField').change(function() {
								console.log('hack.selection:', hack.selection);
								$('#' + hack.selection).css('width', $('#editField').val() + 'px');
								if (window.confirm('Resize all items that has, width: ' + hack.lastWidth)) {
									for (var y = 0; y < hackData.length; y++) {
										if ($('#' + hackData[y].id).css('width') === hack.lastWidth) {
											$('#' + hackData[y].id).css('width', $('#editField').val() + 'px')
										}

									}
								}

							});
							console.log('hack.selection:', hack.selection);
						}
					}
				});