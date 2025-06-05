import customtkinter as ctk
from character import Warrior, Mage
from skill import Skill
from PIL import Image, ImageTk
import os
import json

ASSETS_PATH = "assets"
SKILLS_PATH = os.path.join(ASSETS_PATH, "skills")
MAX_POINTS = 22

os.makedirs("characters", exist_ok=True)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1000x700")
app.title("RPG Character Creator")

main_frame = ctk.CTkFrame(app)
main_frame.pack(pady=20, padx=20, expand=True, fill="both")

left_frame = ctk.CTkFrame(main_frame, width=300)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

input_frame = ctk.CTkFrame(right_frame)
input_frame.pack(pady=10)

name_label = ctk.CTkLabel(input_frame, text="Name")
name_label.grid(row=0, column=0, padx=5)
name_entry = ctk.CTkEntry(input_frame, width=120)
name_entry.grid(row=1, column=0, padx=5)

class_label = ctk.CTkLabel(input_frame, text="Class")
class_label.grid(row=0, column=1, padx=5)
class_var = ctk.StringVar()
class_dropdown = ctk.CTkOptionMenu(
    input_frame, variable=class_var, values=["Warrior", "Mage"]
)
class_dropdown.grid(row=1, column=1, padx=5)

skill_label = ctk.CTkLabel(input_frame, text="Skill")
skill_label.grid(row=0, column=2, padx=5)
skill_var = ctk.StringVar()
skill_dropdown = ctk.CTkOptionMenu(input_frame, variable=skill_var, values=[""])
skill_dropdown.grid(row=1, column=2, padx=5)

skill_image_label = ctk.CTkLabel(left_frame, text="")
skill_image_label.pack(pady=10)

class_image_label = ctk.CTkLabel(left_frame, text="")
class_image_label.pack(pady=10)

stat_frame = ctk.CTkFrame(right_frame)
stat_frame.pack(pady=10)

strength_label = ctk.CTkLabel(stat_frame, text="Strength")
strength_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
strength_slider = ctk.CTkSlider(stat_frame, from_=0, to=15, number_of_steps=15)
strength_slider.set(5)
strength_slider.grid(row=0, column=1, padx=10, pady=5)
strength_value = ctk.CTkLabel(stat_frame, text="5")
strength_value.grid(row=0, column=2)

intelligence_label = ctk.CTkLabel(stat_frame, text="Intelligence")
intelligence_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
intelligence_slider = ctk.CTkSlider(stat_frame, from_=0, to=15, number_of_steps=15)
intelligence_slider.set(5)
intelligence_slider.grid(row=1, column=1, padx=10, pady=5)
intelligence_value = ctk.CTkLabel(stat_frame, text="5")
intelligence_value.grid(row=1, column=2)

agility_label = ctk.CTkLabel(stat_frame, text="Agility")
agility_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
agility_slider = ctk.CTkSlider(stat_frame, from_=0, to=15, number_of_steps=15)
agility_slider.set(5)
agility_slider.grid(row=2, column=1, padx=10, pady=5)
agility_value = ctk.CTkLabel(stat_frame, text="5")
agility_value.grid(row=2, column=2)

points_left_label = ctk.CTkLabel(right_frame, text=f"Points left: {MAX_POINTS - 15}")
points_left_label.pack()

desc_title = ctk.CTkLabel(
    right_frame, text="JSON Preview", font=ctk.CTkFont(size=14, weight="bold")
)
desc_title.pack(pady=(20, 5))
result_box = ctk.CTkTextbox(right_frame, width=400, height=150)
result_box.pack()
result_box.configure(state="disabled")


def update_slider_values(event=None):
    s = int(strength_slider.get())
    i = int(intelligence_slider.get())
    a = int(agility_slider.get())
    total = s + i + a

    if total > MAX_POINTS:
        excess = total - MAX_POINTS
        if event == strength_slider:
            strength_slider.set(s - excess)
        elif event == intelligence_slider:
            intelligence_slider.set(i - excess)
        elif event == agility_slider:
            agility_slider.set(a - excess)
        total = MAX_POINTS

    strength_value.configure(text=str(int(strength_slider.get())))
    intelligence_value.configure(text=str(int(intelligence_slider.get())))
    agility_value.configure(text=str(int(agility_slider.get())))
    points_left_label.configure(text=f"Points left: {max(0, MAX_POINTS - total)}")


