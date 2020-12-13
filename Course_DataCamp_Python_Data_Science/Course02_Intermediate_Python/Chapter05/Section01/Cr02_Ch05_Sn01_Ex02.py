# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
throw_one = np.random.randint(1, 7)

# Use randint() again
throw_two = np.random.randint(1, 7)

print(throw_one)
print(throw_two)