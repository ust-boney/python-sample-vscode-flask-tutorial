# move files
import os
import shutil
soucepath="orders/"
destinationpath="neworders/"

for filename in os.listdir(soucepath):
 
 if filename.endswith(".json.txt"):
   print(filename)
   print(soucepath+filename," ",destinationpath+filename)
   shutil.move(soucepath+filename,destinationpath+filename)