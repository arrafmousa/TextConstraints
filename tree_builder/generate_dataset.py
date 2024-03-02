from TreeBuilder import build_tree


class GenerateDataset:
    """
    Constraints types :
        * Word :
            generate a word that is a {noun / verb/ adjective}
            generate a word that has {> n letters / < n letters / n letters}
            generate a word that is an anagram with {word} (has the same letters)
            generate a word that is a palindrome
            generate a word that {ends/starts} with {letter / letters}

        * Sentence:
            Initial words consist a sentene cr word
            generate a sentence that has {> n words / < n words / n words}
            generate a sentence that has {> n characters / < n characters / n characters}
            generate a sentence that is a palindrome (read the same forward and backward)
            generate a sentence that is an anagram with {sentence} (has the same words)
            generate a sentence that {ends/starts} with {word}
            generate a sentence that has the {word} {exactly / more} than {n} times

        * Paragraph:
            generate a paragraph that has {> n sentences / < n sentences / n sentences}
            generate a paragraph that has {> n words / < n words / n words}
            generate a paragraph and do not use {word-s}

        * Format:
            generate a haiku
            generate a json
            generate a csv
            generate a latex
            generate a text with {symbol} between each word { / not between {words}}

    Multiple constraints:
        A generation prompt can include multiple constraints, where each constrain can include conditions from multiple
         types that are mentioned above. For example, a prompt can ask to generate a paragraph where each sentence has
         more than n words, and each word starts with the letter 'r'.

         The constraint can be on {all / most / {> / < / == } n %} of the {word / sentence / paragraph} in the
         generated dataset.

    """

    def generate_dataset(self):
        for i in range(10):
            print(f"------{i}-------")
            root_node = build_tree()
            print("generate a paragraph" + root_node.format_response())

generator = GenerateDataset()
generator.generate_dataset()
