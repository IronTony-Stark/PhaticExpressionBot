from typing import List, Tuple, Dict

from exceptions import NoStatementsException, NoAnswersException


def parse_templates(file: str) -> Dict[int, List[Tuple[List[str], List[str]]]]:
    priority_list = {k: [] for k in range(1, 6)}

    with open(file, "r") as f:
        statements = []
        answers = []
        priority = 5

        for line in f:
            line = line.strip()
            if line:
                if line[0] == '~':
                    priority = int(line[1])
                    text_start_from = 3
                elif line[0] != '@':
                    priority = 5
                    text_start_from = 1
                else:
                    text_start_from = 1

                if line[text_start_from - 1] == "#":
                    statements.append(line[text_start_from:])
                elif line[text_start_from - 1] == "@":
                    if statements:
                        answers.append(line[text_start_from:])
                    else:
                        raise NoStatementsException()
            else:
                if answers:
                    priority_list[priority].append((statements, answers))
                    answers = []
                    statements = []

        if statements and not answers:
            raise NoAnswersException()
        else:
            priority_list[priority].append((statements, answers))

    return priority_list


def parse_defaults(file: str) -> Dict[int, List[str]]:
    defaults = {k: [] for k in range(1, 6)}

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                if line[0] == '~':
                    priority = int(line[1])
                    text_start_from = 2
                else:
                    priority = 5
                    text_start_from = 0

                defaults[priority].append(line[text_start_from:])

    return defaults
