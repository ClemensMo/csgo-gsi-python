from information import Player, Map, Provider, PhaseCountdowns, Bomb, Round


class GameState:
    def __init__(self):
        self.player = Player()
        self.map = Map()
        self.provider = Provider()
        self.phase_countdowns = PhaseCountdowns()
        self.bomb = Bomb()
        self.round = Round()

    def prettyprint(self):
        print(f'Player: {self.player.state = }, {self.player.state = }, {self.player.state = }, {self.player.state = },'
              f' {self.player.state = }, {self.player.state = }, {self.player.state = }')
