def parse(file):
    loaded = []
    with open(file, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.split(" ")
        # TODO: make real validation
        if len(line) < 4: 
            continue
        tmst = line[0] + " " + line[1]
        lvl = line[2]
        msg = " ".join(line[3:]).strip()
        loaded.append({
            "timestamp": tmst,
            "level": lvl,
            "message": msg,
            })
    return loaded


if __name__ == "__main__":
    import pprint
    l = parse(input("Enter the text file to parse: "))
    pprint.pprint(l, sort_dicts=False)
