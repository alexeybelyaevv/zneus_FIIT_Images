#translates the directory names in the images archive
#move this file to archive where translate file is!!!
import translate
import os
basedir = 'C:/<your_path_to_archive>/archive/raw-img'
for fn in os.listdir(basedir):
    if not os.path.isdir(os.path.join(basedir, fn)):
        continue # Not a directory
    if fn not in translate.translate: 
        continue
    print(translate.translate[fn])
    os.rename(os.path.join(basedir,fn), os.path.join(basedir, translate.translate[fn]))