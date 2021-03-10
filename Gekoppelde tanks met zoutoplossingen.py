import numpy
import matplotlib.pyplot

end_time = 90  # minuten
h = 1  # minutes
num_steps = int(end_time / h)  # aantal stappen
times = h * numpy.array(range(num_steps + 1))

x_volume = 100  # liter water
y_volume = 100  # liter water
x_zout = 0  # kg zout
y_zout = 20  # kg zout
zout_instroom = 0.2  # kg zout


# functie die de stoming door de pijpleidingen modeleert.
def pijpleiding(tank, zout, stroming):
    return zout / tank * stroming  # per minuut


def zoutoplossing_model():
    tank_x = numpy.zeros(num_steps + 1)
    tank_y = numpy.zeros(num_steps + 1)

    tank_x[0] = x_zout
    tank_y[0] = y_zout

    for stap in range(num_steps):

        tank_x[stap + 1] = tank_x[stap] + (zout_instroom * 6 + pijpleiding(y_volume, tank_y[stap], 1)) \
                           - (pijpleiding(x_volume, tank_x[stap], 3) + pijpleiding(x_volume, tank_x[stap], 4))

        tank_y[stap + 1] = tank_y[stap] + (pijpleiding(x_volume, tank_x[stap], 3)) \
                           - (pijpleiding(y_volume, tank_y[stap], 1) + pijpleiding(y_volume, tank_y[stap], 2))

    return tank_x, tank_y


def plot_me():
    s_plot = matplotlib.pyplot.plot(times, x, label='tank X')
    i_plot = matplotlib.pyplot.plot(times, y, label='tank Y')
    matplotlib.pyplot.legend(('tank X', 'tank Y'), loc='upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('tijd in minuten')
    axes.set_ylabel('kg zout')
    matplotlib.pyplot.xlim(xmin=0.)
    matplotlib.pyplot.ylim(ymin=0.)
    matplotlib.pyplot.show()


x, y = zoutoplossing_model()
plot_me()