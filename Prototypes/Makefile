# Angelo Battaglia, 2021

all: Simulation

SHELL := /bin/bash
MAIN = Simulation.py
RESOURCES = Makefile\
		./simulazione\
            $(MAIN)\
            Classe.py\
            School.py\
            Subject.py\
            Teacher.py\
            GeneticAlgorithm.py\
            SimulatedAnnealing.py

Simulation: $(RESOURCES)
	python3 $(MAIN)

# Clean pycache
clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}

.PHONY: clean all
