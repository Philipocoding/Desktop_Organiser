import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Desktop")

extensions = {
    ".jpg": "Photos",
    ".html": "Other",
    ".exe": "Photos",
    ".jpeg": "Photos",
    ".iso": "Other",
    ".png": "Photos",
    ".gif": "Photos",
    ".pdf": "Docs",
    ".txt": "Docs",
    ".doc": "Docs",
    ".zip": "Docs",
    ".docx": "Docs"
}

for filename in os.listdir(directory): # iterates iver all files/directries returned from listdir( ) method
    file_Path = os.path.join(directory, filename) # assigns a filepath

    if(os.path.isfile(file_Path)):
        extension = os.path.splitext(filename)[1].lower() #  splits the filename into (name, ext)

        if extension in extensions: #  if the extension is a key in the extensions dictionary
            folderName = extensions[extension] # Gets value from location in dictionary 
            folderPath = os.path.join(directory, folderName)
            os.makedirs(folderPath, exist_ok=True) # creates dir

            destinationPath = os.path.join(folderPath, filename)
            shutil.move(file_Path, destinationPath)
            print("Moved " + filename + " to " + file_Path)

print('Complete')

    
