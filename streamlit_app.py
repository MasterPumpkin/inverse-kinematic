import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(theta1, theta2, theta3):
    l1 = 1
    l2 = 1
    l3 = 1
    
    x = l1*np.cos(theta1) + l2*np.cos(theta1+theta2) + l3*np.cos(theta1+theta2+theta3)
    y = l1*np.sin(theta1) + l2*np.sin(theta1+theta2) + l3*np.sin(theta1+theta2+theta3)
    
    return x, y

def inverse_kinematics(x, y):
    l1 = 1
    l2 = 1
    l3 = 1
    
    D = (x**2 + y**2 - l1**2 - l2**2 - l3**2)/(2*l2*l3)
    theta3 = np.arctan2(np.sqrt(1-D**2), D)
    theta2 = np.arctan2(y, x) - np.arctan2(l3*np.sin(theta3), l1+l2*np.cos(theta3))
    theta1 = np.arctan2(y-l2*np.sin(theta2)-l3*np.sin(theta2+theta3), x-l2*np.cos(theta2)-l3*np.cos(theta2+theta3))
    
    return theta1, theta2, theta3

def main():
    st.title('3 DOF Robotic Arm Inverse Kinematics')

    theta1 = st.slider('Theta 1', 0.0, 360.0, 0.0)
    theta2 = st.slider('Theta 2', 0.0, 360.0, 0.0)
    theta3 = st.slider('Theta 3', 0.0, 360.0, 0.0)

    x, y = forward_kinematics(theta1, theta2, theta3)

    st.write('End effector position: ({}, {})'.format(x, y))

    x_target = st.slider('Target X', -3.0, 3.0, 0.0)
    y_target = st.slider('Target Y', -3.0, 3.0, 0.0)

    theta1, theta2, theta3 = inverse_kinematics(x_target, y_target)

    st.write('Joint angles: Theta 1: {}, Theta 2: {}, Theta 3: {}'.format(theta1, theta2, theta3))

    # Visualisation
    plt.figure()
    plt.plot([0, l1*np.cos(theta1), l1*np.cos(theta1) + l2*np.cos(theta1+theta2), x_target], 
             [0, l1*np.sin(theta1), l1*np.sin(theta1) + l2*np.sin(theta1+theta2), y_target], '-o')
    plt.xlim([-3, 3])
    plt.ylim([-3, 3])
    plt.title('3 DOF Robotic Arm')
    st.pyplot()
    

if __name__ == '__main__':
    main()
