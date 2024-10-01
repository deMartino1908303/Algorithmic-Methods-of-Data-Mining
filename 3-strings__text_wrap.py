import textwrap

def wrap(string, max_width):
    splitted = textwrap.wrap(string, max_width)
    return "\n".join(splitted)


if __name__ == '__main__':
