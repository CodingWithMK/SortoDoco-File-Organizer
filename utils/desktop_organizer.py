"""

"""

import os
import shutil

class DesktopOrganizer:
    def __init__(self):
        self.desktop_folder = os.path.expanduser("~\\Desktop")

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

    