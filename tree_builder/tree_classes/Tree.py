import random

from tree_builder.tree_classes.Node import Node, generate_random_content
from tree_builder.tree_classes.enums import AggregationType, NodeType


def select_aggregation_type(aggregation_value):
    aggregation_types = list(AggregationType)
    if aggregation_value == 3:
        aggregation_types.remove(AggregationType.MORE_THAN)
    elif aggregation_value == 0:
        aggregation_types.remove(AggregationType.LESS_THAN)
    return random.choice(aggregation_types)


class Tree:
    root: Node = None
    simple: bool = False

    def __init__(self, simple: bool = False):
        """
        Initializes the tree with a root node.
        """
        self.simple = simple
        if simple:
            self.root = self.build_simple_tree()
        else:
            self.root = self.build_tree()
            self.remove_duplicate_constraints(self.root)

    def build_simple_tree(self) -> Node:
        """
        Builds a simple tree with a single constraint chosen randomly from different levels.
        The structure is kept the same as content then paragraph then sentence then word.
        """
        level = random.choice(list(NodeType))
        root = Node(generate_random_content(NodeType.CONTENT, dummy=True), level, AggregationType.COUNT, 1)
        if level == NodeType.PARAGRAPH:  # generate a constraint node and exit
            paragraph_node = Node(generate_random_content(NodeType.PARAGRAPH), NodeType.PARAGRAPH,
                                  AggregationType.NONE, 0)
            root.add_child(paragraph_node)
        else:  # generate dummy paragraph constraint node
            paragraph_node = Node(generate_random_content(NodeType.PARAGRAPH, dummy=True), NodeType.PARAGRAPH,
                                  AggregationType.COUNT, 1)
            root.add_child(paragraph_node)
            if level == NodeType.SENTENCE:  # generate a constraint node and exit
                sentence_node = Node(generate_random_content(NodeType.SENTENCE), NodeType.SENTENCE,
                                     AggregationType.NONE, 0)
                paragraph_node.add_child(sentence_node)
            else:  # have to be a word constraint node
                sentence_node = Node(generate_random_content(NodeType.SENTENCE, dummy=True), NodeType.SENTENCE,
                                     AggregationType.COUNT, 1)
                paragraph_node.add_child(sentence_node)
                word_node = Node(generate_random_content(NodeType.WORD), NodeType.WORD, AggregationType.NONE, 0)
                sentence_node.add_child(word_node)
        self.root = root
        return root

    def build_tree(self) -> Node:
        """
        Builds a tree of constraints - at the root level, a content constraint is generated, and then a random number of
        paragraph constraints are generated, each with a random number of sentence constraints, each with a random number of
        word constraints.
        each Node has a constraint, a level, and an aggregation type.
        :return:
        """
        root_children = random.randint(1, 3)
        root_aggregation_value = random.randint(0, root_children)
        root_aggregation = select_aggregation_type(root_aggregation_value)
        root = Node(generate_random_content(NodeType.CONTENT), NodeType.CONTENT, root_aggregation,
                    root_aggregation_value)
        for _ in range(root_children):  # Number of children of root.
            paragraph_children = random.randint(0, 3)
            paragraph_aggregation_value = random.randint(0, paragraph_children)
            paragraph_aggregation = select_aggregation_type(paragraph_aggregation_value)
            paragraph_node = Node(generate_random_content(NodeType.PARAGRAPH), NodeType.PARAGRAPH,
                                  paragraph_aggregation, paragraph_aggregation_value)
            root.add_child(paragraph_node)
            for _ in range(paragraph_children):  # Number of children of each paragraph.
                sentence_children = random.randint(0, 3)
                sentence_aggregation_value = random.randint(0, sentence_children)
                sentence_aggregation = select_aggregation_type(sentence_aggregation_value)
                sentence_node = Node(generate_random_content(NodeType.SENTENCE), NodeType.SENTENCE,
                                     sentence_aggregation, sentence_aggregation_value)
                paragraph_node.add_child(sentence_node)
                for _ in range(sentence_children):  # Number of children of each sentence.
                    word_node = Node(generate_random_content(NodeType.WORD), NodeType.WORD, AggregationType.NONE, 0)
                    sentence_node.add_child(word_node)
        self.root = root
        return root

    def remove_duplicate_constraints(self, node):
        if not node.children:
            return

        constraint_counts = {}
        for child in node.children:
            if child.constraint.constraint_type in constraint_counts:
                constraint_counts[child.constraint.constraint_type] += 1
            else:
                constraint_counts[child.constraint.constraint_type] = 1

        for constraint_type, count in constraint_counts.items():
            if count > 1:
                # Remove extra nodes
                nodes_to_remove = [child for child in node.children if
                                   child.constraint.constraint_type == constraint_type][1:]
                for node_to_remove in nodes_to_remove:
                    node.children.remove(node_to_remove)

        for child in node.children:
            self.remove_duplicate_constraints(child)

    def validate_content(self, content: str) -> bool:
        """
        Validates the content against the constraints of the tree.
        :param content: The content to validate.
        :return: True if the content is valid, False otherwise.
        """
        return self.root.validate_content(content)

    def print_tree(self):
        self.root.print_tree()

    def format_response(self) -> str:
        return self.root.format_response()
