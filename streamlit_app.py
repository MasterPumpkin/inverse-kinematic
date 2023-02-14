import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Define the length of the two links
l1 = 1
l2 = 1

def forward_kinematic(theta1, theta2):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y

def inverse_kinematic(x, y):
    # Solve for theta1
    theta1 = np.arctan2(y, x)

    # Solve for theta2
    D = np.sqrt(x**2 + y**2)
    a = np.arccos((l1**2 + D**2 - l2**2) / (2 * l1 * D))
    b = np.arccos((l2**2 + D**2 - l1**2) / (2 * l2 * D))
    theta2 = np.pi - a - b
    return theta1, theta2

st.title("2 DOF Robotic Arm Inverse Kinematic")

x = st.slider("End-effector X position", 0.0, 2.0, 1.0)
y = st.slider("End-effector Y position", 0.0, 2.0, 1.0)

theta1, theta2 = inverse_kinematic(x, y)

st.write("Theta1:", theta1)
st.write("Theta2:", theta2)

# Plot the forward kinematic
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

x1 = 0
y1 = 0
x2 = l1 * np.cos(theta1)
y2 = l1 * np.sin(theta1)
x3 = x2 + l2 * np.cos(theta1 + theta2)
y3 = y2 + l2 * np.sin(theta1 + theta2)

ax.plot([x1, x2, x3], [y1, y2, y3], marker="o")

st.pyplot()
