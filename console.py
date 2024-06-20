#!/usr/bin/python3
"""
console.py that contains the entry point of the command interpreter
"""


import cmd
import sys
import models
import re
from models import storage
from models.patient import Patient
from models.doctor import Doctor
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    HBNBC command interpreter
    """

    prompt = "(hbnb) "
    Classes_dict = {
        "BaseModel": BaseModel,
        "Patient": Patient,
        "Doctor": Doctor
        }


    all_objs = storage.all()
    instance_representation = []

    def do_EOF(self, args):
        """Exit command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def help_quit(self):
        """help quit command to display ...
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help quit command to display ...
        """
        print("Exit command to exit the program\n")

    def emptyline(self):
        """an empty line + ENTER should not execute anything
        """
        ...

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Usage: create <class name>
        """
        if arg:
            arguments = arg.split()
            class_name = arguments.pop(0)

        if not arg or not class_name:
            print("** class name missing **")
            return
        if class_name not in self.Classes_dict:
            print("** class doesn't exist **")
            return

        if class_name in self.Classes_dict.keys():
            new_obj = self.Classes_dict[class_name]() 
            for argument in arguments:
                attribute, value = argument.split('=')
                if '"' in value:
                    value = value.strip('"').replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        value = float(value)
                setattr(new_obj, attribute, value)
            new_obj.save()
            print("{}".format(new_obj.id))

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <object id>
        """
        if not arg:
            print("** class name missing **")
            return

        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(cmd_args[0], cmd_args[1])
        try:
            cls_name = self.Classes_dict[cmd_args[0]]
            print(self.all_objs[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Usage: destroy <class name> <object id>
        """
        if not arg:
            print("** class name missing **")
            return

        cmd_args = arg.split(" ")
        if cmd_args[0] not in self.Classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(cmd_args[0], cmd_args[1])
        try:
            if len(self.instance_representation) == 0:
                self.instance_representation = []
                for obj_dict in self.all_objs.values():
                    self.instance_representation.append(str(obj_dict))
            deleted_representaiton = str(self.all_objs[key])
            self.instance_representation.remove(deleted_representaiton)
            del self.all_objs[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all OR all <class name>
        """
        self.instance_representation = []
        if not arg:
            if self.all_objs:
                for obj_dict in self.all_objs.values():
                    self.instance_representation.append(str(obj_dict))

        else:
            if arg not in self.Classes_dict.keys():
                print("** class doesn't exist **")
                return
            for obj_dict in self.all_objs.values():
                cls_name = self.Classes_dict[arg]
                if type(obj_dict) == cls_name:
                    self.instance_representation.append(str(obj_dict))
        print(self.instance_representation)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        update <class name> <id> <attribute name> "<attribute value>"
        """

        if not arg:
            print("** class name missing **")
            return

        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(cmd_args[0], cmd_args[1])
        try:
            obj_dict = self.all_objs[key]
        except KeyError:
            print("** no instance found **")
            return

        if len(cmd_args) < 3:
            print("** attribute name missing **")
            return

        if len(cmd_args) < 4:
            print("** value missing **")
            return

        var, value = cmd_args[2], cmd_args[3].strip('"')
        list_args = ["id", "updated_at", "created_at"]
        list_values = [str, int, float]
        if var not in list_args and type(value) in list_values:
            setattr(obj_dict, var, value)
            obj_dict.save()

    def count(self, arg):
        count = 0
        for i in self.all_objs.keys():
            if arg in i:
                count += 1
        print(count)

    def default(self, arg):
        exp = r'(\w+)\.(\w+)\("([^"]+)"(?:,\s*"([^"]+)")?(?:,\s*"([^"]+)")?\)'
        commands_dict = {"all": self.do_all, "count": self.count}
        commands_dict2 = {"show": self.do_show, "destroy": self.do_destroy}
        pattern_count = re.compile(r'(\w+)\.(\w+)\(\)')
        pattern_show_update = re.compile(exp)

        # Iterate over the lines

        # Try to match the count pattern
        match_count = pattern_count.match(arg)
        if match_count:
            class_name = match_count.group(1)
            command = match_count.group(2)
        else:
            # Try to match the show or update pattern
            match_show_update = pattern_show_update.match(arg)
            if match_show_update:
                class_name = match_show_update.group(1)
                command = match_show_update.group(2)
                id_value = match_show_update.group(3)
                key = match_show_update.group(4)
                value = match_show_update.group(5)

        if class_name in self.Classes_dict:
            if command in commands_dict.keys():
                commands_dict[command](class_name)
                return
            elif command in commands_dict2.keys():
                commands_dict2[command](f"{class_name} {id_value}")
            elif command == "update":
                self.do_update(f"{class_name} {id_value} {key} {value}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()