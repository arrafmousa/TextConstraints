import random
from enum import Enum
from typing import Tuple, List

from random_constraints import *


class ConstraintType(Enum):
    MORE_THAN = 'EDGE: more than'
    LESS_THAN = 'EDGE: less than'
    EXACTLy = 'EDGE: exactly'


class NodeType(Enum):
    CONTENT = 'NODE: content'
    PARAGRAPH = 'NODE: paragraph'
    SENTENCE = 'NODE: sentence'
    WORD = 'NODE: word'


class AggregationType(Enum):
    ALL = "AGG : all of the following"
    NONE = "AGG : none of the following"
    OR = "AGG : at least one one of the following"


class Node:
    def __init__(self, constraint: str, level: NodeType, aggregation: AggregationType):
        self.constraint = constraint  # The string content of the node.
        self.level = level  # The level of the constraint (content, paragraph, etc.)
        self.aggregation = aggregation  # The aggregation format of the sub-nodes
        self.children: List[Node] = []  # List of child nodes.
        self.edge_values: List[Tuple[ConstraintType, int]] = []  # Edge values to child nodes.

    # Method to add a child node.
    def add_child(self, child):
        edge_value = (child.level, random.randint(1, 100))  # Random number for simplicity.
        self.children.append(child)
        self.edge_values.append(edge_value)

    def print_tree(self, depth=0):
        # Print the current node with indentation based on its depth in the tree.
        tabs = '\t' * depth  # Create a string of tab characters for indentation.
        print(f"{tabs}{self.level.value}: {self.constraint} : {self.aggregation}")
        # Print each child, increasing the depth.
        for child in self.children:
            child.print_tree(depth + 1)

    def format_response(self, depth=0) -> str:
        accum_constraint =  self.constraint + " where " + self.aggregation.value + " conditions are met "
        for child in self.children:
            accum_constraint += child.format_response(depth + 1)
        return accum_constraint




def generate_random_content(level: NodeType) -> str:
    constraint = ""
    if level == NodeType.PARAGRAPH:
        constraint = generate_paragraph_constraint()
    elif level == NodeType.SENTENCE:
        constraint = generate_sentence_constraint()
    elif level == NodeType.WORD:
        constraint = generate_word_constraint()
    return constraint


def build_tree() -> Node:
    root = Node(generate_random_content(NodeType.CONTENT), NodeType.CONTENT, random.choice(list(AggregationType)))
    for _ in range(random.randint(0, 2)):  # Number of children of root.
        paragraph_node = Node(generate_random_content(NodeType.PARAGRAPH), NodeType.PARAGRAPH,
                              random.choice(list(AggregationType)))
        root.add_child(paragraph_node)
        for _ in range(random.randint(0, 2)):  # Number of children of each paragraph.
            sentence_node = Node(generate_random_content(NodeType.SENTENCE), NodeType.SENTENCE,
                                 random.choice(list(AggregationType)))
            paragraph_node.add_child(sentence_node)
            for _ in range(random.randint(0, 2)):  # Number of children of each sentence.
                word_node = Node(generate_random_content(NodeType.WORD), NodeType.WORD, AggregationType.ALL)
                sentence_node.add_child(word_node)
    return root
