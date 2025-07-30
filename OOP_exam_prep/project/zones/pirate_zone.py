from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone (BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        royalships_count = len([s for s in self.ships if isinstance(s, RoyalBattleship)])
        ships_names = ", ".join([s.name for s in self.get_ships()])
        result = (f"@Pirate Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Pirate Zone: {len(self.ships)}, {royalships_count} out of them are Royal Battleships.\n")

        result += "#" + ships_names + "#" if ships_names else ""
        return result
