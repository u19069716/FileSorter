###########
# Imports #
###########

from FileSorter.functions import *

#################
# Configuration #
#################

directories = ['/home/alexwhuman/Downloads/']

################
# Main Program #
################

for directory in directories:
    print("Directory: " + directory)
    for content in getFormattedDirectoryContents(directory):
        print('\t' + content)
