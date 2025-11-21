import subprocess
import os
import sys

def run_script(script_name):
    script_path = os.path.join("generate_dirs", script_name)
    print(f"Running {script_path}...")
    try:
        subprocess.run([sys.executable, script_path], check=True)
        print(f"Finished {script_path}")
    except FileNotFoundError:
        print(f"⚠️ Script not found: {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script_path}: {e}")

def main():
    scripts = [
        "initialize_convos_low_grid.py",
        "initialize_convos_mid_grid.py",
        "initialize_convos_high_grid.py",
        "initialize_no_os_grid.py"
    ]
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()
