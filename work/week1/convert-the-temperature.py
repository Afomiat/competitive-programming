class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr = []
        K = celsius + 273.15
        F = (celsius *1.80)+ 32.00
        arr.append(K)
        arr.append(F)
        return arr