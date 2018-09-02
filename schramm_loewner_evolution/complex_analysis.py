import numpy as np


def cayley_to_upper(z):
    #
    # Compute the image of z via the Cayley map into the uper half plane.
    # 
    # Input:
    #   z: complex number (most likely, in the unit disk)
    # 
    # Output:      
    #   w       : complex number (in the upper half plane)
    #
    return 1j*(1.0+z)/(1.0-z);


def cayley_from_upper(z):
    #
    # Compute the image of z via the Cayley map from the uper half plane into the unit disk.
    # 
    # Input:
    #   z       : complex number (most likely, in the upper half plane)
    # 
    # Output:    
    #   w       : complex number (in the unit disk);
    #
    return (z-1j)/(z+1j);


def moebius_transformation(z,a,b,c,d):
    #
    # Compute the image of z via the Moebius transformation defined by the real paramters a,b,c,d.
    # 
    # Input:
    #   z       : complex number 
    #   a,b,c,d : parameters such a*b-c*d!=0
    # 
    # Output:    
    #   w       : complex number
    #
    if a*b-c*d==0 :
        raise ValueError("In order to be a proper Moebius Transformaion, it must be a*b-c*d!=0");
    else:
        return (a*z-b)/(c*z+d);


def moebius_unit_disk(z,theta=np.pi, a=np.complex(0,0)):
    #
    # Compute the image of z via the Moebius transformation which is an automorphism of the unit disk.
    # 
    # Input:
    #   z       : complex number (most likely, in the unit disk) 
    #   theta   : angle of rotation 
    #   a       : point of the unit disk such that 0-->a
    # 
    # Output:    
    #   w       : complex number (in the unit disk)
    #
    return np.exp(1j*theta*np.pi)*(z-a)/(1-np.conjugate(a)*z);


def moebius_upper_half_plane(z,a,b,c,d):
    #
    # Compute the image of z via the Moebius transformation which is an automorphism of the unit disk.
    # 
    # Input:
    #   z       : complex number (most likely, in the upper half plane) 
    #   theta   : angle of rotation 
    #   a,b,c,d : real parameters such that a*b-c*d>0
    # 
    # Output:    
    #   w       : complex number (in the upper half plane)
    #
    if not a*b-c*d>0 :
        raise ValueError("In order to be a proper Moebius Transformaion, it must be a*b-c*d!=0");
    else:
        return (a*z-b)/(c*z+d);

    
def principal_sqrt(x):
    #
    # Compute the principal squareroot of the real number x.
    # 
    # Input:
    #   x       : a real number
    # 
    # Output:    
    #   y       : a real number
    #   
    if np.any(np.angle(x) > 0): 
        return np.exp(1j * np.angle(x) / 2) * np.sqrt(np.sqrt(np.real(x)**2 + np.imag(x)**2));
    else:
        return np.exp(1j * (np.angle(x)+2*np.pi) / 2) * np.sqrt(np.sqrt(np.real(x)**2 + np.imag(x)**2));