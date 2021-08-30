

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


from os import path
class Simple_JSON_Fix:
	def __init__( self, path_or_code, i=0, save=None ):
		self.index={}
		if path.isfile(path_or_code):
			with open( path_or_code, 'r' ) as file:
				self.asset = file.read()
		else:
			self.asset = path_or_code

		while self.asset.startswith(' ') or self.asset.startswith('\t'):
			self.asset=self.asset[1:]
		code=self.asset
		self.index = self.vindex(self.asset,i)
		self.var=self.variable()

		if not save is None and save and path.isfile(path_or_code):
			if type(save) == str:
				path_or_code=save

			try:
				import simplejson
				f = open(path_or_code,'w')
				f.write(str(simplejson.dumps(self.var, indent=4, sort_keys=False)))
				f.close()
			except Exception as e:
				print(e)



	def vindex( self,code, i=0, esc='\\', n='', v=True,r=False,both=True ):
		if type(code)==list:
			code=''.join(code)
		at=i

			
		table={}
		
		table['brackets'] = {}
		table['brackets']['i']=0
		table['brackets']['open'] = {}

		table['braces'] = {}
		table['braces']['i']=0
		table['braces']['open'] = {}

		table['par'] = {}
		table['par']['i']=0
		table['par']['open'] = {}



		index={}

		i-=1
		while True:
			i+=1
			if i >= len(code):
				break
			c=code[i]
			try:
				c2=c+code[i+1]
			except Exception as e:
				c2=''
			try:
				c3=c2+code[i+2]
			except Exception as e:
				c3=''
			try:
				c4=c3+code[i+3]
			except Exception as e:
				c4=''
			try:
				c5=c4+code[i+4]
			except Exception as e:
				c5=''
			if len(esc) == 1 and c==esc:
				i+=1
			else:
				if len(esc) == 1 and c==esc:
					i+=1
				if n=='\n' and r:
					ii=i
					c=code[i]
					while not ii == 0 and c == '\n':
						ii-=1
						c=code[ii]
						if ii == 0:
							return 0
						elif c == '\n':
							return ii

				elif len(n) == 1 and c==n:
					return i
				elif len(n) == 2 and c2==n:
					return i+1
				elif len(n) == 3 and c3==n:
					return i+2
				elif len(n):
					pass
				else:
					if not n and c in '0123456789.':
						cx = c
						ii=i-1
						while cx in '0123456789.':
							ii+=1
							try:
								cx=code[ii]
							except Exception as e:
								ii-=1
								index[i] = ii
								if both:
									index[ii] = i
								break
						index[i] = ii
						if both:
							index[ii] = i
						i=ii
					elif not n and c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
						cx = c
						ii=i-1
						while cx in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._':
							ii+=1
							try:
								cx=code[ii]
							except Exception as e:
								ii-=1
								index[i] = ii
								if both:
									index[ii] = i
								break

						index[i] = ii
						if both:
							index[ii] = i
						i=ii
					elif not n and c3 == '"""':
						s=self.vindex(code,i+3,esc,n='"""',v=0)
						index[i] = s
						if both:
							index[s] = i
						i=s
					elif not n and c3 == "'''":
						s=self.vindex(code,i+3,esc,n="'''",v=0)
						index[i] = s
						if both:
							index[s] = i
					elif not n and c == "'":
						s=self.vindex(code,i+1,esc,n="'",v=0)
						index[i] = s
						if both:
							index[s] = i
						i=s
					elif not n and c == '"':
						s=self.vindex(code,i+1,esc,n='"',v=0)
						index[i] = s
						if both:
							index[s] = i
						i = s
					elif not n and c2 == '/*':
						i = vindex(code,i+2,esc,n='*/',v=0)
					elif not n and c2 == '//':
						i = vindex(code,i+2,esc,n='\n',v=0)+1


					elif not n and c == '{':
						table['brackets']['i']+=1
						table['brackets']['open'][table['brackets']['i']]=i
					elif not n and c == '}':
						s=table['brackets']['open'][table['brackets']['i']]
						index[ s ]=i
						if both:
							index[ i ]=s
						table['brackets']['i']-=1
						if s==at:
							return index
					elif not n and c == '[':
						table['braces']['i']+=1
						table['braces']['open'][table['braces']['i']]=i
					elif not n and c == ']':
						s=table['braces']['open'][table['braces']['i']]
						index[ s ]=i
						if both:
							index[ i ]=s
						table['braces']['i']-=1
						if s==at:
							return index
					elif not n and c == '(':
						table['par']['i']+=1
						table['par']['open'][table['par']['i']]=i
					elif not n and c == ')':
						s=table['par']['open'][table['par']['i']]
						index[ s ]=i
						if both:
							index[ i ]=s
						table['par']['i']-=1
						if s==at:
							return index
		
		return index


	def genJson_rec( self, dic ):

		n = {}
		for k in dic:
			n[k] = dic[k]
		self.var_records.append(n)


	def variable( self ):
		self.var_records = []
		def getData(o,c,f=None, p=[],v={}, l=None, spent=[], rec=[], top=True, li=[]):
			oo = o
			cc = c

			while oo < c :
				if oo in spent:
					oo+=1
				spent.append(oo)
				if oo in self.index:
					
					cc = self.index[oo]
					txt=self.asset[oo:cc+1]
					# print(txt)
					txtl=txt.lower()
					if txt.startswith('"') or txt.startswith('"'):
						txtq=txt[1:-1]
					else:
						txtq=txt
					
					if txt.startswith('['):
						if not f is None:
							z2 = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=[], top=True, li=[])
							v[f] = z2
						else:
							vx = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=False, li=li)
						f = None
					elif txt.startswith('{'):
						if not f is None:
							z2 = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=True, li=li)
							v[f] = z2
						else:
							vy = getData( oo, cc, None, p, {}, l, spent, rec, False, li )
							self.genJson_rec(vy)
						f = None
					elif txt and txt[0] in '"':
						li.append(txtq)

						if self.asset[o] == '{':
							if f is None:
								f = txtq
								p.append(f)
							else:
								v[f] = txtq
								f = None


					elif txt and txt[0] in '0123456789.-':
						if '.' in txt:
							xx = float(txt.replace(',',''))
						else:
							xx = int(txt.replace(',',''))
						li.append(xx)
						v[f] = xx
						f = None

					elif txtl.lower().startswith('true'):
						li.append(True)
						v[f] = True
						f = None
					elif txtl.lower().startswith('false'):
						li.append(False)
						v[f] = False
						f = None
					elif txtl.lower().startswith('null'):
						li.append(None)
						v[f] = None
						f = None
					oo = cc


				oo+=1
			if top:
				if self.asset[o] == '[':
					if self.var_records:
						return self.var_records
					else:
						return li
				else:
					if len(self.var_records) > 1:
						return self.var_records
					if self.var_records:
						return self.var_records[0]
					return v
			if self.asset[o] == '[':
				return li
			return v
			if self.asset[o] == '{':
				return v

		o = 0
		c = len(self.asset)-1
		ss = getData(o,c)
		self.var=ss
		return ss

	def find_all( self, string, sub ):
		def find_all_run( string, sub ):
			s = 0
			while True:
				s = string.find(sub, s)
				if s == -1: return
				yield s
				s += len(sub)
		return list(find_all_run(string, sub))



test=Simple_JSON_Fix( 'D:\\.rightthumb-widgets\\hosts\\VULCAN\\tables\\fileBackup.json', save=1 )
python_variable=test.var

