import os
from unittest.mock import patch

import openai

from Utils.CodeWrapper import CodeWrapper


class Inspectors:
    def __init__(self, codes: list[CodeWrapper]):
        self.codes = codes

    def inspect(self):
        results = []
        for code in self.codes:
            result = code.execute()
            if result is not None:
                results.append(str(result))
        return ' '.join(results)

    import openai
    from Utils.CodeWrapper import CodeWrapper

    class Inspectors:
        def __init__(self, codes: list[CodeWrapper]):
            self.codes = codes

        def inspect(self):
            results = []
            for code in self.codes:
                result = code.execute()
                if result is not None:
                    results.append(str(result))
            return ' '.join(results)

        class MockResponse:
            def __init__(self):
                self.choices = [{'text': 'Your specific string'}]

        # Mock the 'openai.ChatCompletion.create' method
        @patch('openai.ChatCompletion.create', return_value=MockResponse())
        def generate_code(self, prompt: str, mock_create):
            openai.api_type = "azure"
            openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
            openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
            openai.api_version = "2023-05-15"

            response = openai.ChatCompletion.create(
                engine="gpt-35-turbo",  # engine = "deployment_name".
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
                    {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
                    {"role": "user", "content": "Do other Azure AI services support this too?"}
                ]
            )

            code_snippets = response.choices[0].text.strip().split('\n ---------- \n')
            for code in code_snippets:
                try:
                    code_wrapper = CodeWrapper(code)
                    self.codes.append(code_wrapper)
                except ValueError as e:
                    print(f"Error compiling code: {e}")
