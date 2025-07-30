from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        pirateships_count = len([s for s in self.ships if isinstance(s, PirateBattleship)])
        ships_names = ", ".join([s.name for s in self.get_ships()])
        result = (f"@Royal Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Royal Zone: {len(self.ships)}, {pirateships_count} out of them are Pirate Battleships.\n")

        result += "#" + ships_names + "#" if ships_names else ""
        return result
