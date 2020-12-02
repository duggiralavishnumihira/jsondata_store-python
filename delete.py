#Enter your code here...
from sys import exit
from argparse import ArgumentParser
import FilePreprocess
import datastore
DEFAULT_DB_PATH = 'db'
DEFAULT_DB_NAME = 'db.json'


parser = ArgumentParser()
parser.add_argument('--datastore', help='Enter the datastore absolute path.')
args = parser.parse_args()

if args.datastore:
    db_path = args.datastore
else:
    db_path = configurations.DEFAULT_DB_PATH


directory_created = FilePreprocess(db_path).create_folder()
if not directory_created:
    print(f"Permission denied: You can not create the directory `{db_path}`.\n")
    exit(0)


key = 'ghi'


_data_found, message = check_delete_data(key, db_path)
print(message)
