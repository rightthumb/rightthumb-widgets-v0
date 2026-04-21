#!/bin/bash
# distro-info.sh
# A script to tell you exactly what Linux distro you are using

echo "Detecting Linux distribution..."

if [ -f /etc/os-release ]; then
    # Standard on most modern distros
    . /etc/os-release
    echo "Name: $NAME"
    echo "Pretty Name: $PRETTY_NAME"
    echo "Version: $VERSION"
    echo "ID: $ID"
    echo "Version ID: $VERSION_ID"
elif [ -f /etc/lsb-release ]; then
    # Ubuntu/Debian derivatives
    . /etc/lsb-release
    echo "Distributor ID: $DISTRIB_ID"
    echo "Description: $DISTRIB_DESCRIPTION"
    echo "Release: $DISTRIB_RELEASE"
    echo "Codename: $DISTRIB_CODENAME"
elif command -v lsb_release >/dev/null 2>&1; then
    # If the lsb_release command exists
    lsb_release -a
elif [ -f /etc/redhat-release ]; then
    # Red Hat, CentOS, AlmaLinux, Rocky Linux, etc.
    echo "Red Hat-based distribution: $(cat /etc/redhat-release)"
elif [ -f /etc/debian_version ]; then
    # Debian
    echo "Debian version: $(cat /etc/debian_version)"
else
    # Fallback
    echo "Unknown distribution"
    uname -a
fi
