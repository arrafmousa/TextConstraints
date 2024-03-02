import random
from functools import partial

from validator.constraint_codes import *


class Constraint:
    constraint: str
    validator_f: callable

    def __init__(self, constraint: str, validator_f: callable):
        self.constraint = constraint
        self.validator_f = validator_f


def generate_word_constraint():
    """ generate word constraint prompts"""
    pos = random.choice(['noun', 'verb', 'adjective'])
    choices = [
        lambda: Constraint("", constraint_empty),
        lambda: Constraint(f"that is a {pos}", partial(tag_parts_of_speech, required=pos)),
        lambda n=random.randint(3, 10), q=random.choice([' more than ', ' less than ', ' exactly ']):
        Constraint(
            f"that has {q} {n} letters", partial(count_letters, required=n, comparator=q)
        ),
        lambda w=random.choice(['time', 'note', 'star']):  # TODO: change words
        Constraint(
            f"that is an anagram with {w}", partial(is_anagram, reference=w)
        ),
        lambda: Constraint("a word that is a palindrome", is_plaindrome),
        lambda l=random.choice('abcdefghijklmnopqrstuvwxyz'), p=random.choice(['ends', 'starts']):
        Constraint(
            f"that {p} with {l}", partial(end_start_with, position=p, letter=l)
        ),
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, 3)):
        Constraint(f"that doesnt include the letters {w}", partial(check_letters, letters=w))
    ]
    return random.choice(choices)()


# Sentence constraints
def generate_sentence_constraint():
    choices = [
        lambda: Constraint("", constraint_empty),
        lambda r="someword":  # TODO : change this word
        Constraint(
            f"Initials of the words make up {r}", partial(initials_make_up, reference=r)
        ),
        lambda n=random.randint(5, 15), c=random.choice(['more than', 'less than', 'exactly']):
        Constraint(f"that has {c} {n} words", partial(count_words, required=n, comparator=c)),
        lambda n=random.randint(20, 100), c=random.choice(['more than', 'less than', 'exactly']):
        Constraint(f"that has {c} {n} characters", partial(count_letters, required=n, comparator=c)),
        lambda: Constraint("that is a palindrome", is_plaindrome),
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, 3)):
        Constraint(f"generate a paragraph and do not use the letters {w}", partial(check_letters, letters=w)),
        lambda s=random.choice(['The quick brown fox jumps over the lazy dog', 'An apple a day keeps the doctor away']):
        Constraint(f"that is an anagram with {s}", partial(is_anagram, reference=s)),
        lambda w=random.choice(['time', 'love', 'world']), t=random.choice(['ends', 'starts']):
        Constraint(f"that {t} with {w}", partial(end_start_with, position=t, letter=w)),
        lambda w=random.choice(['time', 'love', 'world']), c=random.choice(['exactly', 'more than']),
               n=random.randint(1, 5):
        Constraint(f"that doesnt include the letters {w} {c} {n} times",
                   partial(count_word_appearance, word=w, number=n, comparator=c))
    ]
    return random.choice(choices)()


# Paragraph constraints
def generate_paragraph_constraint():
    choices = [
        lambda n=random.randint(2, 10), c=random.choice(['more than', 'less than', 'exactly']):
        Constraint(f"that has {c} {n} sentences",
                   partial(check_sentence_count, expected_count=n, comparator=c)),
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, 3)):
        Constraint(f"that doesnt include the letters {w}", partial(check_letters, letters=w))
    ]
    return random.choice(choices)()
