#!/usr/bin/env python3
"""
Module: console.py
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class that contains entry point of command interpreter """

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
