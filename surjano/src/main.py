from factory.rotated_factory import RotatedEllipsoidFactory
from factory.dixon_factory import DixonFactory
from controllers.ag import Ag

MAX_INDIVIDUALS = 40
ELITE = 8
GENERATIONS = 2000

ag = Ag()

print("ROTATED HYPER-ELLIPSOID FUNCTION")
ag.execute( nGen=GENERATIONS,
            nInd=MAX_INDIVIDUALS,
            elitism=ELITE,
            maximization=False,
            interval=(-65.536, 65.536),
            factory=RotatedEllipsoidFactory.factory )

print("DIXON-PRICE FUNCTION")
ag.execute( nGen=GENERATIONS,
            nInd=MAX_INDIVIDUALS,
            elitism=ELITE,
            maximization=False,
            interval=(-10, 10),
            factory=DixonFactory.factory )








