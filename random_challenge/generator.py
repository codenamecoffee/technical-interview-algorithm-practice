import os
import random
from pathlib import Path

# --- Configuración ---
BASE_DIR = Path(__file__).parent.parent

CATEGORIES = ["basics", "intermediate", "advanced"]


def pick_random_exercise(category: str) -> str:
    """Devuelve un archivo random dentro de una categoría."""
    folder = BASE_DIR / category
    files = [f for f in folder.iterdir() if f.is_file() and f.suffix == ".py"]

    if not files:
        return f"[No hay ejercicios en {category}]"

    return random.choice(files).name


def main():
    print("=" * 40)
    print("🎯  RANDOM PYTHON EXERCISE GENERATOR")
    print("=" * 40)

    for cat in CATEGORIES:
        chosen = pick_random_exercise(cat)
        print(f"- {cat.capitalize()}: {chosen}")

    print("=" * 40)


if __name__ == "__main__":
    main()
