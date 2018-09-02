import numpy                                as np
import matplotlib.pyplot                    as plt
import schramm_loewner_evolution.multiple   as msle

if __name__ == '__main__':

    plt.style.use('seaborn-darkgrid')

    slits = 10;
    x0 = np.random.uniform(-0.01,0.01,slits);
    print(x0)

    t  = np.linspace(0.0, 50.0, 50000);
    u  = msle.multiple_driving_functions(x0, t, kappa=2.618);
    z  = msle.multiple_slits(t,*u);

    for slit in range(0, len(z), 1): 
        plt.plot(z[slit][:].real, z[slit][:].imag, lw=0.5);
    
    ax = plt.gca();
         
    ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False);
    ax.grid(alpha=0.5);

    fig = plt.gcf();
    fig.patch.set_alpha(0.0);
    fig.patch.set_antialiased(True);

    plt.show()
