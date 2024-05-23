#!/usr/bin/python3
#!/usr/bin/python3
""" /"MyList" class inherits from list class """


class MyList(list):
    """ MyList inherits from list. """
    def print_sorted(self):
        """ Prints the list: ascending order. """
        sorted_list = sorted(self)
        print(sorted_list)
