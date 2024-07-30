#!/bin/bash

# Check if the argument is provided
if [ -z "$1" ]; then
	echo "Please provide the server name."
	exit 1
fi

# Upload operations
scp $ww/python/vps*.py root@$1.m-eta.app:$ww/python/ 
ssh root@$1.m-eta.app 'chmod -R 777 $ww/'

scp -r $ww/bash/vps-srv/ root@$1.m-eta.app:$ww/widgets/bash/ 
ssh root@$1.m-eta.app 'chmod -R 777 $ww/widgets/bash/vps-srv/'

scp $ww/databank/tables/*.* root@$1.m-eta.app:$ww/widgets/databank/tables/ 
ssh root@$1.m-eta.app 'chmod -R 777 $ww/'