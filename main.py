###########
# Imports #
###########

from FileSorter.functions import *
from FileSorter.classes import *

#################
# Configuration #
#################

directories = ['/home/alexwhuman/Downloads/']
sortingConfiguration = [
    sortConfig('/home/alexwhuman/Downloads/textFiles',
               [matchesFileExtensions(['.txt'])]),
    sortConfig('/home/alexwhuman/Downloads/Unsorted', [sortCriterion()])
]

################
# Main Program #
################

for directory in directories:
    directoryPurePaths, nonDirectoryPurePaths = getPurePathsFromDirectory(
        directory)
    sortedPurePaths = sortPurePathsOnCriteria(
        nonDirectoryPurePaths, sortingConfiguration)
    printFormattedSortedPurePaths(sortedPurePaths)
