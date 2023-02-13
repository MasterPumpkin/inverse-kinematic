import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

L1, L2, L3 = 1, 1, 1 # Length of each link of the robot

def forward_kinematic(theta1, theta2, theta3):
    """
    Calculates the forward kinematics of the 3DOF robotic arm
    """
    x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2) + L3 * np.cos(theta1 + theta2 + theta3)
    y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2) + L3 * np.sin(theta1 + theta2 + theta3)
    return x, y

def inverse_kinematic(x, y):
    """
    Calculates the inverse kinematics of the 3DOF robotic arm
    """
    theta1 = np.arctan2(y, x)
    x_ = np.sqrt(x**2 + y**2) - L3
    c2 = (x_**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    s2 = np.sqrt(1 - c2**2)
    theta2 = np.arctan2(s2, c2)
    theta3 = np.arctan2(y, x_) - np.arctan2(L2 * s2, L1 + L2 * c2)
    return theta1, theta2, theta3

def plot_robot(theta1, theta2, theta3):
    """
    Plots the robot using the forward kinematics
    """
    x1 = 0
    y1 = 0
    x2 = L1 * np.cos(theta1)
    y2 = L1 * np.sin(theta1)
    x3 = x2 + L2 * np.cos(theta1 + theta2)
    y3 = y2 + L2 * np.sin(theta1 + theta2)
    x4 = x3 + L3 * np.cos(theta1 + theta2 + theta3)
    y4 = y3 + L3 * np.sin(theta1 + theta2 + theta3)
    
    plt.plot([x1, x2, x3, x4], [y1, y2, y3, y4], 'o-', markersize=10)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    st.title("3DOF Robotic Arm Inverse Kinematics")

    x = st.slider("End-effector x position", -2, 2, 1)
    y = st.slider("End-effector y position", -2, 2, 1)

    theta1, theta2, theta3 = inverse_kinematic(x, y)
    st.write("Joint angles (in radians):")
    st.write("Theta 1: ", theta1)
    st.write("Theta 2: ", theta2)
    st.write("Theta 3: ", theta3)

    if st.button("Visualize"):
        plot_robot(theta1, theta2, theta3)

if __name__ == "__main__": 
	main()
