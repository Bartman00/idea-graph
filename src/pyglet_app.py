import pyglet
from pyglet.window import key as key

class IdeaGraph(pyglet.window.Window):
    def __init__(self, *args, **kwargs):



        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        background_color = (30/255, 30/255, 30/255, 1)  # Python RGBA format
        pyglet.gl.glClearColor(*background_color)
        pyglet.clock.schedule_interval(self.update, 1/60)

        self.circle = pyglet.shapes.Circle(x=self.width/2, y=self.height/2, radius=100, color=(255, 255, 255), batch=self.batch)
        

    def update(self, dt):
        pass
    
    def on_draw(self):
        window.clear()
        self.batch.draw()

    def on_resize(self, width, height):
        self.circle.delete()
        self.circle = pyglet.shapes.Circle(x=self.width/2, y=self.height/2, radius=100, color=(255, 255, 255), batch=self.batch)
        return super().on_resize(width, height)
    
    def on_key_press(self, symbol, modifiers):
        # Exit when Escape key is pressed
        if symbol == key.ESCAPE:
            pyglet.app.exit()
            return True
        elif symbol == key.LEFT:
            self.circle.x -= 20
        elif symbol == key.RIGHT:
            self.circle.x += 20
        elif symbol == key.UP:
            self.circle.y += 20
        elif symbol == key.DOWN:
            self.circle.y -= 20

    def on_mouse_press(self, x, y, button, modifiers):
        self.circle.x = x
        self.circle.y = y

    def on_mouse_release(self, x, y, button, modifiers):
        self.circle.x = x
        self.circle.y = y

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.circle.x = x
        self.circle.y = y

if __name__ == "__main__":
    # Start the application
    window = IdeaGraph(width=1920, height=1080, caption='Idea Graph', resizable=True)
    window.maximize()
    pyglet.app.run()
