import matplotlib.pyplot as plt
import numpy as np

def rotation(x, alpha):
    """
    Defines a circle rotation by alpha.
    
    @param x the point being rotated
    @param alpha the angle to rotate by.
    """
    return (x + alpha) % 1

def plot(alpha):
    domain = list(np.linspace(0.0, 1.0, 100000))
    image = [(x + alpha) % 1 for x in domain]
    plt.plot(domain, image)
    plt.show()

if __name__ == "__main__":
    alpha = float(input("Enter a rotation value:"))
    plot(alpha)
