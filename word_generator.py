import random
import string

def create_word_file(num_words=50000, word_length=42, filename="wordFile.txt"):
    """
    Generates `num_words` unique random strings, each of length `word_length`,
    and writes them to `filename`, one per line.
    Intended to generate long strings that can be used to stress test
    data structures like hash tables, tries, etc while parsing or searching

    Args:
        num_words (int): The number of unique words to generate.
        word_length (int): The length of each random string.
        filename (str): The output text file name.
    """
    random_strings = set()
    letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

    # Generate until we have num_words unique items
    while len(random_strings) < num_words:
        word = "".join(random.choices(letters, k=word_length))
        random_strings.add(word)

    # Write words to file, one per line
    with open(filename, "w") as f:
        for w in random_strings:
            f.write(w + "\n")



def create_weighted_word_file(num_words=50000, word_length=42, filename="weightedWords.txt"):
    """
    Generates `num_words` unique random strings, each of length `word_length`,
    and writes them to `filename`, one per line.
    Weights for each letter will determine the relative frequency of that letter
    Set to  >40 for lots of that letter repeated
    Set to 0 if you don't want that letter in any string
    Set() Makes sure each string generated is unique
    Intended to generate long strings that can be used to stress test
    data structures like hash tables, tries, etc while parsing or searching

    Args:
        num_words (int): The number of unique strings to generate.
        word_length (int): The length of each random string.
        filename (str): The output text file name.
    """
    random_strings = set()

    letter_weights = {
        'a': 10, 'b': 1, 'c': 1, 'd': 1, 'e': 40,
        'f': 1, 'g': 1, 'h': 2, 'i': 8, 'j': 1,
        'k': 1, 'l': 2, 'm': 10, 'n': 4, 'o': 8,
        'p': 1, 'q': 1, 'r': 4, 's': 4, 't': 4,
        'u': 8, 'v': 0, 'w': 1, 'x': 0 , 'y': 2,
        'z': 1
    }

    # Convert to lists for use in `random.choices`
    letters = list(letter_weights.keys())
    weights = list(letter_weights.values())


    # Generate until we have num_words unique items
    while len(random_strings) < num_words:
        word = "".join(random.choices(letters, weights=weights, k=word_length))
        random_strings.add(word)

    # Write words to file, one per line
    with open(filename, "w") as f:
        for w in random_strings:
            f.write(w + "\n")

# Example usage (uncomment to run):
#create_weighted_word_file()
#create_word_file()
