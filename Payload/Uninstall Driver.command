#!/bin/sh

# Uninstall Ultraschall Driver
if [ -d /Library/Extensions/UltraschallHub.kext ]; then
	sudo kextunload /Library/Extensions/UltraschallHub.kext
	sudo kextunload /Library/Extensions/UltraschallHub.kext
	sudo rm -rf /Library/Extensions/UltraschallHub.kext
fi

# Remove installer receipts
if [ -f /var/db/receipts/fm.ultraschall.Driver.bom ]; then
	sudo rm -f /var/db/receipts/fm.ultraschall.Driver.bom
fi

if [ -f /var/db/receipts/fm.ultraschall.Driver.plist ]; then
	sudo rm -f /var/db/receipts/fm.ultraschall.Driver.plist
fi

