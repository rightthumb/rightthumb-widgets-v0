## start replace:

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

## end replace:

## remove all before: 
## def appSwitches():
## replace with
from rightthumb import app
from rightthumb import func as _
reg = app.space(__name__, __file__)
## move up registration variables

## start replace:



_.appInfo[focus()]
reg.documentation

_.appData[focus()]
reg.data

__.thisApp
app.this_app

_.hp
app.hp

## end replace:

## add above appSwitches()
reg.rent = app.register(reg)
app.rent = app.focus(reg.rent)
app.switches()
# app.tables()






## start replace:

appSwitches()
app_switches

_.switches.register
app.switch.reg

registerSwitches
sw

_.load()
app.load()

__.constructRegistration
app.construct_registration

_.argvProcess
app.argv_process

registerSwitches()
sw()

fieldSet(
field_set(

theFocus
rent

_.setPipeData
app.set_pipe_data

_.postLoad
app.post_load

__.isExit()
__.isExit(diagram=False)

## end replace:

## start convert

_.switches.isActive('Subject')
app.switch('Subject').status

_.switches.value('Files')
app.switch('Files').value

## start convert

## start replace:

_.switches.
app.switch.

## end replace:

