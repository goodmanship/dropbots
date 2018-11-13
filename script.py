import config
import dropbox
import json

with open('config.json') as json_data_file:
  config = json.load(json_data_file)

dbx = dropbox.Dropbox(config["api_key"])
print dbx.users_get_current_account()