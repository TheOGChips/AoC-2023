
def what_color (s: str):
    return 'red' if 'red' in s else 'blue' if 'blue' in s else 'green' if 'green' in s else None

def main ():
    with open('input.txt', 'r') as infile:
        text = infile.read()

    MAX_RED = 12
    MAX_BLUE = 14
    MAX_GREEN = 13
    games_possible = []
    for count, line in enumerate(text.splitlines()):
        #red = 0
        #blue = 0
        #green = 0
        num_cubes = 0
        impossible = False
        for item in line.split():
            if item.isnumeric():
                num_cubes = int(item)
            else:
                color = what_color(item)
                if color == 'red' and num_cubes > MAX_RED:
                    impossible = True
                elif color == 'blue' and num_cubes > MAX_BLUE:
                    impossible = True
                elif color == 'green' and num_cubes > MAX_GREEN:
                    impossible = True

        if not impossible:
            games_possible.append(count + 1)

    print('sum:', sum(games_possible))

if __name__ == '__main__':
    main()
