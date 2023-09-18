import json
import sys

with open('data.csv', 'a') as csv:
    csv.write('emdb_id,url,resolution,title,fitted_model,molecular_weight,spacing_x,spacing_y,spacing_z,voxel_x,voxel_y,voxel_z\n')
f = open('all.json')

all_json = json.load(f)

for data in all_json:
    emdb_id = data["emdb_id"]
    url = "https://www.ebi.ac.uk/emdb/" + emdb_id
    resolution = data["structure_determination_list"]["structure_determination"][0]["image_processing"][0]["final_reconstruction"]["resolution"]["valueOf_"]
    title = data["admin"]["title"]
    title = title.replace(","," ")
    try:
        fitted_model = data["crossreferences"]["pdb_list"]["pdb_reference"][0]["pdb_id"]
    except:
        fitted_model = ""

    total = 0.00
    weight_error = False
    try:
        for protein in data["sample"]["macromolecule_list"]["macromolecule"]:
            try:
                if (protein["molecular_weight"]["theoretical"]["units"] != "MDa"):
                    sys.exit("{} was not in MDa".format(emdb_id))
            except:
                weight_error = True
                continue
            total += float(protein["molecular_weight"]["theoretical"]["valueOf_"]) * float(protein["number_of_copies"])
    except:
        weight_error = True
        
    if weight_error:
        total = ""
    spacing_x = data["map"]["spacing"]["x"]
    spacing_y = data["map"]["spacing"]["y"]
    spacing_z = data["map"]["spacing"]["z"]

    voxel_x = data["map"]["pixel_spacing"]["x"]["valueOf_"]
    voxel_y = data["map"]["pixel_spacing"]["y"]["valueOf_"]
    voxel_z = data["map"]["pixel_spacing"]["z"]["valueOf_"]

    with open('data.csv', 'a') as csv:
        csv.write("{},{},{},{},{},{},{},{},{},{},{},{},\n".format(emdb_id,url,resolution,title,fitted_model,total,spacing_x,spacing_y,spacing_z,voxel_x,voxel_y,voxel_z))