strength_slider.configure(command=lambda e: update_slider_values(strength_slider))
intelligence_slider.configure(
    command=lambda e: update_slider_values(intelligence_slider)
)
agility_slider.configure(command=lambda e: update_slider_values(agility_slider))


def get_character_data():
    name = name_entry.get()
    char_class = class_var.get()
    skill_name = skill_var.get()
    strength = int(strength_slider.get())
    intelligence = int(intelligence_slider.get())
    agility = int(agility_slider.get())

    if char_class == "Warrior":
        char = Warrior(name)
        skill_list = Warrior.available_skills()
    else:
        char = Mage(name)
        skill_list = Mage.available_skills()

    skill_obj = next((s for s in skill_list if s.name == skill_name), None)
    if skill_obj:
        char.set_skill(skill_obj)

    char.set_stats(strength, intelligence, agility)

    return {
        "Name": name,
        "Class": char_class,
        "Skill": skill_obj.name if skill_obj else "None",
        "Stats": char.stats,
        "Derived Stats": char.get_derived_stats(),
    }


def on_preview():
    name = name_entry.get().strip()
    char_class = class_var.get().strip()
    skill = skill_var.get().strip()

    if not name or not char_class or not skill:
        result_box.configure(state="normal")
        result_box.delete("0.0", "end")
        result_box.insert(
            "0.0", "\u26a0 Please enter a name, class, and skill before previewing.\n"
        )
        result_box.configure(state="disabled")
        return

    result = get_character_data()
    result_box.configure(state="normal")
    result_box.delete("0.0", "end")
    result_box.insert("0.0", json.dumps(result, indent=4))
    result_box.configure(state="disabled")


def on_export():
    result = get_character_data()
    name = result["Name"].lower().replace(" ", "_")
    cls = result["Class"].lower()
    filename = f"{name}_{cls}.json"
    path = os.path.join("characters", filename)

    with open(path, "w") as f:
        json.dump(result, f, indent=4)

    result_box.configure(state="normal")
    result_box.insert("0.0", f"Exported to: {path}\n\n")
    result_box.configure(state="disabled")


def update_skill_image(skill_name):
    current_class = class_var.get()
    skills = (
        Warrior.available_skills()
        if current_class == "Warrior"
        else Mage.available_skills()
    )
    skill_obj = next((s for s in skills if s.name == skill_name), None)
    if skill_obj:
        img = Image.open(skill_obj.icon_path).resize((64, 64))
        photo = ImageTk.PhotoImage(img)
        skill_image_label.configure(image=photo, text="")
        skill_image_label.image = photo


def on_skill_change(choice):
    update_skill_image(choice)


def on_class_change(choice):
    if choice == "Warrior":
        skills = Warrior.available_skills()
        icon_path = Warrior("temp").get_class_icon()
    else:
        skills = Mage.available_skills()
        icon_path = Mage("temp").get_class_icon()

    skill_dropdown.configure(values=[s.name for s in skills])
    skill_var.set(skills[0].name)
    update_skill_image(skills[0].name)

    img = Image.open(icon_path).resize((128, 128))
    photo = ImageTk.PhotoImage(img)
    class_image_label.configure(image=photo, text="")
    class_image_label.image = photo


button_frame = ctk.CTkFrame(right_frame)
button_frame.pack(pady=10)

preview_btn = ctk.CTkButton(button_frame, text="Preview JSON", command=on_preview)
preview_btn.grid(row=0, column=0, padx=10)

export_btn = ctk.CTkButton(button_frame, text="Export to File", command=on_export)
export_btn.grid(row=0, column=1, padx=10)

class_dropdown.configure(command=on_class_change)
skill_dropdown.configure(command=on_skill_change)

app.mainloop()
