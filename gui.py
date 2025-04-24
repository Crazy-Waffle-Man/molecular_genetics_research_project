from pgone import *
class button(SpriteActor):
    def __init__(self):
        """
        A SpriteActor with some extra functionality that detects when a tuple of form (x,y) is within\nthe bounds of the image.
        Args:
            image (str): an image in images/sprites/buttons
            pos (tuple): where to put the center of the image
            frame_width (int): The width of each frame in the sprite sheet.
            frame_height (int): The height of each frame in the sprite sheet.
            row_number (int): The row number (starting from 0) from which the frames will be extracted.
            frame_count (int): The number of frames in the animation.
            fps (int, optional): The number of frames per second for the animation. Defaults to 10.
            transparent_color (tuple, optional): RGB color key for transparency. Defaults to (0, 0, 0).
            scale (float, optional): the scale of the image...
        """
        # Debug prints
        # print(self.SpriteActor)
        # print(self.SpriteActor.sprite)
        # print(self.SpriteActor.sprite.filename)
    def mouse_collision_bool(self, mouse_pos):
        """
        Use in on_mouse_down(pos) or on_mouse_move(pos) as follows:\n
        def on_mouse_down/move(pos):
            if self.mouse_collision_bool(pos):
                #Your code goes here
        """
        if self.SpriteActor.right >= mouse_pos[0] and self.SpriteActor.left <= mouse_pos[0] and self.SpriteActor.top <= mouse_pos[1] and self.SpriteActor.bottom >= mouse_pos[1]:
            return True
        else:
            return False
    
    def get_filename(self):
        return self.sprite.filename