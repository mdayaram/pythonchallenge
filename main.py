import os

# Expecting the environment variable CURRENT_CHALLENGE
# to be set to a number corresponding to the file name
# to run.
current_challenge = os.environ['CURRENT_CHALLENGE'].strip()
current_challenge = int(current_challenge)
current_challenge = "{:02d}".format(int(current_challenge))

import importlib
importlib.import_module(current_challenge)