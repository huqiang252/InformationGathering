

class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(self, coord):
        return coord in self.limits


if __name__ == '__main__':
    grid = Grid(6, 10)
    print((1,1) in grid)
    print((5,3) in grid)
    print((7,6) in grid)  #False


