from textblob import TextBlob
import wikipedia

def search_wiki(name):
    """Search Wikipedia"""
    print(f"searching for {name}")
    try:
        return wikipedia.search(name)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0])
    except wikipedia.exceptions.PageError:
        return "No page found"

def summarize_wiki(name):
    """ Summarize Wikipedia"""  
    print(f"summarizing {name}")
    try:
        return wikipedia.summary(name)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0])
    except wikipedia.exceptions.PageError:
        return "No page found"

def get_text_blob(text):
    """Get TextBlob object"""
    return TextBlob(text)

def get_noun_phrases(name):
    """Get noun phrases from name"""
    text = summarize_wiki(name)
    blob = get_text_blob(text)
    return blob.noun_phrases
