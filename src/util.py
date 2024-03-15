class EdgeDetection:
    def __init__(self, value):
        self.prev_val = value

    # Mostly used to toggle things on button press
    # Rising edge
    def is_redge(self, value):
        edge = False
        if self.prev_val < value:
            edge = True

        self.prev_val = value
        return edge

    # Mostly used to toggle things on button release
    # Falling edge
    def is_fedge(self, value):
        edge = False
        if self.prev_val > value:
            edge = True

        self.prev_val = value
        return edge

    # Not sure what the use case is, but I added it before I realized that
    def is_edge(self, value):
        edge = False
        if not self.prev_val == value:
            edge = True

        self.prev_val = value
        return edge
