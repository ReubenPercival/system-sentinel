import os, time, platform, webbrowser, shutil, subprocess

class S:
    HEADER, CYAN, GREEN, WARN, BOLD, END = '\033[95m\033[1m', '\033[96m', '\033[92m', '\033[93m', '\033[1m', '\033[0m'

def get_linux_distro():
    """Detect the Linux distribution base"""
    if os.path.exists("/etc/arch-release"):
        return "arch"
    elif os.path.exists("/etc/debian_version"):
        return "debian"
    elif os.path.exists("/etc/fedora-release"):
        return "fedora"
    return "unknown"

def run_advanced_security_check(distro):
    """Advanced security audit utilizing live malware definition databases"""
    print(f"\n{S.CYAN} > Initializing Advanced Security Audit (Real-time DB Scan)...{S.END}")
    time.sleep(1)
    
    if distro != "arch":
        print(f"{S.GREEN}  Your system does not use AUR. You are completely safe from this threat!{S.END}")
        return

   
    shell_type = os.environ.get("SHELL", "")
    

    if "fish" in shell_type:
        cmd = (
            "set malware (begin; curl -fsS --proto '=https' https://githubusercontent.com; "
            "curl -fsS --proto '=https' https://archlinux.org; "
            "curl -fsS --proto '=https' https://pastes.sh; end | grep -E '^[a-z0-9][a-z0-9._+-]*$' | sort -u); "
            "set affected (comm -12 (pacman -Qqm | sort | psub) (printf '%s\\n' $malware | psub)); "
            "if test -n \"$affected\"; echo \"AFFECTED:\"; printf '%s\\n' $affected; else; echo \"Clean — \"(count $malware)\" packages checked, none installed.\"; end"
        )
        executable_shell = "fish"
    else:
        cmd = (
            "m=$( { curl -fsS --proto '=https' https://githubusercontent.com; "
            "curl -fsS --proto '=https' https://archlinux.org; "
            "curl -fsS --proto '=https' https://pastes.sh; } | grep -E '^[a-z0-9][a-z0-9._+-]*$' | sort -u); "
            "o=$(comm -12 <(pacman -Qqm | sort) <(printf '%s\\n' \"$m\")); "
            "[ -n \"$o\" ] && { echo \"AFFECTED:\"; printf '%s\\n' \"$o\"; } || echo \"Clean — $(printf '%s\\n' \"$m\" | grep -c .) packages checked, none installed.\""
        )
        executable_shell = "bash"

    print(f"{S.CYAN} Fetching latest malware definitions and cross-checking packages...{S.END}")
    try:
        res = subprocess.run([executable_shell, "-c", cmd], capture_output=True, text=True, check=True)
        print(f"\n{S.BOLD}--- Live Scan Result ---{S.END}")
        if "AFFECTED:" in res.stdout:
            print(f"{S.WARN}{res.stdout}{S.END}")
            print(f"{S.WARN}![ALERT] Name match detected. Do not panic, double-check with full scan below.{S.END}")
        else:
            print(f"{S.GREEN}{res.stdout.strip()}{S.END}")
    except Exception as e:
        print(f"{S.WARN}![ERROR] Live DB check failed (network issue or missing curl). Skipping to full check...{S.END}")

   
    run_full = input(f"\n{S.CYAN}Do you want to run Full Rootkit & Persistence Scan? (y/N): {S.END}")
    if run_full.lower() == 'y':
        print(f"\n{S.CYAN} > Cloninig and executing lenucksi/aur-malware-check-v2...{S.END}")
        try:
            
            if os.path.exists("aur-malware-check"):
                shutil.rmtree("aur-malware-check")
            
          
            subprocess.run(["git", "clone", "https://github.com"], check=True)
            os.chdir("aur-malware-check")
            subprocess.run(["chmod", "+x", "aur_check-v2.sh"], check=True)
            
            print(f"\n{S.BOLD} Running full rootkit verification (Requires sudo access):{S.END}")
            subprocess.run(["sudo", "./aur_check-v2.sh", "--full"], check=True)
            
       
            os.chdir("..")
            shutil.rmtree("aur-malware-check")
        except Exception as e:
            print(f"{S.WARN}![ERROR] Full scan interrupted or failed.{S.END}")

            if os.path.basename(os.getcwd()) == "aur-malware-check":
                os.chdir("..")

def deep_clean(distro):
    print(f"{S.CYAN} > Initializing Deep Scan...{S.END}")
    home = os.path.expanduser("~")
    dirs_to_clean = [os.path.join(home, "Downloads"), os.path.join(home, ".cache")]
    count = 0
    
    for d in dirs_to_clean:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith((".tmp", ".log", ".cache")):
                    print(f"  Deleting: {f}")
                    try:
                        os.remove(os.path.join(d, f))
                        count += 1
                        time.sleep(0.02)
                    except: pass
                    
    print(f"  Removed {count} temporary files.")
    print(f"\n{S.CYAN} > Optimizing system package caches...{S.END}")
    time.sleep(0.5)
    
    if distro == "arch":
        print(f"{S.BOLD}Cleaning unused pacman cache...{S.END}")
        try:
            subprocess.run(["sudo", "paccache", "-rk0"], check=True)
        except Exception:
            subprocess.run(["sudo", "pacman", "-Scc", "--noconfirm"], check=True)
    elif distro == "debian":
        print(f"{S.BOLD}Cleaning apt cache and removing orphan packages...{S.END}")
        subprocess.run(["sudo", "apt-get", "clean"], check=True)
        subprocess.run(["sudo", "apt-get", "autoremove", "-y"], check=True)
    elif distro == "fedora":
        print(f"{S.BOLD}Cleaning dnf package manager cache...{S.END}")
        subprocess.run(["sudo", "dnf", "clean", "all"], check=True)
    else:
        print(f"{S.WARN}Unknown package manager. Skipping system cache cleanup.{S.END}")
    
    print(f"\n{S.GREEN} > Deep Cleanup complete!{S.END}")

def launch_menu():
    distro = get_linux_distro()
    while True:
        os.system('clear')
        print(f"{S.HEADER}=== SYSTEM SENTINEL COMMAND CENTER ==={S.END}")
        print(f" 1. {S.BOLD}Work Mode{S.END} - Open dev tools")
        print(f" 2. {S.BOLD}Maintenance{S.END} - Deep system cleanup & optimization")
        print(f" 3. {S.BOLD}Security Check{S.END} - Scan for AUR malware")
        print(f" 4. {S.BOLD}Exit{S.END}")
        
        choice = input(f"\n{S.CYAN}Enter command ID: {S.END}")
        
        if choice == "1":
            webbrowser.open("https://chatgpt.com")
            webbrowser.open("https://github.com")
            print(f"{S.GREEN}Work environment initialized.{S.END}")
            time.sleep(2)
        elif choice == "2":
            deep_clean(distro)
            input(f"\n{S.CYAN}Press Enter to return to menu...{S.END}")
        elif choice == "3":
            run_advanced_security_check(distro)
            input(f"\n{S.CYAN}Press Enter to return to menu...{S.END}")
        elif choice == "4" or choice.lower() == "exit":
            break

if __name__ == "__main__":
    launch_menu()
