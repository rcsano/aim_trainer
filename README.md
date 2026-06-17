# Aim Trainer (OOP Edition)

A 2D aim training game built in Python using the Pygame library to help users practice and improve their clicking speed and accuracy. This version refactors the original project to strictly implement Object-Oriented Programming (OOP) principles and clean coding standards.

> [!NOTE]
> **Disclaimer:** This repository is modified and maintained solely as a submission for my **Final Project**. 

---

## 📌 Attribution & Credit

> [!IMPORTANT]
> **Original Creator:** [techwithtim](https://github.com/techwithtim)  
> **Original Repository:** [Python-Aim-Trainer](https://github.com/techwithtim/Python-Aim-Trainer.git)  

---

## 🗂️ OOP Project Structure 

This project has been broken down into modular files to demonstrate core software engineering concepts:

### 1. `aim_target.py`
*Handles the core target logic using the 4 pillars of OOP.*
* **Abstraction:** Implemented a `BaseTarget` parent class to handle the general mathematical equations for tracking a target's position and checking if a player clicked inside its radius.
* **Encapsulation:** Hidden the target's size variable by naming it `_current_size`, and created a safe getter method called `get_current_size()` to let other files read it securely without direct modification.
* **Inheritance:** Created `StandardTarget` and `GoldenTarget` as child classes that automatically inherit all core attributes and math functions from `BaseTarget`.
* **Polymorphism:** Both child classes use the exact same `draw_target()` method name, but override it to behave differently—the standard target draws alternating red/white rings, while the golden target draws a solid gold reward circle.

### 2. `aim_trainer_game.py`
*Manages game states, scores, and UI layout.*
* **Encapsulation:** Grouped all individual game variables (such as hits, clicks, misses, lives, and timers) inside a single class called `GameStateManager`. This keeps all scoring variables organized, cohesive, and protected in one place.
* **Clean Code Practices:** Separated the user interface drawing logic (like displaying the top dashboard scoreboard and the game-over screen) away from the core execution mechanics so it doesn't clutter the rendering pipelines.

### 3. `aim_trainer_main.py`
*The main execution entry point connecting all components.*
* **File Connection:** Sets up the core runtime execution loop to import and run components seamlessly from `aim_target.py` and `aim_trainer_game.py`.
* **Polymorphism at Work:** Programmed the game loop to randomly spawn either standard or golden targets, then treated them completely uniformly by iterating through a single target list and calling `.update_size()` and `.draw_target()` on them without needing messy, repetitive `if/else` checks for their specific type.
* **Coding Standards:** Refactored the codebase to replace all single-letter variable names with clear, descriptive names using strict `snake_case` style naming rules.

---

## 🛠️ Built With
* [Python 3.x](https://www.python.org/) - Core programming language
* [Pygame](https://www.pygame.org/) - Used for rendering graphics, handling target mechanics, and managing user mouse inputs.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your system. You will also need to install `pygame`.

```bash
pip install pygame
