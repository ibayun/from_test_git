def check_ice_cream(ball):
    for i in range( 0, ball, 3):
        if ball % 3 == 0 or ball % 5 == 0 or (ball - i) % 5 == 0:
            return True


if __name__ == "__main__":
    """ 
    Ivan, why did you write dump message?
    """
    ball = int(input('Hi  everyone!!! enter the numbers of balls-'))
    print("yes" if check_ice_cream(ball) else "no")
