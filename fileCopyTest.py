from distutils.dir_util import copy_tree
import os

# copy subdirectory example
fromDirectory = "C:\\Users\\user\\AppData\\Local\\SessionGame\\Saved\\SaveGames"
toDirectory = "backupFolder"

fullPath = "resources\\games\\" + toDirectory

if not os.path.exists("resources\\games\\" + toDirectory):
    os.makedirs("resources\\games\\" + toDirectory)

copy_tree(fromDirectory, "resources\\games\\" + toDirectory)