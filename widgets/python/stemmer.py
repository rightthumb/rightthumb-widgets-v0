#!/usr/bin/python3.11
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import sys

try:
    from nltk.stem import PorterStemmer  # type: ignore
    stemmer = PorterStemmer()
except ImportError:
    stemmer = None

def get_stems(text):
    if stemmer is None:
        return text
    words = text.split()
    stems = [stemmer.stem(word) for word in words]
    return " ".join(stems)

def main():
    if '-s' not in sys.argv:
        print("""
Word Stemmer
------------
Usage:
    ./stems.py -s your text here

Example:
    ./stems.py -s running jumped swimming

Description:
    -s    Stem the words provided after -s
""")
        sys.exit(1)
    
    index = sys.argv.index('-s') + 1
    if index >= len(sys.argv):
        print("❌ No words provided after -s.")
        sys.exit(1)
    
    text = " ".join(sys.argv[index:])
    result = get_stems(text)
    print(result)

if __name__ == "__main__":
    main()
