#!/usr/bin/env python


from nlplogic import corenlp
from fire import Fire


def get_phrases(name: str):
    """Get noun phrases from name"""
    return corenlp.get_noun_phrases(name)


if __name__ == "__main__":
    Fire(get_phrases)
