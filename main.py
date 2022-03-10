import os
import importlib

# Expecting the environment variable CURRENT_CHALLENGE
# to be set to a number corresponding to the file name
# to run.
current_challenge = os.getenv('CURRENT_CHALLENGE')
try:
  current_challenge = int(current_challenge.strip())
  current_challenge = "{:02d}".format(int(current_challenge))
  importlib.import_module(current_challenge)
except:
  print("Env variable CURRENT_CHALLENGE was incorrectly set to " + str(current_challenge))
  print("So defaulting to running 00.py")
  print()
  importlib.import_module("00")