import numpy                                as np
import schramm_loewner_evolution.multiple   as msle
import matplotlib.pyplot                    as plt


if __name__ == '__main__':
   
    plt.style.use('seaborn-darkgrid')

    result = msle.burgers(np.linspace(0, 1, 1000), 1000)

    plt.plot(result.real, result.imag, lw=1)

    ax = plt.gca()
    ax.set_title('Multiple SLE driving functions')
    ax.set_xlabel('Re$(\gamma_k(t))$', fontsize='xx-large')
    ax.set_ylabel('Im$(\gamma_k(t))$', fontsize='xx-large')
    ax.fill_between(result.real, result.imag)
    ax.set_alpha(0.0)

    plt.show()
