class Stack:
    # create an empty container for pushing the data
    def __init__(self):
        self.stack = []

    # Adding the data to the Container
    def add_data(self, dataval):
        self.stack.append(dataval)

    # Poping out the data
    def popout_the_data(self):
        if len(self.stack) <= 0:
            print("NO ELEMENTS EXISTS")
        else:
            self.stack.pop()

    def print_top_val(self):
        if len(self.stack) <= 0:
            print("NO ELEMENTS EXISTS")
        else:
            print(f"{self.stack[-1]}")


Stack_ex = Stack()
Stack_ex.add_data("Madhu1")
Stack_ex.add_data("Madhu2")
Stack_ex.add_data("Madhu3")
Stack_ex.print_top_val()
Stack_ex.popout_the_data()
Stack_ex.print_top_val()
