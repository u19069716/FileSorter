#####################
# Imports & Logging #
#####################

from FileSorter.functions import *
from FileSorter.classes import *
import logging
logger = logging.getLogger(__name__)
setup_logging()

logger.info('Main Program Starting')


#################
# Configuration #
#################


directories, label_configuration = get_config('./config.ini')
logger.info('Configuration successfully loaded')


################
# Main Program #
################

for directory in directories:

    directory_pure_paths, non_directory_pure_paths = get_pure_paths_from_directory(
        directory)

    labelled_pure_paths = label_pure_paths_on_criteria(
        non_directory_pure_paths, label_configuration)

    print_formatted_labelled_pure_paths(labelled_pure_paths)
