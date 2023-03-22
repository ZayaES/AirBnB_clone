import cmd

class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """quits the interpreter"""

        return True

    def do_quit(self, line):
        """quits the interpreter"""

        return True

    def checkline(self, line):
        """Does nothing"""
        pass
