import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Define the length of each arm segment
L1 = 1
L2 = 0.5
L3 = 0.25

# Define the initial position of the end-effector
p0 = np.array([0, 0])

# Define the forward kinematics function
def forward_kinematics(theta1, theta2, theta3):
    p1 = np.array([L1 * np.cos(theta1), L1 * np.sin(theta1)])
    p2 = p1 + np.array([L2 * np.cos(theta1 + theta2), L2 * np.sin(theta1 + theta2)])
    p3 = p2 + np.array([L3 * np.cos(theta1 + theta2 + theta3), L3 * np.sin(theta1 + theta2 + theta3)])
    return p3

# Define the inverse kinematics function
def inverse_kinematics(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    theta1 = np.arctan2(y, x)
    A = L2 + L3 * np.cos(np.pi - np.arccos((L1 ** 2 + r ** 2 - L2 ** 2 - L3 ** 2) / (2 * L1 * r)))
    B = L3 * np.sin(np.pi - np.arccos((L1 ** 2 + r ** 2 - L2 ** 2 - L3 ** 2) / (2 * L1 * r)))
    theta2 = np.arctan2(B, A)
    theta3 = np.pi - np.arccos((A ** 2 + B ** 2 - L2 ** 2 - L3 ** 2) / (2 * L2 * L3))
    return theta1, theta2, theta3

# Define the Streamlit app
st.title('3 DOF Robotic Arm Inverse Kinematics')
x = st.slider('X-coordinate', -2.0, 2.0, 1.0, 0.1)
y = st.slider('Y-coordinate', -2.0, 2.0, 1.0, 0.1)

theta1, theta2, theta3 = inverse_kinematics(x, y)
p = forward_kinematics(theta1, theta2, theta3)

# Define the Pyplot visualization
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.plot([0, p[0]], [0, p[1]], 'r-', linewidth=2)
ax.plot(p[0], p[1], 'ro', markers)

st.pyplot(fig)
