from typing import List

from tree_builder.builder.random_constraints import *
from tree_builder.tree_classes.Constraint import Constraint
from tree_builder.tree_classes.enums import NodeType, AggregationType
from validator.constraint_codes import split_paragraphs, split_sentences, split_words


class Node:
    def __init__(self, constraint: Constraint, level: NodeType, aggregation: AggregationType, aggragation_value=0):
        self.constraint = constraint  # The string content of the node.
        self.level = level  # The level of the constraint (content, paragraph, etc.)
        self.aggregation = aggregation  # The aggregation format of the sub-nodes
        self.children: List[Node] = []  # List of child nodes.
        self.aggregation_value = aggragation_value  # The value of the aggregation.

    # Method to add a child node.
    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, depth=0):
        # Print the current node with indentation based on its depth in the tree.
        tabs = '\t' * depth  # Create a string of tab characters for indentation.
        print(f"{tabs}{self.level.value}: {self.constraint.instruction} : {self.aggregation}")
        # Print each child, increasing the depth.
        for child in self.children:
            child.print_tree(depth + 1)

    def format_response(self, depth=1) -> str:
        accum_constraint = ''
        if self.constraint.dummy:
            accum_constraint += f"{self.children[0].format_response()}"
        else:
            accum_constraint += self.constraint.instruction
        return accum_constraint


        # accum_constraint = self.constraint.instruction if self.constraint.instruction else ''
        # if len(self.children) == 0:
        #     return accum_constraint
        # if not self.constraint.dummy:
        #     accum_constraint += (". And in it " +
        #                          f"{self.aggregation.value} "
        #                          f"{self.aggregation_value if self.aggregation != AggregationType.NONE else ''}"
        #                          + " of the following is true:")
        # for child in self.children:
        #     accum_constraint += "\n" + "\t" * depth + f"{child.level.value} {child.format_response(depth + 1)}"
        return accum_constraint

    def split_text(self, text: str) -> List[str]:
        if self.level == NodeType.CONTENT:
            return split_paragraphs(text)
        if self.level == NodeType.PARAGRAPH:
            return split_sentences(text)
        if self.level == NodeType.SENTENCE:
            return split_words(text)
        return []

    def validate_content(self, content: str) -> bool:
        """
        Validates the content against the constraints of the tree.
        :param content:
        :return:
        """
        if self.constraint.dummy:
            return True
        if not self.constraint.validator_f(content):
            return False
        texts = self.split_text(content)
        comply = [1 if child.validate_content(text) else 0 for text, child in zip(texts, self.children)]
        compliance_num = sum(comply)
        if self.aggregation == AggregationType.MORE_THAN:
            return compliance_num > self.aggregation_value
        if self.aggregation == AggregationType.LESS_THAN:
            return compliance_num < self.aggregation_value
        if self.aggregation == AggregationType.COUNT:
            return compliance_num == self.aggregation_value
        if self.aggregation == AggregationType.NONE:
            return compliance_num == 0
        raise ValueError("Invalid aggregation type")


def generate_random_content(level: NodeType, dummy: bool = False) -> Constraint:
    if dummy:
        return Constraint(dummy=dummy)
    if level == NodeType.PARAGRAPH:
        constraint = generate_paragraph_constraint()
    elif level == NodeType.SENTENCE:
        constraint = generate_sentence_constraint()
    elif level == NodeType.WORD:
        constraint = generate_word_constraint()
    elif level == NodeType.CONTENT:
        constraint = generate_content_constraint()
    else:
        raise ValueError("Invalid level")
    return constraint
