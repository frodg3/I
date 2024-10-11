import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed

    def __repr__(self):
        return self.name

class Tournament:
    def __init__(self, distance, *participants):  # Здесь все правильно
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in sorted(self.participants, key=lambda x: -x.speed):  # Сортируем по скорости
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break  # Выходим из цикла после финиша

        return finishers

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", speed=10)
        self.runner2 = Runner("Andrei", speed=9)
        self.runner3 = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"{place}: {runner}")

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)  # Позиционные аргументы
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(results.keys()) == 1 and results[1] == self.runner1)

    def test_race_andrei_and_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)  # Позиционные аргументы
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(results.keys()) == 1 and results[1] == self.runner2)

    def test_race_usain_andrei_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)  # Позиционные аргументы
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(results.keys()) == 1 and results[1] == self.runner1)

if __name__ == "__main__":
    unittest.main()
