# Monte-Carlo-Simulation-of-Particle-Dynamics-and-Energy-Evolution-in-a-2D-Grid
How can a computational model simulate the dynamics of ion movement within a biological membrane, considering random diffusion, energy interactions using the principles of the Metropolis criterion, association/disassociation?

## Explanation --> <br>

Function Definition: A function create_matrix is defined to encapsulate the matrix creation process 

### Parameters: The function takes four parameters:
+ matrix_size: The size of the matrix (n x n)
+ num_neutral: The number of neutral particles (0)
+ num_negative: The number of negatively charged particles (-1)
+ num_positive: The number of positively charged particles (1)
  
Matrix Initialization: The matrix A is initialized with all elements set to 2 <br>
Particle Placement: Particles are placed in the matrix according to the specified counts for neutral, negative, and positive particles <br>
Iteration Limit: The iteration limit in the loop is adjusted to 1000 * matrix_size to accommodate larger matrices <br>

### Energy Function

The `energy` function takes two parameters, `x` and `y`, which represent the charges of two interacting particles. The function returns the energy of interaction based on predefined rules. The energy function is a crucial component in the simulation, helping to calculate the interactions based on the charges of the particles

### Calculating Initial Energy
+ initial_energy(A) function computes the total initial energy of the system <br>
+ It initializes old_energy to zero and first_energy as a matrix of zeros to store interaction energies <br>
+ Iterates through each element of matrix A to calculate interaction energies:
  - Handles boundary conditions to ensure proper energy calculation at matrix edges
  - Accumulates total energy in old_energy 
+ The computed old_energy is printed, representing the total initial energy of the particle system based on initial particle configurations.

### Particle Movement using Metropolis criterion

This part of the code uses the Metropolis Monte Carlo method to simulate the movement of particles within the matrix. The key aspects of this process are:

1. **Random Selection of Particles:** 
     The code randomly selects a particle within the matrix to move. Particles can be neutral (0), negatively charged (-1), or positively charged (1).

2. **Movement Direction:** 
     A random direction is chosen for the particle to move (left, right, up, or down). This is determined by generating a random number and using it to select one of the four possible directions.

3. **Periodic Boundary Conditions:** 
     The code applies periodic boundary conditions to ensure particles that move out of one side of the matrix re-enter from the opposite side. This simulates a continuous, unbounded space.

4. **Swapping Positions:** 
     If the selected direction leads to an empty position (value 2), the particle is moved to the new position, and the old position is marked as empty.

5. **Iteration:** 
     The process is repeated for a defined number of steps, allowing particles to move multiple times and achieve a more realistic simulation of dynamic movement.

**KT Value:** The KT value (related to thermal energy) can be adjusted to influence the likelihood of particle movement

This method helps in studying the statistical behavior and equilibrium properties of the system by simulating the movement and interaction of particles under controlled conditions
