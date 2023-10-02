class MyString:
    def __init__(self, strr):
        self.strr = strr

    def append(self, char):
        char_list = list(self.strr)
        char_list.append(char)
        return MyString("".join(char_list))

    def pop(self, index):
        char_list = list(self.strr)
        try:
            popped_char = char_list.pop(index)
        except IndexError:
            raise IndexError("Pop index out of range")
        return MyString("".join(char_list))

    def __str__(self):
        return self.strr


call = MyString("Hello, World!")
print(call)
print(call.append("H"))
print(call.pop(-1))
