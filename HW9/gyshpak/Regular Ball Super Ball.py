class Ball(object):
    # your code goes here
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

B1 = Ball()
B2 = Ball("super")

print(B1.ball_type)
print(B2.ball_type)
