from tree_builder.tree_classes.enums import ConstraintType


class Constraint:
    dummy: bool
    instruction: str
    validator_f: callable

    def __init__(self, constraint: str = None, validator_f: callable = None, constraint_type: ConstraintType = None,
                 dummy: bool = False):
        self.dummy = dummy
        self.instruction = constraint
        self.validator_f = validator_f
        self.constraint_type = constraint_type
