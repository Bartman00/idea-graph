import numpy as np
import numpy.typing as npt
from typing import Callable



def rk4(p: npt.NDArray[np.float64], 
        v: npt.NDArray[np.float64], 
        t: float, 
        dt: float, 
        forces: Callable) -> tuple[npt.NDArray[np.float64],
                                   npt.NDArray[np.float64],
                                   npt.NDArray[np.float64]]:
    """Perform runge-kutta 4 numberical integration

    Reference:
    https://www.physicsforums.com/threads/using-runge-kutta-method-for-position-calc.553663/#google_vignette
    Provides both position and velocity vectors in one call so this was used instead of scipy

    forces function will receive a time which allows for time dependent forces.

    Args:
        p (npt.NDArray[np.float64]): position vector
        v (npt.NDArray[np.float64]): velocity vector
        t (float): time at start of step
        dt (float): change in time over step
        forces (Callable): Function that takes 

    Returns:
        tuple[npt.NDArray[np.float64], npt.NDArray[np.float64], npt.NDArray[np.float64]]: 
        position, velocity, acceleration vectors at end of time step
    """

    # Input validation. Could be dry'd out a little
    if not isinstance(p, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    if not np.issubdtype(p.dtype, np.number):
        raise TypeError("p must contain numeric data.")
    if not isinstance(v, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    if not np.issubdtype(v.dtype, np.number):
        raise TypeError("p must contain numeric data.")
    if not isinstance(t, (int, float)):
        raise TypeError("t must be a number")
    if not isinstance(dt, (int, float)):
        raise TypeError("dtt must be a number")
    if not callable(forces):
        raise TypeError("forces must be a callable object.")

    # Acceleration at initial time
    p1, v1 = p, v
    a1 = forces(p1, v1, t)

    p2 = p + dt/2 * v1
    v2 = v + dt/2 * a1
    a2 = forces(p2, v2, t + dt/2)

    p3 = p + dt/2 * v2
    v3 = v + dt/2 * a2
    a3 = forces(p3, v3, t + dt/2)

    p4 = p + dt * v3
    v4 = v + dt * a3
    a4 = forces(p4, v4, t + dt)

    pret = p + dt/6 * (v1 + 2*v2 + 2*v3 + v4)
    vret = p + dt/6 * (v1 + 2*v2 + 2*v3 + v4)
    aret = forces(pret, vret, t+dt)

    return pret, vret, aret