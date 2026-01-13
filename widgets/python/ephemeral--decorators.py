#!/usr/bin/python3

import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()


_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ))
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper



@my_decorator
def say_hello1():
    print("Hello!")

print()
say_hello1()

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                print(f"Iteration {_+1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello2():
    print("Hello!")


print()
say_hello2()
print()

#####################

def conditional_execution_decorator(target_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args[0] == target_value:
                print(f"Variable matches {target_value}. Executing special code.")
                # Execute some code here
                # Optionally, return here if you don't want to call the function
                return
            else:
                print(f"Variable does not match {target_value}. Executing function.")
                return func(*args, **kwargs)
        return wrapper
    return decorator

@conditional_execution_decorator('abc')
def my_function(variable):
    print("Function is running with variable:", variable)

# Example usage
print()
my_function('abc')  # Special code is executed, function is not called
print()
my_function('xyz')  # Function is executed as normal


