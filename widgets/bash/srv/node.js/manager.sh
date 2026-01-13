#!/bin/bash

# Colors for output
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m" # No Color

# Function to display help menu
show_help() {
  echo -e "${GREEN}Node.js Project Management Script${NC}"
  echo -e "${YELLOW}Usage:${NC} $0 [command] [options]"
  echo
  echo "Commands:"
  echo "  setup             Set up a new Node.js project (install all dependencies)"
  echo "  build             Build the project using Webpack"
  echo "  run               Run the app (node app.js)"
  echo "  minify            Minify the output using Terser"
  echo "  package           Package the project into a single file"
  echo "  clean             Remove build artifacts"
  echo "  help              Show this help menu"
  echo
}

# Function to set up the project
setup_project() {
  echo -e "${YELLOW}Setting up the Node.js project...${NC}"
  
  echo -e "${GREEN}Installing global tools: Webpack and Webpack CLI...${NC}"
  npm install -g webpack webpack-cli

  echo -e "${GREEN}Installing project dependencies...${NC}"
  npm install express body-parser crypto-js node-cryptojs-aes --save

  echo -e "${GREEN}Setup complete!${NC}"
}

# Function to build the project using Webpack
build_project() {
  echo -e "${YELLOW}Building the project using Webpack...${NC}"
  
  if [ ! -f webpack.config.js ]; then
	echo -e "${RED}Error: webpack.config.js not found. Please create it first.${NC}"
	exit 1
  fi

  npx webpack --config webpack.config.js

  echo -e "${GREEN}Build complete!${NC}"
}

# Function to run the app
run_app() {
  if [ ! -f app.js ]; then
	echo -e "${RED}Error: app.js not found. Please create it first.${NC}"
	exit 1
  fi

  echo -e "${YELLOW}Running the app...${NC}"
  node app.js
}

# Function to minify JavaScript files using Terser
minify_js() {
  echo -e "${YELLOW}Minifying JavaScript files...${NC}"
  npx terser dist/main.js -o dist/main.min.js --compress --mangle

  echo -e "${GREEN}Minification complete: dist/main.min.js${NC}"
}

# Function to package the project
package_project() {
  echo -e "${YELLOW}Packaging the project into a single file...${NC}"
  tar -czf project.tar.gz .

  echo -e "${GREEN}Packaging complete: project.tar.gz${NC}"
}

# Function to clean build artifacts
clean_build() {
  echo -e "${YELLOW}Cleaning build artifacts...${NC}"
  rm -rf dist *.tar.gz

  echo -e "${GREEN}Clean complete.${NC}"
}

# Main execution
case $1 in
  setup)
	setup_project
	;;
  build)
	build_project
	;;
  run)
	run_app
	;;
  minify)
	minify_js
	;;
  package)
	package_project
	;;
  clean)
	clean_build
	;;
  help)
	show_help
	;;
  *)
	echo -e "${RED}Error: Unknown command '$1'. Use 'help' for a list of available commands.${NC}"
	exit 1
	;;
esac