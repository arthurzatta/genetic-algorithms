from model.dataset import and_table, or_table, xor_table, robot_table
from services.mlp import MLP

AGES = 10000
MIN = -0.3
MAX = 0.3

and_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=and_table, ages=AGES, min_value=MIN, max_value=MAX).executar()
or_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=or_table, ages=AGES, min_value=MIN, max_value=MAX).executar()
xor_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=xor_table, ages=AGES, min_value=MIN, max_value=MAX).executar()
robot_resolution = MLP(qtd_in=3, qtd_out=2, qtd_h=3, dataset=robot_table, ages=AGES, min_value=MIN, max_value=MAX).executar()

