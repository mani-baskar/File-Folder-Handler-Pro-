import os
import csv
import zipfile
import tkinter as tk
from tkinter import filedialog

class FileToolkit:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def select_folder(self, title="Select Folder"):
        folder = filedialog.askdirectory(title=title)
        return folder
    # Functionality 1: List all files recursively and save info to CSV
    def list_files_to_csv(self, folder_path, output_csv=None):
        if not folder_path:
            print("No folder selected.")
            return

        file_info = []
        for root_dir, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root_dir, file)
                file_info.append([full_path, file])

        if not output_csv:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            folder_name = os.path.basename(folder_path.rstrip(r"\\/"))
            output_csv = os.path.join(script_dir, f"{folder_name}_file_list.csv")

        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["full_path", "file_name"])
            writer.writerows(file_info)

        print(f"CSV saved to: {output_csv}")
    # Functionality 2: List ZIP content info without extraction, save to CSV
    def list_zip_contents_to_csv(self, folder_path, output_csv=None):
        if not folder_path:
            print("No folder selected.")
            return

        zip_contents = []
        for root_dir, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('.zip'):
                    zip_path = os.path.join(root_dir, file)
                    try:
                        with zipfile.ZipFile(zip_path, 'r') as z:
                            for zip_info in z.infolist():
                                zip_contents.append([
                                    zip_path,
                                    zip_info.filename,
                                    zip_info.file_size
                                ])
                    except zipfile.BadZipFile:
                        print(f"Warning: Bad ZIP file skipped: {zip_path}")

        if not output_csv:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            folder_name = os.path.basename(folder_path.rstrip(r"\\/"))
            output_csv = os.path.join(script_dir, f"{folder_name}_zip_contents.csv")

        with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['zip_file_path', 'file_inside_zip', 'file_size_bytes'])
            writer.writerows(zip_contents)

        print(f"ZIP contents info CSV saved to: {output_csv}")
    # Functionality 3: Extract all ZIP files in folder and subfolders into their own folders
    def extract_all_zips(self, folder_path):
        if not folder_path:
            print("No folder selected.")
            return

        for dirpath, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('.zip'):
                    zip_path = os.path.join(dirpath, file)
                    try:
                        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                            zip_ref.extractall(dirpath)
                        print(f"Extracted '{zip_path}' in folder '{dirpath}'")
                    except zipfile.BadZipFile:
                        print(f"Bad ZIP file skipped: {zip_path}")
    # Example to run all or specific functionality via UI menus (optional)
    def run(self):
        print("Select operation:")
        print("1. List all files to CSV")
        print("2. List ZIP contents to CSV")
        print("3. Extract all ZIPs in folder")
        choice = input("Enter choice (1/2/3): ").strip()

        folder = self.select_folder("Select the target folder")
        if not folder:
            print("No folder selected. Exiting.")
            return

        if choice == '1':
            self.list_files_to_csv(folder)
        elif choice == '2':
            self.list_zip_contents_to_csv(folder)
        elif choice == '3':
            self.extract_all_zips(folder)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    toolkit = FileToolkit()
    toolkit.run()
