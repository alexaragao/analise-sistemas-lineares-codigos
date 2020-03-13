import numpy  as np
import matplotlib.pyplot as plt

class EdoLinearPrimeiraOrdem():
  def __init__(self, a: float, b: float):
    self.a = a
    self.b = b
    self.n = np.arrange(10)
    self.p0 = 0
  
  def plot_config(self, n=10, p0=0):
    self.n = np.arange(n)
    self.p0 = 0
  
  def getFunc(self):
    c = self.p0 - self.b/self.a
    return np.array(-self.b/self.a + c*np.exp(a*(n*t)))

def plot(edo: object):
  plt.stem(edo.n, edo.getFunc(), use_line_collection=True)
  plt.show()

edo = EdoLinearPrimeiraOrdem(3, 2)
edo.plot_config(n=5)
plot(edo)