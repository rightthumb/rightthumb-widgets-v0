#!/bin/bash

command1 || command2





{ # try

	command1 &&
	#save your output

} || { # catch
	# save log for exception 
}



# https://stackoverflow.com/questions/22009364/is-there-a-try-catch-command-in-bash