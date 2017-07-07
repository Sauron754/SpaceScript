import sys

settings = open("settings.txt", "r")
path = settings.readline().replace("path = ", "")
#enter additional settings here
settings.close()

pythonCompatiblePath = path.replace(chr(92), "/")

sys.path.append(pythonCompatiblePath)