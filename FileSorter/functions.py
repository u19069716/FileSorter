from pathlib import Path, PurePath


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


def getFormattedDirectoryContents(directory):
    pureDirectoryPaths, pureNonDirectoryPaths = getPurePaths(
        getPathsInDirectory(directory))
    return [(str(path.name) + " [directory]") for path in pureDirectoryPaths] + [str(path.name) for path in pureNonDirectoryPaths]
