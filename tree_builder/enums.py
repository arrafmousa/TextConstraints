from enum import Enum

class NodeType(Enum):
    CONTENT = 'content'
    PARAGRAPH = 'paragraph'
    SENTENCE = 'sentence'
    WORD = 'word'


class AggregationType(Enum):
    MORE_THAN = "at least "
    LESS_THAN = "less than "
    COUNT = "exactly "
    NONE = "none"

class ConstraintType(Enum):
    TAG_PARTS_OF_SPEECH = "tag_parts_of_speech"
    COUNT_LETTERS = "count_letters"
    IS_ANAGRAM = "is_anagram"
    IS_PALINDROME = "is_palindrome"
    END_START_WITH = "end_start_with"
    CHECK_LETTERS = "check_letters"
    INITIALS_MAKE_UP = "initials_make_up"
    COUNT_WORDS = "count_words"
    COUNT_WORD_APPEARANCE = "count_word_appearance"
    CHECK_SENTENCE_COUNT = "check_sentence_count"
    CONSTRAINT_EMPTY = "constraint_empty"