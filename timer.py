import time, mouse
from kivy.app import App
from kivy.lang import Builder
from datetime import datetime
from threading import Thread
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from KivyOnTop import register_topmost, unregister_topmost
from kivy.uix.button import Button  
Window.size=(260,50)
Builder.load_string("""
<Drag_option>:
<timer_class>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos:self.pos
            size:self.size

    Drag_option:
        id:Drag_button
        size_hint:.000001,.0000001
        background_color:  0,0,0,0
        
    Widget:
        canvas:
            Color:
                rgba: .5, .5, .5, 1
            Line:
                width: 5
                rectangle: self.x, self.y, self.width, self.height
    Label:
        id:timer_label
        font_size:self.height/2.7
        font_name:'Arial'
        markup:True
   """)

TITLE = 'SanTime'
Window.borderless = True 

class Drag_option(Button):
    def on_touch_down(self, touch):         
        self.window_left, self.window_top = Window.left, Window.top 
        self.touch_x, self.touch_y = mouse.get_position()[0], mouse.get_position()[1]
        return super(Drag_option, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        horizontal_movement = mouse.get_position()[0] - self.touch_x
        Vertical_movement = mouse.get_position()[1] - self.touch_y 
        if Window.height >= 50 and Window.height <= 100:
            Window.top = self.window_top + Vertical_movement
            Window.left = self.window_left + horizontal_movement
        else:
            pass
        return super(Drag_option, self).on_touch_move(touch)

class timer_class(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Thread(target = self.timer_loop).start()

    def timer_loop(self):
        while True:
            date=datetime.strftime(datetime.now(),'%d-%m-%Y %I:%M:%S:%p')
            self.ids["timer_label"].text = f"[b][color=#4D12F6]{date}"
            time.sleep(1)
        

class timerApp(App):
    def build(self):
        return timer_class()

    def on_start(self, *args):
        Window.set_title(TITLE)

        # Register top-most
        register_topmost(Window, TITLE)

        # Unregister top-most (not necessary, only an example)
        self.bind(on_stop=lambda *args, w=Window, t=TITLE: unregister_topmost(w, t))

if __name__ == '__main__':
    timerApp().run()
