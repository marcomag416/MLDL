from abc import ABCMeta
from dataclasses import dataclass
from typing import Tuple


class BaseGTALabels(metaclass=ABCMeta):
    pass


@dataclass
class GTA5Label:
    ID: int
    color: Tuple[int, int, int]


class GTA5Labels_TaskCV2017(BaseGTALabels):
    road = GTA5Label(ID=0, color=(128, 64, 128))
    sidewalk = GTA5Label(ID=1, color=(244, 35, 232))
    building = GTA5Label(ID=2, color=(70, 70, 70))
    wall = GTA5Label(ID=3, color=(102, 102, 156))
    fence = GTA5Label(ID=4, color=(190, 153, 153))
    pole = GTA5Label(ID=5, color=(153, 153, 153))
    light = GTA5Label(ID=6, color=(250, 170, 30))
    sign = GTA5Label(ID=7, color=(220, 220, 0))
    vegetation = GTA5Label(ID=8, color=(107, 142, 35))
    terrain = GTA5Label(ID=9, color=(152, 251, 152))
    sky = GTA5Label(ID=10, color=(70, 130, 180))
    person = GTA5Label(ID=11, color=(220, 20, 60))
    rider = GTA5Label(ID=12, color=(255, 0, 0))
    car = GTA5Label(ID=13, color=(0, 0, 142))
    truck = GTA5Label(ID=14, color=(0, 0, 70))
    bus = GTA5Label(ID=15, color=(0, 60, 100))
    train = GTA5Label(ID=16, color=(0, 80, 100))
    motocycle = GTA5Label(ID=17, color=(0, 0, 230))
    bicycle = GTA5Label(ID=18, color=(119, 11, 32))
    unlabeled = GTA5Label(ID=255, color=(0, 0, 0))
                       
    list_ = [
        road,
        sidewalk,
        building,
        wall,
        fence,
        pole,
        light,
        sign,
        vegetation,
        terrain,
        sky,
        person,
        rider,
        car,
        truck,
        bus,
        train,
        motocycle,
        bicycle,
        unlabeled,
    ]

    @property
    def support_id_list(self):
        ret = [label.ID for label in self.list_]
        return ret


"""
import os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Define paths
images_path = 'GTA5/GTA5/images'
labels_path = 'GTA5/GTA5/labels'

# Initialize lists to hold data
data = []

# Load images and corresponding masks
for image_filename in os.listdir(images_path):
    if image_filename.endswith('.png'):
        image_path = os.path.join(images_path, image_filename)
        mask_path = os.path.join(labels_path, image_filename)
        
        # Check if corresponding mask file exists
        if os.path.exists(mask_path):
            # Open image and mask to ensure they can be loaded (optional, for validation)
            try:
                image = Image.open(image_path)
                mask = Image.open(mask_path)
                
                # Add data to list
                data.append({
                    'image_path': image_path,
                    'mask_path': mask_path
                })
            except Exception as e:
                print(f"Error loading {image_path} or {mask_path}: {e}")

# Create a DataFrame from the data list
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('gta5_segmentation_dataset.csv', index=False)

print("Semantic segmentation dataset created and saved as 'gta5_segmentation_dataset.csv'")
------------------------------------------------------------------
def _map_mask(self, mask):
        new_mask = np.zeros_like(mask)
        for color, label_id in self.label_mapping.items():
            color_mask = np.all(mask == color, axis=-1)
            new_mask[color_mask] = color  # Keep original color
        return new_mask
"""