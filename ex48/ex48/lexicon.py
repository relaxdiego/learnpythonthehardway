directions = ["north", 
              "south", 
              "east", 
              "west", 
              "down", 
              "up", 
              "left", 
              "right", 
              "back"]

nouns = ["door", "bear", "princess", "cabinet"]

stops = ["the", "in", "of", "from", "at", "it"]

verbs = ["eat", "go", "kill", "stop"]


def scan(keywords):
    keywords = keywords.split()
    tokens = []

    for keyword in keywords:
        if keyword in directions:
            tokens.append(("direction", keyword))
        elif keyword in stops:
            tokens.append(("stop", keyword))
        elif keyword in verbs:
            tokens.append(("verb", keyword))
        elif keyword in nouns:
            tokens.append(("noun", keyword))
        elif keyword.isdigit():
            tokens.append(("number", int(keyword)))
        else:
            tokens.append(("error", keyword))

    return tokens
