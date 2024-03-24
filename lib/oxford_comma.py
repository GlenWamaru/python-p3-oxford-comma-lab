def oxford_comma(elements):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return " and ".join(elements)
    else:
        comma_separated = ", ".join(elements[:-1])
        return f"{comma_separated}, and {elements[-1]}"
