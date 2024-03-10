#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Constants for the number of values and the preferred temperature range
# NUM_VALUES = 500
# MIN_TEMP = 18
# MAX_TEMP = 21
#
#
# # Class definition for the DataGenerator
# class DataGenerator:
#     def __init__(self, min_value=0, max_value=1, min_output=MIN_TEMP, max_output=MAX_TEMP):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.min_output = min_output
#         self.max_output = max_output
#
#     def _private_method(self):
#         # Generates random values in the range 0-1
#         return np.random.rand()
#
#     @property
#     def public_property(self):
#         # Uses the private method to get a random value and then scales it to the preferred range
#         raw_value = self._private_method()
#         return raw_value * (self.max_output - self.min_output) + self.min_output
#
#
# # Create an instance of the DataGenerator
# data_generator = DataGenerator()
#
# # Generate values and simulate sensor readings
# sensor_values = [data_generator.public_property for _ in range(NUM_VALUES)]
# time_stamps = list(range(NUM_VALUES))
#
# # Plotting the sensor values
# plt.figure(figsize=(10, 5))
# plt.plot(time_stamps, sensor_values, label='Simulated Sensor Data')
# plt.xlabel('Time')
# plt.ylabel('Sensor Reading')
# plt.title('Sensor Data Simulation')
# plt.legend()
# plt.show()
#
# # Save the plot
# plt.savefig('sensor_data_simulation.png')

##------------------------------------
import matplotlib.pyplot as plt
import numpy as np


class DataGenerator:
    def __init__(self, min_value=18, max_value=21):
        self.min_value = min_value
        self.max_value = max_value

    def _generate_random_value(self):
        # Private method to generate a normalized random value between 0 and 1
        return np.random.rand()

    @property
    def random_sensor_value(self):
        # Public property to scale and translate the random value to the preferred range
        return (self.max_value - self.min_value) * self._generate_random_value() + self.min_value

    def generate_data(self, num_points=500):
        # Generate a list of random sensor values
        return [self.random_sensor_value for _ in range(num_points)]


# Example usage
data_gen = DataGenerator()
data_values = data_gen.generate_data()

# Plotting the data
plt.plot(data_values, 'r+')
plt.xlabel('Measurement Number')
plt.ylabel('Sensor Value')
plt.title('Simulated Sensor Data')
plt.show()
