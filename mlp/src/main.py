from model.dataset import and_table, or_table, xor_table, robot_table
from model.dataset_selection import selection
from services.mlp import MLP

AGES = 1000
MIN = -0.3
MAX = 0.3

print("BALANCE")
MLP(qtd_in=4, qtd_out=3, qtd_h=4, dataset=selection('BALANCE'), ages=AGES, min_value=MIN, max_value=MAX, ni=0.3, quadratic_error=True).runner()

print("WDBC")
MLP(qtd_in=30, qtd_out=2, qtd_h=16, dataset=selection('WDBC'), ages=AGES, min_value=MIN, max_value=MAX, ni=0.3, quadratic_error=True).runner()

print("WPBC")
MLP(qtd_in=32, qtd_out=2, qtd_h=16, dataset=selection('WPBC'), ages=AGES, min_value=MIN, max_value=MAX, ni=0.3, quadratic_error=True).runner()
