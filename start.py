import os, time, platform, webbrowser, shutil, subprocess

class S:
    HEADER, CYAN, GREEN, WARN, BOLD, END = '\033[95m\033[1m', '\033[96m', '\033[92m', '\033[93m', '\033[1m', '\033[0m'

def get_linux_distro():
    """Определяет базу дистрибутива Linux"""
    if os.path.exists("/etc/arch-release"):
        return "arch"
    elif os.path.exists("/etc/debian_version"):
        return "debian"
    elif os.path.exists("/etc/fedora-release"):
        return "fedora"
    return "unknown"

def check_aur_malware(distro):
    """Проверка системы на наличие следов недавней атаки на AUR"""
    print(f"\n{S.CYAN} > Running Cyber Security Scan (AUR Malware Check)...{S.END}")
    time.sleep(1)
    
    if distro != "arch":
        print(f"{S.GREEN}  Your system does not use AUR. You are completely safe from this threat!{S.END}")
        return

    suspicious_paths = [
        "/usr/local/bin/atomic-lockfile",
        "/usr/bin/atomic-lockfile",
        os.path.expanduser("~/.config/atomic-lockfile"),
        os.path.expanduser("~/.local/share/js-digest")
    ]
    
    infected = False
    for path in suspicious_paths:
        if os.path.exists(path):
            print(f"  {S.WARN}[ ALERT] Found suspicious file:{S.END} {path}")
            infected = True
            
    if infected:
        print(f"\n{S.WARN}![WARNING] System might be compromised. Please review your AUR packages!{S.END}")
    else:
        print(f"\n{S.GREEN} > Security Scan complete! No known AUR malware signatures found.{S.END}")

def deep_clean(distro):
    print(f"{S.CYAN} > Initializing Deep Scan...{S.END}")
    home = os.path.expanduser("~")
    dirs_to_clean = [os.path.join(home, "Downloads"), os.path.join(home, ".cache")]
    count = 0
    
    for d in dirs_to_clean:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith((".tmp", ".log", ".cache")):
                    print(f"  {S.WARN}Deleting:{S.END} {f}")
                    try:
                        os.remove(os.path.join(d, f))
                        count += 1
                        time.sleep(0.02)
                    except: pass
                    
    print(f"  {S.GREEN}Removed {count} temporary files.{S.END}")
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
            check_aur_malware(distro)
            input(f"\n{S.CYAN}Press Enter to return to menu...{S.END}")
        elif choice == "4" or choice.lower() == "exit":
            break

if __name__ == "__main__":
    launch_menu()
