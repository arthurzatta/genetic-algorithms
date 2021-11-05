from model.dataset import and_table, or_table, xor_table, robot_table
from services.mlp import MLP

if __name__ == "__main__":
    #qtd_h = (qtd_in+1+qtd_out)/2
    # one more element is considered because of the bias

    and_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=and_table).executar()
    # or_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=or_table)
    # xor_resolution = MLP(qtd_in=2, qtd_out=1, qtd_h=2, dataset=xor_table)
    # robot_resolution = MLP(qtd_in=3, qtd_out=2, qtd_h=3, dataset=robot_table).executar()
