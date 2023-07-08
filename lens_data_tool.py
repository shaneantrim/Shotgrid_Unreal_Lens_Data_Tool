# This Python tool fetches lens data from Shotgrid using the API and exports it directly into Unreal Engine.

import shotgun_api3

# Connect to Shotgrid
SERVER_PATH = 'https://shaneantrim.shotgrid.autodesk.com'
SCRIPT_NAME = 'unreal_lens_data_tool'
SCRIPT_KEY = 'ahrtdp&hxvdbKgheha9sssufc'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

# Have the user enter the shot ID
print([symbol for symbol in sorted(dir(sg)) if not symbol.startswith('_')])




shot_id = unreal.EditorUtilityLibrary().InputBox(
    "Enter the shot ID",
    "Please enter the ID of the shot you want to query",
    "",
)

# The filters for the query
ENTITY_FILTERS = [
    ['id', 'is', int(shot_id)],
]

# Query Shotgrid for the lens data
shot_data = sg.find_one('Shot', filters=ENTITY_FILTERS, fields=['code', 'sg_lens_data'])

# Retrieve the lens data
if shot_data:
    lens_data = shot_data.get('sg_lens_data')
    print(f"Lens data for Shot ID {shot_id}: {lens_data}")
else:
    print(f"No shot found with ID {shot_id}")

print r.json()