#!/usr/bin/python3
"""This module is the package entry point"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
list_class = {"BaseModel": BaseModel,
              "User": User, "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review}


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
        if line not in list_class:
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

    def default(self, line):
        """Retrieve all instances of a class by using: <class.name>"""
        if line == "":
            print("** command name missing **")
            return False

        all_dict = []
        print_list = []
        all_dict = storage.all()
        count = 0
        name_class = ""
        if line.startswith("BaseModel"):
            name_class = "BaseModel"
        elif line.startswith("User"):
            name_class = "User"
        elif line.startswith("State"):
            name_class = "State"
        elif line.startswith("City"):
            name_class = "City"
        elif line.startswith("Amenity"):
            name_class = "Amenity"
        elif line.startswith("Place"):
            name_class = "Place"
        elif line.startswith("Review"):
            name_class = "Review"

        if line == name_class:
            print("** command name missing **")
            print(all_dict)
            return False

        for key, value in all_dict.items():
            if name_class in key:
                print_list.append(str(value))
                count += 1

        command = line.strip(name_class)
        if command == ".all()":
            print(print_list)
            return False
        if command == ".count()":
            print(count)
            return False
        if command.startswith(".show"):
            id_model = command.strip('.show("")')
            if id_model == "":
                print("** instance id missing **")
                return False
            for key in all_dict.keys():
                if f"{name_class}.{id_model}" == key:
                    print(all_dict[key])
                    return False
            print("** no instance found **")
            return False
        if command.startswith(".destroy"):
            id_model = command.strip('.destroy("")')
            if id_model == "":
                print("** instance id missing **")
                return False
            for key in all_dict.keys():
                if f"{name_class}.{id_model}" == key:
                    del all_dict[key]
                    storage.save()
                    return False
            print("** no instance found **")
            return False
        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
