#!/bin/bash

echo "======================================"
echo " AppImage Installer - Setup Script"
echo "======================================"
echo ""

echo "[1/4] Installing Python Tkinter (requires sudo password)..."
sudo apt update && sudo apt install -y python3-tk

echo "[2/4] Creating directories..."
mkdir -p ~/.scripts
mkdir -p ~/.local/share/applications

echo "[3/4] Copying files..."
cp appimage-installer-gui.py ~/.scripts/
chmod +x ~/.scripts/appimage-installer-gui.py

sed "s|~|$HOME|g" appimage-installer.desktop > ~/.local/share/applications/appimage-installer.desktop
chmod +x ~/.local/share/applications/appimage-installer.desktop

echo "[4/4] Restarting Cinnamon menu cache (optional)..."
if command -v cinnamon-dbus-command &> /dev/null; then
    cinnamon-dbus-command RestartCinnamon 2>/dev/null || true
fi

echo ""
echo "======================================"
echo " Setup Complete!"
echo " You can now find 'AppImage Installer' in your start menu."
echo "======================================"
sleep 3
