#!/usr/bin/python3
"""This module is the package entry point"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
list_class = {"BaseModel": BaseModel, "User": User}


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
        for key, value in list_class.items():
            if line == key:
                new_inst = value()
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
        """
        Print all string of all instances
        based or not on the class name
        """
        all_dict = storage.all()
        print_list = []
        if line == "":
            for value in all_dict.values():
                print_list.append(str(value))
            print(print_list)
        elif line in list_class:
            for key, value in all_dict.items():
                if line in key:
                    print_list.append(str(value))
            print(print_list)
        else:
            print("** class doesn't exist **")
            return False

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
                setattr(value, args[2], args[3].strip('"'))
                storage.save()
                return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
