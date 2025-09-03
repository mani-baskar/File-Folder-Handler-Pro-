import os
import csv

def get_all_files(folder_path):
    file_info = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_info.append([full_path, file])
    return file_info

folder_path = r"G:\.shortcut-targets-by-id\1VU40ZbsGt1Ev2FrwZZPLeZ8qqQo4wyhq\client Manikandan Wedding Photos and videos"
files_list = get_all_files(folder_path)

# Define output CSV path (change this as needed)
output_csv = r"G:\client_Manikandan_Wedding_Photos_and_videos_file_list.csv"
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["full_path", "file_name"])
    writer.writerows(files_list)

print("CSV saved to:", output_csv)
