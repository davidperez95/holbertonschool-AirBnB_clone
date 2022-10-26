#!/usr/bin/python3
"""This module is the package entry point"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point for the console"""

    prompt = "(hbnb) "
    def do_EOF(self, line):
        """Implement the EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        "quit"
        return True

    def emptyline(self):
        """Change the empty line method"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
