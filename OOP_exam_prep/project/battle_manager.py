from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


zone_mapper = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
ship_mapper = {"RoyalBattleship": RoyalBattleship, "PirateBattleship":PirateBattleship}
def sum_nums(a, b):
    return a + b
mapper = {"+": sum_nums}

def do_something(sign, a,b):
    mapper[sign](a,b)




class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in zone_mapper:
            raise Exception("Invalid zone type!")
        # try:
        #     next(z for z in self.zones if z.code == zone_code)
        #     raise Exception("Zone already exists!")
        # except StopIteration:
        #     zone = zone_mapper[zone_type](zone_code)

        # try:
        #     [z for z in self.zones if z.code == zone_code][0]
        #     raise Exception("Zone already exists!")
        # except IndexError:
        #     zone = zone_mapper[zone_type](zone_code)

        zone = next((z for z in self.zones if z.code == zone_code), None)
        if zone is not None:
            raise Exception("Zone already exists!")
        zone = zone_mapper[zone_type](zone_code)

        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."


    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in ship_mapper:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        ship = ship_mapper[ship_type](name, health, hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    # Todo check this might be static?
    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if ((isinstance(ship, PirateBattleship) and isinstance(zone, PirateZone)) or
                (isinstance(ship, RoyalBattleship) and isinstance(zone, RoyalZone))):
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if ship is None:
            return f"No ship with this name!"
        if not ship.is_available:
            return f"The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."


    def start_battle(self, zone: BaseZone):
        attacking_ships = [s for s in zone.ships if s.is_attacking]
        target_ships = [s for s in zone.ships if not s.is_attacking]

        ship_type = RoyalBattleship
        if isinstance(zone, PirateZone):
            ship_type = PirateBattleship

        target_ship_type = RoyalBattleship if isinstance(zone, PirateZone) else PirateBattleship

        if not attacking_ships or not target_ships:
            return "Not enough participants. The battle is canceled."

        sorted_attackers = sorted(attacking_ships, key=lambda ship: -ship.hit_strength)
        attacker = next(s for s in sorted_attackers if isinstance(s, ship_type))

        sorted_targets = sorted(target_ships, key=lambda ship: -ship.health)
        target = next(s for s in sorted_targets if isinstance(s, target_ship_type))

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."


    def get_statistics(self):
        available_ships = [s.name for s in self.ships if s.is_available]
        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{', '.join(available_ships)}#\n" if available_ships else ""
        ordered_zones = sorted(self.zones, key=lambda zone: zone.code)
        result += f"***Zones Statistics:***\nTotal Zones: {len(self.zones)}\n"
        result += "\n".join([z.zone_info() for z in ordered_zones])
        return result