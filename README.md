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
+ initial_energy(A) function computes the total initial energy of the system
+ It initializes old_energy to zero and first_energy as a matrix of zeros to store interaction energies
+ Iterates through each element of matrix A to calculate interaction energies:
  - Handles boundary conditions to ensure proper energy calculation at matrix edges
  - Accumulates total energy in old_energy 
+ The computed old_energy is printed, representing the total initial energy of the particle system based on initial particle configurations

### Particle Movement using random motion

This part of the code uses the Monte Carlo method to simulate the movement of particles within the matrix. The key aspects of this process are:

+ **Random Selection of Particles:** 
     The code randomly selects a particle within the matrix to move. Particles can be neutral (0), negatively charged (-1), or positively charged (1)

+ **Movement Direction:** 
     A random direction is chosen for the particle to move (left, right, up, or down). This is determined by generating a random number and using it to select one of the four possible directions

+ **Periodic Boundary Conditions:** 
     The code applies periodic boundary conditions to ensure particles that move out of one side of the matrix re-enter from the opposite side. This simulates a continuous, unbounded space

+ **Swapping Positions:** 
     If the selected direction leads to an empty position (value 2), the particle is moved to the new position, and the old position is marked as empty

+ **Iteration:** 
     The process is repeated for a defined number of steps, allowing particles to move multiple times and achieve a more realistic simulation of dynamic movement

**KT Value:** The KT value (related to thermal energy) can be adjusted to influence the likelihood of particle movement

This method helps in studying the statistical behavior and equilibrium properties of the system by simulating the movement and interaction of particles under controlled conditions

### Calculating Energy again after the particle movement
+ A new energy matrix (sec_energy) is created to store the interaction energies of particles after they have moved
+ The code iterates through each element in the matrix A, checking the interaction energies of adjacent particles 
+ For particles on the last row or column, it ensures that interactions with adjacent particles are correctly handled. Periodic boundary conditions are considered to ensure continuity
+ The total energy of the system is calculated by summing the interaction energies of all particle pairs

### Metropolis Criterion Application
This section of the code applies the Metropolis criterion of the Monte Carlo algorithm to decide whether to accept or reject new particle configurations based on their energies

+ New Energy Accumulation: The new energy of the system (new_energy) is accumulated by summing the interaction energies of particles in the matrix
+ Energy Comparison: The new energy is compared with the old energy (old_energy). If the new energy is lower, the new state is accepted unconditionally
+ Probabilistic Acceptance: If the new energy is higher, a probabilistic acceptance criterion is applied:
  - A random number r2 is generated
  - The Boltzmann factor (exp(-(new_energy - old_energy) / KT)) is calculated
  - If the Boltzmann factor is less than r2, the new state is accepted
  - Otherwise, the system reverts to the previous state (A1) and energy
+ Output: The final energies (old_energy and new_energy) are printed for analysis

### Association and Dissociation of Particles
This part of the code simulates the association and dissociation of particles within a 2D matrix. Particles can move randomly, form complexes, or dissociate based on defined probabilities. The simulation helps study the dynamics and equilibrium properties of the system

Initialization:
- A 3D matrix B is initialized to keep track of particle complexes
- Constants k_a (association rate) and k_d (dissociation rate) is to be provided
- R is the sum of k_a and k_d

Main Simulation Loop:
- The simulation runs for your defined of iterations (num_iterations)
- A copy of the current state of the matrix A is created (A1)
- A random position (x, y) in the matrix is selected

Random Movement:
Based on a random number r, particles move to adjacent positions (left, right, up, or down) with periodic boundary conditions applied

Complex Formation:
  - Association:
    - If certain conditions are met (particles are not empty spaces or complexes), particles at adjacent positions may form a complex
    - The type of complex formed depends on the types of particles involved
    - The matrix A is updated to reflect the formation of a complex, and the matrix B is updated to keep track of the components of the complex

  - Dissociation:
    - If a complex is present, it may dissociate based on the dissociation rate
    - The matrix A and B are updated to reflect the dissociation, reverting to the original particles

Particle Counting:
- After the main simulation loop, the code counts the number of each type of particle (+1, -1, neutral, and complexes)
- It also sums the components of all complexes

