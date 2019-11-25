import re


def escape_text(text):
    text = text.encode('unicode_escape').decode()
    text = text.replace('"', r'\"').replace("'", r"\'")
    return text


def unescape_text(text):
    text = text.encode().decode('unicode_escape')
    text = text.replace(r'\"', '"').replace(r"\'", "'")
    return text


def get_id_for_header(header_content):

    pattern_1 = re.compile(r'[ _]')
    replacement_1 = '-'

    pattern_2 = re.compile(r'[^a-zA-Z0-9-]')
    replacement_2 = ''

    res = pattern_1.sub(replacement_1, header_content)
    res = pattern_2.sub(replacement_2, res)
    res = res.lower()

    return res
