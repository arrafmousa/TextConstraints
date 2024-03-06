from Utils.Inspectors import Inspectors
from unittest.mock import patch

def mock_chat_completion_create(engine, messages):
    class MockResponse:
        @property
        def choices(self):
            return [{"text": "mocked response"}]
    return MockResponse()

@patch('openai.ChatCompletion.create', new=mock_chat_completion_create)
def test_inspect():
    inspector = Inspectors("write a text with 10 words")
    result = inspector.inspect()
    print(result)  # This should print "mocked response"



test_inspect()