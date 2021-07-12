from controllers.rotated_ellipsoid import RotatedEllipsoid
    
class RotatedEllipsoidFactory:
    @staticmethod
    def factory(chromosome: list) -> RotatedEllipsoid:
        return RotatedEllipsoid(chromosome)
