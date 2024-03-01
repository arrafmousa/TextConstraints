import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

pos_translation = {
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
}


def split_paragraphs(text: str) -> list[str]:
    return text.split("\n")


def split_sentences(text: str) -> list[str]:
    return sent_tokenize(text)


def tag_parts_of_speech(text: str, required: str, comparator: str) -> bool:
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    if 'exactly' in comparator:
        return required == pos_translation[tagged_tokens[0][1]]
    if 'more' in comparator:
        return required > pos_translation[tagged_tokens[0][1]]
    if 'less' in comparator:
        return required < pos_translation[tagged_tokens[0][1]]
    return False


def count_letters(text: str, required: int) -> bool:
    return required == sum(1 for char in text if char.isalpha())


def is_anagram(text: str, reference: str) -> bool:
    return sorted(text) == sorted(reference)


def is_plaindrome(text: str) -> bool:
    return text == text[::-1]


def end_start_with(text: str, position: str, letter: str) -> bool:
    if 'start' in position:
        return text.startswith(letter)
    elif 'end' in position:
        return text.endswith(letter)
    return False


def initials_make_up(text: str, reference: str) -> bool:
    initials = ''.join(word[0] for word in text.split())
    return initials.lower() == reference.lower()


def count_words(text: str, required: int, comparator: str) -> bool:
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
    text = text.lower()
    word = word.lower()
    words = text.split()
    if 'more' in comparator:
        return words.count(word) > number
    elif 'exactly' in comparator:
        return words.count(word) == number
    return False


def check_sentence_count(text: str, expected_count: int, comparator: str) -> bool:
    sentences = sent_tokenize(text)
    if 'more' in comparator:
        return len(sentences) > expected_count
    elif 'exactly' in comparator:
        return len(sentences) == expected_count
    elif 'less' in comparator:
        return len(sentences) < expected_count
    return False


def check_letters(text: str, letters: list[str]) -> bool:
    for letter in letters:
        if letter in text:
            return True
    return False


def constraint_empty(text: str):
    return True

# tag_parts_of_speech("eat","Noun")
