GREETINGS = {
    "en": "Hello, {name}!",
    "zh": "你好，{name}！",
}

DEFAULT_NAMES = {
    "en": "world",
    "zh": "世界",
}


def greet(name=None, lang="en"):
    """Return a friendly greeting in the requested language.

    Args:
        name: Who to greet. Defaults to a language-appropriate word
            (e.g. "world" / "世界") when not provided.
        lang: Language code, "en" for English or "zh" for Chinese.
            Falls back to English for unknown codes.
    """
    if lang not in GREETINGS:
        lang = "en"
    if name is None:
        name = DEFAULT_NAMES[lang]
    return GREETINGS[lang].format(name=name)


if __name__ == "__main__":
    print(greet())
    print(greet(lang="zh"))
