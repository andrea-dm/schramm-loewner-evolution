import sdeint               
import complex_analysis 
import numpy            as np
import numexpr          as ne

from typing             import Type, List, NoReturn, Union, Dict


RealNumber    = Union[np.float16, np.float32, np.float64, float];
ComplexNumber = Union[np.complex64, np.complex128];


def vslit_zip(z:Union[ComplexNumber,Type[np.ndarray]], dt:RealNumber, u:RealNumber) -> Union[ComplexNumber,Type[np.ndarray]]:
    #
    # Discretization of Chordal Loewner chains.
    # This function is the inverse of the solution to the Chordal Loewner Equation with driving function
    #   U(t) = du
    # where t runs in [0,dt].
    # Notice that it maps the origin to the point w = du + 2j * dt**0.5.
    #
    return ne.evaluate("1j * sqrt(4 * dt - (z-u) ** 2) + u")


def multiple_slits(t:Type[np.ndarray], *driving_fncs:Type[np.ndarray]) -> Type[np.ndarray]:
    #
    # Compute the discretized Loewner trace of a multiple SLEs with prescribed driving functions, 
    # which are sampled at discrete time instants.
    # The trace is defined as the union z(t) of curves z_i(t) such that
    #   z(t) = f_1(t, u_1(t)) + ... + f_n(t, u_n(t))
    # where f_i(t, w) is the inverse of g_i(t, w), which is the solution to the chordal Loewner Equation
    #
    #   dg_i            2
    #  ------ = ------------------ 
    #    dt     g_i(t, w) - u_i(t)
    # 
    #
    # Input:
    #   t            : 1d ndarray of floats
    #   driving_fncs : n 1d ndarrays of floats
    # 
    # Output:    
    #   z            : list of n 1d ndarray of complex
    #
    nsteps = len(t);
    #if n driving functions are given, use them!
    if driving_fncs:
        nslits = len(driving_fncs);
        u = np.array(driving_fncs);
    #else, just use a constant one!
    else :
        nslits = 1;
        u = np.zeros(nsteps);        
    #initializing the trace array...
    z = np.empty([nslits,nsteps], dtype=np.complex)
    for slit in range(0,nslits) :
        z[slit][:nsteps] += (u[slit][:nsteps]+0.000001j);
    #getting the trace...
    for step in range(nsteps-1, 0, -1):
        dt = (t[step] - t[step-1]) / nslits              
        for slit1 in range(0, nslits, 1): 
            for slit2 in range(0, nslits, 1): 
                z[slit2][step:] = vslit_zip(z[slit2][step:], dt, u[slit1][step]);
    #done!
    return z[:]


def single_slit(t:Type[np.ndarray], u:Type[np.ndarray]) -> Type[np.ndarray]:
    #
    # Compute the discretized Loewner trace of a one slit with prescribed driving function, 
    # which are sampled at discrete time instants. 
    #
    # Input:
    #   t       : 1d ndarray of floats
    #   u       : 1d ndarrays of floats
    # 
    # Output:    
    #   z       : 1d ndarray of complex
    #
    z = multiple_slits(t,u)
    return z[0][:]
    

def multiple_driving_functions(x0:RealNumber, t:RealNumber, kappa:RealNumber=1.0) -> List[RealNumber]:
    #number of slits: it will be the number of starting points
    nslits = len(x0);
    #nslits independent Brownian motions with scaling factor kappa
    B = np.diag(np.zeros(nslits, dtype=np.complex) + np.sqrt(kappa/nslits));
    #defining the equation...
    def f(x, t):
        res = np.zeros(nslits, dtype=np.complex)
        for k in range(0, nslits):
            for m in range(0, nslits):
                if k != m:
                    res[k] += 2/(x[k]-x[m]) #res = [ res[k]+2/(x[k]-x[m]) for k in range(0, Nslits) for m in range(0, Nslits, 1) if k!=m 
        return res;
    #solving the SDE
    result = sdeint.itoint(f, lambda x,t : B, x0, t);    
    #returning the nslits driving functions
    return [list(i) for i in zip(*result)];


def driving_function(sample_size:int,
                     dt:RealNumber,
                     x0:RealNumber=1.0,
                     method:str='BM',
                     mu:RealNumber=0.0,
                     sigma:RealNumber=1.0,
                     kappa:RealNumber=1.0) -> Union[NoReturn,Union[RealNumber,List[RealNumber]]]:
    if method=='BM':
        U = np.cumsum( np.sqrt(dt*kappa)*np.random.standard_normal(size=sample_size) );
        U += x0;
    elif method=='GBM':
        U = x0 * np.exp( np.cumsum( (mu - 0.5*sigma**2)*dt  + sigma*np.sqrt(dt*kappa)*np.random.standard_normal(size=sample_size),  axis=0 ) );
        U[0] = x0;
    else :
        raise ValueError(f"no such method as {method}")
    return U


def burgers(t:Type[np.ndarray], N:int) -> Type[np.ndarray]:
    #
    # Compute the bla bla bla 
    #
    # Input:
    #   t
    #   N
    # 
    # Output:    
    #   output
    #
    B = np.diag([0]); # diagonal, so independent Brownian motions
    T = t[-1];
    result = [];

    def f(x, t):
        res = np.sqrt(x**2-16*(T-t));
        return -4/(x+ res) if (res.imag > 0) else -4/(x- res);

    for j in range(0, N, 1):
        bremen = sdeint.itoint(f, lambda x,t : B, -5+10*j/N + 1j/1000, t);
        munich = bremen[-1];
        result.append(np.complex(munich[0]));

    output = np.empty(len(result), np.complex128);
    for i in range(len(result)) :
        output[i] = np.complex(result[i]);

    return output;