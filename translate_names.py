#translates the directory names in the images archive
translate = {"cane": "dog", "cavallo": "horse", "elefante": "elephant", "farfalla": "butterfly", "gallina": "chicken", "gatto": "cat", "mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel", "ragno": "spider"}
import os
working_dir = os.getcwd()
print(working_dir)
basedir = os.path.join(working_dir, "archive/raw-img")
#or if the basedir doesnt work use this >
#basedir = "<path_to_archive>/archive/raw-img"
print(basedir)
for fn in os.listdir(basedir):
    if not os.path.isdir(os.path.join(basedir, fn)):
        continue # Not a directory
    if fn not in translate: 
        continue
    print(translate[fn])
    os.rename(os.path.join(basedir,fn), os.path.join(basedir, translate[fn]))