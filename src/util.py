class EdgeDetection:
    def __init__(self, value):
        self.prev_val = value

    def is_rising_edge(self, value):
        edge = 0
        if self.prev_val < value:
            edge = 1
        else: edge = 0

        self.prev_val = value
        return edge

    def is_falling_edge(self, value):
        if self.prev_val > value:
            return 1
