#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#835B0032-Legacy
from clockwork import clockwork

api = clockwork.API("429ea819b2049a9e95c437a6caf33c33da5be506")
# message = clockwork.SMS( from_name = "Santa", to = "18136901260", message = "{6E477D20-F971-728A-64B8-B833\n\nCD8E1B45}" )
# message = clockwork.SMS( from_name = "Santa", to = "18134695709", message = "Official Notice\n\nYour brother is the favorite\n\n" )
# message = clockwork.SMS( from_name = "Santa", to = "17279023028", message = "Karla is officialy VERY cool\n\nAlmost as cool as Scott\n\n" )
response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_description)


