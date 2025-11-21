import os
import shutil
import numpy as np

def create_directories(base_dir="no_os"):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    mass_range = np.arange(2, 15.5, 0.5)
    metallicity_range = np.arange(0.0015, 0.0205, 0.0005)

    files_to_copy = ["rn", "mk", "clean", "star", "re"]
    directories_to_copy = ["src", "make"]

    overwrite_all = None

    for mass in mass_range:
        for metallicity in metallicity_range:
            dir_name = f"run_{base_dir}_{mass:.1f}MSUN_z{metallicity:.4f}"
            dir_path = os.path.join(base_dir, dir_name)

            if os.path.exists(dir_path):
                if os.listdir(dir_path):
                    if overwrite_all is None:
                        response = input(f"The directory {dir_path} already exists and is not empty. Overwrite files? (y/n/all/none): ")
                        if response.lower() == 'y':
                            overwrite_all = 'y_all'
                        elif response.lower() == 'n':
                            overwrite_all = 'no_all'
                        elif response.lower() == 'all':
                            overwrite_all = 'y_all'
                        elif response.lower() == 'none':
                            overwrite_all = 'no_all'
                        else:
                            print(f"Unknown response, skipping: {dir_path}")
                            continue
                    if overwrite_all == 'no_all':
                        print(f"{dir_path} already exists and is not empty, skipped.")
                        continue
                else:
                    print(f"{dir_path} already exists but is empty. Proceeding with file copy.")
            else:
                os.makedirs(dir_path)
                print(f"Created: {dir_path}")

            # Copy executables from ../exec/
            for file_name in files_to_copy:
                src_path = os.path.join("../exec", file_name)
                dest_path = os.path.join(dir_path, file_name)
                if os.path.exists(src_path):
                    if not os.path.exists(dest_path) or overwrite_all == 'y_all':
                        shutil.copy(src_path, dest_path)
                        print(f"Copied: {file_name} -> {dest_path}")

            # Copy include directories from ../include/
            for dir_name in directories_to_copy:
                src_path = os.path.join("../include", dir_name)
                dest_path = os.path.join(dir_path, dir_name)
                if os.path.exists(src_path):
                    if not os.path.exists(dest_path) or overwrite_all == 'y_all':
                        shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                        print(f"Directories copied: {dir_name} -> {dest_path}")

            inlist_content = """! This is the first inlist file that MESA reads when it starts.

&star_job
    read_extra_star_job_inlist = .true.
    extra_star_job_inlist_name = 'inlist_project'
/ ! end of star_job namelist

&eos
    read_extra_eos_inlist = .true.
    extra_eos_inlist_name = 'inlist_project'
/ ! end of eos namelist

&kap
    read_extra_kap_inlist = .true.
    extra_kap_inlist_name = 'inlist_project'
/ ! end of kap namelist

&controls
    read_extra_controls_inlist = .true.
    extra_controls_inlist_name = 'inlist_project'
/ ! end of controls namelist

&pgstar
    read_extra_pgstar_inlist = .false.
!    read_extra_pgstar_inlist = .true.
    extra_pgstar_inlist_name = 'inlist_pgstar'
/ ! end of pgstar namelist
"""

            inlist_path = os.path.join(dir_path, "inlist")
            if not os.path.exists(inlist_path) or overwrite_all == 'y_all':
                with open(inlist_path, "w") as f:
                    f.write(inlist_content)
                print(f"Created: {inlist_path}")

            inlist_project_content = f"""&star_job
    pgstar_flag = .false.
    pause_before_terminate = .false.
    create_pre_main_sequence_model = .true.
    change_initial_net = .true.      
    new_net_name = 'pp_cno_extras_o18_ne22.net'
    show_net_species_info = .false.
    save_model_when_terminate = .true.
    save_model_filename = '{base_dir}_{mass:.1f}M_sun_z_{metallicity:.4f}.mod'
/ ! end of star_job namelist

&eos
/ ! end of eos namelist

&kap
    Zbase = {metallicity:.4f}
    kap_file_prefix = 'a09'
    kap_lowT_prefix = 'lowT_fa05_a09p'
    kap_CO_prefix = 'a09_co'
    use_Type2_opacities = .true.
    
/ ! end of kap namelist

&controls
  initial_mass = {mass:.1f}
  mixing_length_alpha = 2.22
  stop_at_phase_TP_AGB = .true.
  max_model_number = 6000
  initial_Y = 0.256d0
  initial_Z = {metallicity:.4f}

  log_directory = 'LOGS'
  calculate_Brunt_N2 = .true.
  write_profiles_flag = .true.
  profile_interval = 10
  write_pulse_data_with_profile = .true.
  pulse_data_format = 'GYRE'
  terminal_interval = 10
  history_interval = 1
/ ! end of controls namelist
"""

            inlist_project_path = os.path.join(dir_path, "inlist_project")
            if not os.path.exists(inlist_project_path) or overwrite_all == 'y_all':
                with open(inlist_project_path, "w") as f:
                    f.write(inlist_project_content)
                print(f"Created: {inlist_project_path}")

    print(f"{len(mass_range) * len(metallicity_range)} directories created.")

if __name__ == "__main__":
    create_directories()
