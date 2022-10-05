def heading(text, level=1):
    if 1 <= level <= 6:
        num_hash = "#" * level
        modified_text = "{} {}".format(num_hash, text)
    elif level < 1:
        num_hash = "#"
        modified_text = "{} {}".format(num_hash, text)
    else:
        num_hash = "#" * 6
        modified_text = "{} {}".format(num_hash, text)
    return modified_text


