"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""", 'Original Story'
)
story2 = Story(
    ["noun1", "verb1", "verb2", "noun2", "adjective"],
    """One day, while a {noun1} was {verb1}ing, he {verb2}ed a {noun2}. It was a {adjective} day.""", "An Unexpected Day"
)
story3 = Story(
    ['plural_noun', 'verb', 'noun1', 'noun2', 'adjective', 'adjective2'],
    """Many years ago, when the {plural_noun} were always {verb}ing. My {noun1} found a secret {noun2}. It was {adjective} and {adjective2}""", "Secret Tales"
)

stories = {s.title: s for s in [story1, story2, story3]}

