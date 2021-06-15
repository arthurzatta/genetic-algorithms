from nRainhasInd import nRainhasInd

class RainhasFactory:

    #factory method
    @staticmethod    
    def rainhasFactory(genes: list):
        return nRainhasInd(genes)
