import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_simulation(base_dir, cores):
    """Run simulations in a given base_dir with specified cores."""
    try:
        subprocess.run(
            [sys.executable, "run_grid_helper.py", "--base_dir", base_dir, "--cores", str(cores)],
            check=True
        )
        print(f"✅ Finished grid for {base_dir}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running grid for {base_dir}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Run MESA grids in parallel.")
    parser.add_argument(
        "--base_dir",
        nargs="+",
        default=["no_os", "nad_convos_low", "nad_convos_mid", "nad_convos_high"],
        help="Which base_dir(s) to run. Default: all four."
    )
    parser.add_argument(
        "--cores",
        type=int,
        default=4,
        help="Number of cores to use for each grid (default: 4)."
    )
    args = parser.parse_args()

    print(f"Running grids: {args.base_dir} with {args.cores} cores each.")

    with ThreadPoolExecutor(max_workers=len(args.base_dir)) as executor:
        futures = {executor.submit(run_simulation, bd, args.cores): bd for bd in args.base_dir}
        for future in as_completed(futures):
            bd = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"❌ Grid failed for {bd}: {e}")

if __name__ == "__main__":
    main()
