import random
import re
from typing import Optional

from parse import parse_templates, parse_defaults

templates = parse_templates("templates.txt")
defaults = parse_defaults("defaults.txt")
# print(templates)
# print(defaults)


def get_default_answer() -> str:
    return random.choice(defaults)


def get_answer(query: str) -> Optional[str]:
    for statements, answers in templates:
        for statement in statements:
            result = re.search(statement.lower(), query.lower())
            if result:
                groups = result.groups()
                if groups:
                    return random.choice(answers).format(*groups)
                else:
                    return random.choice(answers)
    return None


if __name__ == '__main__':
    print("Hello there :)")
    while True:
        userInput = input('> ')
        if not userInput:
            continue
        if userInput.lower() == "bye":
            print(get_answer('bye'))
            break
        answer = get_answer(userInput)
        if not answer:
            answer = random.choice(defaults)
        print(answer)
