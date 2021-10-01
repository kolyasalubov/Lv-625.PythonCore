"""
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = new Ball();
ball2 = new Ball("super");

ball1.ballType     //=> "regular"
ball2.ballType     //=> "super"
"""

class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
    def ballType(self):
        return (self.ball_type)
ball1 = Ball()
ball2 = Ball("super")
print(ball1.ballType())   
print(ball2.ballType())    