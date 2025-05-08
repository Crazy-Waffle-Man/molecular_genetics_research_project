from python_utils.pgone import *
class button(SpriteActor):
    def mouse_collision_bool(self, mouse_pos):
        """
        Use in on_mouse_down(pos) or on_mouse_move(pos) as follows:\n
        def on_mouse_down/move(pos):
            if self.mouse_collision_bool(pos):
                #Your code goes here
        """
        if self.bottom >= mouse_pos[1] and self.top <= mouse_pos[1] and self.right >= mouse_pos[0] and self.left <= mouse_pos[0]:
            return True
        else:
            return False
    
    def get_filename(self):
        return self.sprite.filename