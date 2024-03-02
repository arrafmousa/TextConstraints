import random
from functools import partial

from tree_builder.enums import ConstraintType
from validator.constraint_codes import *


class Constraint:
    instruction: str
    validator_f: callable

    def __init__(self, constraint: str, validator_f: callable, constraint_type: ConstraintType):
        self.instruction = constraint
        self.validator_f = validator_f
        self.constraint_type = constraint_type


def generate_word_constraint() -> Constraint:
    """ generate word constraint prompts"""
    pos = random.choice(['noun', 'verb', 'adjective'])
    choices = [
        lambda: Constraint(f"that is a {pos}", partial(tag_parts_of_speech, required=pos),
                           ConstraintType.TAG_PARTS_OF_SPEECH),
        lambda n=random.randint(3, 10), q=random.choice([' more than ', ' less than ', ' exactly ']):
        Constraint(
            f"that has {q} {n} letters", partial(count_letters, required=n, comparator=q), ConstraintType.COUNT_LETTERS
        ),
        lambda w=random.choice(['time', 'note', 'star']):  # TODO: change words
        Constraint(
            f"that is an anagram with {w}", partial(is_anagram, reference=w), ConstraintType.IS_ANAGRAM
        ),
        lambda: Constraint("a word that is a palindrome", is_plaindrome, ConstraintType.IS_PALINDROME),
        lambda l=random.choice('abcdefghijklmnopqrstuvwxyz'), p=random.choice(['ends', 'starts']):
        Constraint(
            f"that {p} with {l}", partial(end_start_with, position=p, letter=l), ConstraintType.END_START_WITH
        ),
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, 3)):
        Constraint(f"that doesnt include the letters {w}", partial(check_letters, letters=w),
                   ConstraintType.CHECK_LETTERS)
    ]
    return random.choice(choices)()


# Sentence constraints
def generate_sentence_constraint() -> Constraint:
    choices = [
        lambda: Constraint("", constraint_empty, ConstraintType.CONSTRAINT_EMPTY),
        lambda r="someword":  # TODO : change this word
        Constraint(
            f"Initials of the words make up {r}", partial(initials_make_up, reference=r),
            ConstraintType.INITIALS_MAKE_UP
        ),
        lambda n=random.randint(5, 15), c=random.choice(['more than', 'less than', 'exactly']):
        Constraint(f"that has {c} {n} words", partial(count_words, required=n, comparator=c),
                   ConstraintType.COUNT_WORDS),
        lambda n=random.randint(20, 100), c=random.choice(['more than', 'less than', 'exactly']):
        Constraint(f"that has {c} {n} characters", partial(count_letters, required=n, comparator=c),
                   ConstraintType.COUNT_LETTERS),
        lambda: Constraint("that is a palindrome", is_plaindrome, ConstraintType.IS_PALINDROME),
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, 3)):
        Constraint(f"generate a paragraph and do not use the letters {w}", partial(check_letters, letters=w),
                   ConstraintType.CHECK_LETTERS),
        lambda s=random.choice(['The quick brown fox jumps over the lazy dog', 'An apple a day keeps the doctor away']):
        Constraint(f"that is an anagram with {s}", partial(is_anagram, reference=s), ConstraintType.IS_ANAGRAM),
        lambda w=random.choice(['time', 'love', 'world']), t=random.choice(['ends', 'starts']):
        Constraint(f"that {t} with {w}", partial(end_start_with, position=t, letter=w), ConstraintType.END_START_WITH),
        lambda w=random.choice(['time', 'love', 'world']), c=random.choice(['exactly', 'more than']),
               n=random.randint(1, 5):
        Constraint(f"that doesnt include the letters {w} {c} {n} times",
                   partial(count_word_appearance, word=w, number=n, comparator=c), ConstraintType.COUNT_WORD_APPEARANCE)
    ]
    return random.choice(choices)()


# Paragraph constraints
def generate_paragraph_constraint() -> Constraint:
    choices = [
        lambda n=random.randint(2, 10), c=random.choice(['more than', 'less than', 'exactly']):
        Constraint(f"that has {c} {n} sentences",
                   partial(check_sentence_count, expected_count=n, comparator=c), ConstraintType.CHECK_SENTENCE_COUNT),
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, 3)):
        Constraint(f"that doesnt include the letters {w}", partial(check_letters, letters=w),
                   ConstraintType.CHECK_LETTERS),
    ]
    return random.choice(choices)()


def generate_content_constraint() -> Constraint:
    return Constraint("Generate a text ", constraint_empty, ConstraintType.CONSTRAINT_EMPTY)
