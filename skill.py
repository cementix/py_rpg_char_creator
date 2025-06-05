class Skill:
    def __init__(self, name: str, description: str, icon_path: str):
        self.name = name
        self.description = description
        self.icon_path = icon_path

    def __str__(self):
        return f"{self.name} - {self.description}"
