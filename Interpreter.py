import turtle
import LSystem


class Interpreter(object):

    def __init__(self, distance, angle):
        self.woodland = turtle.Screen()
        self.franklin = turtle.Turtle()
        # Turtle Configuration
        self.franklin.speed(0)
        self.franklin.hideturtle()
        # A lazy way of repositioning turtle. Redo this with a new coordinate system
        self.franklin.penup()
        self.franklin.back(200)
        self.franklin.pendown()

        self.stack = []
        self.dist = distance
        self.angle = angle
        self.rules = {
            "F": self.fwd,
            "f": self.no_pen_fwd,
            "-": self.l,
            "+": self.r,
            "[": self.save_state,
            "]": self.load_state,
        }

    def fwd(self):
        # Move the turtle forward by a specified distance
        self.franklin.forward(self.dist)

    def no_pen_fwd(self):
        # Move the turtle forward, but don't draw anything
        self.franklin.penup()
        self.fwd()
        self.franklin.pendown()

    def l(self):
        # Make the turtle turn (theta) degrees left from current
        # heading
        self.franklin.left(self.angle)

    def r(self):
        self.franklin.right(self.angle)

    def save_state(self):
        # Create a tuple which represents the turtles current position
        # Then save this to the stack
        state = (self.franklin.pos(), self.franklin.heading())
        self.stack.append(state)

    def load_state(self):
            # Pop the last state saved, and use it to set the turtle's
            # position
            self.franklin.penup()
            state = self.stack.pop()
            self.franklin.setposition(state[0])
            self.franklin.setheading(state[1])
            self.franklin.pendown()

    def draw(self, code_string):
        """
        :param code_string: The string produced by an l-system
        :return: A drawing done by the interpreter's turtle
        """
        for char in code_string:
            try:
                self.rules[char]()
            except KeyError:
                pass
            except:
                raise


terp = Interpreter(7, 90)
print terp.dist
alpha = ['F','f', '+', '-','[', ']']
axiom = 'F-F-F-F'
prod = {
    'F' : 'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'
}
bush = LSystem.LSystem(alpha, axiom, prod)
data = bush.produce_string(2)
terp.draw(data)
turtle.mainloop()