import os.path
import json

try:
    from pkg_resources import resource_filename
except ImportError:
    def resource_filename(package_or_requirement, resource_name):
        return os.path.join(os.path.dirname(__file__), resource_name)

DATABASE_DIR = resource_filename('pyhobbies', 'database')

with open (os.path.join(DATABASE_DIR, 'database.json')) as list:
    load = json.load(list)
    hobbies = load["hobby"]




    

    



