from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAIN_VALUE = 2

    def train(self):
        self.speed = min(self.speed + Appaloosa.TRAIN_VALUE, Appaloosa.MAX_SPEED)
