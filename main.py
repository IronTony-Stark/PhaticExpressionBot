import random
import re
from typing import Optional, Dict, List, Tuple

from parse import parse_templates, parse_defaults

templates = parse_templates("templates.txt")
templates_used: List[Tuple[List[str], Dict[str, int]]] =\
    [(statements, {answer: 0 for answer in answers}) for statements, answers in templates]
defaults = parse_defaults("defaults.txt")
defaults_used: Dict[str, int] = {k: 0 for k in defaults}


# print(templates_used)
# print(defaults)


def get_min_used_replies(possible_replies: Dict[str, int]) -> List[str]:
    min_used = min(possible_replies.values())
    return [ans for ans, used_count in possible_replies.items() if used_count == min_used]


def get_default_answer() -> str:
    print(defaults_used)
    answers_to_use = get_min_used_replies(defaults_used)
    used_answer = random.choice(answers_to_use)
    defaults_used[used_answer] += 1
    return used_answer


def get_answer(query: str) -> Optional[str]:
    for i, (statements, answers) in enumerate(templates):
        for statement in statements:
            result = re.search(statement.lower(), query.lower())
            if result:
                possible_replies = templates_used[i][1]
                answers_to_use = get_min_used_replies(possible_replies)
                print(answers_to_use)
                groups = result.groups()
                used_answer = random.choice(answers_to_use)
                possible_replies[used_answer] += 1
                if groups:
                    return used_answer.format(*groups)
                else:
                    return used_answer
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
            answer = get_default_answer()
        print(answer)
