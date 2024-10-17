from dataclasses import dataclass
import cv_viewer.labels as labels
import json
import numpy as np
import ast

@dataclass
class ObjectsOutput:
    nObjects: str
    objects: list


@dataclass
class ObjectOutput:
    label : str
    #height: list # [x, y, z]
    #weight: list # [x, y, z]
    position: list# [x, y, z]
    dimensions: list # [width, height, length]


def write_json(obj_output) : 
    with open("data.txt", "a")  as f : 
        #json.dump(obj_output.__dict__, f)
        f.write(str(obj_output.__dict__))
        f.write('\n')
        f.close()

def retrieve_data(objects) : 
    #if len(objects.object_list) == 0 : return
    objects_out = []
    for obj in objects:    
        if len(obj.bounding_box) == 0 : pass  
        if np.isnan(obj.position).any(): pass
     
        #height = list(obj.bounding_box[0] - obj.bounding_box[4])
        #weight = list(obj.bounding_box[3] - obj.bounding_box[0])
        position = list(obj.position)
        label = labels.labelDict[int(obj.raw_label)] 
        dimensions = list(obj.dimensions)
        
        obj_output = ObjectOutput(label=label, position=position, dimensions=dimensions) 
        objects_out.append(obj_output)  
    
    objs_output = ObjectsOutput(nObjects=len(objects), objects=objects_out) 
    write_json(objs_output)  


def get_z_values():
    # Liste pour stocker les valeurs z
    z_values = []
    
    # Ouvre le fichier en mode lecture
    with open("data.txt", "r") as f: 
        for line in f:
            line = line.replace("ObjectOutput(", "{").replace(")", "}")
            line = line.replace("label=", "'label':").replace("position=", "'position':").replace("dimensions=", "'dimensions':")

            # Convertit la ligne en dictionnaire
            data = ast.literal_eval(line.strip())
            
            # Vérifie si le nombre d'objets est supérieur à 0
            if data['nObjects'] > 0:
                # Récupère les objets
                objects = data['objects']
                for obj in objects:
                    # Récupère la position et le z
                    position = obj['position']
                    z = position[2]  # La valeur z est le troisième élément
                    z_values.append(z)
    return z_values
        
def get_distance():
    z_values = get_z_values()
    first_average = sum(z_values) / len(z_values)
    true_z_values = []
    print(first_average / 2) 
    print(first_average * 2)
    for val in z_values:

        if (val < first_average / 2) and (val > first_average * 2):

            true_z_values.append(val)
        
    true_average = sum(true_z_values) / len(true_z_values)
    print(f"Moyenne des valeurs z: {true_average}")
    return true_average

        