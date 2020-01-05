import os

root = "pa/units"

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file[-13:] == "_diffuse.papa":
            print(os.path.join(subdir, file))
        elif file[-10:] == "_mask.papa":
            print(os.path.join(subdir, file))
        elif file[-14:] == "_material.papa":
            print(os.path.join(subdir, file))
        else:
            os.remove(os.path.join(subdir, file))