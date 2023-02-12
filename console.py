#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel, storage

class HBNBCommand(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'hbnb'
    def do_create(self, arg):
        if arg is None:
            print('** class name missing **')
        elif getattr(sys.modules[__name__], arg) is None:
            print("** class doesn't exist **")
        else :
            className = getattr(sys.modules[__name__], arg)
            newClass = className()
            print(newClass.id)
            newClass.save()

    def do_show(self, className, classId):
        if arg is None:
            print('** class name missing **')
        elif classId is None:
            print("** instance id is missing **")
        elif getattr(sys.modules[__name__], arg) is None:
            print("** class doesn't exist **")
        else:
            jsonFile = storage.reload()
            instance = jsonFile.__objects[className.classId]
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)
    def do_destroy(self, className, classId):
        if arg is None:
            print('** class name missing **')
        elif classId is None:
            print("** instance id is missing **")
        elif getattr(sys.modules[__name__], arg) is None:
            print("** class doesn't exist **")
        else:
            jsonFile = storage.reload()
            instance = jsonFile.__objects.pop(className.classId)
            if instance is None:
                print("** no instance found **")
            else:
                storage.__objects = jsonFile
                storage.save()

    def do_all(self, className):
        jsonFile = storage.reload()
        if className is None:
            for inst in jsonFile:
                print(inst)
        else:
            instance = jsonFile.__objects.(className)
            if instance is None:
                print("** class doesn't exist **")
            else:
                print(instance)
    def do_update(self, *args):
        pass


    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self):
        return True


if __name__ = "__main__":
    HBNBCommand().cmdloop()