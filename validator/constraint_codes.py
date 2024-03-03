import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict

#  Part of speech translation


pos_translation = defaultdict(lambda: 'NONE',
                              {
                                  # Nouns
                                  'NN': 'noun',
                                  'NNS': 'noun',
                                  'NNP': 'noun',
                                  'NNPS': 'noun',
                                  # Verbs
                                  'VB': 'verb',
                                  'VBD': 'verb',
                                  'VBG': 'verb',
                                  'VBN': 'verb',
                                  'VBP': 'verb',
                                  'VBZ': 'verb',
                                  # Adjectives
                                  'JJ': 'adjective',
                                  'JJR': 'adjective',
                                  'JJS': 'adjective',
                              })


def split_paragraphs(text: str) -> list[str]:
    """
    Split the text into paragraphs based on newlines
    :param text: string
    :return: a list of paragraphs
    """
    return text.split("\n")


def split_sentences(text: str) -> list[str]:
    """
    Split the text into sentences based on punctuation
    :param text: string
    :return: a list of sentences
    """
    return sent_tokenize(text)


def split_words(text: str) -> list[str]:
    """
    Split the text into words based on whitespace
    :param text: string
    :return: a list of words
    """
    return word_tokenize(text)


def tag_parts_of_speech(text: str, required: str) -> bool:
    """
    Tag the parts of speech in the text and compare them to the required part of speech
    :param text: string
    :param required: number of letters required
    :param comparator: one of the following ['exactly', 'more', 'less'] each representing the number of letters required
    :return: True if the number of letters in the text matches the required number
    """
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    return required == pos_translation[tagged_tokens[0][1]]


def count_letters(text: str, required: int, comparator: str) -> bool:
    """
    Count the number of letters in the text and compare it to the required number
    :param comparator: one of the following ['exactly', 'more', 'less'] each representing the number of letters required
    :param text: string
    :param required: number of letters required
    :return: True if the number of letters in the text matches the required number
    """
    letters_count = sum(1 for char in text if char.isalpha())
    if 'more' in comparator:
        return letters_count > required
    if 'less' in comparator:
        return letters_count < required
    if 'exactly' in comparator:
        return letters_count == required
    return False


def is_anagram(text: str, reference: str) -> bool:
    """
    Check if the text is an anagram of the reference
    :param text: string
    :param reference: the reference string
    :return: True if the text is an anagram of the reference
    """
    return sorted(text) == sorted(reference)


def is_plaindrome(text: str) -> bool:
    """
    Check if the text is a palindrome
    :param text: string
    :return: True if the text is a palindrome
    """
    return text == text[::-1]


def end_start_with(text: str, position: str, letter: str) -> bool:
    """
    Check if the text starts or ends with the letter
    :param text: string
    :param position: one of the following ['start', 'end'] representing the required position of the letter
    :param letter: the required letter
    :return: True if the text starts or ends with the letter
    """
    if 'start' in position:
        return text.startswith(letter)
    elif 'end' in position:
        return text.endswith(letter)
    return False


def initials_make_up(text: str, reference: str) -> bool:
    """
    Check if the initials of the words in the text make up the reference
    :param text: string
    :param reference: the reference string that the intials should make up
    :return: True if the initials of the words in the text make up the reference
    """
    initials = ''.join(word[0] for word in text.split())
    return initials.lower() == reference.lower()


def count_words(text: str, required: int, comparator: str) -> bool:
    """
    Count the words in the text and compare it to the required number
    :param text: string
    :param required: number of words required
    :param comparator: one of the following ['exactly', 'more', 'less'] each representing the number of words required
    :return: True if the number of words in the text matches the required number
    """
    # Split the text into words based on whitespace and count them
    words = text.split()
    if 'more' in comparator:
        return len(words) > required
    if 'less' in comparator:
        return len(words) < required
    if 'exactly' in comparator:
        return len(words) == required
    return False


def count_word_appearance(text: str, word: str, number: int, comparator: str) -> bool:
    """
    Count the number of times a word appears in the text and compare it to the required number
    :param text: string
    :param word: the word to count
    :param number: the required number of times the word should appear
    :param comparator: one of the following ['exactly', 'more'] each representing the number of times the word should appear
    :return: True if the number of times the word appears in the text matches the required number
    """
    text = text.lower()
    word = word.lower()
    words = text.split()
    if 'more' in comparator:
        return words.count(word) > number
    elif 'exactly' in comparator:
        return words.count(word) == number
    return False


def check_sentence_count(text: str, expected_count: int, comparator: str) -> bool:
    """
    Count the sentences in the text and compare it to the required number
    :param text: string
    :param expected_count: number of sentences required
    :param comparator: one of the following ['exactly', 'more', 'less'] each representing the number of sentences required
    :return: True if the number of sentences in the text matches the required number
    """
    sentences = sent_tokenize(text)
    if 'more' in comparator:
        return len(sentences) > expected_count
    elif 'exactly' in comparator:
        return len(sentences) == expected_count
    elif 'less' in comparator:
        return len(sentences) < expected_count
    return False


def check_letters(text: str, letters: list[str]) -> bool:
    """
    Check if the text includes any of the letters
    :param text: string
    :param letters: list of letters to check
    :return: True if the text includes any of the letters
    """
    for letter in letters:
        if letter in text:
            return True
    return False


def constraint_empty(text: str):
    """
     An empty constraint
    :param text:string
    :return: True
    """
    return True
