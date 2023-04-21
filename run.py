#!/usr/bin/env python3
from datetime import datetime
from shutil import which
import cmd
import subprocess

if which('docker') is None:
    print("Please install docker: https://docs.docker.com/engine/install/")
    exit(1)

class DockerShell(cmd.Cmd):
    intro = "Manage your docker services."
    prompt = '-> '
    command = ['docker', 'compose']


    def do_start(self, arg):
        """
        Start the service/s.

        Usage: start <--build> <service>
        """
        command = DockerShell.command.copy()
        command.extend(['up', '-d'])
        args = arg.split()
        command.extend(args)
        output = self.run_command(command)
        if output != None:
            print(f"{output}\nServices started successfully!")

    def do_logs(self, arg):
        """
        Print logs of services.

        Usage: logs <service_name> <number_of_lines>
                            or
               logs <number_of_lines>
        """
        command = DockerShell.command.copy()
        command.extend(['logs', '-t'])
        args = arg.split()
        if len(args) == 0:
            output = self.run_command(command)
            if output is not None:
                output = output.split('\n')
                del output[-1]
                output = sorted(output, key=lambda x: datetime.fromisoformat(x.split()[2].split('.')[0]))
                print('\n'.join(output))
        else:
            if not args[0].isdigit():
                command.append(args[0])
                if len(args) >= 2:
                    nlines = int(args[1]) + 1
                else:
                    nlines = 0
            else:
                nlines = int(args[0]) + 1

            output = self.run_command(command)
            if output is not None:
                output = output.split('\n')
                del output[-1]
                output = sorted(output, key=lambda x: datetime.fromisoformat(x.split()[2].split('.')[0]))
                print('\n'.join(output[-nlines:-1]))

    def do_stop(self, arg):
        """
        Stop the service/s.

        Usage: stop
        """
        command = DockerShell.command.copy()
        command.append('down')
        output = self.run_command(command)
        if output is not None:
            print("Services stopped successfully.")

    def do_list(self, arg):
        """
        List the contiainers
        """
        command = DockerShell.command.copy()
        command.append('ps')
        output = self.run_command(command)
        if output is not None:
            if len(output.splitlines()) == 1:
                print("Services aren't started !!")
            else:
                print(output)


    def run_command(self, command):
        proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              check=False)
        if proc.returncode != 0:
            print(f"Command is unsuccessful, Error: {proc.stdout.decode('utf-8')}")
            return None

        else:
            return proc.stdout.decode('utf-8')

if __name__ == "__main__":
    DockerShell().cmdloop()
