#!/bin/bash








# Recoll is a desktop search application for Linux (and other Unix-like systems) that allows users to search for text within documents on their computer. It is known for its ability to index and search a wide variety of document formats, making it a versatile tool for finding information on a local machine.

# Key features of Recoll include:

# - **Wide Format Support**: Recoll can index many document types, including but not limited to plain text, HTML, email (Thunderbird, KMail), PDF, OpenOffice.org and LibreOffice files, Microsoft Office files, PostScript, RTF, and many more.

# - **Powerful Search Capabilities**: It supports complex search queries, including phrase searches, boolean queries, and even regular expressions.

# - **Full-Text Indexing**: Recoll creates an index of the contents of files, allowing for fast searches.

# - **User Interface**: It provides both a graphical user interface (GUI) and a command-line interface (CLI), catering to different user preferences.

# - **Configuration and Customization**: Users can configure and customize Recoll to include or exclude certain directories, file types, and more.

# - **Cross-Platform**: Although primarily used on Linux, Recoll is also available for other platforms, including Windows and macOS.

# Recoll is well-regarded for its efficiency and effectiveness, particularly for users who need to manage and search through large collections of documents. It is open-source software, meaning that it is free to use and modify under the terms of its license.









set -e

# Exit if already installed
if command -v recollq >/dev/null 2>&1; then
	echo "✅ recollq is already installed."
	exit 0
fi

# Function to build from source
install_recoll_from_source() {
	echo "🔧 Building recoll CLI from source..."

	sudo mkdir -p /usr/local/src/recoll-cli && cd /usr/local/src/recoll-cli

	# Install dependencies
	if command -v dnf >/dev/null 2>&1; then
		sudo dnf install -y git make gcc xapian-core-devel python3-devel qt5-qttools qt5-qtbase-devel
	fi
	if command -v yum >/dev/null 2>&1; then
		sudo yum install -y git make gcc xapian-core-devel python3-devel qt5-qttools qt5-qtbase-devel
	fi
	if command -v apt >/dev/null 2>&1; then
		sudo apt update && sudo apt install -y git make g++ libxapian-dev python3-dev qttools5-dev qtbase5-dev
	fi
	if command -v pacman >/dev/null 2>&1; then
		sudo pacman -Sy --noconfirm git base-devel xapian-core python qt5-base qt5-tools
	fi

	# Clone and build Recoll
	git clone https://framagit.org/medoc92/recoll.git .
	./configure --without-gui
	make
	sudo make install

	echo "✅ recoll CLI installed successfully."
}

# Try system package managers first
if command -v apt >/dev/null 2>&1; then
	sudo apt update && sudo apt install -y recoll && exit 0
fi

if command -v pacman >/dev/null 2>&1; then
	sudo pacman -Sy --noconfirm recoll && exit 0
fi

if command -v dnf >/dev/null 2>&1; then
	echo "❌ recoll not found in dnf repos. Building from source..."
	install_recoll_from_source
	exit $?
fi

if command -v yum >/dev/null 2>&1; then
	echo "❌ recoll not found in yum repos. Building from source..."
	install_recoll_from_source
	exit $?
fi

echo "❌ No supported package manager found."
exit 1