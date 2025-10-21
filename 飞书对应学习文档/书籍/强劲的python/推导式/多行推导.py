def double_short_words(words):
    return [
        word+word
        for word in words
        if len(word) < 5
    ]