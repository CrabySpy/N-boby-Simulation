# Orbital-Simulation

An interactive 2D orbital simulation in Python using Pygame, allowing you to explore gravitational dynamics with multiple celestial bodies. Simulate stars, planets, and particles with real-time physics and interactive controls.

## Features

- **Multiple presets:**
  - **Basic** – Single stationary star at the center.
  - **Circular Orbit** – Planet orbiting a star with circular velocity.
  - **Elliptical Orbit** – Planet orbiting a star with elliptical trajectory.
  - **Gravitational Collapse** – Many-body system showing dynamic collapse.
- **Interactive body addition:** Click and drag to add new planets/bodies.
- **Collision handling:** Bodies are destroyed on contact.
- **Real-time visualization:** Orbit trails are not displayed for clarity.
- **Adjustable simulation speed** via FPS.
- **Simulation controls:** Pause, reset, and return to main menu anytime.

## Physics and Equations

The simulation uses Newtonian gravity with Verlet integration for stability.

### Gravitational Acceleration

<img width="380" height="110" alt="image" src="https://github.com/user-attachments/assets/63b8c989-6137-46a2-b4a0-a87770845e44" />

Where:

- $\vec{a}_j$ = acceleration of body $j$  
- $G$ = gravitational constant (scaled to 100 in simulation)  
- $m_i$ = mass of body $i$  
- $\vec{r}_i - \vec{r}_j$ = displacement vector from body $j$ to $i$  
- $\varepsilon$ = softening constant  

### Position Update (Verlet Integration)

The next position of a body is calculated using Verlet integration:

<img width="457" height="74" alt="image" src="https://github.com/user-attachments/assets/34690289-1b50-4154-85a2-c6bbc28cc59b" />

Where:

- $\vec{r}_t$ = current position  
- $\vec{r}_{t-\Delta t}$ = previous position  
- $\vec{a}_t$ = acceleration at current time step  
- $\Delta t$ = time step  

### Collision Detection

Two bodies collide if the distance between their centers is less than the sum of their radii:

<img width="312" height="67" alt="image" src="https://github.com/user-attachments/assets/a8140205-1c1c-43c3-a743-180ea6347128" />

Where:

- $\vec{r}_1, \vec{r}_2$ = positions of the two bodies  
- $r_1, r_2$ = radii of the two bodies  

## Algorithm Overview

1. **Initialization**  
   Set up Pygame window, constants, sprite groups, and fonts.

2. **Preset Selection**  
   Spawn bodies based on the chosen preset with initial positions, velocities, and masses.

3. **Simulation Loop**  
   - Compute gravitational acceleration for each body  
   - Update positions using Verlet integration  
   - Check and handle collisions  
   - Draw bodies and UI buttons on screen  
   - Handle user input (pause, reset, back, quit, add bodies)  

   Repeat FPS-controlled loop until user quits or returns to menu.

## Presets

| Preset | Description |
|--------|-------------|
| Basic | Single stationary star at the center. |
| Circular Orbit | Star + planet with velocity set for circular orbit. |
| Elliptical Orbit | Star + planet with slightly altered velocity for elliptical trajectory. |
| Gravitational Collapse | Many small bodies initialized randomly for a dynamic collapse simulation. |

## Controls

| Key / Action | Description |
|--------------|-------------|
| ESC or Close | Quit simulation |
| Q | Quit simulation |
| B | Back to previous menu |
| R | Reset the current simulation |
| Mouse Click / Drag | Add a new planet/body at mouse position (velocity fixed as (100, 0)) |
