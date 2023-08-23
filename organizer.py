import os
import shutil

def organize_files(source_folder):
    files = os.listdir(source_folder)

    file_categories = {
        "Images": ["jpg", "jpeg", "png", "gif", "bmp"],
        "Documents": ["pdf", "doc", "docx", "txt", "csv", "xlsx", "pptx", "zip", "rar"],
        "Videos": ["mp4", "avi", "mkv", "mov", "wmv"],
        "Audio": ["mp3", "wav", "ogg"],
        "Programming": ["py", "java", "cpp", "c", "html", "css", "js"],
        "Applications": ["exe","app","msi"],
    }

    for file in files:
        if os.path.isfile(os.path.join(source_folder, file)):
            extension = os.path.splitext(file)[1][1:].lower()
            for category, extensions in file_categories.items():
                if extension in extensions:
                    folder_path = os.path.join(source_folder, category)
                    os.makedirs(folder_path, exist_ok=True)
                    source_path = os.path.join(source_folder, file)
                    destination_path = os.path.join(folder_path, file)
                    shutil.move(source_path, destination_path)
                    break

def main():
    print("Welcome to File Organizer!")
    source_folder = input("Enter the path of the folder you want to organize: ")
    if not os.path.isdir(source_folder):
        print("Invalid folder path. Please try again.")
        return

    organize_files(source_folder)
    print("Files have been organized successfully!")

if __name__ == "__main__":
    main()

