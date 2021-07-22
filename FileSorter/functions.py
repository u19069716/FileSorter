from pathlib import Path, PurePath
import configparser
from FileSorter.classes import *


def get_pure_paths_from_directory(directory):
    '''
    Get the contents of a directory

    Return: 2 lists of instances of pathlib.PurePath. The first list contains directories, the second list contains non-directory objects.

    Input: the absolute directory for which you'd like to get the contents
    '''

    paths = Path(directory).iterdir()
    directories = []
    non_directories = []
    for path in paths:
        if path.is_dir():
            directories.append(PurePath(path))
        else:
            non_directories.append(PurePath(path))
    return directories, non_directories


def label_pure_paths_on_criteria(paths, label_config_list):
    '''
    Label the contents of a directory based on specific criteria

    Return: a list of instances of FileSorter.classes.sortedPurePath.

    Input: a list of instances of pathlib.PurePath and a list of instances of FileSorter.classes.sortConfig

    '''

    labelled_pure_paths = {}
    unlabelled_pure_paths = paths
    for sort_config in label_config_list:
        config_label = sort_config.get_label()
        if not config_label in [labelled_pure_paths[labelled_pure_path].get_label() for labelled_pure_path in labelled_pure_paths]:
            labelled_pure_paths[config_label] = LabelledPurePath(
                config_label)
        currently_unlabelled_pure_paths = unlabelled_pure_paths

        for unlabelled_pure_path in unlabelled_pure_paths:
            if sort_config.pass_criteria(unlabelled_pure_path):
                labelled_pure_paths[config_label].add_pure_path(
                    unlabelled_pure_path)
                unlabelled_pure_paths.remove(unlabelled_pure_path)

    return labelled_pure_paths

def print_formatted_labelled_pure_paths(labelled_pure_paths):
    '''
    Print the sorted contents of a directory

    Input: A list of instances of FileSorter.classes.sortedPurePath
    '''
    for label in labelled_pure_paths:
        print("Label: " + label)
        for pure_path in labelled_pure_paths[label].get_labelled_pure_paths():
            print("\tFile: " + str(pure_path))


def get_config(configDirectory):
    '''
    Read the configuration file, get the target directories and the label configurations

    Return: A list of target directories and a list of instances of labelConfig
    '''

    config = configparser.ConfigParser()
    config.optionxform = str  # Retain upper case characters in config file
    config.read(configDirectory)

    target_directories = []
    for target_directory in config['DIRECTORIES']:
        target_directories.append(config['DIRECTORIES'][target_directory])

    label_configs = []
    for label in config['LABELS']:
        label_criteria = []
        label_criteria_strings = config['LABELS'][label].split('&')
        for label_criterion_string in label_criteria_strings:
            label_criterion_instance = eval(label_criterion_string)
            label_criteria.append(label_criterion_instance)
        label_configs.append(LabelConfig(label, label_criteria))

    return target_directories, label_configs
