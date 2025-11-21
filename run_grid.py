import os
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_simulation(run_dir):
    """Run clean, mk, rn inside a given directory."""
    try:
        for cmd in ["./clean", "./mk", "./rn"]:
            subprocess.run(cmd, cwd=run_dir, check=True)
        print(f"✅ Finished simulation in {run_dir}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {run_dir}: {e}")

def run_all(base_dir, max_workers=4):
    """Run simulations in all run_* directories under base_dir using max_workers cores."""
    run_dirs = [
        os.path.join(base_dir, d)
        for d in os.listdir(base_dir)
        if d.startswith("run_") and os.path.isdir(os.path.join(base_dir, d))
    ]

    print(f"Found {len(run_dirs)} run directories under {base_dir}.")
    print(f"Running with {max_workers} parallel workers...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(run_simulation, rd): rd for rd in run_dirs}
        for future in as_completed(futures):
            rd = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"❌ Simulation failed in {rd}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MESA simulations in parallel.")
    parser.add_argument("--base_dir", required=True, help="Base directory containing run_* subdirectories")
    parser.add_argument("--cores", type=int, default=4, help="Number of parallel workers (default: 4)")
    args = parser.parse_args()

    run_all(args.base_dir, args.cores)
