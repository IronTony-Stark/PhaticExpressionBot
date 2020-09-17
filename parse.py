from typing import Dict, List

from exceptions import NoQuestionException, NoAnswersException


def parseTemplates(file: str) -> Dict[str, List[str]]:
    question_answers = {}

    with open(file, "r") as f:
        statement = ""
        answers = []

        for line in f:
            line = line.strip()
            if line:
                if line[0] == "@":
                    if statement:
                        answers.append(line[1:])
                    else:
                        raise NoQuestionException()
                elif not statement:
                    statement = line
                elif not answers:
                    raise NoAnswersException()
                else:
                    question_answers[statement] = answers
                    statement = line
                    answers = []

        if statement and not answers:
            raise NoAnswersException()
        else:
            question_answers[statement] = answers

    return question_answers


def parseDefaults(file: str) -> List[str]:
    defaults = []

    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                defaults.append(line)

    return defaults
