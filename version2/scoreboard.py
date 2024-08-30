from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=280)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write('GAME OVER!', align=ALIGNMENT, font=('Arial', 24, 'normal'))

    def score_record(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
