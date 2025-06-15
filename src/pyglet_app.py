import pyglet

# Create a window that is large enough to fill most screens but still has window decorations
# Using a common resolution that should work on most displays
window = pyglet.window.Window(
    width=1920,
    height=1080,
    caption="Pyglet App"
)
# Maximize the window to fill the screen
window.maximize()

# Set background color (RGB: 30, 30, 30)
background_color = (30/255, 30/255, 30/255, 1)  # RGBA format normalized to 0-1

@window.event
def on_draw():
    # Clear the window with the specified color
    pyglet.gl.glClearColor(*background_color)
    window.clear()

@window.event
def on_key_press(symbol, modifiers):
    # Exit when Escape key is pressed
    if symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()
        return True

if __name__ == "__main__":
    # Start the application
    pyglet.app.run()
