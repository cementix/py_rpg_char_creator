from skill import Skill
from utils import AVATARS_PATH
from utils import SKILLS_PATH


class Character:
    def __init__(self, name: str, level: int = 1):
        self._name = name
        self._level = level
        self._strength = 0
        self._intelligence = 0
        self._agility = 0
        self._skill = None

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def stats(self):
        return {
            "Strength": self._strength,
            "Intelligence": self._intelligence,
            "Agility": self._agility,
        }

    def set_stats(self, strength: int, intelligence: int, agility: int):
        self._strength = strength
        self._intelligence = intelligence
        self._agility = agility

    def set_skill(self, skill: Skill):
        self._skill = skill

    def get_derived_stats(self):
        hp = self._strength * 10
        mp = self._intelligence * 12
        dodge = self._agility * 1.5

        return {
            "HP": hp,
            "MP": mp,
            "Dodge": dodge,
        }

    def get_class_icon(self):
        return f"{AVATARS_PATH}/default.jpg"

    def get_skill_icon(self):
        return self._skill.icon_path if self._skill else None


class Warrior(Character):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, level)

    def set_stats(self, strength: int, intelligence: int, agility: int):
        strength = int(strength * 1.1)
        super().set_stats(strength, intelligence, agility)

    def get_class_icon(self):
        return f"{AVATARS_PATH}/warrior.jpg"

    @staticmethod
    def available_skills():
        return [
            Skill(
                "Berserk",
                "Boosts strength for a short time",
                f"{SKILLS_PATH}/berserk.png",
            ),
            Skill(
                "Shield Wall", "Reduces incoming damage", f"{SKILLS_PATH}/shield.png"
            ),
            Skill("Rush", "Charges at enemy", f"{SKILLS_PATH}/rush.png"),
        ]


class Mage(Character):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, level)

    def set_stats(self, strength: int, intelligence: int, agility: int):
        intelligence = int(intelligence * 1.2)
        super().set_stats(strength, intelligence, agility)

    def get_class_icon(self):
        return f"{AVATARS_PATH}/mage.jpg"

    @staticmethod
    def available_skills():
        return [
            Skill(
                "Fireball", "Deals fire damage to enemy", f"{SKILLS_PATH}/fireball.png"
            ),
            Skill("Heal", "Restores HP", f"{SKILLS_PATH}/heal.png"),
            Skill("Teleport", "Move instantly", f"{SKILLS_PATH}/teleport.jpg"),
        ]
