class sortConfig():
    def __init__(self, targetDirectory, sortCriteria):
        self.targetDirectory = targetDirectory
        self.sortCriteria = sortCriteria

    def getTargetDirectory(self):
        return self.targetDirectory

    def passCriteria(self, pureFilePath):
        for criterion in self.sortCriteria:
            if criterion.passCriterion(pureFilePath):
                return True

        return False


class sortedPurePath():
    def __init__(self, targetDirectory):
        self.targetDirectory = targetDirectory
        self.purePaths = []

    def addPurePath(self, purePath):
        self.purePaths.append(purePath)

    def getTargetDirectory(self):
        return self.targetDirectory

    def getSortedPurePaths(self):
        return self.purePaths


class sortCriterion():
    def passCriterion(self, PureFilePath):
        return True


class matchesFileExtensions(sortCriterion):
    def __init__(self, fileExtensions):
        self.fileExtensions = fileExtensions

    def passCriterion(self, PureFilePath):
        if PureFilePath.suffix in self.fileExtensions:
            return True
        return False
