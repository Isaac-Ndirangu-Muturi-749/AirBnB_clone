#!/usr/bin/python3
"""

"""

import cmd
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to the JSON file."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = globals()[arg]
        except KeyError:
            print("** class doesn't exist **")
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not arg or len(args) == 1:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg or len(args) == 1:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representations of all instances, or all instances of a class."""
        args = arg.split()
        if not arg or len(args) == 1:
            instances = models.storage.all().values()
            print([str(instance) for instance in instances])
        else:
            try:
                cls = globals()[args[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
            instances = [str(instance) for key, instance in models.storage.all().items() if key.startswith(args[0])]
            if not instances:
                print("** class doesn't exist **")
                return
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not arg or len(args) == 1:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) == 3:
            print("** attribute name missing **")
            return
        if len(args) == 4:
            print("** value missing **")
            return
        instance = models.storage.all()[key]
        setattr(instance, args[2], args[3])
        models.storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
