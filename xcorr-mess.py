from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as pp
#matplotlib inline

def xcorr(a, b, mode='same'):
    a = np.asarray(a)
    b = np.asarray(b)
    
    a = (a - a.mean()) / np.sqrt(np.correlate(a, a))
    b = (b - b.mean()) / np.sqrt(np.correlate(b, b))
    
    r = np.correlate(a, b, mode)
    
    lag_max = int(len(r) / 2)
    lags = np.asarray(xrange(-lag_max, lag_max + len(r) % 2))
    
    sl = 2 / np.sqrt(len(r))
    
    return r, lags, sl


def xcorr_sf(a, b, lag_max=None):
    a = np.asarray(a)
    b = np.asarray(b)
    assert len(a) == len(b)
    n = len(a)
    if lag_max == None:
        lag_max = n - 1
    assert lag_max >= 0 and lag_max < n
    lags = xrange(-lag_max, lag_max + 1)
    sl = np.zeros(len(lags)) # Significance level
    r = np.zeros(len(lags))
    for i in xrange(len(lags)):
        lag = lags[i]
        sl[i] = 2 / (np.sqrt(n - abs(lag)))
        a2 = a[:n - lag] if lag >= 0 else a[-lag:]
        a2 -= a2.mean()
        b2 = b[lag:]     if lag >= 0 else b[:lag]
        b2 -= b2.mean()
        r[i] = np.correlate(a2, b2) / np.sqrt(np.correlate(a2, a2) * np.correlate(b2, b2))
    return r, lags, sl


n=100
x=np.array(range(n))
a=np.random.normal(size=n)
b=np.random.normal(size=n)

r, lags, sl = xcorr(a, a)
pp.plot(lags, r)
pp.plot(lags, np.ones(len(lags)) * sl, color='r')
pp.plot(lags, np.ones(len(lags)) * -sl, color='r')
pp.show()

r, lags, sl = xcorr_sf(a, a, lag_max=int(len(a)/2))
pp.plot(lags, r)
pp.plot(lags, sl, color='r')
pp.plot(lags, -sl, color='r')
pp.show()