from typing import List, Tuple

from exceptions import NoStatementsException, NoAnswersException


def parse_templates(file: str) -> List[Tuple[List[str], List[str]]]:
    question_answers = []

    with open(file, "r") as f:
        statements = []
        answers = []

        for line in f:
            line = line.strip()
            if line:
                if line[0] == "#":
                    if answers:
                        question_answers.append((statements, answers))
                        statements = [line[1:]]
                        answers = []
                    else:
                        statements.append(line[1:])
                elif line[0] == "@":
                    if statements:
                        answers.append(line[1:])
                    else:
                        raise NoStatementsException()

        if statements and not answers:
            raise NoAnswersException()
        else:
            question_answers.append((statements, answers))

    return question_answers


def parse_defaults(file: str) -> List[str]:
    defaults = []

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                defaults.append(line)

    return defaults
