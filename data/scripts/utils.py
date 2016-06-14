import os
from fnmatch import fnmatch

def listfiles(root, pattern):
  for path, subdir, files in os.walk(root):
    if path == root:
    #if path == './':
      for name in files:
        if fnmatch(name, pattern):
          yield os.path.join(path, name)

