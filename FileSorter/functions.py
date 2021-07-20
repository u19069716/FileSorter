from pathlib import Path, PurePath
from FileSorter.classes import *


def getPathsInDirectory(directory):
    entries = Path(directory)
    return entries.iterdir()


def getPurePaths(paths):
    directories = []
    nonDirectories = []
    for path in paths:
        if path.is_dir():
            directories.append(PurePath(path))
        else:
            nonDirectories.append(PurePath(path))
    return directories, nonDirectories


def getPurePathsFromDirectory(directory):
    return getPurePaths(getPathsInDirectory(directory))


def getFormattedDirectoryContents(directory):
    pureDirectoryPaths, pureNonDirectoryPaths = getPurePaths(
        getPathsInDirectory(directory))
    return [(str(path.name) + " [directory]") for path in pureDirectoryPaths] + [str(path.name) for path in pureNonDirectoryPaths]


def sortPurePathsOnCriteria(paths, sortConfigList):
    sortedPurePaths = {}
    unsortedPurePaths = paths
    for sortConfig in sortConfigList:
        configDirectory = sortConfig.getTargetDirectory()
        if not configDirectory in [sortedPurePaths[sortedPurePath].getTargetDirectory() for sortedPurePath in sortedPurePaths]:
            sortedPurePaths[configDirectory] = sortedPurePath(configDirectory)

        for unsortedPurePath in unsortedPurePaths:
            if sortConfig.passCriteria(unsortedPurePath):
                sortedPurePaths[configDirectory].addPurePath(
                    unsortedPurePath)
                unsortedPurePaths.remove(unsortedPurePath)

    return sortedPurePaths


def printFormattedSortedPurePaths(sortedPurePaths):
    for targetDirectory in sortedPurePaths:
        print("Directory: " + targetDirectory)
        for purePath in sortedPurePaths[targetDirectory].getSortedPurePaths():
            print("\tFile: " + str(purePath))
