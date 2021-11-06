# Todo
- [ ] Understand MLP
- [ ] Code the basics parts
  - [ ] Implement most isolated functions as possible
  - [ ] Focused on reusabilitie
- [ ] Implement the dataset
- [ ] Test
- [ ] Refactoring


# MLP
- Entradas: normalmente de n+1 entradas, x0 = 1
- H: camadas escondidas
  - um vetor com x_in + 1 posições, sempre uma posição a mais pro bias
  


# Implementation

- An abstract class called RNA with the main mathods of mlp
- An MLP class to implement executer and trainer
- Number of hiden layers depends of the function used, in normal cases a continuos function uses one layer, but with discontinuous two or more can be used, normaly two.
