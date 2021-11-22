import random
from math import floor,ceil
import numpy as np

def balance_dataset(): 

  balance = {
    "B": [0,1,0],
    "R": [0,0,1],
    "L": [1,0,0]
  }

  data = []

  with open("/home/arthur/Desktop/Faculdade/IC/genetic-algorithms/mlp/src/model/balance-scale.data") as file:
    for line in file:
      dataset_line = line.splitlines()[0].split(',')
      outputs = balance[dataset_line[0]]
      x_in = list(map(int, dataset_line[1:]))
      x_in.extend(outputs)
      data.append(x_in)
  return data

def wdbc_dataset(): 

  diagnosis = {
    "M": [1, 0],
    "B": [0, 1]
  }

  data = []

  with open("/home/arthur/Desktop/Faculdade/IC/genetic-algorithms/mlp/src/model/wdbc.data") as file:
    for line in file:
      dataset_line = line.splitlines()[0].split(',')
      outputs = diagnosis[dataset_line[1]]
      x_in = list(map(float, dataset_line[2:]))
      x_in.extend(outputs)
      data.append(x_in)
  return data

def wpbc_dataset(): 

  recurrence = {
    "R": [1, 0],
    "N": [0, 1]
  }

  data = []

  with open("/home/arthur/Desktop/Faculdade/IC/genetic-algorithms/mlp/src/model/wpbc.data") as file:
    for line in file:
      dataset_line = line.splitlines()[0].split(',')
      outputs = recurrence[dataset_line[1]]
      x_in = list(map(float, dataset_line[3:]))
      x_in.extend(outputs)
      data.append(x_in)
  return data


def selection(dataset_name):

  datasets = {
    "WPBC": wpbc_dataset(),
    "WDBC": wdbc_dataset(),
    "BALANCE": balance_dataset(),
  }

  bases = {
    "training": [],
    "test": [],    
  }

  dataset = datasets[dataset_name]
  dataset_length = len(dataset)-1
  
  training_percent = ceil(dataset_length * 0.75)
 
  for i in range(training_percent):
    rand_index = random.randint(0, dataset_length)
    element = dataset.pop(rand_index)
    bases['training'].append(element)
    dataset_length -= 1
  
  bases['test'] = np.asarray(dataset)
  bases['training'] = np.asarray(bases['training'])

  return bases
  