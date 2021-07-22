class labelConfig():
    '''
    Used to check whether a non-directory path matches a set of criteria 
    '''

    def __init__(self, label, sortCriteria):
        '''
        Constructor

        Input: a string label to identify this configuration and a list of instances of FileSorter.classes.sortCriterion 
        '''

        self.label = label
        self.sortCriteria = sortCriteria

    def getLabel(self):
        return self.label

    def passCriteria(self, pureFilePath):
        '''
        Determines whether a given pure path matches the criteria stored within the class

        Input: instance of pathlib.PurePath

        Return: True or False
        '''
        for criterion in self.sortCriteria:
            if criterion.passCriterion(pureFilePath):
                return True

        return False


class labelledPurePath():
    '''
    Used to attach a label to list of instances of pathlib.PurePath
    '''

    def __init__(self, label):
        '''
        Constructor

        Input: The label attached to this list of instances of pathlib.PurePath
        '''
        self.label = label
        self.purePaths = []

    def addPurePath(self, purePath):
        '''
        Add another instance of pathlib.PurePath to the list within this class

        Input: An instance of pathlib.PurePath
        '''
        self.purePaths.append(purePath)

    def getLabel(self):
        return self.label

    def getLabelledPurePaths(self):
        return self.purePaths


class labelCriterion():
    '''
    Parent class for all criteria a given filepath can match
    '''

    def passCriterion(self, PureFilePath):
        '''
        Will be redefined by child classes, currently just returns True 
        (used for the "unsorted" label)
        '''
        return True


class matchesFileExtensions(labelCriterion):
    '''
    Used to check if a filepath matches a specific list of file extensions
    '''

    def __init__(self, fileExtensions):
        '''
        Constructor

        Input: A list of strings, containing the file extensions a provided file must match against
        '''
        self.fileExtensions = fileExtensions

    def passCriterion(self, PureFilePath):
        '''
        Check if the provided filepath's suffix matches the list of stores file extensions

        Input: An instance of pathlib.PurePath

        Return: True or False
        '''
        if PureFilePath.suffix in self.fileExtensions:
            return True
        return False
