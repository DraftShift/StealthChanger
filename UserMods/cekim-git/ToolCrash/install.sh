#!/bin/bash

KDIR="${HOME}/klipper"
KEXTRAS="${KDIR}/klippy/extras"
GITROOT="https://raw.githubusercontent.com"
GITREPO="StealthChanger/refs/heads/main"
GITUSER="DraftShift"
#GITREPO="Toolchanger/refs/heads/main"
#GITUSER="cekim-git"

if [ ! -d "$KDIR" ]; then
    echo "tool_crash: klipper doesn't exist"
    exit 1
fi

if [ ! -d "~/tool_crash" ]; then
   echo "Creating directory..."
   mkdir ~/tool_crash
fi
cd ~/tool_crash
rm -rf ~/tool_crash/tool_crash.py
wget -O ~/tool_crash/README.md "${GITROOT}/${GITUSER}/${GITREPO}/UserMods/cekim-git/ToolCrash/README.md"
wget -O ~/tool_crash/LICENSE.txt "${GITROOT}/${GITUSER}/${GITREPO}/UserMods/cekim-git/ToolCrash/LICENSE.txt"
wget -O ~/tool_crash/tool_crash.py "${GITROOT}/${GITUSER}/${GITREPO}/UserMods/cekim-git/ToolCrash/tool_crash.py"

# create symlink if it doesn't exist
if [ -f "${KEXTRAS}/tool_crash.py" ]; then
    rm -rf "${KEXTRAS}/tool_crash.py"
fi
ln -s ~/tool_crash/tool_crash.py "${KEXTRAS}/tool_crash.py"

# exclude beacon.py from klipper git tracking
if ! grep -q "${KEXTRAS}/tool_crash.py" "${KDIR}/.git/info/exclude" ; then
    echo "${KEXTRAS}/tool_crash.py" >> "${KDIR}/.git/info/exclude"
fi

# re-start klipper
sudo systemctl restart klipper

cd ~
