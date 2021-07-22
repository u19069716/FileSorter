from pathlib import Path, PurePath
from FileSorter.classes import *


def getPurePathsFromDirectory(directory):
    '''
    Get the contents of a directory

    Return: 2 lists of instances of pathlib.PurePath. The first list contains directories, the second list contains non-directory objects.

    Input: the absolute directory for which you'd like to get the contents
    '''

    paths = Path(directory).iterdir()
    directories = []
    nonDirectories = []
    for path in paths:
        if path.is_dir():
            directories.append(PurePath(path))
        else:
            nonDirectories.append(PurePath(path))
    return directories, nonDirectories


def labelPurePathsOnCriteria(paths, labelConfigList):
    '''
    Label the contents of a directory based on specific criteria

    Return: a list of instances of FileSorter.classes.sortedPurePath.

    Input: a list of instances of pathlib.PurePath and a list of instances of FileSorter.classes.sortConfig

    '''

    labelledPurePaths = {}
    unlabelledPurePaths = paths
    for sortConfig in labelConfigList:
        configDirectory = sortConfig.getLabel()
        if not configDirectory in [labelledPurePaths[labelledPurePath].getLabel() for labelledPurePath in labelledPurePaths]:
            labelledPurePaths[configDirectory] = labelledPurePath(
                configDirectory)

        for unsortedPurePath in unlabelledPurePaths:
            if sortConfig.passCriteria(unsortedPurePath):
                labelledPurePaths[configDirectory].addPurePath(
                    unsortedPurePath)
                unlabelledPurePaths.remove(unsortedPurePath)

    return labelledPurePaths


def printFormattedSortedPurePaths(sortedPurePaths):
    '''
    Print the sorted contents of a directory

    Input: A list of instances of FileSorter.classes.sortedPurePath
    '''
    for label in sortedPurePaths:
        print("Label: " + label)
        for purePath in sortedPurePaths[label].getLabelledPurePaths():
            print("\tFile: " + str(purePath))
