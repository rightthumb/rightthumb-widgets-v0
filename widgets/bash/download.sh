#!/bin/bash

# Check if the argument is provided
if [ -z "$1" ]; then
	echo "Please provide the server name."
	exit 1
fi

# Download operations
scp -rp root@$1.m-eta.app:$ww/python/vps* $ww/python/
chmod 777 -R $ww/python/

scp -r root@$1.m-eta.app:$ww/widgets/bash/vps-srv/ $ww/bash/
chmod 777 -R $ww/bash/vps-srv/

scp -rp root@$1.m-eta.app:$ww/widgets/databank/tables/*.* $ww/databank/tables/
chmod 777 -R $ww/databank/tables/