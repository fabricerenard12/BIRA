from dataclasses import dataclass
import cv_viewer.labels as labels
import json
import numpy as np

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


    
        
        