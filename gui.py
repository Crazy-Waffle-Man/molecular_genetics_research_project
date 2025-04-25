from pgone import *
class button(SpriteActor):
    def __init__(self):
        """
        A SpriteActor with some extra functionality that detects when a tuple of form (x,y) is within\nthe bounds of the image.
        Args:
            sprite_instance (Sprite): The sprite instance to use for animation.
            position (tuple, optional): Initial position of the actor. Defaults to `POS_TOPLEFT`.
            anchor_point (tuple, optional): Anchor point of the actor. Defaults to `ANCHOR_CENTER`.
            **kwargs: Additional arguments for the base Actor class.
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