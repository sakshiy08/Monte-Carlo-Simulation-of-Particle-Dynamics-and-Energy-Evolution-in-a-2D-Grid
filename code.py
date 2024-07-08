import numpy as np
import random

def create_matrix(matrix_size, num_neutral, num_negative, num_positive):
    # Initialize the matrix with all elements set to 2
    A = np.zeros((matrix_size, matrix_size)) + 2  
    count = 0  # Counter to track the number of particles placed
    
    # Loop to place the particles
    for i in range(1000 * matrix_size):  # Increased iteration limit to account for larger matrices
        x = random.randint(0, matrix_size - 1)
        y = random.randint(0, matrix_size - 1)
        
        # Place neutral particles
        if A[x][y] == 2 and count < num_neutral:
            A[x][y] = 0
            count += 1
        # Place negatively charged particles
        elif A[x][y] == 2 and count >= num_neutral and count < num_neutral + num_negative:
            A[x][y] = -1
            count += 1
        # Place positively charged particles
        elif A[x][y] == 2 and count >= num_neutral + num_negative and count < num_neutral + num_negative + num_positive:
            A[x][y] = 1
            count += 1
        # Stop if the required number of particles has been placed
        elif count == num_neutral + num_negative + num_positive:
            break
    
    return A

-----------------------------------------------------------------------------------------

def energy(x, y):
    # Define energy values based on particle interactions
    if x == 0 and y == -1:
        e = -0.1
    elif x == 0 and y == 1:
        e = 0.1
    elif x == 0 and y == 0:
        e = 0.1
    elif x == 1 and y == 1:
        e = 0.5
    elif x == -1 and y == -1:
        e = 0.5
    elif x == 1 and y == -1:
        e = -0.7
    else:
        e = 0  # Default energy value for non-defined interactions
    
    return e

------------------------------------------------------------------------------------------

n, m = A.shape  # Get the dimensions of the matrix
old_energy = 0  # Initialize the total energy
    first_energy = np.zeros((n, m))  # Matrix to store interaction energies

    # Iterate over each element in the matrix
    for i in range(n):
        for j in range(m):
            if i == n - 1 and j != m - 1:  # If on the last row but not the last column
                first_energy[i][j] = energy(A[i][j], A[i][j + 1])
            elif i != n - 1 and j == m - 1:  # If not on the last row but on the last column
                first_energy[i][j] = energy(A[i][j], A[i + 1][j])
            elif i == n - 1 and j == m - 1:  # If on the last row and last column
                continue
            else:
                first_energy[i][j] += energy(A[i][j], A[i + 1][j])
                first_energy[i][j] += energy(A[i][j], A[i][j + 1])

            old_energy += first_energy[i][j]  # Sum the energies

    print(old_energy)  # Print the total initial energy


-------------------------------------------------------------------------------------------

import math

def metropolis_monte_carlo(matrix, KT, steps):
    n, m = matrix.shape  # Get the dimensions of the matrix
    for _ in range(steps):
        matrix_copy = matrix.copy()  # Create a copy of the matrix
        x = random.randint(0, n - 1)  # Randomly select a row
        y = random.randint(0, m - 1)  # Randomly select a column
        if matrix[x][y] == 0 or matrix[x][y] == 1 or matrix[x][y] == -1:  # Check if the selected position has a movable particle
            r = random.random()  # Generate a random number for movement direction
            if r <= 0.25:  # Move left
                x1 = x - 1
                y1 = y
                if x1 < 0:
                    # Apply Periodic Boundary Condition
                    x1 = x1 + n
            elif r > 0.25 and r <= 0.5:  # Move right
                x1 = x + 1
                y1 = y
                if x1 >= n:
                    x1 = x1 - n
            elif r > 0.5 and r <= 0.75:  # Move up
                x1 = x
                y1 = y - 1
                if y1 < 0:
                    y1 = y1 + m
            elif r > 0.75:  # Move down
                x1 = x
                y1 = y + 1
                if y1 >= m:
                    y1 = y1 - m

            # Swap positions if the target position is empty (value is 2)
            if matrix[x1][y1] == 2:
                matrix[x1][y1] = matrix[x][y]
                matrix[x][y] = 2
                x = x1
                y = y1

    return matrix


------------------------------------------------------------------------------------

# Energy after the random movement of particles
new_energy = 0
sec_energy = np.zeros((matrix_size, matrix_size))  # Matrix to store interaction energies after movement

# Iterate over each element in the matrix
for i in range(matrix_size):
    for j in range(matrix_size):
        if i == matrix_size - 1 and j != matrix_size - 1:  # If on the last row but not the last column
            sec_energy[i][j] = energy(A[i][j], A[i][j + 1])
        elif i != matrix_size - 1 and j == matrix_size - 1:  # If not on the last row but on the last column
            sec_energy[i][j] = energy(A[i][j], A[i + 1][j])
        elif i == matrix_size - 1 and j == matrix_size - 1:  # If on the last row and last column
            continue
        else:
            sec_energy[i][j] += energy(A[i][j], A[i + 1][j])
            sec_energy[i][j] += energy(A[i][j], A[i][j + 1])

        new_energy += sec_energy[i][j]  # Sum the energies

print(new_energy)  # Print the total energy after movement

-------------------------------------------------------------------------------------

