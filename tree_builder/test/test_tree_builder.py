import unittest

from tree_builder.tree_classes.Tree import Tree

if __name__ == '__main__':
    text = ("The garden was a blend of colors, with flowers ranging from deep violet to bright yellow."
            " Bees buzzed gently from bloom to bloom, contributing to the serene atmosphere."
            " The air was filled with the sweet fragrance of roses and jasmine, creating"
            " a sense of tranquility and peace. "
            "\n"
            "In the city, the streets were alive with the sound of bustling people and cars honking."
            " The tall buildings stretched towards the sky, windows reflecting the bright sunlight."
            " Amidst the chaos, a small café offered a quiet escape, where the aroma of fresh coffee"
            " and the sound of soft music provided a comforting respite.")

    for i in range(10):
        tree = Tree(simple=True)
        print("generate a text that has a ", tree.format_response())
        if tree.validate_content(text):
            print("Correct")
            print("--------------------")
        else:
            print("Incorrect")
            print("--------------------")

    unittest.main()
