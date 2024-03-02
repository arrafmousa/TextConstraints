from enum import Enum

class ErrorCode(Enum):
    SYNTAX_ERROR = "Syntax Error"
    RUNTIME_ERROR = "Runtime Error"
    UNKNOWN_ERROR = "Unknown Error"

class CodeWrapper:
    def __init__(self, code: str):
        try:
            self.code = compile(code, '<string>', 'exec')
        except SyntaxError:
            raise ValueError(ErrorCode.SYNTAX_ERROR.value)
    def execute(self):
        try:
            exec(self.code)
        except Exception as e:
            if isinstance(e, SyntaxError):
                return ErrorCode.SYNTAX_ERROR.value
            elif isinstance(e, RuntimeError):
                return ErrorCode.RUNTIME_ERROR.value
            else:
                return ErrorCode.UNKNOWN_ERROR.value