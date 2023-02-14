import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Define the lengths of the robot arm links in meters
L1 = 0.5
L2 = 0.5
L3 = 0.5

# Define the joint angles in radians
theta1 = st.slider("Joint 1 angle (in degrees)", -180, 180, 0, 1) * np.pi / 180
theta2 = st.slider("Joint 2 angle (in degrees)", -180, 180, 0, 1) * np.pi / 180
theta3 = st.slider("Joint 3 angle (in degrees)", -180, 180, 0, 1) * np.pi / 180

# Calculate the forward kinematics to find the end effector position
x = L1*np.cos(theta1) + L2*np.cos(theta1+theta2) + L3*np.cos(theta1+theta2+theta3)
y = L1*np.sin(theta1) + L2*np.sin(theta1+theta2) + L3*np.sin(theta1+theta2+theta3)

# Define the points to plot the robot arm
x_points = [0, L1*np.cos(theta1), L1*np.cos(theta1) + L2*np.cos(theta1+theta2), x]
y_points = [0, L1*np.sin(theta1), L1*np.sin(theta1) + L2*np.sin(theta1+theta2), y]

# Create a plot to display the robot arm
fig, ax = plt.subplots()
ax.plot(x_points, y_points, 'o-')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
st.pyplot(fig)
