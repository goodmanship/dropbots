import config
import dropbox
import json

with open('config.json') as json_data_file:
  config = json.load(json_data_file)

dbx = dropbox.Dropbox(config["api_key"])

for entry in dbx.files_list_folder('').entries:
  print(entry.name)

# dbx.files.DeleteArgs('dev/')