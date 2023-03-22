#!/usr/bin/python3
""" contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """command interpreter class"""


    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, line):
        """quits the interpreter"""

        return True

    def do_quit(self, line):
        """quits the interpreter"""

        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, cls):
        """Creates a new instance of BaseModel
        saves it(to the JSON FILE) and print the id
        """
        
        if cls == "":
            print("** class name missing **")
        try:
            f = eval(cls)()
            print(f.id)
        except Exception:
            print("** class doesn't exist **")
        storage.save()

    def do_show(self, arg):
        """Shows the string representation of an instance
        based on class name and id
        """

        s_arg = parse(arg)
        all_obj = storage.all()
        print(s_arg)
        if arg == "":
            print("** class name missing **")
        else:
            try:
                type(eval(s_arg[0])())
            except Exception:
                print("** class doesn't exist **")
        if len(s_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(s_arg[0],s_arg[1]) not in all_obj:
            print("** no instance found **")
        else:
            print(all_obj["{}.{}".format(s_arg[0],s_arg[1])])
        storage.save()

    def do_destroy(self, arg):
        s_arg = parse(arg)
        all_obj = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            try:
                type(eval(s_arg[0])())
            except Exception:
                print("** class doesn't exist **")
        if len(s_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(s_arg[0],s_arg[1]) not in all_obj:
            print("** no instance found **")
        else:
            del(all_obj["{}.{}".format(s_arg[0],s_arg[1])])
        storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

def parse(arg):
    #splits the argument line
    return tuple(arg.split())
"""def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()