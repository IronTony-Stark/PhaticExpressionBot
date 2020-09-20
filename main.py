import random
import re
from typing import Optional, Dict, List, Tuple

from parse import parse_templates, parse_defaults

priority_templates = parse_templates("templates.txt")
templates_used: Dict[int, List[Tuple[List[str], Dict[str, int]]]] = \
    {k: [(statements, {answer: 0 for answer in answers}) for statements, answers in v] for k, v in
     priority_templates.items()}
del priority_templates

defaults = parse_defaults("defaults.txt")
defaults_used: Dict[int, Dict[str, int]] = {k: {default: 0 for default in v} for k, v in defaults.items()}
del defaults


def get_min_used_replies(possible_replies: Dict[str, int]) -> List[str]:
    min_used = min(possible_replies.values())
    return [ans for ans, used_count in possible_replies.items() if used_count == min_used]


def get_min_unused_defaults(possible_replies: Dict[int, Dict[str, int]]) -> int:
    min_used = 5
    prior = 5
    for priority, default_list in possible_replies.items():
        if not default_list:
            continue
        for used_count in default_list.values():
            if used_count < min_used:
                min_used = used_count
                prior = priority
    return prior


def get_default_answer() -> str:
    min_unused_priority = get_min_unused_defaults(defaults_used)
    answers_to_use = get_min_used_replies(defaults_used[min_unused_priority])
    used_answer = random.choice(answers_to_use)
    defaults_used[min_unused_priority][used_answer] += 1
    return used_answer


def get_answer(query: str) -> Optional[str]:
    for priority, templates in templates_used.items():
        for i, (statements, answers) in enumerate(templates):
            for statement in statements:
                result = re.search(statement.lower(), query.lower())
                if result:
                    possible_replies = templates_used[priority][i][1]
                    answers_to_use = get_min_used_replies(possible_replies)
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
