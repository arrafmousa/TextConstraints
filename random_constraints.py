import random

# Word constraints
def generate_word_constraint():
    choices = [
        lambda : "",
        lambda: f"that is a {random.choice(['noun', 'verb', 'adjective'])}",
        lambda n=random.randint(3,
                                10): f"that has {random.choice([' more than ', ' less than ', ' exactly '])} {n} letters",
        lambda w=random.choice(['time', 'note', 'star']): f"that is an anagram with {w}",
        lambda: "a word that is a palindrome",
        lambda l=random.choice('abcdefghijklmnopqrstuvwxyz'), p=random.choice(['ends', 'starts']): f"that {p} with {l}"
    ]
    return random.choice(choices)()


# Sentence constraints
def generate_sentence_constraint():
    choices = [
        lambda: "",
        lambda: "Initial words consist a sentence cr word",
        lambda n=random.randint(5, 15): f"that has {random.choice(['more than', 'less than', 'exactly'])} {n} words",
        lambda
            n=random.randint(20,
                             100): f"that has {random.choice(['more than', 'less than', 'exactly'])} {n} characters",
        lambda: "that is a palindrome",
        lambda s=random.choice(['The quick brown fox jumps over the lazy dog',
                                'An apple a day keeps the doctor away']): f"that is an anagram with {s}",
        lambda w=random.choice(['time', 'love', 'world']),
               t=random.choice(['ends', 'starts']): f"that {t} with {w}",
        lambda w=random.choice(['time', 'love', 'world']), c=random.choice(['exactly', 'more than']),
               n=random.randint(1, 5): f"generate a sentence that has the word {w} {c} {n} times"
    ]
    return random.choice(choices)()


# Paragraph constraints
def generate_paragraph_constraint():
    choices = [
        lambda n=random.randint(2,
                                10): f"generate a paragraph that has {random.choice(['more than', 'less than', 'exactly'])} {n} sentences",
        lambda w=random.sample("abcdefghijklmnopqrstuvwxyz",
                               random.randint(1, 3)): f"generate a paragraph and do not use {w}"
    ]
    return random.choice(choices)()
