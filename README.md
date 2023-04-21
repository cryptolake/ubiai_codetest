# Containarized webapp with auto reload and helpful shell

## How to start it:

Do `./run.py` and you will enter an interactive shell for dealing with the compose
interface, type `start` and press enter and the services will start, type `help`
to see all the available commands.

## Why this approach?

This is the most robust approach in which the automatic reloading and checking is handled by docker
compose, the webapp can access aws using the keys in the aws file this a good layer of security so
if the code leaks for example there's less chance of the keys to leak as they are handled on their 
own file and can be even more secured (encryption, keymanagement), furthermore docker compose
offers a nice syntax and plenty of commands to interacte with the services! Note: this can be
more expanded by the use docker desktop.

## Role of python script:

The `run.py` script offers a nicer way to interact with docker compose especially the logging
and monitoring and it also offers a solid base to build more helpful commands (render graphs of the runtime, detailed logging etc.)
