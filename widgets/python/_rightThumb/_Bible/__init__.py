import _rightThumb._construct as __
import _rightThumb._base3 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._Bible as _B
# from _rightThumb._Bible import _build_indexes

query = []
Bible = {}
Books = {}

files = {
			'query': {
				'single': 'single.index',
				'double': 'double.index',
			},
			'app': {
				'book_labels': 'Bible_books_labels.index',
				'books': 'Bible_books.index',
				'Bible': 'Bible_av.index',
			},
}

def load():
	global Bible
	global Books
	global labels
	global files
	# global Verses

	labels = _.getTableProject( 'Bible.app', files['app']['book_labels'] )
	Books = _.getTableProject( 'Bible.app', files['app']['books'] )

	Bible = _.getTableProject( 'Bible.app', files['app']['Bible'] )


	# _build_indexes.build()
	# Verses = _.getTableDB( 'Bible_Verses.index' )

