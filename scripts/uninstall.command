#!/bin/bash

# Company Name: ZeegySolutions
# App Name: Focus Timer

# Remove application
rm -rf "/Applications/FocusTimer.app"

# Remove support files
rm -rf ~/Library/Application\ Support/ZeegySolutions/FocusTimer

# Remove preferences
rm -rf ~/Library/Preferences/com.zeegysolutions.focustimer.plist

echo ""
echo "---------------------------------------------------"
echo " Focus Timer has been completely removed."
echo " Thank you for using our software!"
echo "---------------------------------------------------"
echo ""