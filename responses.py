from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Well you're awfully silent..."
    elif "hello" in lowered or "hi" in lowered:
        return "Hello there!"
    elif ":d" in lowered:
        return ":D"
    else:
        return choice(["erm... what the scallop?",
                       "chat, what is this?",
                       "meow?"])