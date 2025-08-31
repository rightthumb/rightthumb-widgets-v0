#!/bin/bash

# Usage function to display help
usage() {
	echo "Usage: $0 [options]"
	echo "Options:"
	echo "  -a, --all        Compile and serve all frameworks (must provide project directories)"
	echo "  -r, --react      Compile and serve React (must provide project directory)"
	echo "  -v, --vue        Compile and serve Vue (must provide project directory)"
	echo "  -ng, --angular   Compile and serve Angular (must provide project directory)"
	echo "  -s, --svelte     Compile and serve Svelte (must provide project directory)"
	echo "  -so, --solid     Compile and serve SolidJS (must provide project directory)"
	echo "  -q, --qwik       Compile and serve Qwik (must provide project directory)"
	echo "  -p, --preact     Compile and serve Preact (must provide project directory)"
	echo "  -d, --directory  Specify project directory path (required)"
	echo "  -h, --help       Show this help message"
	exit 1
}

# Helper function to check if a package is installed
is_installed() {
  dpkg -l | grep -qw $1 || rpm -qa | grep -qw $1 || pacman -Qs $1 > /dev/null
}

# Function to install necessary packages based on the distro
install_dependencies() {
  # Check if Node.js and npm are installed, and install them if necessary
  if ! is_installed "nodejs"; then
	echo "🔄 Installing Node.js and npm..."
	if [ -f /etc/os-release ]; then
	. /etc/os-release
	case $ID in
		rhel|centos|alma)
		sudo dnf install -y nodejs npm
		;;
		debian|ubuntu)
		sudo apt-get update && sudo apt-get install -y nodejs npm
		;;
		arch)
		sudo pacman -Syu --noconfirm nodejs npm
		;;
		*)
		echo "❌ Unsupported distribution: $ID"
		exit 1
		;;
	esac
	fi
  fi

  # Check if Yarn is installed, and install it if necessary
  if ! is_installed "yarn"; then
	echo "🔄 Installing Yarn..."
	npm install -g yarn
  fi

  # Check if Babel is installed, and install it if necessary
  if ! is_installed "babel"; then
	echo "🔄 Installing Babel CLI globally..."
	npm install -g @babel/cli
  fi

  # Check if Webpack is installed, and install it if necessary
  if ! is_installed "webpack"; then
	echo "🔄 Installing Webpack globally..."
	npm install -g webpack webpack-cli
  fi

  echo "✅ Dependencies installed successfully!"
}

# Function to compile and run a given framework
compile_and_run() {
	local dir=$1
	local build_cmd=$2
	local run_cmd=$3
	local framework_name=$4

	if [ -d "$dir" ]; then
		echo "🔄 Building $framework_name app in '$dir'..."
		cd "$dir" || exit 1
		eval "$build_cmd"
		echo "✅ $framework_name build complete!"
		eval "$run_cmd"
		cd ..
	else
		echo "❌ Error: Directory '$dir' not found for $framework_name!"
	fi
}

# Parse arguments
if [ "$#" -eq 0 ]; then
	usage
fi

# Flags for selected frameworks
COMPILE_ALL=false
COMPILE_REACT=false
COMPILE_VUE=false
COMPILE_ANGULAR=false
COMPILE_SVELTE=false
COMPILE_SOLID=false
COMPILE_QWIK=false
COMPILE_PREACT=false
PROJECT_DIR=""

# Argument parsing loop
while [[ "$#" -gt 0 ]]; do
	case "$1" in
		-a|--all)        COMPILE_ALL=true ;;
		-r|--react)      COMPILE_REACT=true ;;
		-v|--vue)        COMPILE_VUE=true ;;
		-ng|--angular)   COMPILE_ANGULAR=true ;;
		-s|--svelte)     COMPILE_SVELTE=true ;;
		-so|--solid)     COMPILE_SOLID=true ;;
		-q|--qwik)       COMPILE_QWIK=true ;;
		-p|--preact)     COMPILE_PREACT=true ;;
		-d|--directory)  PROJECT_DIR="$2"; shift ;;  # Store project directory
		-h|--help)       usage ;;
		*) echo "❌ Unknown option: $1"; usage ;;
	esac
	shift
done

# Validate if the project directory was set when a framework option is selected
if [ -z "$PROJECT_DIR" ]; then
	echo "❌ Error: You must specify a project directory with '-d' or '--directory'."
	usage
fi

# Install dependencies for compiling JavaScript (Node.js, npm, Yarn, Babel, Webpack)
install_dependencies

# Compile all if flag is set
if [ "$COMPILE_ALL" = true ]; then
	COMPILE_REACT=true
	COMPILE_VUE=true
	COMPILE_ANGULAR=true
	COMPILE_SVELTE=true
	COMPILE_SOLID=true
	COMPILE_QWIK=true
	COMPILE_PREACT=true
fi

# Compile selected frameworks
if [ "$COMPILE_REACT" = true ]; then
	compile_and_run "$PROJECT_DIR" "npm run build" "npm start" "React"
fi

if [ "$COMPILE_VUE" = true ]; then
	compile_and_run "$PROJECT_DIR" "npm run build" "npm run dev" "Vue"
fi

if [ "$COMPILE_ANGULAR" = true ]; then
	compile_and_run "$PROJECT_DIR" "ng build --prod" "ng serve --open" "Angular"
fi

if [ "$COMPILE_SVELTE" = true ]; then
	compile_and_run "$PROJECT_DIR" "npm run build" "npm run dev" "Svelte"
fi

if [ "$COMPILE_SOLID" = true ]; then
	compile_and_run "$PROJECT_DIR" "npm run build" "npm run dev" "SolidJS"
fi

if [ "$COMPILE_QWIK" = true ]; then
	compile_and_run "$PROJECT_DIR" "npm run build" "npm run dev" "Qwik"
fi

if [ "$COMPILE_PREACT" = true ]; then
	compile_and_run "$PROJECT_DIR" "npm run build" "npm run dev" "Preact"
fi

echo "🎉 Compilation process finished!"


# ./compile-js.sh --react --directory /path/to/react-project
# ./compile-js.sh --all --directory /path/to/project
# ./compile-js.sh --vue --directory /path/to/vue-project
# ./compile-js.sh --help