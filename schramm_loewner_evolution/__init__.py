#!/usr/bin/env python
#
# Schramm-Loewner Evolution Library
# https://github.com/andrea-dm/schramm-loewner-evolution
#
# Copyright (c) 2016-2021 Andrea del Monaco and Sebastian Schleissinger
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


__name__    = "Schramm-Loewner-Evolution-Library";
__version__ = "0.0.1";
__author__  = "Andrea del Monaco; Sebastian Schleissinger";

import complex_analysis
from .multiple import *


'''
--------------------
References:
--------------------
Kennedy, T., "Numerical Computations for the Schramm-Loewner Evolution", J Stat Phys (2009) 137: 839. doi:10.1007/s10955-009-9866-2
del Monaco, A. and Schleissinger, S., "Multiple SLE and the complex Burgers equation". Math. Nachr. (2016), 289: 2007–2018. doi: 10.1002/mana.201500230
--------------------
'''