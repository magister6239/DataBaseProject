import random


def random_color_pick(r:set=(0, 255), g:set=(0, 255), b:set=(0, 255)):
    r = random.randint(r[0], r[1])
    g = random.randint(g[0], g[1])
    b = random.randint(b[0], b[1])

    return f'#{r:02x}{g:02x}{b:02x}'
