import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if self._value == '':
            return 0
            
        return len(re.findall(r'[^\s][.!?](?=\s|$)', self._value))


# Usage example
simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

print(simple_string.count_sentences())   # Output: 3
print(complex_string.count_sentences())  # Output: 3
print(empty_string.count_sentences())    # Output: 0
