# 🧙 RPG Character Creator

This is a final project for my **OOP in Python** class. It is a GUI-based character creation app made using **Python**, **object-oriented programming principles**, and **customtkinter** for the graphical interface.

It demonstrates key OOP concepts:

- Classes, inheritance (`Character`, `Warrior`, `Mage`)
- Encapsulation and methods
- Decorators like `@property`
- Composition (using `Skill` inside `Character`)

---

## 🔧 Features

- Choose a **name**, **class** (`Warrior` / `Mage`) and **skill** (e.g., Berserk, Fireball)
- Distribute **15 stat points** between Strength, Intelligence, Agility
- Shows **remaining points** in real-time
- Displays **class and skill icons**
- Shows **derived stats** (HP, MP, Dodge)
- **Preview JSON** data
- **Export character** to `/characters` as `.json`
- Input validation: preview is disabled if any field is missing

---

## 📦 Installation & Setup

1. Make sure you have **Python 3.9+** installed.
2. Install dependencies:

```bash
pip install customtkinter pillow
```

3. Run the project:

```bash
python main.py
```

---

## 📁 Project Structure

```
.
├── main.py                  # main application logic and GUI
├── character.py             # OOP logic for Character, Warrior, Mage
├── skill.py                 # Skill class
├── assets/
│   ├── warrior.png
│   ├── mage.png
│   └── skills/
│       ├── berserk.png
│       ├── fireball.png
│       └── ...
├── characters/              # exported character files
└── README.md
```

---

## 📝 Example Output (JSON)

```json
{
  "Name": "Thorg",
  "Class": "Warrior",
  "Skill": "Berserk",
  "Stats": {
    "Strength": 15,
    "Intelligence": 2,
    "Agility": 3
  },
  "Derived Stats": {
    "HP": 100,
    "MP": 24,
    "Dodge": 4.5
  }
}
```

---

## ✅ OOP Concepts Used

- Classes & Instances
- Inheritance (`Character` → `Warrior`, `Mage`)
- Encapsulation (`_strength`, `set_stats()`)
- Properties & Getters/Setters
- Static Methods (e.g. `available_skills()`)
