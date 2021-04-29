"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start = 0):
        "create the serial generator with initial value a"
        self.start = start
        self.next = start
    def generate(self):
        "return the next number in sequence"
        self.next = self.next + 1
        return self.next-1
    def reset(self):
        "reset to initial value"
        self.next = self.start
    def __repr__(self):
        "Represents the serial Generator"
        return f" <Generates the next number starting with {self.start}, next = {self.start +1}>"
   