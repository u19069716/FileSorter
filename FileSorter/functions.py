from pathlib import Path, PurePath
import configparser
import os
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


def get_config(config_directory):
    '''
    Read the configuration file, get the target directories and the label configurations

    Return: A list of target directories and a list of instances of labelConfig
    '''
    if does_file_exist(config_directory):
        config = configparser.ConfigParser()
        config.optionxform = str  # Retain upper case characters in config file
        config.read(config_directory)

        try:
            target_directories = []
            for target_directory in config['TARGET DIRECTORIES']:
                if does_file_exist(
                        config['TARGET DIRECTORIES'][target_directory], PurePath(config['TARGET DIRECTORIES'][target_directory]).parent):
                    target_directories.append(
                        config['TARGET DIRECTORIES'][target_directory])
                else:
                    # TODO: Log an error here
                    print("ERROR: Cannot find \'{}\' target directory".format(
                        target_directory))  # debug
                    print("TERMINATING")  # debug
                    os.sys.exit()

        except KeyError:
            # TODO: Log an error here
            print("ERROR: Can't find \'DIRECTORIES\' section in config.ini")  # debug
            print("TERMINATING")  # debug
            os.sys.exit()

        try:
            label_configs = []
            for label in config['LABELS']:
                label_criteria = []
                label_criteria_strings = config['LABELS'][label].split('&')
                try:
                    for label_criterion_string in label_criteria_strings:
                        label_criterion_instance = eval(label_criterion_string)
                        label_criteria.append(label_criterion_instance)
                    label_configs.append(LabelConfig(label, label_criteria))
                except SyntaxError:
                    # TODO: Log an error here
                    print("ERROR: Incorrect Syntax in \'LABELS\' section")  # debug
                    print("TERMINATING")  # debug
                    os.sys.exit()
            return target_directories, label_configs
        except KeyError:
            # TODO: Log an error here
            print("ERROR: Can't find \'LABELS\' section in config.ini")  # debug
            print("TERMINATING")  # debug
            os.sys.exit()
    else:
        # TODO: Log an error here
        print("ERROR: Can't find config file")  # debug
        print("TERMINATING")  # debug
        os.sys.exit()


def does_file_exist(file_path, search_path='.'):
    '''
    Check whether or not a file exists

    Input: An instance of pathlib.PurePath & an optional search directory 

    Return: True or False
    '''
    pure_file_path = PurePath(file_path)
    directory_paths, non_directory_paths = get_pure_paths_from_directory(
        search_path)
    if pure_file_path in [pure_path for pure_path in non_directory_paths + directory_paths]:
        return True
    return False
