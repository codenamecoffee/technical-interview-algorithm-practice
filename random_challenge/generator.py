import os
import random
from pathlib import Path
from datetime import datetime
import time
import threading
import msvcrt

# --- Configuración ---
BASE_DIR = Path(__file__).parent.parent

evaluation_status = {
    "finished": False,
    "mode": None,  # mode: "deliver", "giveup", "timeout"
    "awaiting_confirmation": False
}

CATEGORIES = ["basics", "intermediate", "advanced"]

def listen_for_keys():
    while not evaluation_status["finished"]:
        if msvcrt.kbhit():
            try:
                key = msvcrt.getch().decode("utf-8").lower()
            except UnicodeDecodeError:
                # If it cannot be decoded, ignore the key and continue.
                continue
            if key == "s":
                evaluation_status["awaiting_confirmation"] = True
                print("\n¿Are you sure you want to submit the work? (Y/N): ", end="", flush=True)
                confirm = msvcrt.getch().decode("utf-8").lower()
                if confirm == "y":
                    evaluation_status["finished"] = True
                    evaluation_status["mode"] = "deliver"
                    print("\n¡Solutions submitted!")
                elif confirm == "n":
                    print("\nContinuing with the assessment...")
                else:
                    print("\nInvalid option. The timer continues running.")
                evaluation_status["awaiting_confirmation"] = False
            elif key == "x":
                evaluation_status["awaiting_confirmation"] = True
                print("\n¿Are you sure you want to give up? (Y/N): ", end="", flush=True)
                confirm = msvcrt.getch().decode("utf-8").lower()
                if confirm == "y":
                    evaluation_status["finished"] = True
                    evaluation_status["mode"] = "giveup"
                    print("\nYou have abandoned the assessment.")
                elif confirm == "n":
                    print("\nContinuing with the assessment...")
                else:
                    print("\nInvalid option. The timer continues running.")
                evaluation_status["awaiting_confirmation"] = False
            else:
                print("\nInvalid option. Press S to submit the work, X to give up.")

def countdown_and_lock_files(files, minutes=60):
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        if evaluation_status["finished"]:
            break
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        if not evaluation_status.get("awaiting_confirmation", False):
            print(f"\r⏳ Time left: {timer} ", end="", flush=True)
        time.sleep(1)
        if remaining == 5 * 60:
            print("\n[WARNING] Only 5 minutes left!")
    if not evaluation_status["finished"]:
        evaluation_status["finished"] = True  
        evaluation_status["mode"] = "timeout"
        print("\nTime is up! Setting files to read-only...")
    for file_path in files:
        os.chmod(file_path, 0o444)

def extract_docstring(filepath):
    # Extracts the first triple-quoted docstring from a Python file.
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    docstring = []
    inside = False
    for line in lines:
        if '"""' in line:
            if not inside:
                inside = True
                docstring.append(line)
                if line.count('"""') == 2:  # Docstring in one line
                    break
            else:
                docstring.append(line)
                break
        elif inside:
            docstring.append(line)
    return "".join(docstring) if docstring else None

def create_practice_files(selected_exercises) -> tuple[list[str], str]:
    # Step 1: Check if the 'practice' folder exists in the repo root. If not, create it.
    practice_dir = os.path.join(BASE_DIR, "practice")
    if not os.path.exists(practice_dir):
        os.mkdir(practice_dir)

    # Step 2: Create a subfolder named with today's date (YYYY_MM_DD format) inside 'practice'.
    today = datetime.now().strftime("%Y_%m_%d")
    date_dir = os.path.join(practice_dir, today)
    if not os.path.exists(date_dir):
        os.mkdir(date_dir)

    created_files = [] # Save the paths to return them after

    # Step 3: For each selected exercise, create a new file in the date folder.
    # The file name format is: {difficulty}_{original_name}_attempt.py
    for difficulty, filename in selected_exercises.items():
        base_name = filename.replace(".py", "")
        new_filename = f"{difficulty}_{base_name}_attempt.py"
        file_path = os.path.join(date_dir, new_filename)
        created_files.append(file_path)
        # Get the original file path
        original_path = os.path.join(BASE_DIR, difficulty, filename)
        docstring = extract_docstring(original_path)
        with open(file_path, "w", encoding="utf-8") as f:
            if docstring:
                f.write(docstring + "\n\n")
            f.write(f"# Attempt for {filename} ({difficulty})\n\n")

    return created_files, date_dir

def pick_random_exercise(category: str) -> str:
    """Devuelve un archivo random dentro de una categoría."""
    folder = BASE_DIR / category
    files = [f for f in folder.iterdir() if f.is_file() and f.suffix == ".py"]

    if not files:
        return f"[No hay ejercicios en {category}]"

    return random.choice(files).name

def write_results_file(date_dir, selected_exercises, start_time, end_time, mode):
    results_path = os.path.join(date_dir, "results.txt")
    duration = end_time - start_time
    minutes, seconds = divmod(duration.seconds, 60)
    duration_str = f"{minutes:02d}m:{seconds:02d}s"
    start_24 = start_time.strftime('%H:%M')
    start_12 = start_time.strftime('%I:%M %p').lstrip('0')
    end_24 = end_time.strftime('%H:%M')
    end_12 = end_time.strftime('%I:%M %p').lstrip('0')
    with open(results_path, "w", encoding="utf-8") as f:
        f.write("=== PRACTICE SESSION RESULTS ===\n")
        f.write(f"Date: {start_time.strftime('%Y-%m-%d')}\n")
        f.write(f"Start time: {start_24} hrs || {start_12.lower()}\n")
        f.write(f"End time: {end_24} hrs || {end_12.lower()}\n")
        f.write(f"Duration: {duration_str}\n")
        f.write(f"Completion mode: {mode}\n\n")
        f.write("Exercises assigned:\n")
        for diff, name in selected_exercises.items():
            f.write(f"- {diff.capitalize()}: {name}\n")
        f.write("\nCorrections & Comments:\n# Write your feedback here\n")

def main():
    try:
        start_time = datetime.now()
        print("=" * 40)
        print("🎯  RANDOM PYTHON EXERCISE GENERATOR")
        print("=" * 40)

        selected_exercises = {}

        for cat in CATEGORIES:
            chosen = pick_random_exercise(cat)
            selected_exercises[cat] = chosen
            print(f"- {cat.capitalize()}: {chosen}")

        print("=" * 40)

        created_files, date_dir = create_practice_files(selected_exercises)
        print("\n(*) Press 'S' to submit your work, 'X' to give up at any time during the timer.\n")

        # Start key listening thread
        key_thread = threading.Thread(target=listen_for_keys, daemon=True)
        key_thread.start()

        # Start the timer and lock files after 60 minutes
        countdown_and_lock_files(created_files, minutes=6)
        end_time = datetime.now()

        write_results_file(date_dir, selected_exercises, start_time, end_time, evaluation_status["mode"])

    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
