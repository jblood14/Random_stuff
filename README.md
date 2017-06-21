# Random_stuff
These are just a few random codes I have thrown together for anybody interested in using Python to solve somewhat interesting maths problems.

Feel free to contact me to suggest improvements or to discuss anything.

The notebook on simultaneous equations is more of a tutorial than anything else.
It is possible, of course, to solve simultaneous equations using sympy. My first test suggested that my function using numpy is approximately twice as fast. Admittedly this is for 4 unknowns and my code is 5 ms vs sympy which was 10 ms (the algebraic method is about 14 ms). I will be interested to see how this scales with size, but I have not yet tested it. It should also be noted that numpy does have a specific linalg.solve(a,b) function, which gives a similar result to the code I have used for explanation purposes in terms of speed (with a 4 variable system of equations). Once again further testing with a larger number of equations is necessary.
