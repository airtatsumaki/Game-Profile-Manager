from distutils.dir_util import copy_tree
import os

# copy subdirectory example
fromDirectory = r"C:\Users\user\AppData\Local\SessionGame\Saved\SaveGames"
toDirectory = "backupFolder"

fullPath = r"resources\games\\" + toDirectory

if not os.path.exists(r"resources\games\\" + toDirectory):
    os.makedirs(r"resources\games\\" + toDirectory)

copy_tree(fromDirectory, r"resources\games\\" + toDirectory)