def knight(me: tuple[int, int], enemy: tuple[int, int]) -> bool:
    dx = abs(me[0] - enemy[0])
    dy = abs(me[1] - enemy[1])
    return (dx, dy) in [(1, 2), (2, 1)]


def queen(me: tuple[int, int], enemy: tuple[int, int]) -> bool:
    dx = abs(me[0] - enemy[0])
    dy = abs(me[1] - enemy[1])
    return dx == dy or me[0] == enemy[0] or me[1] == enemy[1]
