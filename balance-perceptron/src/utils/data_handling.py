import csv
import numpy as np

def open_sample(sample_file: str):
    sample = [] 
    with open(sample_file, 'r') as f:
        reader = csv.reader(f)
        sample = [row for row in reader]
    return sample
        
def write_sample(data, sample_file: str):
    with open(sample_file, 'w') as f:
        writer = csv.writer(f)
        for value in data:
            writer.writerow(data)

def balance_data_handling(sample_file: str):
    chars = {
        'L': [1,0,0],
        'B': [0,1,0],
        'R': [0,0,1]
    }

    sample = open_sample(sample_file)
    new_array = []

    for array in sample:
        letter = array.pop(0)

        aux = [ int(value) for value in array]
    
        aux.extend(chars[letter])

        new_array.append(aux)

    return new_array
            