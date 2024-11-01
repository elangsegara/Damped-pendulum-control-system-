import control as ct
import matplotlib.pyplot as plt
import numpy as np
from math import sin

s = ct.TransferFunction.s
# System parameters
m = 0.5
l = 1
k = 0.5
J = m*l*l
g = 9.81
pi = np.pi
theta = np.pi/2

dtheta = 0
ddtheta= (-k * dtheta + m * g * l * (theta - np.pi / 2)) / J
# Non-linear system:
# tau = J*ddtheta + k*dtheta + m*g*l*sin(theta)
# Linearised system in theta = pi/2:
# tau = J*ddtheta + k*dtheta - m*g*l*theta

# Transfer function
P = 1/(J*s**2 + k*s - m*g*l)

# Plot root-locus of P
plt.figure()
ct.root_locus(P)

# Controller transfer function - lead-lag
Tc = 0.5
z = -3
K = 4
C = K*(s-z)/(Tc*s+1)

# Close-loop transfer function
G = ct.feedback(C*P, 1)

# Plot root-locus of C*P
plt.figure()
ct.root_locus(C*P)

# Plot Nyquist diagram
plt.figure()
ct.nyquist_plot(C*P)

# Ideal step response
t, yout = ct.step_response(G)
plt.figure()
plt.plot(t, yout)
plt.grid()
plt.xlabel("Time [s]")

#print tau for linear and non-linear systems

# print(tau)
# Show plots
plt.show()