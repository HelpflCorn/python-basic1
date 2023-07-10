def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines in {name}: {lines}")
    print(f"Number of characters in {name}: {chars}")

