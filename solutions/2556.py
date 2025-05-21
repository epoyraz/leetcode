class Solution:
    def convertTemperature(self, celsius):
        # Kelvin conversion
        kelvin = celsius + 273.15
        # Fahrenheit conversion
        fahrenheit = celsius * 1.8 + 32.0
        return [kelvin, fahrenheit]
