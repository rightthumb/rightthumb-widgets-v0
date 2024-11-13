import inspect

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

 
 
class ReverseEngineerCode:
   def __init__(self):
	self.full_stack = inspect.stack()
	self.this_module = __file__
	self.recursion_level = 0
	self.max_recursion_level = 2000
 
   def follow_frame(self, fframe):
	if self.recursion_level <= self.max_recursion_level:
		try:
			for group in fframe:
				if group.code_context is None:
					continue
				if group.filename == self.this_module and group.function == '__init__':
					continue
				print('group.filename level-{}: {}'.format(self.recursion_level, group.filename))
				print('group.lineno level-{}: {}'.format(self.recursion_level, group.lineno))
				print('group.function level-{}: {}'.format(self.recursion_level, group.function))
				print('group.code_contextlevel-{}:'.format(self.recursion_level))
				for line in group.code_context:
					print(line)
				print('group.index level-{}: {}'.format(self.recursion_level, group.index))
				print('group.frame level-{}: {}'.format(self.recursion_level, group.frame))
				print('---------------------------------------------------------\n')
				if inspect.isfunction(group.function):
					self.recursion_level += 1
					self.follow_frame(group.frame)
		except:
			print("Unexpected error:", sys.exc_info()[0])
		finally:
			del fframe
 
 
   def start_trace(self):
	self.recursion_level = 0
	self.follow_frame(self.full_stack)
 
def function1():
   te = ReverseEngineerCode()
   te.start_trace()
 
def function3():
   function1()
 
 
def function2():
   function3()
 
 
def main():
   function2()
 
 
if __name__ == '__main__':
   main()


