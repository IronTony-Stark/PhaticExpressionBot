import random
import re
from typing import Optional

from parse import parseTemplates, parseDefaults

templates = parseTemplates("templates.txt")
defaults = parseDefaults("defaults.txt")
print(templates)
print(defaults)


def getDefaultAnswer() -> str:
    return random.choice(defaults)


def getAnswer(query: str) -> Optional[str]:
    for statements, answers in templates:
        for statement in statements:
            if re.search(statement, query):
                return random.choice(answers)
    return None


print("Hello there :)")
while True:
    userInput = input()
    if not userInput:
        continue
    if userInput == "bye":
        print("Bye!")
        break
    answer = getAnswer(userInput)
    if not answer:
        answer = random.choice(defaults)
    print(answer)
