// https://eyeformeta.com/tools/tool.js
hackTool = {
    hack: { 'instructions': [] },
    v: {labels: []},
    examples: [],
    payload: {},
    records: [],
    tempID: '9CE9B7A1-6BCE-1D46-FCA6-5CA95A8B13A4',
    printable: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`\{\|\}~',
    autoHack: function() {
        for (var iy = 0, len = hackTool.hack['instructions'].length; iy < len; iy++) {
            try {
                var n = hackTool.hack['instructions'][iy]['name'];
                var t = hackTool.hack['instructions'][iy]['type'];
                var l = hackTool.hack['instructions'][iy]['location'];
                var s = hackTool.hack['instructions'][iy]['settings'];
                
                if (t === 'single') {
                    var el = document.querySelectorAll( l );
                    try {
                        hackTool.payload[n] = hackTool.cleaner( hackTool.recordSettings( el[0].innerText, s ) );
                    } catch (err) {}
                        
                    // try {
                    // } catch (err) {}
                }
                if (t === 'list') {
                    hackTool.v.preData = [];
                    var el = document.querySelectorAll( l );
                    hackTool.payload[n] = [];
                    el.forEach(function(aChild) {
                        var rec = hackTool.recordSettings( aChild.innerText, s );
                        if ( rec !== null )
                            hackTool.payload[n].push( rec );
                    });
                    if ( Object.keys(s).indexOf( 'convert' ) > -1 && s.convert === 'text' ) {
                        var preData = hackTool.payload[n].slice();
                        hackTool.payload[n] = '';
                        for (var i = 0; i < preData.length; i++) {
                            hackTool.payload[n] += preData[i] + '\n';
                        }
                        hackTool.payload[n] = hackTool.cleanBE( hackTool.payload[n], '\n' );
                    }
                    hackTool.payload[n] = hackTool.recordSettings( hackTool.payload[n], s );
                }
                if (t === 'table') {
                    if ( Object.keys(s).indexOf( 'file' ) < 0 ) { 
                        s.file = n;
                    }
                    hackTool.v.myTables = hackTool.tableToJson( l, s );
                    hackTool.payload[n] = [];
                    if ( Object.keys(s).indexOf( 'nth' ) > -1 ) {
                        for (var i = 0; i < hackTool.v.myTables.length; i++) {
                            if ( s['nth'].split(',').indexOf( i.toString() ) > -1 ) {
                                hackTool.payload[n].push( hackTool.v.myTables[i] );
                            }
                        }
                    } else {
                        hackTool.payload[n] = hackTool.v.myTables;
                    }
                    hackTool.payload[n] = hackTool.recordSettings( hackTool.payload[n], s );
                }
                if (t === 'records') {
                    try {
                        hackTool.payload[n] = hackTool.acquireFamily( l, 0, s );
                    } catch (err) {}
                    try {
                        hackTool.payload[n] = hackTool.recordSettings( hackTool.payload[n], s );
                    } catch (err) {}
                }
            } catch (err) { console.log(err); }
        }
    },
    recordSettings: function( data, s ) {
        
        if (false) {
        } else if ( Object.keys(s).indexOf( 'delim_label' ) > -1 && Object.keys(s).indexOf( 'record' ) > -1 ) {
            hackTool.v.preData = hackTool.cleanWhiteSpace( data );
            hackTool.v.preData = hackTool.replaceAll( hackTool.v.preData, s.delim_label+s.record, s.delim_label );
            hackTool.v.prepData = hackTool.v.preData.split(s.record);
            var payload = {};
            for (var i = 0; i < hackTool.v.prepData.length; i++) {
                var pre = hackTool.v.prepData[i].split(s.delim_label);
                payload[pre[0]] = pre[1];
            }
        } else if ( Object.keys(s).indexOf( 'delim_fields' ) > -1 && Object.keys(s).indexOf( 'fields' ) > -1 ) {
            if ( data.indexOf( s.delim_fields ) < 0 )
                return null;
            hackTool.v.preData = hackTool.removeWhiteSpace( data ).split(s.delim_fields);
            var payload = {};
            for (var i = 0; i < hackTool.v.preData.length; i++) {
                payload[ s.fields[i] ] = hackTool.v.preData[i];
            }
        } else if ( Object.keys(s).indexOf( 'delim_label' ) > -1 ) {
            hackTool.v.preData = hackTool.removeWhiteSpace( data ).split(s.delim_label);
            var payload = {};
            payload[ hackTool.v.preData[0] ] = hackTool.v.preData[1];
        } else if ( Object.keys(s).indexOf( 'record' ) > -1 ) {
            hackTool.v.preData = hackTool.cleanWhiteSpace( data );
            hackTool.v.prepData = hackTool.v.preData.split(s.record);
            var payload = [];
            for (var i = 0; i < hackTool.v.prepData.length; i++) {
                if ( hackTool.v.prepData[i].length )
                    payload.push( hackTool.v.prepData[i] );
            }
        } else if ( Object.keys(s).indexOf( 'format' ) > -1 ) {
            if ( false ) {
            } else if ( s.format === 'csv' || s.format === 'tab' ) {
                
                var formatField = function (dX) {
                    if ( true || dX.indexOf('\n') > -1 || dX.indexOf('"') > -1 || dX.indexOf('\t') > -1  ) {
                        var temp = JSON.stringify({ 'xyz': dX })
                        temp = temp.replace( '{"xyz":', '' );
                        temp = temp.replace( '}', '' );
                        temp = temp.replace( ',', '\\,' );
                        return temp;
                    } else {
                        return dX;
                    }
                };



                var exportToCsv = function (filename, rows, delim) {
                    var processRow = function (row) {
                        var finalVal = '';
                        for (var j = 0; j < row.length; j++) {
                            var innerValue = row[j] === null ? '' : row[j].toString();
                            if (row[j] instanceof Date) {
                                innerValue = row[j].toLocaleString();
                            };
                            var result = innerValue.replace(/"/g, '""');
                            if (result.search(/("|,|\n)/g) >= 0)
                                result = '"' + result + '"';
                            if (j > 0)
                                finalVal += delim;
                            finalVal += result;
                        }
                        return finalVal + '\n';
                    };

                    var csvFile = '';
                    for (var i = 0; i < rows.length; i++) {
                        csvFile += processRow(rows[i]);
                    }
                    if ( delim === ',' ) {
                        var blob = new Blob([csvFile], { type: 'text/csv;charset=utf-8;' });
                    } else if ( delim === '\t' ) {
                        var blob = new Blob([csvFile], { type: 'text/tab;charset=utf-8;' });
                    } else {
                        console.log( 'FORMAT ERROR' );
                        return 'error: format';
                    }
                    if (navigator.msSaveBlob) { // IE 10+
                        navigator.msSaveBlob(blob, filename);
                    } else {
                        var link = document.createElement("a");
                        if (link.download !== undefined) { // feature detection
                            // Browsers that support HTML5 download attribute
                            var url = URL.createObjectURL(blob);
                            link.setAttribute("href", url);
                            link.setAttribute("download", filename);
                            link.style.visibility = 'hidden';
                            document.body.appendChild(link);
                            link.click();
                            document.body.removeChild(link);
                        }
                    }
                }




                hackTool.traverse( data, {} );

                var tables = [];

                if ( Object.keys(s).indexOf( 'labels' ) > -1 ) {


                    for (var i = 0; i < hackTool.v.traverse.paths.length; i++) {
                        var index = hackTool.v.traverse.index[  hackTool.v.traverse.paths[i]  ];
                        if ( index === 'string' ) {
                            var location = JSON.parse(  hackTool.v.traverse.paths[i]  );
                            location.pop();
                            location.pop();
                            var table = JSON.stringify( location );
                            if ( tables.indexOf(table) < 0 )
                                tables.push( table );
                        }
                    }


                } else {


                    for (var i = 0; i < hackTool.v.traverse.ipaths.length; i++) {
                        var index = hackTool.v.traverse.iindex[  hackTool.v.traverse.ipaths[i]  ];
                        if ( index === 'string' ) {
                            var location = JSON.parse(  hackTool.v.traverse.ipaths[i]  );
                            location.pop();
                            location.pop();
                            var table = JSON.stringify( location );
                            if ( tables.indexOf(table) < 0 )
                                tables.push( table );
                        }
                    }


                }



                var labelSpent = [];
                if ( tables.length > 1 ) {
                    var isMulti = true;
                } else {
                    var isMulti = false;
                }

                var csv = '';
                var allRecords = [];
                // console.log( JSON.stringify(tables) );
                for (var i = 0; i < tables.length; i++) {
                    var location = JSON.parse(  tables[i]  );
                    if ( Object.keys(s).indexOf( 'prefix' ) > -1 ) {
                        var prefix = s.prefix;
                        if (prefix.length)
                            prefix += '-';
                    } else {
                        var prefix = '';
                    }
                    var filename2 = prefix+s.file;
                    if ( Object.keys(s).indexOf( 'labels' ) > -1 && location[ location.length-1 ] !== '-i-'  ) {
                        var filename = prefix+location[ location.length-1 ];
                    } else {
                        var filename = prefix+s.file;
                        var filename = filename.replace( '.csv', '' );
                        var filename = filename.replace( '.CSV', '' );
                        var filename = filename.replace( '.tab', '' );
                        var filename = filename.replace( '.TAB', '' );
                    }

                    if ( labelSpent.indexOf(filename) > -1  && s.save !== 'one' ) {
                        var ixN = i+1;
                        filename += '-' + ixN.toString() + '';
                    } else {
                        labelSpent.push( filename );
                    }

                    // if ( filename.indexOf('.csv') < 0 && filename.indexOf('.CSV') < 0 )
                    filename += '.'+s.format;
                    if ( Object.keys(s).indexOf( 'labels' ) > -1 ) {
                        hackTool.traverse( data, { 'list': tables[i] } );
                    } else {
                        hackTool.traverse( data, { 'ilist': tables[i] } );
                    }

                    if ( hackTool.v.traverse.records.length ) {


                        var records = [];
                        var keys = Object.keys( hackTool.v.traverse.records[0] );
                        records.push( keys );


                        for (var iii = 0; iii < hackTool.v.traverse.records.length; iii++) {
                            var record = [];
                            for (var ii = 0; ii < keys.length; ii++) {
                                record.push( hackTool.v.traverse.records[iii][   keys[ii]   ] );
                            }
                            records.push(record);
                        }

                        if ( s.format === 'csv' ) {
                            var theDelim = ',';
                        } else if ( s.format === 'tab' ) {
                            var theDelim = '\t';
                        }


                        if ( Object.keys(s).indexOf( 'save' ) > -1 && s.save === 'all' ) {
                            exportToCsv( filename, records, theDelim );
                        } else if ( Object.keys(s).indexOf( 'save' ) > -1 && s.save === 'one' ) {

                            if ( isMulti )
                                allRecords.push( [filename.replace('.csv','')] );

                            for (var Ai = 0; Ai < records.length; Ai++) {
                                allRecords.push(records[Ai]);
                            }

                            if ( isMulti )
                                allRecords.push([]);allRecords.push([]);

                        } else {

                            // console.log( 'filename', filename );
                            // console.log( 's.filename', s.filename );

                            if ( isMulti )
                                csv += filename.replace('.csv','') + '\n'

                            var thisCSV = records.map(e => e.join(theDelim)).join("\n");

                            // var thisCSV = "data:text/csv;charset=utf-8," 
                            //     + records.map(e => e.join(",")).join("\n");


                            csv += thisCSV.toString();
                            if ( isMulti )
                                csv += '\n\n'

                        }


                        // var keys = Object.keys( hackTool.v.traverse.records[0] );
                        // csv += keys.join();
                        // csv += '\n';
                        // for (var iii = 0; iii < hackTool.v.traverse.records.length; iii++) {
                        //     var record = [];
                        //     for (var ii = 0; ii < keys.length; ii++) {
                        //         record.push( formatField( hackTool.v.traverse.records[iii][   keys[ii]   ] ) );
                        //     }
                        //     csv += record.join();
                        //     csv += '\n';
                        // }


                    } else {
                        console.log( 'No Records' );
                    }
                }

                // var payload = hackTool.replaceAll( 'data:text/csv;charset=utf-8,', '' );
                if ( Object.keys(s).indexOf( 'save' ) > -1 && s.save === 'one' ) {
                    exportToCsv( filename2+'.'+s.format, allRecords, theDelim );
                } else {
                    var payload = csv;
                }






                // if ( false ) {
                // } else if ( hackTool.objectType( data ) === 'list of list of dics' ) {
                // }
                // data = hackTool.replaceAll( data, '\r', '\n' );
            } else if ( s.format === 'csv' ) {
            }
        } else {
            if ( hackTool.objectType( data ) === 'string' && s.convert !== 'text' ) {
              var payload = hackTool.removeWhiteSpace(data);
            } else {
                var payload = data;
            }
        }
        return payload;
    },
    cleanWhiteSpace: function( data ) {
        data = hackTool.replaceAll( data, '\r', '\n' );
        data = hackTool.replaceAll( data, '\t', ' ' );
        data = hackTool.replaceAll( data, '  ', ' ' );
        data = hackTool.replaceAll( data, '\n ', '\n' );
        data = hackTool.replaceAll( data, '  ', ' ' );
        data = hackTool.replaceAll( data, '\n ', '\n' );
        data = hackTool.replaceAll( data, '\n\n', '\n' );
        data = hackTool.cleanBE( data, ' ' );
        data = hackTool.cleanBE( data, '\n' );
        data = hackTool.cleanBE( data, ' ' );
        data = hackTool.cleanBE( data, '\n' );
        data = hackTool.cleanBE( data, ' ' );
        // data = hackTool.cleanCharBE( data );
        return data;
    },
    replaceAll: function( data, what, to ) {
        while ( data.indexOf(what) > -1 ) {
            data = data.replace( what, to );
        }
        return data;
    },
    cleanBE: function( data, what ) {
        data = hackTool.replaceAll( hackTool.tempID + data + hackTool.tempID, hackTool.tempID + what, '' );
        data = hackTool.replaceAll( data, what + hackTool.tempID, '' );
        data = hackTool.replaceAll( data, hackTool.tempID, '' );
        return data;
    },
    cleanCharBE: function( data ) {
        if ( hackTool.printable.indexOf( data[0] ) < 0 )
            data = data.substr(1);
        if ( hackTool.printable.indexOf( data[ data.length-1 ] ) < 0 )
            data = data.substring(0, data.length - 1);
        return data;
    },
    removeWhiteSpace: function( data ) {
        data = hackTool.replaceAll( data, '\n', '' );
        data = hackTool.replaceAll( data, '\t', ' ' );
        data = hackTool.replaceAll( data, '  ', ' ' );
        data = hackTool.cleanBE( data, ' ' );
        data = hackTool.cleanBE( data, ' ' );
        // data = hackTool.cleanCharBE( data );
        return data;
    },
    acquire: function( el, output ) {
        var elems = document.querySelectorAll( el );
        var $elems = [].slice.call(elems);
        if ( output === 'list' ) {
            var payload = [];
            $elems.map( (elem) => { payload.push(elem.innerText) });
        } else if ( output === 'lines' ) {
            var payload = '';
            $elems.map( (elem) => { payload += elem.innerText + '\n' });
        } else if ( output === 'single' ) {
            var payload = '';
            $elems.map( (elem) => { payload += elem.innerText + ' ' });
        }
    },
    acquireFamily: function( query, parent, sp ) {

        var hasLabel = false;
        if ( Object.keys(sp).indexOf( 'labels' ) > -1 ) {
            hasLabel = true;
            var labels = document.querySelectorAll( sp.labels );
            hackTool.v.labels = [];
            labels.forEach(function(aLabel) {
                hackTool.v.labels.push({ 'label': aLabel.innerText, 'location': aLabel.offsetTop });
                hackTool.v.TEMP_OFFSET = aLabel.offsetTop;
            });
            hackTool.v.labels.push({ 'label': 'blank', 'location': hackTool.v.TEMP_OFFSET *2 });
        }

        var data = { 'record': {}, 'records': [] };
        if ( !parent ) {
            var items = document.querySelectorAll( query['parent'] );
        } else {
            var items = parent;
        }
        items.forEach(function(aChild) {
            data.record = {};
            var blank = '';
            try {
                for (var iy = 0; iy < query.children.length; iy++) {
                    var n = query.children[iy]['name'];
                    var l = query.children[iy]['location'];
                    var t = query.children[iy]['type'];
                    var sc = query.children[iy]['settings'];
                    childRecord = aChild.querySelectorAll(l);
                    if ( t === 'list' ) {
                        data.record[n] = [];
                        var blank = JSON.stringify(data.record[n]);
                        childRecord.forEach(function(bChild) {
                            var rec = hackTool.recordSettings( bChild.innerText, sc );
                            if ( rec !== null ) {
                                data.record[n].push( rec );
                            }
                        });
                    } else if ( t === 'single' ) {
                        data.record[n] = hackTool.recordSettings( childRecord[0].innerText, sc );
                    } else if ( t === 'records' ) {
                        data.record[n] = hackTool.acquireFamily( l, childRecord, sp );
                    }
                }
            // data.records.push( data.record );
            // console.log( 'data.records',data.records )
            } catch (err) {}

            if ( JSON.stringify(data.record) !== blank && JSON.stringify(data.record) !== '{}' && JSON.stringify(data.record).indexOf('[]') < 0 ) {
                if ( hasLabel ) {
                    var thisTable = {};
                    var thisKEY = Object.keys(data.record);
                    thisTable[  hackTool.tableLabel( aChild.offsetTop )  ] = data.record[ thisKEY[0] ];
                    // console.log( 'hasLabel', JSON.stringify(thisTable) )
                    data.records.push( thisTable );
                } else {
                    data.records.push( data.record );
                }
            }
                

            
        });
        return data.records;
    },
    tableToJson: function( el, s ) {
        var hasLabel = false;
        if ( Object.keys(s).indexOf( 'labels' ) > -1 ) {
            hasLabel = true;
            var labels = document.querySelectorAll( s.labels );
            hackTool.v.labels = [];
            hackTool.v.TEMP_OFFSET_MAX = 0;
            labels.forEach(function(aLabel) {
                hackTool.v.labels.push({ 'label': aLabel.innerText, 'location': aLabel.offsetTop });
                hackTool.v.TEMP_OFFSET = aLabel.offsetTop;
                if ( hackTool.v.TEMP_OFFSET > hackTool.v.TEMP_OFFSET_MAX )
                    hackTool.v.TEMP_OFFSET_MAX = hackTool.v.TEMP_OFFSET;
            });
            hackTool.v.labels.push({ 'label': 'blank', 'location': hackTool.v.TEMP_OFFSET_MAX *2 });
            hackTool.v.labels = hackTool.sort( hackTool.v.labels, 'location', 'asc' );
        }

        var data = { 'fields': [], 'record': {}, 'records': [], 'tables': [] };
        var tables = document.querySelectorAll( el );
        tables.forEach(function(aTable) {
            data.records = [];
            data.fields = [];
            cells = aTable.querySelectorAll('th');
            cells.forEach(function(aCell) {
                if ( typeof aCell.innerText !== 'undefined' )
                    data.fields.push( aCell.innerText );
            });
            cells = aTable.querySelectorAll('td');
            data.iCell = 0;
            data.record = {};
            if ( typeof data.tables == 'undefined' ) { data.tables=[]; }
            cells.forEach(function(aCell) {
                if ( data.iCell == data.fields.length ) {
                    if ( JSON.stringify(data.record) !== '{}' )
                        data.records.push( data.record );
                    data.record = {};
                    data.iCell = 0;
                }
                if ( typeof aCell.innerText !== 'undefined' ) {
                    
                    if ( data.fields[data.iCell] !== 'undefined' && typeof data.fields[data.iCell] !== 'undefined' ) {
                        data.record[  data.fields[data.iCell]  ] = aCell.innerText;
                    }
                    data.iCell++;
                }
                if ( data.iCell == data.fields.length ) {
                    if ( JSON.stringify(data.record) !== '{}' )
                        data.records.push( data.record );
                    data.record = {};
                    data.iCell = 0;
                }
            });
            if ( data.fields.length ) {
                
                if ( hasLabel ) {
                    var thisTable = {};
                    thisTable[  hackTool.tableLabel( aTable.offsetTop )  ] = data.records;
                    data.tables.push( thisTable );
                } else {
                    data.tables.push( data.records );
                }
            }
                data.records = [];
        });
        if (!data.tables) {return [];}
        return data.tables;
    },
    tableLabel: function( location ) {
        // console.log( 'location',location )
        var last = { 'label': '' };
        for (var i = 0; i < hackTool.v.labels.length; i++) {
            if ( hackTool.v.labels[i].location > location )
                return hackTool.removeWhiteSpace(last.label);

            last = hackTool.v.labels[i];
        }
    },
    sort: function( arr, key, direction ) {
        direction = direction.toLowerCase();
        // var exec = 'a.'+key+' - b.'+key+';';
        try {
                        var exec = 'arr.sort((a, b) => (a.'+key+' > b.'+key+') ? 1 : -1)'
                        var data =  eval( exec );
                        if ( direction.indexOf('d') > -1 ) {
                            data.reverse();
                        }
        } catch (err) {}
        return data;
        // hackTool.sort( arr, key, 'asc' );
    },
    help: function( query ) {
        var text = '';
        if ( typeof query === 'undefined' ) {

            text += '\n\nDisplay example by tags:';
            var tagList = [];
            for (var i = 0; i < hackTool.examples.length; i++) {
                var tags = hackTool.examples[i].tags.split(',');
                for (var ii = 0; ii < tags.length; ii++) {
                    if ( tagList.indexOf(tags[ii]) < 0 ) {
                        tagList.push( tags[ii] );
                    }
                }
            }
            for (var i = 0; i < tagList.length; i++) {
                text += '\n    hackTool.help( {\'tags\': \''+tagList[i]+'\'} )';
            }
            text += '\n\nDisplay example by difficulty:';
            var spent = [];
            for (var i = 0; i < hackTool.examples.length; i++) {
                if ( spent.indexOf(hackTool.examples[i].difficulty) < 0 ) {
                    spent.push( hackTool.examples[i].difficulty );
                    text += '\n';
                    text += '   hackTool.help( {\'difficulty\': \''+hackTool.examples[i].difficulty+'\'} )';
                }
            }
            text += '\n\n';
            text += 'want to make your own?\n';
            text += '    try:\n';
            text += '         hackTool.help(\'?\')\n';
            console.log(text);

        } else {
            if ( false ) {
            } else if ( query === 'ids' ) {
                text += '\n\nDisplay example by ID:';
                for (var i = 0; i < hackTool.examples.length; i++) {
                 text += '\n    ';
                 text += hackTool.examples[i].description;
                 text += '\n    ';
                 text += 'hackTool.help('+i+')\n';
                }
                console.log(text);
            } else if ( query === '?' ) {
                var text = "\n\ninstructions:\n    name: is the name of the field in the payload variable\n    \n    location: h1, #id, .class\n    \n    types:  recordDelim single list table tables\n    settings per type:\n        list\n            no settings is ok\n            can have delim_fields\n                example { 'delim_fields': ' - ', 'fields': ['label','description'] }\n                if delim_fields must have fields list\n            \n            can have text\n                example { 'convert': 'text' }\n        single\n            no settings is ok\n            can have delim or record\n                example { 'delim_label': ':', 'record': '\n' }\n                example { 'delim_label': ':' }\n                example { 'record': '\n' }\n                    '\n' is return carriage (each line is a record)\n        table\n            no settings is ok\n            can have nth\n                nth is what table number if multiple tables\n                example { 'nth': '2' }\n                example { 'nth': '2,3' }\n            \n            can have label\n                example { 'labels': 'h2' }\n        records\n            no settings is ok\n            no settings are available\n            example of entire record\n                {\n                    'name': 'movies',\n                    'location': {\n                         'parent': '.listicle-slide', 'children': [ \n                            { 'name': 'movie', 'location': '.listicle-slide-hed-text', 'type': 'single', 'settings': {} },\n                            { 'name': 'description', 'location': '.listicle-slide-dek', 'type': 'single', 'settings': {} },\n                     ] },\n                    'type': 'records',\n                    'settings': {}\n                },\n\ncopy(  hackTool.payload  )\n\n";
                console.log( text );
            } else if ( typeof query === 'number' ) {
                hackTool.selectExample(query);
            } else if ( typeof query === 'object' && Object.keys(query).indexOf( 'tags' ) > -1 ) {
                for (var i = 0; i < hackTool.examples.length; i++) {
                    if ( hackTool.examples[i].tags === query.tags ) {
                        hackTool.selectExample(i);
                    } else if ( hackTool.xLists(  hackTool.examples[i].tags.split(','), query.tags.split(',')  ) ) {
                        hackTool.selectExample(i);
                    }
                }

            } else if ( typeof query === 'object' && Object.keys(query).indexOf( 'difficulty' ) > -1 ) {
                for (var i = 0; i < hackTool.examples.length; i++) {
                    if ( hackTool.examples[i].difficulty === query.difficulty )
                        hackTool.selectExample(i);
                }
            }
        }
    },
    selectExample: function( idx ) {
        idx = Number(idx);

        var text = '';
        text += '\n\n';

        text += '// ';
        text += hackTool.examples[idx].url;
        text += '\n\n';
        text += 'hackTool.hack.instructions = ';
        text += hackTool.formatConfig( hackTool.examples[idx].config );
        text += '\n';
        text += 'hackTool.autoHack();\n';
        var copy_field = '';
        if ( hackTool.examples[idx].config.length === 1 )
            copy_field = hackTool.examples[idx].config[0].name;
        if ( copy_field.length ) {
            if ( copy_field.indexOf(' ') > -1 ) {
              text += 'copy(  hackTool.payload[\''+copy_field+'\']  )\n';

            } else {
              text += 'copy(  hackTool.payload.'+copy_field+'  )\n';
            }
        } else {
            text += 'copy(  hackTool.payload  )\n';
        }
        text += '\n\n';

            hackTool.helper = text;
            text += '\n copy(hackTool.helper)\n\n';

        console.log(text);
    },
    xLists: function( haystack, arr ) {
        return arr.some(function (v) {
            return haystack.indexOf(v) >= 0;
        });
    },
    indexChar: function( text ) {
        var chars = [  '{}', '[]', '()'  ];
        var index = {};
        var count = {};
        var table = {};
        for (var ic = 0; ic < chars.length; ic++) {
            index[ chars[ic] ] = {};
            count[ chars[ic][0] ] = 0;
            table[ chars[ic][0] ] = {};
        }

        for (var i = 0; i < text.length; i++) {
            for (var ic = 0; ic < chars.length; ic++) {
                if ( text[i] === chars[ic][0] ) {
                    table[ chars[ic][0] ][ count[ chars[ic][0] ] ] = i;
                    count[ chars[ic][0] ]++;
                }
                if ( text[i] === chars[ic][1] ) {
                    count[ chars[ic][0] ]--;
                    index[ chars[ic][0]+chars[ic][1] ][ table[ chars[ic][0] ][ count[ chars[ic][0] ] ] ] = i;

                }
            }
        }
        return index;
    },
    formatConfig: function( config ) {
        var data = JSON.stringify(config, null, 4);
        // console.log( 'pre', data, 'pre' )
        index = hackTool.indexChar( data );
        var sText = '"settings": {';
        var keys = Object.keys( index['{}'] );
        for (var i = 0; i < keys.length; i++) {
            var n = Number(keys[i]);
            var t = n-sText.length;
            if ( t > 0 ) {
                var sample = data.slice( t, n+1 );
                if ( sample.indexOf('settings') > -1 ) {
                    var section = data.slice( n, index['{}'][n]+1 );
                    data = data.replace( section, hackTool.removeWhiteSpace(section) );
                }
            }
        }
        return data;
    },
    profileFields: function( data ) {
        var report = { 'field': hackTool.objectType( data )  };
        if ( false ) {
        } else if ( report.field === 'list' && data.length ) {
            report.children = hackTool.profileFields( data[0] );
        } else if ( report.field === 'dic' && data.length ) {
            console.log( 'HERE 0' );
            report.children = {};
            var keys = Object.keys(data);
            for (var i = 0; i < keys.length; i++) {
                report.children[ keys[i] ] = hackTool.profileFields( data[ keys[i] ] );
            }
            console.log( 'HERE 1' );
        }

        return report;
    },
    objectType: function( data ) {
        if ( typeof data !== 'object' )
            return typeof data;


        var isDict = function (v) { return typeof v==='object' && v!==null && !(v instanceof Array) && !(v instanceof Date); };


        var typecheck = function (obj) {
            var type;
            
            // faster than if/else
            switch (obj) {
            case undefined:
                type = 'undefined';
                break;
            case null:
                type = 'null';
                break;
            default:
                var m  = (obj.constructor + '').match(/function\s+([a-z_$][0-9a-z_$]*)/i);
                if (m == null) {
                    type = typeof obj;
                } else if (m.length > 0) {
                    type = m[1].toLowerCase();
                } else {
                    type = typeof obj;
                }
            }
            
            return type;
        };

        if ( isDict(data) ) {
            return 'dic';
        } else {
            try {
                var t = typecheck(data);
            } catch (err) {
                var t = 'list';
            }
            if ( t === 'array' )
                return 'list';
            
            return t;
        }

    },
    traverse: function( data, config ) {

        // if ( Object.keys(s).indexOf( 'convert' ) > -1  ) {}
        if ( typeof config === 'undefined' )
            config = {};

        if ( Object.keys(config).indexOf( 'iD' )  < 0 )
            config.iD = '-i-';
        hackTool.v.traverse = {  'fields':[], 'index': {}, 'paths': [], 'ipaths': [], 'iindex': {}, 'records': [] };
        hackTool.traverseRun( data, config, [], [] );
        return hackTool.v.traverse;

    },
    traverseAdd: function( data, np, npi, config ) {
        var npX = JSON.stringify(np);
        var npiX = JSON.stringify(npi);
        // if ( Object.keys(config).indexOf( 'isList' )  > -1 ) {
        //     console.log('');
        //     console.log(npX);
        //     console.log(npiX);
        //     console.log('');
        // }
        if ( hackTool.v.traverse.ipaths.indexOf( npiX ) < 0  ) {
            hackTool.v.traverse.ipaths.push( npiX );
            hackTool.v.traverse.iindex[npiX] = data.type;
        }

        if ( hackTool.v.traverse.paths.indexOf( npX ) < 0  ) {
            hackTool.v.traverse.paths.push( npX );
            hackTool.v.traverse.fields.push( data );
            hackTool.v.traverse.index[npX] = data.type;
        }
    },
    traverseRun: function( data, config, parents, iparents ) {
        if ( false ) {
        } else if ( hackTool.objectType( data ) === 'list' ) {

            var npX = JSON.stringify( parents );
            var npiX = JSON.stringify( iparents );

            var np = parents.slice();
            var field = np[ np.length -1 ];
            np.pop();
            var cfg = config;
            if ( Object.keys(config).indexOf( 'list' )  > -1 && config.list === npX ) {
                cfg.isList = true;
            }
            if ( Object.keys(config).indexOf( 'ilist' )  > -1 && config.ilist === npiX ) {
                cfg.isList = true;
            }
            hackTool.traverseAdd(   { 'type':  hackTool.objectType( data ), 'field': field, 'parents': np }  , parents, iparents, cfg  );
            // console.log( JSON.stringify({ 'type':  hackTool.objectType( data ), 'field': field, 'parents': np }) );



            var np = parents.slice();
            np.push( config.iD );

            // if ( Object.keys(config).indexOf( 'list' )  > -1 ) {
            //     console.log( npX, config.list );
            // }

            for (var i = 0; i < data.length; i++) {
                if ( Object.keys(config).indexOf( 'list' )  > -1 && config.list === npX ) {
                    hackTool.v.traverse.records.push( data[i] );
                }
                if ( Object.keys(config).indexOf( 'ilist' )  > -1 && config.ilist === npiX ) {
                    hackTool.v.traverse.records.push( data[i] );
                }
                
                var npi = iparents.slice();
                npi.push( i );
                hackTool.traverseRun( data[i], config, np, npi );
            }
        } else if ( hackTool.objectType( data ) === 'dic' ) {



            // var p = JSON.stringify( parents );

            var keys = Object.keys(data);
            for (var i = 0; i < keys.length; i++) {

                var np = parents.slice();
                var npi = iparents.slice();
                np.push( keys[i] );
                npi.push( keys[i] );

                var t = hackTool.objectType( data[ keys[i] ] );

                hackTool.traverseAdd(   { 'type':  t, 'field': keys[i], 'parents': parents }  , np, npi, config   );


                if ( Object.keys(config).indexOf( 'returnField' )  > -1 ) {
                    if ( Object.keys(hackTool.v.traverse).indexOf( 'returnField' )  < 0 )
                        hackTool.v.traverse.returnField = [];

                    hackTool.v.traverse.returnField.push({  'data':  data[keys[i]], 'parents': parents, 'iparents': iparents,  });

                }
                if ( Object.keys(config).indexOf( 'find_parents' )  > -1 ) {
                    hackTool.v.traverse.requests = np;
                }


                hackTool.traverseRun( data[ keys[i] ], config, np, npi );

            }

        } else {
            var np = parents.slice();
            var field = np[ np.length -1 ];
            np.pop();

            hackTool.traverseAdd(   { 'type':  hackTool.objectType( data ), 'field': field, 'parents': np }  , parents, iparents, config  );

        }
    },
    traverseX: function( data ) {
        hackTool.traverse( data, {} );
        for (var i = 0; i < hackTool.v.traverse.paths.length; i++) {
            var index = hackTool.v.traverse.index[  hackTool.v.traverse.paths[i]  ];
            console.log( hackTool.v.traverse.paths[i], index );
            // console.log(JSON.stringify( hackTool.v.traverse.fields[i] )  );
        }
    },
    cleaner: function( data ) {
        try {
            while ( data.indexOf(String.fromCharCode(160)) > -1 ) {
                data = data.replace( String.fromCharCode(160), '\n' );
            }
            data = hackTool.cleanBE( data, '\n' );
            data = hackTool.cleanBE( data, '\t' );
            data = hackTool.cleanBE( data, ' ' );
            return data;
        } catch (err) {
            return data;
        }
    },
};
 
hackTool.examples.push({ 
    'url': 'http://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/',
    'description': 'example of several fields',
    'difficulty': 'intermediate',
    'tags': 'diverse',
    'config': [

    {
        'name': 'recipe',
        'location': 'h1',
        'type': 'single',
        'settings': {}
    },

    {
        'name': 'meta',
        'location': '.two-subcol-content-wrapper',
        'type': 'single',
        'settings': { 'delim_label': ':', 'record': '\n' }
    },
    {
        'name': 'ingredients',
        'location': '.ingredients-section .checkbox-list-checkmark',
        'type': 'list',
        'settings': {}
    },
    {
        "name": "steps",
        "location": ".instructions-section li p",
        "type": "list",
        "settings": {}
    },
]});


hackTool.examples.push({ 
    'url': 'http://www.esquire.com/entertainment/movies/g30853622/best-movies-on-netflix/',
    'description': 'example of grouping multiple fields into a record,movies',
    'difficulty': 'hard',
    'tags': 'multiple_fields_per_record',
    'config': [
    {
        'name': 'label',
        'location': { 'parent': '.listicle-slide', 'children': [ 
            { 'name': 'movie', 'location': '.listicle-slide-hed-text', 'type': 'single', 'settings': {} },
            { 'name': 'description', 'location': '.listicle-slide-dek', 'type': 'single', 'settings': {} },
         ] },
        'type': 'records',
        'settings': {}
    },
]});


hackTool.examples.push({ 
    'url': 'http://www.esquire.com/entertainment/movies/g30853622/best-movies-on-netflix/',
    'description': 'list of movies',
    'difficulty': 'simple',
    'tags': 'text_list',
    'config': [
    {
        'name': 'label',
        'location': '.listicle-slide-hed-text',
        'type': 'list',
        'settings': { 'convert': 'text' }
    },
]});


hackTool.examples.push({
    'url': 'http://www.computerhope.com/issues/ch001789.htm',
    'description': 'example of bullet list creating 2 fields for each bullet',
    'difficulty': 'hard',
    'tags': 'make_1_field_2+',
    'config': [
    {
        'name': 'label',
        'location': 'li',
        'type': 'list',
        'settings': { 'delim_fields': ' - ', 'fields': ['extension','description'] }
    },
]});


hackTool.examples.push({ 
    'url': 'http://developer.mozilla.org/en-US/docs/Web/HTML/Element',
    'description': 'example of a bunch of tables with labels',
    'difficulty': 'intermediate',
    'tags': 'tables_w_labels',
    'config': [
    {
        'name': 'label',
        'location': 'table',
        'type': 'table',
        'settings': { 'labels': 'h2' }
    },
]});


hackTool.examples.push({ 
    'url': 'http://www.computerhope.com/issues/ch001789.htm',
    'description': 'example of a bunch of list  with labels split into 2 fields',
    'difficulty': 'hard',
    'tags': 'lists_w_labels_split_into_2_fields',
    'config': [
    {
        'name': 'ext',
        'location': { 'parent': 'ul', 'children': [ 
            {
                "name": "label",
                "location": "li",
                "type": "list",
                "settings": { "delim_fields": " - ", "fields": [ "extension", "description" ] }
            }
         ] },
        'type': 'records',
        'settings': { 'labels': 'h2' }
    },
]});


hackTool.examples.push({ 
    'url': 'http://www.computerhope.com/issues/ch001789.htm',
    'description': 'example of a bunch of list  with labels split into 2 fields AND SAVE ONE FILE',
    'difficulty': 'hard',
    'tags': 'lists_w_labels_split_into_2_fields_SAVE_ONE_FILE',
    'config': [
    {
        'name': 'label',
        'location': { 'parent': 'ul', 'children': [ 
            {
                "name": "subject",
                "location": "li",
                "type": "list",
                "settings": { "delim_fields": " - ", "fields": [ "extension", "description" ] }
            }
         ] },
        'type': 'records',
        'settings': { 'labels': 'h2', 'file': 'extensions', 'format': 'csv', 'save': 'all',  }
    },
]});

hackTool.examples.push({ 
    'url': 'http://developer.mozilla.org/en-US/docs/Web/HTML/Element',
    'description': 'example of a bunch of tables with labels SAVE each as INDIVIDUAL csv file',
    'difficulty': 'hard',
    'tags': 'tables_w_labels_CSV_SAVE_EACH',
    'config': [
    {
        'name': 'label',
        'location': 'table',
        'type': 'table',
        'settings': { 'labels': 'h2', 'format': 'csv', 'save': 'all',  }
    }
]});

hackTool.examples.push({ 
    'url': 'http://developer.mozilla.org/en-US/docs/Web/HTML/Element',
    'description': 'example of a bunch of tables with labels COPY all as ONE csv text',
    'difficulty': 'hard',
    'tags': 'tables_w_labels_CSV_as_SINGLE',
    'config': [
    {
        'name': 'label',
        'location': 'table',
        'type': 'table',
        'settings': { 'labels': 'h2', 'format': 'csv',  }
    }
]});


hackTool.examples.push({ 
    'url': 'https://fastcharacter.com/',
    'description': 'example of several fields',
    'difficulty': 'intermediate',
    'tags': 'fastcharacter',
    'config': [

        {"name": "charactername", "location": "#charactername", "type": "single", "settings": { }},
        {"name": "classlevel", "location": "#classlevel", "type": "single", "settings": { }},
        {"name": "experiencepoints", "location": "#experiencepoints", "type": "single", "settings": { }},
        {"name": "race", "location": "#race", "type": "single", "settings": { }},
        {"name": "background", "location": "#background", "type": "single", "settings": { }},
        {"name": "STRscore", "location": "#STRscore", "type": "single", "settings": { }},
        {"name": "DEXscore", "location": "#DEXscore", "type": "single", "settings": { }},
        {"name": "CONscore", "location": "#CONscore", "type": "single", "settings": { }},
        {"name": "INTscore", "location": "#INTscore", "type": "single", "settings": { }},
        {"name": "WISscore", "location": "#WISscore", "type": "single", "settings": { }},
        {"name": "CHAscore", "location": "#CHAscore", "type": "single", "settings": { }},
        {"name": "savingthrows", "location": "#savingthrows", "type": "single", "settings": { }},
        {"name": "skills", "location": "#skills", "type": "single", "settings": { }},
        {"name": "passiveperception", "location": "#passiveperception", "type": "single", "settings": { }},
        {"name": "armorclass", "location": "#armorclass", "type": "single", "settings": { }},
        {"name": "initiative", "location": "#initiative", "type": "single", "settings": { }},
        {"name": "speed", "location": "#speed", "type": "single", "settings": { }},
        {"name": "proficiencies", "location": "#proficiencies", "type": "single", "settings": { }},
        {"name": "specialabilities", "location": "#specialabilities", "type": "single", "settings": { }},
        {"name": "attackactions", "location": "#attackactions", "type": "single", "settings": { }},
        {"name": "playername", "location": "#playername", "type": "single", "settings": { }},
]});

// hackTool.autoHack();
// copy(  hackTool.payload  )

// type tool_help.txt | p collapseReturns > %tmpf1%
hackTool.help();
console.log("  copy('['+document.title+']('+window.location.href+')')  ");
