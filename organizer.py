import os
import shutil
folder_path = "test_folder"
files = os.listdir(folder_path)
for file in files:
    if file.endswith(".jpg"):
        image_folder = folder_path + "/Images"
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        source = folder_path + "/" + file
        destination = image_folder + "/" + file
        shutil.move(source, destination)
        print(file + " moved to Images folder")
