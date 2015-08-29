
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass


clc
plt.close(all)
clear(all)
#% ========== init some variables:
iteration = 176.
fs = 10000.
t = np.arange(-1., (1.)+(1./fs), 1./fs)
iterationSteps = np.arange(1., (iteration)+(1.), 1.)
crossCorrelation = np.zeros(1., iteration)
convolution = np.zeros(1., iteration)
set(plt.gcf, 'Color', np.array(np.hstack((1., 1., 1.))))
#% ========== plot two signals (y1 and y2):
np.disp('Let y1 and y2 to be defined as following figures:')
np.disp('============================================================')
y1 = rectpuls(t, 1.)
y2 = tripuls(t, 0.5, (-1.))
plt.subplot(4., 2., 1.)
plt.plot(t, y1, 'Color', 'blue', 'LineWidth', 2.)
plt.axis(np.array(np.hstack((-1., 1., -0.2, 1.2))))
plt.ylabel('y1')
plt.subplot(4., 2., 2.)
plt.plot(t, y2, 'Color', 'red', 'LineWidth', 2.)
plt.axis(np.array(np.hstack((-1., 1., -0.2, 1.2))))
plt.ylabel('y2')
np.disp('Press Enter to continue ....')
pause
#% ========== cross correlation of two signals (y1 and y2):
np.disp(' ')
np.disp(' ')
np.disp('Cross Correlation of two signals (y1 and y2):')
np.disp('============================================================')
for i in np.arange(1., (iteration)+1):
    moveStep = (i-100.)/100.
    y1 = rectpuls(t, 1.)
    y2 = tripuls((t-moveStep), 0.5, (-1.))
    plt.subplot(4., 2., np.arange(3., 5.0))
    plt.hold(off)
    plt.plot(t, y1, 'Color', 'blue', 'LineWidth', 2.)
    plt.axis(np.array(np.hstack((-1., 1., -0.2, 1.2))))
    plt.hold(on)
    plt.plot(t, y2, 'Color', 'red', 'LineWidth', 2.)
    plt.axis(np.array(np.hstack((-1., 1., -0.2, 1.2))))
    crossCorrelation[int(i)-1] = np.sum((y1*y2))
    plt.subplot(4., 2., np.arange(5., 7.0))
    plt.hold(off)
    plt.plot(iterationSteps[0:i], crossCorrelation[0:i], 'Color', 'black', 'LineWidth', 2.)
    plt.axis(np.array(np.hstack((1., iteration, -100., 3.1e3))))
    plt.xlabel('t')
    plt.ylabel('CrossCorrelation(y1, y2)(t) ')
    pause(0.05)
    
np.disp('Press Enter to continue ....')
pause
#% ========== convolution of y1 and y2:
np.disp(' ')
np.disp(' ')
np.disp('Convolution of two signals (y1 and y2):')
np.disp('============================================================')
for i in np.arange(1., (iteration)+1):
    moveStep = (i-100.)/100.
    y1 = rectpuls(t, 1.)
    y2 = tripuls((-(t-moveStep)), 0.5, (-1.))
    plt.subplot(4., 2., np.arange(3., 5.0))
    plt.hold(off)
    plt.plot(t, y1, 'Color', 'blue', 'LineWidth', 2.)
    plt.axis(np.array(np.hstack((-1., 1., -0.2, 1.2))))
    plt.hold(on)
    plt.plot(t, y2, 'Color', 'red', 'LineWidth', 2.)
    plt.axis(np.array(np.hstack((-1., 1., -0.2, 1.2))))
    convolution[int(i)-1] = np.sum((y1*y2))
    plt.subplot(4., 2., np.arange(7., 9.0))
    plt.hold(off)
    plt.plot(iterationSteps[0:i], convolution[0:i], 'Color', 'black', 'LineWidth', 2.)
    plt.axis(np.array(np.hstack((1., iteration, -100., 3.1e3))))
    plt.xlabel('t')
    plt.ylabel('(y1 * y2)(t) ')
    pause(0.05)
    