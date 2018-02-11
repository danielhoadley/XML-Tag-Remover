from bs4 import BeautifulSoup
import os
import io
import re

rootdir = '/Users/danielhoadley/PycharmProjects/trainer/!labelled_data_reportXML/'

# Open each XML file

for dirName, subdirList, fileList in os.walk(rootdir):
    for fname in fileList:
        if fname.endswith(".XML"):
            os.chdir(dirName)
            os.remove(fname)
            print('Deleting ' + '\t%s' % fname, dirName)