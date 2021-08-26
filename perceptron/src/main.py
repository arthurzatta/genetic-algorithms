from dataset import and_table, or_table, xor_table, robot_table_first, robot_table_second 
from runner import Runner
from perceptron import Perceptron

AGES = 10000
MIN_INTERVAL = -0.3
MAX_INTERVAL = 0.3

perceptron = Perceptron()

print('Tabela AND')
and_result = Runner(dataset=and_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL, perceptron=perceptron).executer()

print('Tabela OR')
or_result = Runner(dataset=or_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL, perceptron=perceptron).executer()

print('Tabela XOR')
xor_result = Runner(dataset=xor_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL, perceptron=perceptron).executer()

print('Tabela ROBÔ NEURONIO 1')
robot_result_first = Runner(dataset=robot_table_first,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL,perceptron=perceptron).executer() 

print('Tabela ROBÔ NEURONIO 2')
robot_result_second = Runner(dataset=robot_table_second,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL,perceptron=perceptron).executer() 
