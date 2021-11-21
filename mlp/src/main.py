from model.dataset import and_table, or_table, xor_table, robot_table
from services.mlp import MLP

AGES = 10000
MIN = -0.3
MAX = 0.3

print("TABELA AND")
and_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=and_table, ages=AGES, min_value=MIN, max_value=MAX, ni=0.3).executar()
print("TABELA OR")
or_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=or_table, ages=AGES, min_value=MIN, max_value=MAX, ni=0.3).executar()
print("TABELA XOR")
xor_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=xor_table, ages=AGES, min_value=MIN, max_value=MAX, ni=0.3).executar()
print("TABELA ROBO")
robot_resolution = MLP(qtd_in=3, qtd_out=2, qtd_h=3, dataset=robot_table, ages=AGES, min_value=MIN, max_value=MAX, ni=0.3).executar()

