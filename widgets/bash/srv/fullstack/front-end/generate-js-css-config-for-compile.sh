#!/bin/bash

# Usage function to display help
usage() {
	echo "Usage: $0 [options]"
	echo "Options:"
	echo "  -d, --directory  Specify the folder to save config file (optional, default is current folder)"
	echo "  -t, --template   Specify the template to generate (sass, less, stylus, postcss, webpack, gulp, grunt, bower)"
	echo "  -h, --help       Show this help message"
	exit 1
}

# Parse arguments
TARGET_DIR="."
TEMPLATE=""

# Argument parsing loop
while [[ "$#" -gt 0 ]]; do
	case "$1" in
		-d|--directory)  TARGET_DIR="$2"; shift ;;  # Store target directory
		-t|--template)   TEMPLATE="$2"; shift ;;  # Store template choice
		-h|--help)       usage ;;
		*) echo "❌ Unknown option: $1"; usage ;;
	esac
	shift
done

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
	echo "❌ Error: Directory '$TARGET_DIR' not found!"
	exit 1
fi

# Ensure template option is specified
if [ -z "$TEMPLATE" ]; then
	echo "❌ Error: No template specified. Use the -t option to specify a template."
	usage
fi

echo "Generating '$TEMPLATE' config in '$TARGET_DIR'..."

# Generate the specified config template
case "$TEMPLATE" in
	sass)
		CONFIG_FILE="$TARGET_DIR/sass.config.js"
		cat > "$CONFIG_FILE" <<EOL
// SCSS (Sass) config template
module.exports = {
	input: 'src/styles.scss',   // Input file (adjust as needed)
	output: 'dist/styles.css',  // Output file
	options: {
		sourceMap: true,  // Enable source maps
		style: 'compressed'  // Compression options: 'expanded', 'nested', 'compact', 'compressed'
	}
};
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	less)
		CONFIG_FILE="$TARGET_DIR/less.config.js"
		cat > "$CONFIG_FILE" <<EOL
// LESS config template
module.exports = {
	input: 'src/styles.less',  // Input file (adjust as needed)
	output: 'dist/styles.css', // Output file
	options: {
		compress: true  // Enable minification
	}
};
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	stylus)
		CONFIG_FILE="$TARGET_DIR/stylus.config.js"
		cat > "$CONFIG_FILE" <<EOL
// Stylus config template
module.exports = {
	input: 'src/styles.styl',  // Input file (adjust as needed)
	output: 'dist/styles.css', // Output file
	options: {
		compress: true  // Enable minification
	}
};
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	postcss)
		CONFIG_FILE="$TARGET_DIR/postcss.config.js"
		cat > "$CONFIG_FILE" <<EOL
// PostCSS config template
module.exports = {
	plugins: [
		require('autoprefixer'), // Automatically add vendor prefixes
		require('cssnano')       // Minify CSS
	]
};
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	webpack)
		CONFIG_FILE="$TARGET_DIR/webpack.config.js"
		cat > "$CONFIG_FILE" <<EOL
// Webpack CSS bundling config template
const path = require('path');

module.exports = {
	entry: './src/styles.css',  // Input file
	output: {
		filename: 'bundle.css',  // Output file
		path: path.resolve(__dirname, 'dist')
	},
	module: {
		rules: [
			{
				test: /\.css$/,
				use: ['style-loader', 'css-loader']  // CSS processing loaders
			}
		]
	}
};
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	gulp)
		CONFIG_FILE="$TARGET_DIR/gulpfile.js"
		cat > "$CONFIG_FILE" <<EOL
// Gulp config template for CSS tasks
const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const cleanCSS = require('gulp-clean-css');

gulp.task('sass', function () {
	return gulp.src('src/styles.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(cleanCSS())
		.pipe(gulp.dest('dist'));
});

gulp.task('watch', function () {
	gulp.watch('src/styles.scss', gulp.series('sass'));
});

gulp.task('default', gulp.series('sass', 'watch'));
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	grunt)
		CONFIG_FILE="$TARGET_DIR/Gruntfile.js"
		cat > "$CONFIG_FILE" <<EOL
// Grunt config template for CSS tasks
module.exports = function(grunt) {
	grunt.initConfig({
		sass: {
			dist: {
				files: {
					'dist/styles.css': 'src/styles.scss'  // Input and output files
				}
			}
		},
		watch: {
			styles: {
				files: ['src/styles.scss'],
				tasks: ['sass']
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');

	grunt.registerTask('default', ['sass', 'watch']);
};
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	bower)
		CONFIG_FILE="$TARGET_DIR/bower.json"
		cat > "$CONFIG_FILE" <<EOL
{
  "name": "project-name",
  "dependencies": {
	"bootstrap": "^5.0.0",
	"jquery": "^3.6.0"
  }
}
EOL
		echo "✅ Created $CONFIG_FILE"
		;;

	*)
		echo "❌ Error: Invalid template name '$TEMPLATE'. Valid options are: sass, less, stylus, postcss, webpack, gulp, grunt, bower."
		usage
		;;
esac

echo "🎉 '$TEMPLATE' config file generated successfully!"


# ./generate-js-css-config-for-compile.sh -t webpack -d ./config
# ./generate-js-css-config-for-compile.sh -t sass
# ./generate-js-css-config-for-compile.sh -h