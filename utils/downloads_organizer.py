'''
This script is to organizes the download files in the Downloads folder by their extensions.
Every run of the script will create a folder for each category with the current date and the name of the category.
After that, the program will move the files to the corresponding folder.
'''

import os
import shutil
import time
import datetime

class DownloadsFolderOrganizer:
    def __init__(self):
        
        self.downloads_folder = os.path.expanduser("~") + "/Downloads"
        
        self.extensions = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv"],
            "Audios": [".mp3", ".wav", ".ogg"],
            "Documents": [".doc", ".docx", ".pdf", ".txt", ".csv", ".xls", ".xlsx", ".ppt", ".pptx"],
            "Executables": [".exe", ".msi"],
            "Compressed": [".zip", ".rar", ".tar", ".gz", ".7z"],
            "Fonts": [".ttf", ".otf"],
            "Code": [".py", ".java", ".c", ".cpp", ".js", ".css", ".html", ".json"]
        }

    def create_category_folders(self):
        for category, extensions in self.extensions.items():
            category_folder = os.path.join(self.downloads_folder, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

    
    def create_date_folders(self):
        categories = tuple(self.extensions.keys())
        # print(categories)
        for category in categories:
            date_folder = os.path.join(self.downloads_folder, category, datetime.datetime.now().strftime(f"{category} %Y-%m-%d_%H-%M-%S"))
            if not os.path.exists(date_folder):
                os.makedirs(date_folder)
        return date_folder
        
    def move_files_to_date_folders(self, date_folder):
        for category, extensions in self.extensions.items():
            downloads_folder = os.path.join(self.downloads_folder)
            for file in os.listdir(downloads_folder):
                file_path = os.path.join(downloads_folder, file)
                if os.path.isfile(file_path) and file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, date_folder)
        print("Files moved to date folders successfully.")

    def move_date_folders_to_category_folders(self):
        for category, extensions in self.extensions.items():
            category_folder = os.path.join(self.downloads_folder, category)
            for date_folder in os.listdir(category_folder):
                date_folder_path = os.path.join(category_folder, date_folder)
                if os.path.isdir(date_folder_path):
                    for file in os.listdir(date_folder_path):
                        file_path = os.path.join(date_folder_path, file)
                        if os.path.isfile(file_path):
                            shutil.move(file_path, category_folder)
        print("Date folders moved to category folders successfully.")

    def run(self):
        self.create_category_folders()
        date_folder = self.create_date_folders()
        self.move_files_to_date_folders(date_folder)
        self.move_date_folders_to_category_folders()
        print("Files moved to date folders successfully.")


if __name__ == "__main__":
    download_organizer = DownloadsFolderOrganizer()
    download_organizer.run()
