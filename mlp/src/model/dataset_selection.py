import random
from math import floor,ceil
import numpy as np

def base_model():
  return { "training": [], "test": [] }
def balance_dataset(): 

  balance = {
    "B": [0,1,0],
    "R": [0,0,1],
    "L": [1,0,0]
  }

  balance_separation = {
    "B": [],
    "R": [],
    "L": []
  }

  with open("/home/arthur/Desktop/Faculdade/IC/genetic-algorithms/mlp/src/model/balance-scale.data") as file:
    for line in file:
      dataset_line = line.splitlines()[0].split(',')
      result = dataset_line[0]
      outputs = balance[result]
      x_in = list(map(int, dataset_line[1:]))
      x_in.extend(outputs)
      balance_separation[result].append(x_in)

  bases = base_model()

  for key in balance_separation:
    # print("Key: {} Length: {} ".format(key, len(balance_separation[key])))
    # input()
    splited_bases = class_separation(balance_separation[key])
    bases['training'].extend(splited_bases['training'])
    bases['test'].extend( splited_bases['test'])
  
  return bases

def wdbc_dataset(): 

  diagnosis = {
    "M": [1, 0],
    "B": [0, 1]
  }
  diagnosis_separation = {
    "M": [],
    "B": []
  }

  with open("/home/arthur/Desktop/Faculdade/IC/genetic-algorithms/mlp/src/model/wdbc.data") as file:
    for line in file:
      dataset_line = line.splitlines()[0].split(',')
      result = dataset_line[1]
      outputs = diagnosis[result]
      x_in = list(map(float, dataset_line[2:]))
      x_in.extend(outputs)
      diagnosis_separation[result].append(x_in)
  
  bases = base_model()

  for key in diagnosis_separation:
    # print("Key: {} Length: {} ".format(key, len(diagnosis_separation[key])))
    # input()
    splited_bases = class_separation(diagnosis_separation[key])
    bases['training'].extend(splited_bases['training'])
    bases['test'].extend( splited_bases['test'])  
  return bases


def wpbc_dataset(): 

  recurrence = {
    "R": [1, 0],
    "N": [0, 1]
  }

  recurrence_separation = {
    "R": [],
    "N": []
  }

  with open("/home/arthur/Desktop/Faculdade/IC/genetic-algorithms/mlp/src/model/wpbc.data") as file:
    for line in file:
      dataset_line = line.splitlines()[0].split(',')
      result = dataset_line[1]
      outputs = recurrence[result]
      x_in = list(map(float, dataset_line[3:]))
      x_in.extend(outputs)
      recurrence_separation[result].append(x_in)

  bases = base_model()

  for key in recurrence_separation:
    # print("Key: {} Length: {} ".format(key, len(recurrence_separation[key])))
    # input()
    splited_bases = class_separation(recurrence_separation[key])
    bases['training'].extend(splited_bases['training'])
    bases['test'].extend( splited_bases['test'])  
  return bases

def class_separation(class_array):
  bases = {
    "training": [],
    "test": [],    
  }

  dataset_length = len(class_array)-1
  
  training_percent = ceil(dataset_length * 0.75)
 
  for i in range(training_percent):
    rand_index = random.randint(0, dataset_length)
    element = class_array.pop(rand_index)
    bases['training'].append(element)
    dataset_length -= 1
  
  bases['test'] = np.asarray(class_array) 
  bases['training'] = np.asarray(bases['training'])

  return bases

def selection(dataset_name):

  datasets = {
    "WPBC": wpbc_dataset,
    "WDBC": wdbc_dataset,
    "BALANCE": balance_dataset,
  }

  function = datasets[dataset_name] 
  training_bases = function()
  rng = np.random.default_rng()
  rng.shuffle(training_bases['training'])
  rng.shuffle(training_bases['test'])
  
  return training_bases

if __name__ == '__main__':
  print(selection('BALANCE')['training'])