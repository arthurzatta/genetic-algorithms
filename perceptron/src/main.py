from dataset import and_table, or_table, xor_table, robot_table
from runner import Runner
from perceptron import Perceptron

AGES = 1000
MIN_INTERVAL = -0.3
MAX_INTERVAL = 0.3

perceptron = Perceptron()

print('Tabela AND')
and_result = Runner(dataset=and_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL, perceptron=perceptron).executer()
input()
print('Tabela OR')
or_result = Runner(dataset=or_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL, perceptron=perceptron).executer()

print('Tabela XOR')
xor_result = Runner(dataset=xor_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL, perceptron=perceptron).executer()

print('Tabela ROBÔ NEURONIO')
robot_result = Runner(dataset=robot_table,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL,perceptron=perceptron).executer() 
