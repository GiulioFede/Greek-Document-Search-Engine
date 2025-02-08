import os
import numpy as np

# Path della directory TLG
path = '/home/giuliofederico/dataset/tlg'  
#dove salvare la lista npy
path_to_save_list = '/home/giuliofederico/Itserr/name_of_the_tlg_works.npy'

folders = []

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    if os.path.isdir(full_path):
        folders.append(item)


folders_array = np.array(folders)

# Salva l'array in un file .npy
np.save(path_to_save_list, folders_array)
