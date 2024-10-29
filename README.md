# Damped-pendulum-control-system-
This code plots graphs from a transfer function of a control system of a damped pendulum, which the graphs to be plotted are the root locus, step-response, and the Nyquist plot

**Experimentation Results:

From the damped pendulum system with the initial values for each variable of the code, for which the m is 0.5, l is 1, k is 0.5 From the values,  it is found that the system is stable, which is indicated by the root locus graph, which the plot is on the left side of the graph, and the Nyquist plot, which not encircled the points (-1,0)

The experimentation shows that the system has decreased stability if the mass of the ball increases more than 0.61 kg, while other values of the variables remain constant. The instability of the system is shown with the step response graph showing a rising exponential graph, and the Nyquist plot encircled the point right of the critical point, indicating less stability. To keep the system stable from the system aspect, the length of the wire of the pendulum is reduced. 

Meanwhile, when the mass of the system is reduced, the wire length needs to be increased to maintain the stability of the system.

On the controller transfer function aspect, when the time constant of the system increases, the system oscillates around 30 seconds, which indicates that the system is underdamped. 

Meanwhile, when the z constant of the controller function is closer to zero or with a positive value, the step response graph shows the rising exponential of the response, which indicates that the system becomes unstable. However, when the z constant becomes more distant than zero, the state of the system becomes underdamped, with the step response having more oscillations when the value of the z constant becomes farther than zero.

On the other hand, when the gain constant K decreases to 1, the system becomes less stable, with the step-response graph showing a rising exponential, and the Nyquist plot point encircled a point to the right of the critical point (-1,0). Meanwhile, when the gain constant K increases, the step response graph shows oscillations with smaller periods, which indicates that the system is underdamped.

**
