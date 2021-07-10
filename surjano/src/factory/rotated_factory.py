from src.controllers.rotated_ellipsoide import RotatedEllipsoide
class RotatedEllipsoideFactory:
    @staticmethod
    def factory(chromosome):
        return RotatedEllipsoide(chromosome)
