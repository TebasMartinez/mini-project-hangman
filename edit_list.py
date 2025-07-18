"""
Takes a .txt list of words and creates a new file and creates a new .txt list removing all words under 3 letters.
Usage: python edit_list.py <input_file> <output_file>
"""

import sys

def main(old_txt, new_txt):
    oldf = open(old_txt, "r")
    newf = open(new_txt, "x")
    wordlist = oldf.read().split("\n")
    for word in wordlist:
        if len(word) > 3:
            newf.write(f"{word}\n")
    oldf.close()
    newf.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python edit_list.py <input_file> <output_file>")
    else:
        main(sys.argv[1], sys.argv[2])