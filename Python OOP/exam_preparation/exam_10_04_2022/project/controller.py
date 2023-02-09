from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def _find_player(self, p_name):
        player = [x for x in self.players if x.name == p_name]
        if player:
            return player[0]

    def _get_suppl_by_type(self, type):
        for idx in range(len(self.supplies) -1, -1, -1):
            if self.supplies[idx].__class__.__name__ == type:
                result = self.supplies[idx]
                self.supplies.pop(idx)
                return result

    def add_player(self, *args):
        added = []
        for player in args:
            if player in self.players:
                continue
            self.players.append(player)
            Player.used_names.add(player.name)
            added.append(player.name)

        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player(player_name)
        if not player or sustenance_type not in ["Food", "Drink"]:
            return
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        supply = self._get_suppl_by_type(sustenance_type)

        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        increased_stamina = player.stamina + supply.energy
        player.stamina = increased_stamina if increased_stamina <= 100 else 100
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self._find_player(first_player_name)
        player2 = self._find_player(second_player_name)

        players_low_battery = []
        for player in [player1, player2]:
            if player.stamina == 0:
                players_low_battery.append(f"Player {player.name} does not have enough stamina.")
        if players_low_battery:
            return '\n'.join(players_low_battery)

        player_on_turn = sorted([player1, player2], key=lambda x: x.stamina)
        winner = None

        for _ in range(2):
            player_attacks, player_attacked = player_on_turn
            reduced_stamina = player_attacked.stamina - player_attacks.stamina / 2

            if reduced_stamina <= 0:
                player_attacked.stamina = 0
                winner = player_attacks
                break

            player_attacked.stamina = reduced_stamina
            player_on_turn = player_on_turn[::-1]

        if not winner:
            winner = player_on_turn = sorted([player1, player2], key=lambda x: x.stamina)[-1]

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            reduced_stamina = player.stamina - player.age * 2
            player.stamina = reduced_stamina if reduced_stamina >= 0 else 0
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        output = []
        for player in self.players:
            output.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")
        for supply in self.supplies:
            output.append(f"{type(supply).__name__}: {supply.name}, {supply.energy}")
        return '\n'.join(output)
