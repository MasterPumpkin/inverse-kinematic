import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

def inverse_kinematics(x, y, z, L1, L2):
    theta1 = np.arctan2(y, x)
    theta2 = np.arccos((L1**2 + L2**2 - x**2 - y**2)/(2*L1*L2))
    theta3 = np.arctan2(np.sqrt(1 - ((L1**2 + L2**2 - x**2 - y**2)/(2*L1*L2))**2), ((L1 + L2*np.cos(theta2))*z - L2*np.sin(theta2)*np.sqrt(x**2 + y**2))/(L1**2 + 2*L1*L2*np.cos(theta2) + L2**2))
    return [theta1, theta2, theta3]
  
def main():
    st.title("3 DOF Robotic Arm Inverse Kinematics")

    # Set the default values for the end-effector position and arm lengths
    x = st.sidebar.slider("X", -10, 10, 5)
    y = st.sidebar.slider("Y", -10, 10, 5)
    z = st.sidebar.slider("Z", -10, 10, 5)
    L1 = st.sidebar.slider("L1", 1, 10, 5)
    L2 = st.sidebar.slider("L2", 1, 10, 5)

    # Calculate the joint angles using inverse kinematics
    angles = inverse_kinematics(x, y, z, L1, L2)

    # Plot the arm configuration
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

	  # Define the arm segments
    arm_segments = np.array([[0, 0, 0], [L1*np.cos(angles[0]), L1*np.sin(angles[0]), 0], [L1*np.cos(angles[0]) + L2*np.cos(angles[1] + angles[0]), L1*np.sin(angles[0]) + L2*np.sin(angles[1] + angles[0]), L2*np.sin(angles[2])]])

  	# Plot the arm segments
    ax.plot(arm_segments[:, 0], arm_segments[:, 1], arm_segments[:, 2], color="blue")

  	# Set the limits of the plot
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_zlim([0, 20])

  	# Set the labels for the axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

  	# Show the plot
    st.write(fig)

if __name__ == "__main__": 
	main()
