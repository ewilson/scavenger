# Use this file to prepare a qa.txt file for go.py
# Answers will be hashed with md5
# Expects a plain.txt file with each line in the form:
#
# Why did the Chicken?|my answer here
#
from sys import argv
from hashlib import md5

DELIM = "|"


def main():
    filename = argv[1]

    with open(filename) as infile:
        plain = infile.readlines()

        split = [line.split(DELIM) for line in plain]
        encoded = [DELIM.join([t[0], md5(t[1].lower().strip().encode()).hexdigest()]) for t in split]

        with open('qa.txt', 'w') as out:
            for line in encoded:
                out.write("%s\n" % line)


if __name__ == '__main__':
    main()
