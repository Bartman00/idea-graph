import pyglet

class PhysicsBody:
    def __init__(self, size: float, color: list[float, float, float, float]=[1.0, 1.0, 1.0, 1.0],
                 mass: float=1.0, charge: float=0.0, 
                 position: list[float, float]=[0, 0], 
                 velocity: list[float, float]=[0.0, 0.0]):
        """Construct a physics body with size, color, mass, charge, position, and velocity.

        Args:
            size (float): Size to display in the pyglet app
            color (list[float, float, float, float]): Color in RGBA format, where each value is between 0.0 and 1.0.
                Defaults to white [1.0, 1.0, 1.0, 1.0].
            mass (float): Mass of the body, used in for both momentum and gravity. Defaults to 1.0.
            charge (float): Charge of the body, used in electric fields. Defaults to 0.0.
            position (list[float, float], optional): Position of the body. Defaults to [0.0, 0.0].
            velocity (list[float, float], optional): Velocity of the body. Defaults to [0.0, 0.0].
        """
        self.size = size
        self.mass = mass
        self.charge = charge
        self.color = color
        self.velocity = velocity
        self.position = position

    def shape(self, batch=None) -> pyglet.shapes.Circle:
        x, y = self.position
        self.circle = pyglet.shapes.Circle(
            x, y, self.size, color=self.color, batch=batch
        )
        return self.circle
    
    def update_position(self):
        """Update the position of the body in the pyglet app."""
        
        if not hasattr(self, 'circle'):
            raise AttributeError("Circle shape not created. Call 'shape()' method first.")
        
        self.circle.x = self.position[0]
        self.circle.y = self.position[1]