from __future__ import unicode_literals, print_function


def mask_fields(dictionary, fields_to_mask, show_num_chars=2):
    """
    Takes a dictionary and iterates through it and any sub-dictionaries masking any desired fields
    :param dict dictionary:
    :param list fields_to_mask:
    :param int show_num_chars: Number of characters to show at the beginning
    :return:
    """
    if not dictionary or not isinstance(dictionary, dict):
        return dictionary
    for field, value in dictionary.iteritems():
        if field in fields_to_mask:
            dictionary[field] = mask_string(value)
        if isinstance(value, dict):
            dictionary[field] = mask_fields(value, fields_to_mask, show_num_chars)
    return dictionary


def mask_string(text, show_num_chars=2):
    """
    Masks a string, keeping the show_num_chars at the beginning
    :param string text:
    :param int show_num_chars:
    :return:
    """
    if not isinstance(text, basestring):
        return text
    return text[0:show_num_chars].ljust(len(text), "*")
