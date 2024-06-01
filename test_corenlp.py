#!/usr/bin/env python
from nlplogic import corenlp


def test_search_wiki():
    name = "OpenAI"
    result = corenlp.search_wiki(name)
    assert "OpenAI" in result


def test_summarize_wiki():
    name = "OpenAI"
    result = corenlp.summarize_wiki(name)
    assert "OpenAI" in result
