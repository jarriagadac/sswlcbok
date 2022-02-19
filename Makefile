# makefile

bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)

build:
	sphinx-build -b html docs/source/ docs/build/html
