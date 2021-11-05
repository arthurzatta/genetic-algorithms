from abc import ABC, abstractmethod
import numpy as np


class RNA(ABC):

    @abstractmethod
    def treinar(self, x_in: np.ndarray, y: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def executar(self) -> np.ndarray:
        pass
