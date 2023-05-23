from typing import List, Tuple
from math import sqrt


def hp(a, b) -> float:
    ab = sorted([a[0]-b[0], a[1]-b[1]])
    ab[0] = ab[0] * (-1) if ab[0] < 0 else ab[0]
    ab[1] = ab[1] * (-1) if ab[1] < 0 else ab[1]

    return sqrt(ab[0]**2 + ab[1]**2)


def ct(a, b) -> float:
    ab = sorted([a[0]-b[0], a[1]-b[1]])
    ab[0] = ab[0] * (-1) if ab[0] < 0 else ab[0]
    ab[1] = ab[1] * (-1) if ab[1] < 0 else ab[1]

    return sqrt(ab[1]**2 - ab[0]**2)


def cl(d) -> float:
    p = [0, 0]
    p[0] = sorted([d[0][0], d[1][0], d[2][0]])[0] * (-1) if p[0] == 0 else p[0]
    p[1] = sorted([d[0][1], d[1][1], d[2][1]])[0] * (-1) if p[1] == 0 else p[1]

    a = [d[0][0] + p[0], d[0][1] + p[1]]
    b = [d[1][0] + p[0], d[1][1] + p[1]]
    c = [d[2][0] + p[0], d[2][1] + p[1]]

    ab = hp(a, b) if a[0] != b[0] or a[1] != b[1] else ct(a, b)
    ac = hp(a, c) if a[0] != c[0] or a[1] != c[1] else ct(a, c)
    bc = hp(b, c) if b[0] != c[0] or b[1] != c[1] else ct(b, c)

    r = sorted([ab, ac, bc])

    h = sqrt((r[-1]**2) - ((r[1]/2)**2))
    x = (r[-1] * h)/2
    print(f"[{a}, {b}, {c}]")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"ab = {ab}, ac = {ac}, bc = {bc}")
    print(f"base: {ab} altura: {h} área: {x}")

    return x


def similar_triangles(coords_1: List[Tuple[int, int]], coords_2: List[Tuple[int, int]]) -> bool:
    t1 = cl(coords_1)
    t2 = cl(coords_2)
    if t1 > t2:
        if t1 % t2 == 0:
            return True
    elif t1 < t2:
        if t2 % t1 == 0:
            return True
    else:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([[1, 3], [4, 2], [2, 1]],
          [[2, -2], [0, -3], [-1, -1]]))
