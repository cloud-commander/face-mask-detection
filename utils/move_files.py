import os
import shutil

def strip_extension(list):
     striped = [os.path.splitext(x)[0] for x in list]
     return striped
     
def compare_intersect(DIR1, DIR2):
    x = strip_extension(os.listdir(DIR1))
    y = strip_extension(os.listdir(DIR2))
    return list(frozenset(x).intersection(y))

def move_files(source_dir,destination_dir,allowed_list):
    counter = 0
    files = os.listdir(source_dir)
    for f in files:
      if f.endswith(('.png', '.jpg', '.jpeg', '.xml')):
        for item in allowed_list:
          if os.path.splitext(f)[0] == item:
            shutil.move(source_dir+"/"+f, destination_dir+"/")
            counter += 1 
    print(f"Files moved: {counter}")
