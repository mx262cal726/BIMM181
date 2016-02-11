
def bimm101(text):
    text = open(text)
    lines = text.read().split("\n")
    list_lines = list()
    for i in lines:
        list_lines.append(i)
    return list_lines

print bimm101("input.txt")