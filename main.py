###########
# Imports #
###########

from FileSorter.functions import *
from FileSorter.classes import *

#################
# Configuration #
#################

directories = ['/home/alexwhuman/Downloads/']
labellingConfiguration = [
    labelConfig('Text Files', [matchesFileExtensions(['.txt'])]),
    labelConfig('Unsorted', [labelCriterion()])
]

################
# Main Program #
################

for directory in directories:
    directoryPurePaths, nonDirectoryPurePaths = getPurePathsFromDirectory(
        directory)
    labelledPurePaths = labelPurePathsOnCriteria(
        nonDirectoryPurePaths, labellingConfiguration)
    printFormattedSortedPurePaths(labelledPurePaths)
