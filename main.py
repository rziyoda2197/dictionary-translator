class Translator:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def translate(self, word):
        return self.dictionary.get(word, "Siz kiritgan so'z mavjud emas.")

    def add_word(self, word, translation):
        self.dictionary[word] = translation

    def remove_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
        else:
            print("Siz kiritgan so'z mavjud emas.")

    def update_word(self, word, new_translation):
        if word in self.dictionary:
            self.dictionary[word] = new_translation
        else:
            print("Siz kiritgan so'z mavjud emas.")

# Misol:
dictionary = {
    "hello": "salom",
    "world": "dunyo"
}

translator = Translator(dictionary)

print(translator.translate("hello"))  # salom
print(translator.translate("world"))  # dunyo
print(translator.translate("python"))  # Siz kiritgan so'z mavjud emas.

translator.add_word("python", "python")
print(translator.translate("python"))  # python

translator.remove_word("world")
print(translator.translate("world"))  # Siz kiritgan so'z mavjud emas.

translator.update_word("hello", "assalomu alaykum")
print(translator.translate("hello"))  # assalomu alaykum
