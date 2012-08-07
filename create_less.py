#!/usr/bin/env python
import sys

def process_file():
    
    f = open('lib/mixer.css', 'r')
    output = open('gwui.less', 'w')
    output.write('.gwui {\n')
    for line in f:
    	output.write(line)
    output.write('\n}')
    f.close()
    output.close()

def main():
	process_file()

if __name__ == '__main__':
    sys.exit(main())