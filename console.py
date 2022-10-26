#!/usr/bin/python3
"""This module is the package entry point"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point for the console"""

    prompt = "(hbnb) "

    def do_EOF(self):
        """Implement the EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        "quit"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
