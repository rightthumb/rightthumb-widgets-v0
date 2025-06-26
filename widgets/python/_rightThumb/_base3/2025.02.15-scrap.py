		indexOfGroupStuff = dot()
		indexOfGroupStuff.Group = []
		indexOfGroupStuff.SubGroup = []
		indexOfGroupStuff.NoGroup = []
		indexOfGroupStuff.Activity = []
		last_print_of_uncategorized_switch_preceding_dash = -2
		for I, item in enumerate(self.asset):
			result = ''
			for c in column.split(','):
				if switches.isActive('TablePlus'):
					if not  _.showLine(str(item),_.switches.values('TablePlus'),_.switches.values('TableMinus')): continue
				try:
					pass
				except Exception as e:
					pass
				self.isExtraRecord = False
				if self.wrapTableKey+'-sort' in item:
					self.isExtraRecord_000x = item[self.wrapTableKey+'-sort']
				if self.wrapTableKey+'-sort' in item and not item[self.wrapTableKey+'-sort'].endswith('-0001'):
					self.isExtraRecord = True
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab+tableLine
				except Exception as e:
					pass
			maxSize = len(result)+self.prefixSize()
			if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
				ToDo = " result = ''   "
				ToDo = ' for sult in self.wrapTable2(i):  '
				ToDo = '     result += sult  '
			else:
				ToDo = ' the below if will be under this else '
			if len(result) > 0:
				shouldPrint = True
				if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
					testResult = result
					testResult = testResult.replace( ' ', '' ).replace( '\t', '' )
					if not len(testResult):
						shouldPrint = False
				if shouldPrint:
					if 'IsSwitchSpacer' in item:
						print_()
						continue
					hasTotal=False
					_result_=''
					for c in column.split(','):
						if c in self.Groups and not i in self.Groups[c]['lines'] and i-1 in self.Groups[c]['lines']:
							hasTotal=True
					if hasTotal:
						for c in column.split(','):
							total={}
							for gc in self.GroupTotals:
								total[gc]=0
							_g_=switches.values('GroupBy')[0]
							_sub_=self.asset[i-1][_g_]
							for ass in self.asset:
								if _g_ in ass and ass[_g_] == _sub_:
									for gc in self.GroupTotals:
										total[gc]+=ass[gc]
							if c in self.GroupTotals:
								_result_+=addField( addComma(total[c]) ,c)
								self.GroupTotals[c]=0
							else:
								_result_+=addField('',c)
						cp(' '+tableLine+_result_,c='green')
					isSwitchGroup = False
					if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):
						cp( [ self.tab['table']+loopPrint(__.table_prefix_padding) + result ], 'BackgroundGrey.blue' )
					else:
						if result.strip().startswith('Help  '):print_('')
						SwitchGroupPostLabel = ''
						if 'SwitchGroupPostLabel' in item and  'example_or_notes' in item :
							isSwitchGroup = True
							SwitchGroupPostLabel = pr(__.SwitchGroup_Help.PostLabel,item['SwitchGroupPostLabel'],c=helpColorScheme.tableSwitchGroupsPostLabel,p=0)
						if 'SwitchSubGroup' in item and  'example_or_notes' in item :
							isSwitchGroup = True
							if 'SwitchGroupDepth' in item and  'example_or_notes' in item :
								SwitchGroupDepth = item['SwitchGroupDepth']
							else:
								SwitchGroupDepth = 1
							if len(__.SwitchGroup_Help.SubGroup) ==1:
								SwitchGroupDepth +=1
							pr(pr(__.SwitchGroup_Help.SubGroup * SwitchGroupDepth+__.SwitchGroup_Help.Delim+' '+item['SwitchSubGroup'],c='ColorBold.white',p=0),SwitchGroupPostLabel)
						if 'SwitchGroup' in item and  'example_or_notes' in item :
							isSwitchGroup = True
							print()
							if 'HasSwitchSubGroup' in item and  'example_or_notes' in item :
								pr('_' * max_length,c=helpColorScheme.tableSwitchGroupsLine)
								pass
							SwitchGroup = __.SwitchGroup_Help.Group
							if item['SwitchGroup'] == '':
								SwitchGroup = __.SwitchGroup_Help.NoGroup
							if not I-1 == last_print_of_uncategorized_switch_preceding_dash:
								pr(  pr(SwitchGroup+__.SwitchGroup_Help.Delim+' '+item['SwitchGroup'],c='ColorBold.white',p=0)  ,  SwitchGroupPostLabel)
							last_print_of_uncategorized_switch_preceding_dash = I
						if isSwitchGroup:
							theLine = tableLine+result.lstrip()
						else:
							theLine = tableLine+result
						shouldPrint = True
						if not theLine.strip() and switches.isActive('GroupBy'):
							shouldPrint = False
						if shouldPrint:
							colorizeRow( theLine, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )