# Schramm-Loewner Evolution Library

**schramm_loewner_evolution** is a package that brings in Python the wonderful theory of Single and Multiple Schramm-Loewner Evolution!

<br />

## About
While staying at the Department of Mathematics of the University of Rome "Tor Vergata", Andrea del Monaco and Sebastian Schleissinger were working on behavior of multiple SLEs as the number of slits approches infinity.<br />
In order to confirm their guesses, they had the insight of implenting their results in a Python package. This allowed them to simulate such an evolution in many different contexts, and it validated empirically their ideas.<br />

They ended up with writing two papers (the second one in cooperation with Ikkei Hotta):

> - A.del Monaco and S.Schleißinger, *"Multiple SLE and the complex Burgers equation"*. Math. Nachr. (2016), 289: 2007–2018. [doi:10.1002/mana.201500230](doi:10.1002/mana.201500230)
> - A.del Monaco, I.Hotta, and S.Schleißinger, *"Tightness Results for Infinite-Slit Limits of the Chordal Loewner Equation"*. S. Comput. Methods Funct. Theory (2018) 18: 9. [doi:10.1007/s40315-017-0205-3](doi:10.1007/s40315-017-0205-3)

It is worth mentioning that the numerical methods for deterministic evolution are based on:

> - T.Kennedy, *"Numerical Computations for the Schramm-Loewner Evolution"*, J.Stat.Phys (2009) 137: 839. [doi:10.1007/s10955-009-9866-2](doi:10.1007/s10955-009-9866-2)


<br />


## Requirements
**schramm_loewner_evolution** has only been tested to work on `Python >= 3.6`<br />
and it depends on `numpy >= 1.15.1` and `numexpr >= 2.6.6`.<br />

Furthermore, the following packages are required:
- `sdeint >= 0.2.2-dev`

Any help to check compatibility with `Python == 2.x` is welcome and encouraged as well as very much appreciated!


<br />


## Change Log
 _Spring, 2016_ <br />
&nbsp;&nbsp; **Version 0.0.1** <br />
&nbsp;&nbsp;&nbsp;&nbsp; First release


