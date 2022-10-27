#!/usr/bin/python3
"""This module is the package entry point"""
import cmd
from models.base_model import BaseModel
from models import storage
list_class = ["BaseModel"]


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

    def do_create(self, line):
        """Create the new instance"""
        if line == "":
            print("** class name missing **")
            return False
        if not line in list_class:
            print("** class doesn't exist **")
            return False
        new_inst = BaseModel()
        new_inst.save()
        print(new_inst.id)
        return False

    def do_show(self, line):
        """Print the string representation of an instance"""
        if line == "":
            print("** class name missing **")
            return False
        args = line.split()
        if not args[0] in list_class:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False

        all_dict = storage.all()

        for key in all_dict.keys():
            if f"{args[0]}.{args[1]}" == key:
                print(all_dict[key])
                return False
        print("** no instance found **")
        return False

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "":
            print("** class name missing **")
            return False
        args = line.split()
        if not args[0] in list_class:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False

        all_dict = storage.all()

        for key in all_dict.keys():
            if f"{args[0]}.{args[1]}" == key:
                del all_dict[key]
                storage.save()
                return False
        print("** no instance found **")
        return False

    def do_all(self, line):
        """"""
        if not line in list_class:
            print("** class doesn't exist **")
            return False
        all_dict = storage.all()
        print_list = []
        for value in all_dict.values():
            print_list.append(str(value))
        print(print_list)

    def do_update(self, line):
        """
        Update an instance based on the class name an id
        by adding or updating attibute
        """
        if line == "":
            print("** class name missing **")
            return False

        args = line.split()
        if not args[0] in list_class:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        all_dict = storage.all()
        if f"{args[0]}.{args[1]}" not in all_dict:
            print("** no instance found **")
            return False

        if len(args) < 3:
            print("** attribute name missing **")
            return False

        if len(args) < 4:
            print("** value missing **")
            return False

        for key, value in all_dict.items():
            if f"{args[0]}.{args[1]}" == key:
                """
                try:
                    if type(args[3]) is int:
                        setattr(value, args[2], int(args[3]))
                    if type(args[3]) is float:
                        setattr(value, args[2], float(args[3]))
                    else:
                        setattr(value, args[2], args[3].strip('"'))
                """
                setattr(value, args[2], args[3].strip('"'))
                storage.save()
                return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
