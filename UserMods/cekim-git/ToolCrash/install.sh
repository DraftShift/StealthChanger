#!/bin/bash

KDIR="${HOME}/klipper"
KEXTRAS="${KDIR}/klippy/extras"
s
# wget -O - https://raw.githubusercontent.com/Frix-x/klippain-shaketune/main/install.sh | bash

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
wget -O ~/tool_crash/Readme.md https://github.com/DraftShift/StealthChanger/blob/main/UserMods/cekim-git/ToolCrash/Readme.md
wget -O ~/tool_crash/License.txt https://github.com/DraftShift/StealthChanger/blob/main/UserMods/cekim-git/ToolCrash/License.txt
wget -O ~/tool_crash/tool_crash.py https://github.com/DraftShift/StealthChanger/blob/main/UserMods/cekim-git/ToolCrash/tool_crash.py

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
