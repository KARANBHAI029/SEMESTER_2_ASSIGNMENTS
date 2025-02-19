class Converter:
    def __init__(self, length, unit):
        self.length = length  # the length provided by the user
        self.unit = unit.lower()  # the unit provided by the user (converted to lowercase for consistency)
        
        # Conversion rates from each unit to meters
        self.conversion_rates = {
            'inches': 0.0254,  # 1 inch = 0.0254 meters
            'feet': 0.3048,    # 1 foot = 0.3048 meters
            'yards': 0.9144,   # 1 yard = 0.9144 meters
            'miles': 1609.34,  # 1 mile = 1609.34 meters
            'kilometers': 1000,  # 1 kilometer = 1000 meters
            'meters': 1,       # 1 meter = 1 meter
            'centimeters': 0.01,  # 1 centimeter = 0.01 meters
            'millimeters': 0.001  # 1 millimeter = 0.001 meters
        }
        
        # Check if the unit provided is valid
        if self.unit not in self.conversion_rates:
            raise ValueError(f"Invalid unit '{unit}'. Valid units are: inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")
        
        # Convert the input length to meters
        self.length_in_meters = self.length * self.conversion_rates[self.unit]

    def inches(self):
        return self.length_in_meters / self.conversion_rates['inches']

    def feet(self):
        return self.length_in_meters / self.conversion_rates['feet']

    def yards(self):
        return self.length_in_meters / self.conversion_rates['yards']

    def miles(self):
        return self.length_in_meters / self.conversion_rates['miles']

    def kilometers(self):
        return self.length_in_meters / self.conversion_rates['kilometers']

    def meters(self):
        return self.length_in_meters  # already in meters

    def centimeters(self):
        return self.length_in_meters / self.conversion_rates['centimeters']

    def millimeters(self):
        return self.length_in_meters / self.conversion_rates['millimeters']

# Example usage:
c = Converter(9, 'inches')  # Convert 9 inches
print(c.feet())  # 0.75 feet
print(c.yards())  # 0.25 yards
print(c.meters())  # 0.2286 meters
print(c.kilometers())  # 0.0002286 kilometers
print(c.centimeters())  # 22.86 centimeters
print(c.millimeters())  # 228.6 millimeters


