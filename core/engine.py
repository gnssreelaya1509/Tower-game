class TowerEngine:
    def __init__(self):
        self.stack = [{"x": 0, "width": 200}]  # Base block
        self.speed = 5

    def calculate_cut(self, new_x, current_width):
        # Math to check overlap
        top_block = self.stack[-1]
        diff = abs(new_x - top_block["x"])

        if diff >= current_width:
            return 0  # Game over

        new_width = current_width - diff
        return new_width