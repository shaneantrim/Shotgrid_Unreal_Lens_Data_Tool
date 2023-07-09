# This Python tool fetches lens data from Shotgrid using the API and exports it directly into Unreal Engine.

import shotgun_api3

SERVER_PATH = 'https://shaneantrim.shotgrid.autodesk.com'
SCRIPT_NAME = 'unreal_lens_data_tool'
SCRIPT_KEY = 'ahrtdp&hxvdbKgheha9sssufc'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

fields = ['id', 'equipment_name', 'sub_type', 'type']
project_id = 5093
page_id = 5785
filters = [
    ['project', 'is', {'type': 'Project', 'id': project_id}],
    ['page', 'is', {'type': 'Page', 'id': page_id}]
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