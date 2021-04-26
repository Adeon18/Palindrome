"""
Palindrome class realization.
"""

from arraystack import ArrayStack  # or from linkedstack import LinkedStack


class Palindrome:
    """
    A class for managing the Palindrome
    """
    def __init__(self):
        self._symbols = ArrayStack()

    def add_letter(self, letter: str):
        """
        Add a letter to a word
        """
        self._symbols.push(letter)

    def get_letter(self):
        """
        Remove and return that letter
        """
        return self._symbols.pop()

    def read_file(self, path: str):
        """
        Read the file and return the list of words in it
        """
        data = []
        with open(path, "r") as txt:
            file_data = txt.readlines()

        for word in file_data:
            data.append(word.split()[0])

        return data

    def write_to_file(self, path: str, data: list):
        """
        Write all of the data to a file
        """
        with open(path, "a") as work_file:
            for i in data:
                work_file.write(i + "\n")

    def find_palindromes(self, path_from: str, path_to: str):
        """
        Find palindromes from <path_from> and write them to <path_to>
        """
        palindromes = []
        words = self.read_file(path_from)

        for word in words:
            main_pal = Palindrome()
            main_pal_copy = Palindrome()
            compare_pal = Palindrome()
            for letter in word:
                main_pal.add_letter(letter)
                main_pal_copy.add_letter(letter)

            for _ in range(len(word)):
                # print(main_pal_copy.get_letter(), "!!!!!!!!!!!!!!!!")
                compare_pal.add_letter(main_pal_copy.get_letter())
            # print(compare_pal._symbols, main_pal._symbols)
            if compare_pal._symbols == main_pal._symbols:
                palindromes.append(word)

        self.write_to_file(path_to, palindromes)

        return palindromes


if __name__ == "__main__":
    p = Palindrome()
    # print(p.find_palindromes("base.lst", "")[:10])
    print(p.find_palindromes("words.txt", "aaaa"))
    # p.add_letter("a")
    # p.add_letter("b")
    # p.add_letter("c")
    # print(p.get_letter())
