import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'PrintCode', '-p,-print,-code' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register('Save', '-save')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'library-prep.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('pa | p library-prep'),
						_.hp('pa | p library-prep -code | cp'),
						_.hp('p -paste | p library-prep -code | p -copy'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': ['lib'],
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
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

_globals = set('''
switches tables appData appInfo regImps HD fields
'''.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('\n','').split(' '))

baseFN='''
pr,dot,
process_pipe_data,call,build_documentation_tables,cross_multiplication,numerate,nindex,chScan,fometa,json_,print_pr,random_color,print_,fo2,fo,fos,printt,pa,string_preview,tinydic,tailpop,tab,ll,rev,n2w,aiBullet,aiLine,over,ddelim,clear,rstr,get_supporting_line,idlen,strip_comments,ephemeral_strip,qindex,vindex,find_all,find_all_do,bAlias,reFormatSize,path_sep,stripColor,ordinal,back,files,f,chmod,printDicFields,date_diff_dic,isDate,onlyNumbers_strip,tfc,aggregate_trigger,autoWrapText,which,setClip,getClip,cleanString,cleanStringA,path2url,autoComplete,getCryptTable,saveCryptTable,head,header,hex2ascii,loopPrint,linePrint,dic_key_sort,dic_key_sort2,isCrypt,isGz,isBz2,sdFile,secureDeleteFile,zeros3,zeros2,zeros,replaceFile,patternDiff,av,xMultiply,get_change,days_math,time_ago,time_diff,printText,changeM,changeC,modify_timestamp,changeC_END,changeC_START,PowerShell_bashrc_name_break,PowerShell_bashrc_name_break_fix,year,woy,getDOWromEpoch,dow,dowConvert,dicString,check_field_match,fileLabel,getTablesProject,color,factor,flattenInt,isData,payloadCache,json_clean,prep4JSON,delete_keys_from_dict,help,internet_domains,fileFolder,stringType,unixAutoColumns,callers,epochDiff,getDriveID,folderProfileAttribute,getBin,getBin_list,saveBin,pDiff,pDiff2,clean_dic,traverse,traverse_dic,traverse_obj,clean_dic_keys,justTime,wrapText,simpleDic,simpleDic2,lastBackup,textClean,dicf,dicf_,get_size,wordStem,genSerial,extTrigger__File_TYPE__,urlTrigger,myFolderLocations,mod,colorPlus,plusColor,caseUnspecificCode,caseUnspecific,caseISspecific,nth_repl,shuffle,listColor,LoadingDone,loadingAnimation,loadingGif,loadingGifX,ipsumSentence,ipsumParagraph,saveCSV,saveCSV2,getCSV,csvTXT,csv,csv2,csvText,convertTimestamp,changeExtension,getExtension,removeExtension,registerSpent,saveData,getData,colorHelp,buldColorTable,colorNext,colorID,colorizeRow,colorizeRowLength,generateColorIndex,colorThis,ws_sep,inlineColor,printColor,printBold,inlineColorGroup,inlineBold,patternMatch,testPatterns,testPatterns22,generatePatterns,generatePatterns2,patternz,stringDiff,remove_carriage_returns,fromEpoch,postLoad,releaseAcquiredData,reclaimAcquiredData,theCommand,triggerSpace,longDashAdd,longDashRemove,inRelevantFolder,inRelevantFolderSearch,hasExtion,popDelim,addComma2,addComma,genAppName,printFields,removeReturn,flattenList,resolveIDs,printSafe,setUmlData,setPipeData,pipeCleaner,copyVar,openURL,copyDicAsJSON,cleanDic,d2json,printVar1,printVar,printTest,printVar2,printVarSimple,printVarSimple2,printVarSimpleFake3,printVarSimpleFake2,printVarSimpleFake,printVarOld,printVarSimplePostReplace,printVar2,printVarColor,printVarSimpleSTR,hashtag_,printVarColor_OLD,printVarColorChar,class2Dic,json2d,myFileLocationsXYZ,myFileLocations_add_file,_mfl,aliases_file_open,url2file,myFileLocations,myFileLocations2,cleanList,isAdmin,isN,autoDate,friendlyDate2,friendlyDate3,friendlyDate,friendlyDateTouch,resolveEpoch,resolveEpochTest,fileDate,dateAdd2,dateMathEpoch,txt2Date,uuidEpoc,genUUID3,genUUID2,md5UUID,regMD5,regMD5Mini,regID,genUUID,miniUUID,tinyUUID,UUID_Epoch2,UUID_Epoch,saveText,getText2,getText,getSize,monthByNumber,weeks_between,months_between,calculate_monthdelta,showLine,closeResults,positive_results_code,_prepare_plus_input,_is_substring_present,positiveResultsCode,positiveResults,minusResults,saveLog,saveTable,getTable,getTableOld,getTable3,getTable2,getTable2Old,getTableBIG,getTableDB,getTableProject,saveTableProject,saveTableDB,saveTable2,saveTable3,tempFile,stamp2Date,float2Date,float2Date2,float2Date3,float2Date3B,expireCheck,dateDiff,dateDiffX,dateAdd,dateSub,listAverage,date2epoch,validateEmail,figureOutDate,getMonthData,formatPhone00,formatPhone0,formatPhone1,formatPhone2,updateLine,getLastTableSplit,saveTableSplitNew,sort,blank_script_trigger,md5,formatSize,unFormatSize,unFormatSize2,to_bytes,count_bytes,timeAgo,timeAgo22,timeCalc,timeAgo_past,epoch_math,timeAgo_do,timeFuture,monthsDiff,days_in_month,isLeapYear,dateDiffDic,woy_from_year_week,woy2dates,woy2datesFriendly,woy2date,dateDiffText,getWOY,getYearFromEpoch,getWOYFromEpoch,daysDiff,yearMath,monthMath,epoch,isNu,isNu2,number2Words,checkKey,get_size2,genLine,ci,ci2,randomTrueFalse,randomizeCase,onlyAlpha,onlyNumbers,onlyAlphaNumeric,longID,formatColumns_OLD,formatColumns,formatColumnsSort,formatColumnsSortOld,plusCloseClean,defaultScriptTriggers,print_epoch_trigger,default_switch_trigger,aliasesFo,aliasesFi,defaultScriptTriggers_do,autoAbbreviations,printAutoAbbreviations,enableThreadDataSwap,threadTimer,threadAudit,threadSchedule,threadKwargs,percentageInt,percentageDiffInt,percentageDiff,percentageDiffIntAuto,percentageDiffAuto,percentageDiffSmaller,percentageDiffCalc,loadingGraphic,loadingGraphicEnd,isText,isNum,isFloat,appInfoDump,appInfoDump2,load,saveThreadsLog,autoKwargsGetArgsFromApp,err,key,historyPrint,impath,import_path,size_group_print,size_group,size_group_size,appID_nID_password,dict_generator_prefix,dict_generator,timeblock,rli,epoch_times,newid,bk,life,ico,l_fieldSet,l_registerSwitches_vars,l_registerSwitches,l_settings,l_vars,dots,ad,URL,getConfig,saveConfig,HID,cmd,waiting,day,file_len,hush,file_break,_2files,_2lines,_2lists,_2dates,dicKeys,isExit,fak,osvardump,osvar,pyApp,fromYML,toYML,getYML,saveYML,saveYML2,getYML2,inject,percentageReduce,percentageAdd,pipepipe,isData2,_thread_,pattern_probability,pattern_probability_list_best,pattern_probability_list,afile,replace_line_in_file,replace_lines_in_file,appAPI,secureURL,_secure_files_,sort,columnAbbreviations,IS,isZip,ZIP,zip_file,unzip_file,unzip_files,zZip,cleanUnzip,toTMP,encrypt,decrypt,enFi,deFi,has_crypt_header,password_filter,mask_password,getTextFirst,query,sortFo,sortFo2,isTextFi,isTextFiGet,searchColor,pp,zip9,an,ansp,sp1,lis,lisa,dicSort,dict_to_markdown_table,_default_triggers_,_default_settings_,appInfoContinuity,appDataContinuity,injectLines,injectLinesTest,compress2,decompress2,compress,decompress,BYTES,fileMeta,prWC,prWC2,Form,isGui,ptr,mdFig,mdFigSimp,code,code2,codex,acb,codex2,formatSizeUp,next_real_world_drive_size,formatSizeUpMath,rImp,create_backup_filename,pr0,isLink,logLine,bkExpire,md
'''.strip().replace(' ','').replace('\n','').split(',')


methods = set('''
clear copy fromkeys get items keys popitem setdefault pop values update
append extend insert remove index count reverse sort add difference
difference_update discard intersection intersection_update isdisjoint issubset
issuperset symmetric_difference symmetric_difference_update union capitalize
center casefold endswith expandtabs encode find format isalnum isalpha
isdecimal isdigit isidentifier islower isnumeric isprintable isspace
istitle isupper join ljust rjust lower upper swapcase lstrip rstrip
strip partition maketrans rpartition translate replace rfind rindex group start end search compile finditer match fullmatch sub
split rsplit splitlines startswith title zfill format_map append update split append pop items keys values reverse pop startswith endswith
'''.strip().split())

default = set('''
abs all any ascii bin bool bytearray bytes callable chr classmethod
compile complex delattr dict dir divmod enumerate eval exec filter float
endOfLine format frozenset getattr globals hasattr hash help hex id input
int isinstance issubclass iter len list locals map max memoryview min next
object oct open ord pow range repr reversed round set setattr slice sorted
staticmethod str sum super tuple type vars zip
print
'''.strip().split())

def fix(dic):
	global _globals
	global methods
	global default
	bad = set()
	new_with_namespace = []
	without = []
	myGlobals = []

	# Process the 'with_namespace' functions
	for x in dic['function_calls']['without_namespace']:
		if not x in default:
			without.append(x)
	dic['function_calls']['without_namespace'] = without
	

	
	for x in dic['function_calls']['with_namespace']:
		parts = x.split('.')[1]
		if parts in methods:
			bad.add(x.split('.')[0])
		else:
			for g in _globals:
				if x.startswith(g+'.'):
					if not g in myGlobals:
						myGlobals.append(g)
				else:
					new_with_namespace.append(x)
				
	dic['globals'] = myGlobals
	dic['function_calls']['with_namespace'] = new_with_namespace
	for m in myGlobals:
		bad.add(m)
	# Process the 'top_level_namespaces'
	new_top_level = [x for x in dic['top_level_namespaces'] if x not in bad]
	dic['top_level_namespaces'] = new_top_level
	# list(set())
	dic['function_calls']['without_namespace'] = list(set(dic['function_calls']['without_namespace']))
	dic['function_calls']['with_namespace'] = list(set(dic['function_calls']['with_namespace']))

	return dic

import ast

def extract_function_calls_from_code(code):

	# Parse the code
	tree = ast.parse(code)

	# Initialize the results
	function_calls = {
		"with_namespace": set(),  # Functions like `os.path.isfile`
		"without_namespace": set()  # Functions like `print`
	}
	top_level_namespaces = set()

	# Walk the AST tree to find function calls
	for node in ast.walk(tree):
		if isinstance(node, ast.Call):
			# Handle namespaced calls (e.g., `os.path.isfile`)
			if isinstance(node.func, ast.Attribute):
				namespace_parts = []
				current = node.func

				# Traverse the attribute chain (e.g., `os.path.isfile`)
				while isinstance(current, ast.Attribute):
					namespace_parts.append(current.attr)
					current = current.value

				if isinstance(current, ast.Name):
					namespace_parts.append(current.id)
					namespace_parts.reverse()

					namespaced_call = ".".join(namespace_parts)

					# Only consider top-level namespaces that aren't self-references or methods
					if current.id != "self":
						function_calls["with_namespace"].add(namespaced_call)
						top_level_namespaces.add(namespace_parts[0])

			# Handle standalone function calls (e.g., `print()`)
			elif isinstance(node.func, ast.Name):
				function_calls["without_namespace"].add(node.func.id)

	# Convert sets to lists for easier serialization
	function_calls["with_namespace"] = sorted(function_calls["with_namespace"])
	function_calls["without_namespace"] = sorted(function_calls["without_namespace"])
	top_level_namespaces = sorted(top_level_namespaces)

	result = {
		"function_calls": function_calls,
		"top_level_namespaces": top_level_namespaces
	}
	result = fix(result)
	return result





import ast

def replace_function_calls(code, corrections):
	tree = ast.parse(code)
	class FunctionCallReplacer(ast.NodeTransformer):

		def visit_Call(self, node):
			if isinstance(node.func, ast.Name) and node.func.id in corrections:
				node.func.id = corrections[node.func.id]
			return self.generic_visit(node)
	modified_tree = FunctionCallReplacer().visit(tree)
	updated_code = ast.unparse(modified_tree)
	return updated_code












def inject(code,add):
	code = code.replace('    ','\t')
	lines = []
	done = False
	for i,line in enumerate(code.split('\n')):
		lines.append(line)
		if not done:
			if line.startswith('def ') or line.startswith('class '):
				done = True
				for a in add:
					if not a in code:
						lines.append('\t'+a)
	return '\n'.join(lines)

def unGlobal(code,ug):
	lines = []
	done = False
	for g in ug:
		code = code.replace('global '+g,'')
		code = code.replace(''+g+'.','_.'+g+'.')
	for i,line in enumerate(code.split('\n')):
		if line.strip():
			lines.append(line)
	return '\n'.join(lines)

def action():
	global baseFN
	framework = {}
	for k in _.WidgetsFW_Clean:
		framework[_.WidgetsFW_Clean[k]] = k +' as '+_.WidgetsFW_Clean[k]
	
	if _.switches.isActive('Files'):
		code = _.getText(_.switches.value('Files'), raw=True)
	else:
		code = '\n'.join(_.isData(r=0))
	
	
	fn = extract_function_calls_from_code(code)
	if not _.switches.isActive('PrintCode'):
		_.pv(fn)
	hasBase = False
	corrections = {}
	for _fn in fn['function_calls']['without_namespace']:
		if _fn in baseFN:
			hasBase = True
			corrections[_fn] = '_.'+_fn
	head = []
	if hasBase or fn['globals']:
		head.append('import '+framework['_'])
	for m in fn['top_level_namespaces']:
		if m in framework:
			head.append('import '+framework[m])
		else:
			head.append('import '+m)
	hh = []
	for h in head:
		if not h in code:
			hh.append(h)
	head = hh
	code = replace_function_calls(code, corrections)
	add = []
	for g in fn['globals']:
		add.append(g)
	code = unGlobal(code,add)
	code = '\n'.join(head) + '\n\n' + code
	if _.switches.isActive('Save'):
		_.saveText(code, _.switches.value('Save'))	
	if _.switches.isActive('PrintCode'):
		_.pr(code)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);