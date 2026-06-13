# system-sentinel
#  System Sentinel Command Center

An efficient, lightweight TUI (Terminal User Interface) system management utility built for **CachyOS** and **Arch Linux**. Automate your daily developer workflow, system optimization, and security audits with a single command.

##  Features

*   **Work Mode:** Instantly initializes your development environment by opening essential web tools (ChatGPT, GitHub) in your default browser.
*   ** Maintenance (Deep Cleanup):** Scans and purges temporary logging, cache files (`.tmp`, `.log`, `.cache`), and safely clears `pacman` package caches to reclaim disk space.
*   ** Security Check:** Built-in fast signature scanner that audits your system paths for recent AUR malware supply-chain attacks (including `atomic-lockfile` and `js-digest`).

##  Installation & Architecture

System Sentinel is designed to be fully compatible with the Arch Linux package ecosystem.

1. Clone or download this repository.
2. Ensure you have the local `PKGBUILD` and `start.py` in the same directory.
3. Build and install natively using the Arch build system:
   ```bash
   makepkg 
   ```

##  Contributing & Maintainers

This project follows the core philosophies of the Linux ecosystem. Contributions, bug reports, and feature requests from the community are highly welcome!

** Note to contributors:** This project is actively maintained, but updates are reviewed on a scheduled basis due to school and educational commitments. We are looking for co-maintainers to help review pull requests and run automated security audits!

Feel free to fork the repository, open an issue, or submit a Pull Request. Let's make system maintenance safer and faster together!

## License
This project is open-source and licensed under the GNU General Public License v3.0 (GPL-3.0).

## About Me
11 years old. Arch Linux user (btw). Writing Python scripts instead of doing homework. 💻

##  Support My Work

If you like System Sentinel and want to help an 11-year-old developer upgrade his setup for even bigger open-source projects, you can support me here:

[![ko-fi](https://ko-fi.com)](https://ko-fi.com)


