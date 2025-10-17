import os
import subprocess


def main():
    base_dir = os.path.dirname(__file__) 
    steps = [
        "src/01_data_cleaning.py",
        "src/02_data_analysis.py",
        "src/03_load_to_postgres.py"
    ]

    for step in steps:
        script_path = os.path.join(base_dir, step)
        # print(f"\n Running {step} ...")
        # subprocess.run(["python", step], check=True)


        print(f"\n Running: {script_path}")
        # Run from the project root
        subprocess.run(["python", script_path], check=True, cwd=base_dir)

    print("\n All steps completed successfully!")
    print("➡ Data cleaned, analyzed, and uploaded to PostgreSQL.")
    print(" Now open Power BI → connect to PostgreSQL → visualize results.")

if __name__ == "__main__":
    main()
