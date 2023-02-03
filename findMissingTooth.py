import json, os, shutil
from glob import glob

PATH_TO_JSON = 'path to your json label'
PATH_TO_SAVE = 'path to save classified data'

count = 0	# use to count number of data

# read all files
all_files = glob(os.path.join(PATH_TO_JSON, '*.json'))

for current_file in all_files:
    file_name = os.path.basename(current_file).split(".")[0]  # image ID
    label_data = json.load(open(current_file))	
    # if there is less than 2 bbox, there must be a missing tooth
    if (len(label_data["shapes"]) < 2):
        # print(file_name + " miss at least one tooth")
		# save the file with same ID
        save_name = file_name + '.json'	
        save_path = os.path.join(PATH_TO_SAVE, save_name)
        shutil.copy(current_file, save_path)
        count += 1
print("Total file copied: ", count)