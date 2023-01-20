import os
import shutil
import time
seconds=time.time()
path=input("Enter your path: ")
if os.path.exists(path):
  list_of_files=os.walk(path)
  os.path.join(path,list_of_files)
  c_time=os.stat(path).st_ctime
  if c_time>seconds:
    os.remove(path)
else:
  print("path not found")