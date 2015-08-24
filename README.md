# parameterlist
pass a parameter from a parameter list one time only.

## Problem to be solved

Often a problem can be solved by running a program many times, each
time using a different set of parameters. Examples are NLP tasks that
annotate a lot of texts, or algorithms that perform a search in a vast
multi-dimensional space. In a loop, the program takes a set of
parameters and performs the calculation. To save time, the task can be
paralellised. In that case, many parallel processes perform the
loop. The problem is, that it may not happen that two processes
perform the compilation on the same set of parameters. Each
parameterset must be passed one time only to one of the processes.

## Description of the solution

This package contains a webservice that reads a list of paramersets
and responds a parameterset to an HTTP request. 

