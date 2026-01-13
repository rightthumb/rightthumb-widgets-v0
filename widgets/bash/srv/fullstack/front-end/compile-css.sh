#!/bin/bash

# Usage function to display help
usage() {
	echo "Usage: $0 [options]"
	echo "Options:"
	echo "  -a, --all        Compile and serve all CSS frameworks (must provide project directories)"
	echo "  -scss, --sass    Compile and serve SCSS (must provide project directory)"
	echo "  -less, --less    Compile and serve LESS (must provide project directory)"
	echo "  -styl, --stylus  Compile and serve Stylus (must provide project directory)"
	echo "  -postcss         Compile and serve PostCSS (must provide project directory)"
	echo "  -css, --css      Compile plain CSS (must provide project directory)"
	echo "  -bower            Install dependencies with Bower (must provide project directory)"
	echo "  -webpack          Bundle and serve CSS with Webpack (must provide project directory)"
	echo "  -gulp             Compile and serve CSS with Gulp (must provide project directory)"
	echo "  -grunt            Compile and serve CSS with Grunt (must provide project directory)"
	echo "  -d, --directory  Specify project directory path (required)"
	echo "  -h, --help       Show this help message"
	exit 1
}

# Function to compile a given CSS method
compile_and_run() {
	local dir=$1
	local build_cmd=$2
	local run_cmd=$3
	local framework_name=$4

	if [ -d "$dir" ]; then
		echo "🔄 Compiling $framework_name CSS in '$dir'..."
		cd "$dir" || exit 1
		eval "$build_cmd"
		echo "✅ $framework_name compilation complete!"
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
COMPILE_SASS=false
COMPILE_LESS=false
COMPILE_STYLUS=false
COMPILE_POSTCSS=false
COMPILE_CSS=false
COMPILE_BOWER=false
COMPILE_WEBPACK=false
COMPILE_GULP=false
COMPILE_GRUNT=false
PROJECT_DIR=""

# Argument parsing loop
while [[ "$#" -gt 0 ]]; do
	case "$1" in
		-a|--all)        COMPILE_ALL=true ;;
		-scss|--sass)    COMPILE_SASS=true ;;
		-less|--less)    COMPILE_LESS=true ;;
		-styl|--stylus)  COMPILE_STYLUS=true ;;
		-postcss)        COMPILE_POSTCSS=true ;;
		-css|--css)      COMPILE_CSS=true ;;
		-bower)          COMPILE_BOWER=true ;;
		-webpack)        COMPILE_WEBPACK=true ;;
		-gulp)           COMPILE_GULP=true ;;
		-grunt)          COMPILE_GRUNT=true ;;
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

# Compile all if flag is set
if [ "$COMPILE_ALL" = true ]; then
	COMPILE_SASS=true
	COMPILE_LESS=true
	COMPILE_STYLUS=true
	COMPILE_POSTCSS=true
	COMPILE_CSS=true
	COMPILE_BOWER=true
	COMPILE_WEBPACK=true
	COMPILE_GULP=true
	COMPILE_GRUNT=true
fi

# Compile SCSS/SASS
if [ "$COMPILE_SASS" = true ]; then
	compile_and_run "$PROJECT_DIR" "sass input.scss output.css" "serve-css" "SCSS"
fi

# Compile LESS
if [ "$COMPILE_LESS" = true ]; then
	compile_and_run "$PROJECT_DIR" "lessc input.less output.css" "serve-css" "LESS"
fi

# Compile Stylus
if [ "$COMPILE_STYLUS" = true ]; then
	compile_and_run "$PROJECT_DIR" "stylus input.styl -o output.css" "serve-css" "Stylus"
fi

# Compile PostCSS
if [ "$COMPILE_POSTCSS" = true ]; then
	compile_and_run "$PROJECT_DIR" "postcss input.css -o output.css" "serve-css" "PostCSS"
fi

# Compile plain CSS (e.g., via CSS Minification or other bundlers)
if [ "$COMPILE_CSS" = true ]; then
	compile_and_run "$PROJECT_DIR" "css-minifier input.css output.css" "serve-css" "Plain CSS"
fi

# Install Bower dependencies
if [ "$COMPILE_BOWER" = true ]; then
	if [ -f "$PROJECT_DIR/bower.json" ]; then
		echo "🔄 Installing dependencies with Bower in '$PROJECT_DIR'..."
		cd "$PROJECT_DIR" || exit 1
		bower install
		echo "✅ Bower dependencies installed!"
		cd ..
	else
		echo "❌ Error: No 'bower.json' found in the project directory!"
	fi
fi

# Webpack build and serve CSS
if [ "$COMPILE_WEBPACK" = true ]; then
	if [ -f "$PROJECT_DIR/webpack.config.js" ]; then
		echo "🔄 Bundling CSS with Webpack in '$PROJECT_DIR'..."
		cd "$PROJECT_DIR" || exit 1
		webpack --config webpack.config.js
		echo "✅ Webpack build complete!"
		cd ..
	else
		echo "❌ Error: No 'webpack.config.js' found in the project directory!"
	fi
fi

# Gulp build and serve CSS
if [ "$COMPILE_GULP" = true ]; then
	if [ -f "$PROJECT_DIR/Gulpfile.js" ]; then
		echo "🔄 Running Gulp tasks in '$PROJECT_DIR'..."
		cd "$PROJECT_DIR" || exit 1
		gulp
		echo "✅ Gulp build complete!"
		cd ..
	else
		echo "❌ Error: No 'Gulpfile.js' found in the project directory!"
	fi
fi

# Grunt build and serve CSS
if [ "$COMPILE_GRUNT" = true ]; then
	if [ -f "$PROJECT_DIR/Gruntfile.js" ]; then
		echo "🔄 Running Grunt tasks in '$PROJECT_DIR'..."
		cd "$PROJECT_DIR" || exit 1
		grunt
		echo "✅ Grunt build complete!"
		cd ..
	else
		echo "❌ Error: No 'Gruntfile.js' found in the project directory!"
	fi
fi

echo "🎉 CSS compilation process finished!"


# Below are the usage instructions and install commands for each method.

# SCSS (Sass)
# Usage:
# sass input.scss output.css
# Install Sass:
# npm install -g sass
#
# Compile SCSS into CSS
# sass input.scss output.css

# LESS
# Usage:
# lessc input.less output.css
# Install LESS:
# npm install -g less
#
# Compile LESS into CSS
# lessc input.less output.css

# Stylus
# Usage:
# stylus input.styl -o output.css
# Install Stylus:
# npm install -g stylus
#
# Compile Stylus into CSS
# stylus input.styl -o output.css

# PostCSS
# Usage:
# postcss input.css -o output.css
# Install PostCSS:
# npm install -g postcss postcss-cli
#
# Compile CSS with PostCSS
# postcss input.css -o output.css

# Plain CSS (Minification example)
# Usage:
# css-minifier input.css output.css
# Install CSS Minifier:
# npm install -g css-minifier
#
# Minify a CSS file
# css-minifier input.css output.css

# Bower
# Usage:
# bower install
# Install Bower:
# npm install -g bower
#
# Install Bower dependencies
# bower install

# Webpack
# Usage:
# webpack --config webpack.config.js
# Install Webpack:
# npm install -g webpack webpack-cli
#
# Bundle CSS with Webpack
# webpack --config webpack.config.js

# Gulp
# Usage:
# gulp
# Install Gulp:
# npm install -g gulp-cli
#
# Run Gulp tasks
# gulp

# Grunt
# Usage:
# grunt
# Install Grunt:
# npm install -g grunt-cli
#
# Run Grunt tasks
# grunt