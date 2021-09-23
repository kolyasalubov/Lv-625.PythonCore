class Ball():
    """
    class ball has default type 'regular'
    which will show in type request
    can be set to any other type
    """
    def __init__(self, type="regular"):
        self.type = type

ball_one = Ball()
ball_two = Ball("super")
print(ball_one.type)
print(ball_two.type)