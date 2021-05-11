# Makefile-based build system of the prototypes
# Angelo Battaglia, April 2021

# I'll call the executable as output

# Clean pycache
clean:
		find . -name '*.pyc' -exec rm --force {} +
		find . -name '*.pyo' -exec rm --force {} +
		name '*~' -exec rm --force  {}

Python:
		python3 SimulatedAnnealing.py

Julia: SimulatedAnnealing.jl
		julia SimulatedAnnealing.jl

