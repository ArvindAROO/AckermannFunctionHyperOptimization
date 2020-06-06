# Hyper optimization of The Ackermann Function

Ackermann function is a recursive function which is used as an example
for the functions which can be solved only recursively and not iteratively


![function](https://github.com/ArvindAROO/AckermannFunctionHyperOptimization/blob/master/func.jpg)



That is because of the function's third case when none of the parameters is zero,
it calls itself with one of the parameters being the function itself

Sometimes for some languages like python, where recursion depth is fixed to 1000
Unless you use 'sys' module to alter it
This can never be achieved iteratively.

Hence the function will go recursively until the first parameter becomes zero.
There is a workaround for that, that is explained here

Since overtime the function sometimes calculates the same function with the exact same parameters,
we can just store the values for each corresponding parameters and hence avoid quite a number of recursions

To avoid runtime memory wastage, that will stored in a file externally
Once the function is called, regardless of the depth of iteration,
it will check the file if it already has the value,
if it does, it just uses that, or else it will calculate and also append the value to the file for future references

use `python ackermannOptimized.py` for the optimized code
and `python ackermannOriginal.py` for the legacy code

Thank you
