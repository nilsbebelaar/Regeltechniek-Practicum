"""
Created on 10-05-2023

@author: Mark Schelbergen
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle, FancyArrow
import numpy as np


def simulate_and_animate_results(Kp, Kd, simulation_time=3., mass=1., setpoint=1):
    """Simulate and animate the response of a PD-controlled floating mass. Assign the return value to a variable and
    use pyplot's show() function to render the animation.

        Args:
            simulation_time (float): Duration of simulation in seconds.
            Kp (float): Proportional gain of controller.
            Kd (float): Derivative gain of controller.
            mass (float): Mass of floating mass in kilograms.
            setpoint (float): Value of the step function which acts as reference input to the system.

            Returns:
                FuncAnimation: Animation object which should be assigned to variable to show the animation.

    """
    time = np.linspace(0, simulation_time, 1000)
    position, force = solve_motion_floating_mass(time, Kp, Kd, mass, setpoint)
    return animate_simulation_results(time, position, force, setpoint, "$K_p$={}, $K_d$={}".format(Kp, Kd))


def solve_motion_floating_mass(t, Kp, Kd, mass=1., setpoint=1):
    n = len(t)
    if isinstance(setpoint, (int, float)):
        setpoint = np.ones(n-1) * setpoint
    x = np.zeros(n)
    dx = np.zeros(n)
    forces = np.zeros(n-1)
    last_err = 0
    for i in range(n-1):
        dt = t[i+1] - t[i]
        err = setpoint[i] - x[i]
        derr = (err - last_err)/dt
        forces[i] = Kp*err + Kd*derr
        ddx = forces[i] / mass
        dx[i+1] = dx[i] + ddx*dt
        x[i+1] = x[i] + dx[i+1]*dt

        last_err = err
    return x, forces


def animate_simulation_results(time, position, controlled_force, setpoint, plot_title='Simulation'):
    dt = time[1] - time[0]
    assert np.all(np.abs(np.diff(time) - dt) < 1e-4), "Time step in simulation results needs to be constant."
    scale_force_magnitude = 2e-2

    # Setup Figure:
    fig, ax = plt.subplots(3, 1, figsize=[6.4, 6.4])
    plt.subplots_adjust(hspace=.35, top=.95)
    ax[0].set_title(plot_title)
    for a in ax:
        a.grid()
    min_lim = -5
    max_lim = 5
    ax[0].axis('equal')
    ax[0].set_xlim([min_lim, max_lim])
    # ax[0].set_ylim([min_lim, max_lim])
    ax[0].set_xlabel('y [m]')
    ax[0].set_ylabel('z [m]')

    ax[1].set_xlim([0, time[-1]])
    ax[1].set_ylim([0, max([2]+list(position))])
    ax[1].set_ylabel('y [m]')
    ax[1].tick_params(labelbottom=False)
    ax[2].sharex(ax[1])
    ax[2].set_ylim([min([-500] + list(controlled_force)), max([500] + list(controlled_force))])
    ax[2].set_ylim([-500, 500])
    ax[2].set_ylabel('Force [N]')
    ax[2].set_xlabel('Time [s]')

    # Setup Animation Writer:
    FPS = 20
    interval_ms = int(1000 / FPS)
    sample_rate = int(1 / (dt * FPS))  # Plot every nth sample = interval/dt
    if not sample_rate:
        sample_rate = 1

    # Initialize moving objects
    y_offset = 0  # The Y Location of where the Cart and Pole are connected
    width = 1  # Width of Cart
    height = width / 2  # Height of Cart
    xy_cart = (position[0] - width / 2, y_offset - height / 2)  # Bottom Left Corner of Cart
    rect = Rectangle(xy_cart, width, height, color='cornflowerblue')  # Rectangle Patch
    ax[0].add_patch(rect)  # Add Patch to Plot

    arr = FancyArrow(position[0] + width/2, 0, controlled_force[0]*scale_force_magnitude, 0, width=.1, length_includes_head=True, color='green', ec='None')
    ax[0].add_patch(arr)  # Add Patch to Plot
    ax[0].scatter([], [], marker=r'$\rightarrow$', label='Control input', color='green', s=200)  # dummy scatter to add an arrow to the legend

    setpoint_line = ax[0].axvline(0, color='grey', ls='--', label='Setpoint')

    # Draw the Ground:
    ground = ax[0].hlines(-height / 2, min_lim, max_lim, colors='black')
    height_hatch = 0.25
    width_hatch = max_lim - min_lim
    xy_hatch = (min_lim, y_offset - height / 2 - height_hatch)
    ground_hatch = Rectangle(xy_hatch, width_hatch, height_hatch, facecolor='None', linestyle='None', hatch='/')
    ax[0].add_patch(ground_hatch)

    ax[0].legend(loc=2)

    line_position = ax[1].plot([], [], color='cornflowerblue')[0]
    marker_position = ax[1].plot([], [], 's', ms=8, color='cornflowerblue', mfc='None')[0]
    line_force = ax[2].plot([], [], color='green')[0]
    marker_force = ax[2].plot([], [], 's', ms=8, color='green', mfc='None')[0]

    def update_plot(i):
        i *= sample_rate

        setpoint_line.set(xdata=np.array([setpoint, setpoint]))

        # Update Cart Patch:
        rect.set(xy=(position[i] - width/2, y_offset - height/2))
        if controlled_force[i] > 0:
            arr_x = position[i] + width/2
        else:
            arr_x = position[i] - width/2
        if abs(controlled_force[i]) > 10:
            arr_head_length = 4.5 * arr._width
        else:
            arr_head_length = 0
        arr.set_data(x=arr_x, dx=controlled_force[i]*scale_force_magnitude, head_length=arr_head_length)

        line_position.set_data(time[:i+1], position[:i+1])
        marker_position.set_data([time[i]], [position[i]])
        line_force.set_data(time[:i+1], controlled_force[:i+1])
        marker_force.set_data([time[i]], [controlled_force[i]])

        return rect, arr

    return animation.FuncAnimation(fig, update_plot, frames=len(time)//sample_rate, interval=interval_ms)  #, repeat=False)


if __name__ == '__main__':
    t = np.linspace(0, 3, 100)
    x, f = solve_motion_floating_mass(t, 100, 0)
    anim_p = animate_simulation_results(t, x, f, 1)
    plt.show()