# Metropolis criterion of the Monte Carlo algorithm
for i in range(matrix_size):
    for j in range(matrix_size):
        new_energy += sec_energy[i][j]  # Accumulate the new energy
        if new_energy < old_energy:
            # Accept the new state if the energy is lower
            old_energy = new_energy
        elif new_energy > old_energy:
            # Calculate the probability of accepting a higher energy state
            r2 = random.random()
            if math.exp(-(new_energy - old_energy) / KT) < r2:
                # Accept the new state with a certain probability
                old_energy = new_energy
            else:
                # Revert to the previous state and energy
                new_energy = old_energy
                A = A1.copy()
                continue

print(old_energy, new_energy)  # Print the final energies

--------------------------------------------------------------------------------------

# Association and Dissociation of particles after movement
# Initialize matrix B for complex formation tracking and set association/dissociation rates
B = np.zeros((matrix_size, matrix_size, 2))
k_a = input("value of Association constant:")
k_d = input("value of Dissociation constant:")
num_iterations = input("give number of iterations:")
R = k_a + k_d

# Loop for a large number of iterations to simulate the system
for _ in range(num_iterations ):
    A1 = A.copy()  # Copy the current state of matrix A to revert if necessary
    x = random.randint(0, matrix_size - 1)
    y = random.randint(0, matrix_size - 1)
    
    # Check if the selected position contains a particle (neutral, +1, -1, or complex(3))
    if A[x][y]==0 or A[x][y]==1 or A[x][y]==-1 and A[x][y]==3:
    r=random.random()
    if(r<=0.25):
      x1=x-1
      y1=y
      if(x1<0):
        x1=x1 + matrix size
    elif(r>0.25 and r<=0.5):
      x1=x+1
      y1=y
      if(x1>29):
        x1=x1 - matrix size
    elif(r>0.5 and r<=0.75):
      x1=x
      y1=y-1
      if(y1<0):
        y1=y1 + matrix size
    elif(r>0.75):
      x1=x
      y1=y+1
      if(y1>29):
        y1=y1 - matrix size

          
        #complex formation
        
        r1 = random.random()
        rr = r1 * R  # Random number to decide association or dissociation

        # Association process
        if A[x1][y1] != 2 and A[x][y] != 0 and A[x1][y1] != 0 and A[x][y] != 3 and rr <= k_a:
            if A[x][y] == 1 and A[x1][y1] == 1:
                B[x1][y1][0] += 2
            if A[x][y] == -1 and A[x1][y1] == -1:
                B[x1][y1][1] += 2
            if (A[x][y] == 1 and A[x1][y1] == -1) or (A[x][y] == -1 and A[x1][y1] == 1):
                B[x1][y1][0] += 1
                B[x1][y1][1] += 1
            if A[x][y] == 1 and A[x1][y1] == 3:
                B[x1][y1][0] += 1
            if A[x][y] == -1 and A[x1][y1] == 3:
                B[x1][y1][1] += 1
            A[x][y] = 2  # Empty the original cell
            A[x1][y1] = 3  # Mark the new cell as a complex

        # Dissociation process
        elif A[x][y] == 3 and A[x1][y1] == 2 and rr > k_a:
            if np.sum(B[x][y]) == 2:
                if B[x][y][0] == 2:
                    A[x][y] = 1
                    A[x1][y1] = 1
                    B[x][y][0] = 0
                elif B[x][y][1] == 2:
                    A[x][y] = -1
                    A[x1][y1] = -1
                    B[x][y][1] = 0
                elif B[x][y][0] == 1 and B[x][y][1] == 1:
                    A[x][y] = -1
                    A[x1][y1] = 1
                    B[x][y][0] = 0
                    B[x][y][1] = 0
            elif np.sum(B[x][y]) > 2:
                r3 = random.random()
                if r3 <= 0.5:
                    if B[x][y][0] > 1:
                        A[x1][y1] = 1
                        B[x][y][0] -= 1
                    elif B[x][y][1] > 1:
                        A[x1][y1] = -1
                        B[x][y][1] -= 1
                else:
                    if B[x][y][1] > 1:
                        A[x1][y1] = -1
                        B[x][y][1] -= 1
                    elif B[x][y][0] > 1:
                        A[x1][y1] = 1
                        B[x][y][0] -= 1

        # Movement of particles
        elif A[x1][y1] == 2:
            A[x1][y1] = A[x][y]  # Move the particle
            A[x][y] = 2  # Empty the original cell
            x=x1
            y=y1

# Initialize counters for different particle types and complexes
count1 = 0  # Count of +1 charged particles
count0 = 0  # Count of neutral particles
countn1 = 0  # Count of -1 charged particles
count3 = 0  # Count of complexes
total_complex_strength = 0  # Total strength of complexes

# Loop through the entire matrix to count particles and complexes
for i in range(matrix_size):
    for j in range(matrix_size):
        if A[i][j] == 1:
            count1 += 1  # Increment count of +1 particles
        elif A[i][j] == -1:
            countn1 += 1  # Increment count of -1 particles
        elif A[i][j] == 0:
            count0 += 1  # Increment count of neutral particles
        elif A[i][j] == 3:
            count3 += 1  # Increment count of complexes
            total_complex_strength += np.sum(B[i][j])  # Sum the strengths of complexes

# Output the results
print(f"Count of +1 particles: {count1}")
print(f"Count of -1 particles: {countn1}")
print(f"Count of neutral particles: {count0}")
print(f"Count of complexes: {count3}")
print(f"Total complex strength: {total_complex_strength}")


hhju
