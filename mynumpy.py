import numpy as np

# 1. Random integer below the number passed in as a parameter (Scalar or a 0-D Array)
x = np.random.randint(10)
print(x)
print(type(x))

# 2. Random 1 dimensional array with 5 integer elements that are below 10
x = np.random.randint(10, size=(5))
print(x)
print(type(x))

# 3. Random 2 dimensional array with 9 integer elements that are below 10
x = np.random.randint(10, size=(3,3))
print(x)
print(type(x))

# 4. 1-d array of 10 floating point numbers  
x = np.random.rand(10)
print(x)
print(type(x))

# 5. 2-d array of 10 elements  
x = np.random.rand(2,5)
print(x)
print(type(x))

#6. Choose a random number from a list using the choice function
x = np.random.choice([3, 5, 2.73, 3.72, 5])
print(x)

#7. Create a 2d array using the choice function
x = np.random.choice([3, 5, 2.73, 3.72, 5], size=(2,3))
print(x)

#8. Create a 2d array using choice function with a certain probability
x = np.random.choice([3, 5, 2.73, 3.72, 5], size=(2,3),p=[0.5,0.1,0.1,0.2,0.1])
print(x)

#9. The shuffle function. Shuffles elements within an array
arr = np.array([[3, 2], [4, 6], [8, 1]])
np.random.shuffle(arr)
print(arr)

#10. The permutation function does not change the original array like the shuffle function
print(np.random.permutation(arr))
