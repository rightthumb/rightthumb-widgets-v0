	carage = []

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

	whitespace = []
	comma = []

	parenthesesOpen = []
	parenthesesClose = []

	bracketsOpen = []
	bracketsClose = []
	
	bracesOpen = []
	bracesClose = []

	singleQuote = []
	doubleQuote = []

	angleOpen = []
	angleClose = []

	alphanumeric = []
	equals = []
	semicolon = []
	colon = []
	pound = []

	other = []

	star = []
	backslash = []
	forward = []
	period = []


	for i,ch in enumerate(fileText):
		if ch == '\n':
			carage.append( i )
		elif ch == ' ' or ch == '\t':
			whitespace.append( i )
		elif ch == '(':
			parenthesesOpen.append( i )
		elif ch == ')':
			parenthesesClose.append( i )
		elif ch == '[':
			bracketsOpen.append( i )
		elif ch == ']':
			bracketsClose.append( i )
		elif ch == '{':
			bracesOpen.append( i )
		elif ch == '}':
			bracesClose.append( i )
		elif ch == "'":
			singleQuote.append( i )
		elif ch == '"':
			doubleQuote.append( i )
		elif ch in an:
			alphanumeric.append( i )
		elif ch == '=':
			equals.append( i )
		elif ch == ';':
			semicolon.append( i )
		elif ch == ':':
			colon.append( i )
		elif ch == '#':
			pound.append( i )
		elif ch == ',':
			comma.append( i )
		elif ch == _v.slash:
			backslash.append( i )
		elif ch == '/':
			forward.append( i )
		elif ch == '*':
			star.append( i )
		elif ch == '<':
			angleOpen.append( i )
		elif ch == '>':
			angleClose.append( i )
		elif ch == '.':
			period.append( i )
		elif ch == '+':
			pass
		else:
			other.append( i )
			print( ch, len(carage) )

	print( "carage:", len(carage) )
	print( "whitespace:", len(whitespace) )
	print( "comma:", len(comma) )
	print()
	print( "parenthesesOpen:", len(parenthesesOpen) )
	print( "parenthesesClose:", len(parenthesesClose) )
	print()
	print( "bracketsOpen:", len(bracketsOpen) )
	print( "bracketsClose:", len(bracketsClose) )
	print()
	print( "bracesOpen:", len(bracesOpen) )
	print( "bracesClose:", len(bracesClose) )
	print()
	print( "singleQuote:", len(singleQuote) )
	print( "doubleQuote:", len(doubleQuote) )
	print()
	print( "angleOpen:", len(angleOpen) )
	print( "angleClose:", len(angleClose) )
	print()
	print( "alphanumeric:", len(alphanumeric) )
	print( "equals:", len(equals) )
	print( "semicolon:", len(semicolon) )
	print( "colon:", len(colon) )
	print( "pound:", len(pound) )
	print()
	print( "other:", len(other) )
	print()
	print( "star:", len(star) )
	print( "backslash:", len(backslash) )
	print( "forward:", len(forward) )


	print( 'carage:', len(carage) )
	print( 'i:', i )


