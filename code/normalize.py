"""
Normalize data downloaded from DatabaseBasketball website.

The data has the following problems:
1. each csv file is a UTF-8 Unicode (with BOM) text, with CRLF line terminators
2. each csv file ends with :
   \n
   (number of rows affected)
   \n
3. inconsistency of abbreviation of teams names.
   (this will be cleaned up by csv2sqlite.py)
4. extra comma in name of universities, like "University of California, Berkeley"
   should be "University of California Berkeley".
5. Player id with extra space which causes SQL JOIN to be failed.
"""

import os
import re
import csv
import sys
import codecs
import subprocess

csv_dir = '../data_upto2009'
BOMLEN = 3

def remove_BOM_CRLF(fname):
    """
    Remove BOM (Byte Order Mark) and CRLF line terminators.
    """
    fp = open(os.path.join(csv_dir, fname), 'rb')
    text = fp.read()
    if text.startswith(codecs.BOM_UTF8):
        text = text[BOMLEN :]
        text = text.replace('\r', '')
        fp.close()
        fp = open(os.path.join(csv_dir, f), 'w')
        fp.write(text)
        fp.close()

def process_lines(fname):
    fp = open(os.path.join(csv_dir, fname), 'rw+')
    lines = fp.readlines()
    # Get rid of the last three lines which are not valid record.
    lines = lines[:-3]

    for i, line in enumerate(lines):
        # Get rid of extra space of player id 'ilkid'. like: MYERSPE01 , ==> MYERSPE01,
        lines[i] = re.sub(r'([a-zA-Z]+[0-2][1-5])\s+,', r'\1,', line)
        # Get rid of extra space of player's name. like: ,Clifford R. , ==> ,Clifford R.,
        lines[i] = re.sub(r'([a-zA-Z]+\s+[a-zA-Z\.]+)\s+,', r'\1,', lines[i])
        # Get rid of extra comma of player's name. like: Conley, Jr., , ==> Conley Jr.,
        lines[i] = re.sub(r'([a-zA-Z]+),(\s{1}Jr\.,)', r'\1\2', lines[i])
        # Get rid of extra space player's name, like: ,Jasikevicius , ==> ,Jasikevicius,
        lines[i] = re.sub(r'(,[a-zA-Z]+)\s+,', r'\1,', lines[i])
               
    # Remove extra comma of the college column.
    if fname == 'players.csv':
        for i, line in enumerate(lines):
            lines[i] = re.sub(r'(,.*University.*),([a-zA-Z ]+,)', r'\1\2', line)

    # rewind to the beginning of file to rewrite the file content.
    fp.seek(0)
    fp.truncate(0)
    for line in lines:
        fp.write(line)

    fp.close()

if __name__ == '__main__':
    subprocess.call('rm '+csv_dir+'/*.csv', shell=True)
    subprocess.call(['unzip', csv_dir+'/databasebasketball_2009_v1.zip', '-d', csv_dir])

    for f in os.listdir(csv_dir):
        if f.endswith('csv'):
            remove_BOM_CRLF(f)
            process_lines(f)
            print 'file', f, 'is done.'

    subprocess.call(['cp', './nba_champs.csv', csv_dir+'/'])
