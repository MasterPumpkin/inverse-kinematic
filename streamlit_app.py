import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Define the length of the arm segments
L1 = 1
L2 = 1
L3 = 1

# Define the joint angles
theta1 = np.pi/4
theta2 = np.pi/6
theta3 = np.pi/3

# Calculate the end effector position using forward kinematics
x = L1*np.cos(theta1) + L2*np.cos(theta1+theta2) + L3*np.cos(theta1+theta2+theta3)
y = L1*np.sin(theta1) + L2*np.sin(theta1+theta2) + L3*np.sin(theta1+theta2+theta3)

# Define the desired end effector position
x_desired = 2
y_desired = 2

# Calculate the joint angles required to achieve the desired end effector position using inverse kinematics
theta3_desired = np.arccos((x_desired**2 + y_desired**2 - L1**2 - L2**2 - L3**2) / (2*L2*L3))
theta2_desired = np.arctan2(y_desired*(L2 + L3*np.cos(theta3_desired)) - x_desired*L3*np.sin(theta3_desired), x_desired*(L2 + L3*np.cos(theta3_desired)) + y_desired*L3*np.sin(theta3_desired)) - theta1
theta1_desired = np.arctan2(y_desired, x_desired) - np.arctan2(L2*np.sin(theta2_desired) + L3*np.sin(theta2_desired + theta3_desired), L1 + L2*np.cos(theta2_desired) + L3*np.cos(theta2_desired + theta3_desired))

# Define the animation parameters
frames = 100
theta1_vals = np.linspace(theta1, theta1_desired, frames)
theta2_vals = np.linspace(theta2, theta2_desired, frames)
theta3_vals = np.linspace(theta3, theta3_desired, frames)

# Create the Streamlit user interface
x_desired = st.number_input('Desired x position:', value=2.0)
y_desired = st.number_input('Desired y position:', value=2.0)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Define the plot data
arm_data = np.array([[0, 0, 0], [L1*np.cos(theta1), L1*np.sin(theta1), 0, [L1_np.cos(theta1) + L2_np.cos(theta1+theta2), L1_np.sin(theta1) + L2_np.sin(theta1+theta2), 0], [L1_np.cos(theta1) + L2_np.cos(theta1+theta2) + L3_np.cos(theta1+theta2+theta3), L1_np.sin(theta1) + L2_np.sin(theta1+theta2) + L3_np.sin(theta1+theta2+theta3), 0]]) 
desired_data = np.array([[x_desired, y_desired, 0]])

# Plot the arm and desired end effector position

ax.plot(arm_data[:,0], arm_data[:,1], arm_data[:,2], 'bo-', linewidth=2, markersize=12) 
ax.plot(desired_data[:,0], desired_data[:,1], desired_data[:,2], 'ro', markersize=12)

# Create the animation

for i in range(frames): 
	theta1 = theta1_vals[i] 
	theta2 = theta2_vals[i] 
	theta3 = theta3_vals[i]
	arm_data = np.array([[0, 0, 0], [L1*np.cos(theta1), L1*np.sin(theta1), 0], [L1*np.cos(theta1) + L2*np.cos(theta1+theta2), L1*np.sin(theta1) + L2*np.sin(theta1+theta2), 0], [L1*np.cos(theta1) + L2*np.cos(theta1+theta2) + L3*np.cos(theta1+theta2+theta3), L1*np.sin(theta1) + L2*np.sin(theta1+theta2) + L3*np.sin(theta1+theta2+theta3), 0]])
	desired_data = np.array([[x_desired, y_desired, 0]])

ax.clear()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.plot(arm_data[:,0], arm_data[:,1], arm_data[:,2], 'bo-', linewidth=2, markersize=12)
ax.plot(desired_data[:,0], desired_data[:,1], desired_data[:,2], 'ro', markersize=12)

plt.pause(0.01)

# Show the plot

plt.show()
