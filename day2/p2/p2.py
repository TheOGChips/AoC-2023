
def what_color (s: str):
    return 'red' if 'red' in s else 'blue' if 'blue' in s else 'green' if 'green' in s else None

def main ():
    with open('input.txt', 'r') as infile:
        text = infile.read()

    min_sets = []
    for count, line in enumerate(text.splitlines()):
        red = blue = green = 0
        num_cubes = 0
        for item in line.split():
            if item.isnumeric():
                num_cubes = int(item)
            else:
                color = what_color(item)
                if color == 'red':
                    red = num_cubes if num_cubes > red else red
                elif color == 'blue':
                    blue = num_cubes if num_cubes > blue else blue
                elif color == 'green':
                    green = num_cubes if num_cubes > green else green

        min_sets.append((red, green, blue))

    print('sum:', sum([r*g*b for r, g, b in min_sets]))

if __name__ == '__main__':
    main()
