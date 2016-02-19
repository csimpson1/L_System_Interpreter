

class LSystem(object):

    def __init__(self, alphabet, axiom, productions):
        self.alphabet = alphabet
        self.axiom = axiom
        self.productions = productions

    #def valid_grammer(self):
        """
        Check and see if the grammar is valid. This task consists of
        1) Checking that every character in the axiom is in the alphabet
        2) Checking that the right left side of every production is the alphabet
        3) Checking that the left side of every production is a word of letters
        from our alphabet
        :return: A boolean
        """

    def produce_string(self, n):
        """
        :param n: The length of the string we wish to produce
        :return: A string of length n generated from the axiom by the given
        """

        current_string = self.axiom
        for i in range(n):
            new_string = ''
            for char in current_string:

                if char in self.productions:
                    """
                    If we find a related production for a character, we add the
                    production to our new string
                    """
                    new_string += self.productions[char]

                else:
                    """
                    If there is no production listed for a given character
                    we assume it is terminal, so only the current character
                    is carried to the new string
                    """
                    new_string += char

            current_string = new_string
        return current_string



