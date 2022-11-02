from font import Font

class Score:
    def __init__(self, surf):
        self.font = Font()
        self.surf = surf
        self.score = 0
        self.score_formatted = f"{self.score:09}"
        self.x = 190
        self.y = 5

    def render(self):
        self.score_formatted = f"{self.score:09}"
        self.font.render(self.surf, self.score_formatted, (self.x, self.y))  # Score system
