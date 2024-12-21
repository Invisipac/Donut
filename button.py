import pygame as pg

class Button:
    def __init__(self, rect: pg.Rect):
        self.rect = rect
        self.colour = (255, 255, 255)
        self.press_down = False
        self.release_press = True
    
    def press_or_release_button(self):
        m_x, m_y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
        if self.rect.left < m_x < self.rect.right and self.rect.top < m_y < self.rect.bottom:
            return True
        
        return False
    
    def set_button_pressed_down(self, val: bool):
        self.press_down = val
            
    def set_button_release(self, val: bool):
        self.release_press = val
    
    def draw_button(self, screen: pg.Surface):
        pg.draw.rect(screen, self.colour, self.rect)