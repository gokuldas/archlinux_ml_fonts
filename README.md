# Arch Linux Malayalam Fonts (archlinux_ml_fonts)
Arch Linux PKGBUILD generator for installing SMC's Malayalam fonts. A python script (generate.py) generates the PKGBUILD and *.install file necessary to install [SMC's](https://smc.org.in/fonts/) malayalam fonts.

## Installation & Usage

### Prerequisites:
* Arch Linux
* Python 3 (for generating PKGBUILD and file checksums)

### Downloading
Clone the repoitory as:  
> git clone https://github.com/gokuldas/archlinux_ml_fonts

### Usage
The file urls are inside the ./proto folder. The file can be updated if necessary to get the latest package. The fonts are from SMC's site at https://smc.org.in/fonts/. The fontconfig files are from SMC's GitLab group at https://gitlab.com/groups/smc.  

Open a terminal, cd to the cloned folder and run:
> ./generate.py   

This will generate the required PKGBUILD and *.install file. Further, do the usual step in generating and installing arch package:  
> makepkg  
> pacman -U pkgname.pkg.tar.gz

## Credits
[Swatanthra Malayalam Computing](https://smc.org.in/) team for fonts and Fedora team for fontconfig files.

## License
All the contents of this repository are under MIT license.
