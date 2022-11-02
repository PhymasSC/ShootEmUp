from configconst import *


class Font():
    def __init__(self):
        self.spacing = 1
        self.character_order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.characters = []
        for i in range(10):
            fname = f"UI_{i}.png"
            new_image = userInterface.get_image_name(fname)
            self.characters.append(new_image)
        self.space_width = self.characters[9].get_width()

    def render(self, surf, text, loc):
        x_offset = 0
        for char in text:
            if char != ' ':
                surf.blit(self.characters[int(char)], (loc[0] + x_offset, loc[1]))
                x_offset += self.characters[int(char)].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing
