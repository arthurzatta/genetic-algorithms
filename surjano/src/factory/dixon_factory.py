from src.controllers.dixon import Dixon

class DixonFactory:
    @staticmethod
    def factory(chromosome: list)  -> Dixon:
        return Dixon(chromosome)
