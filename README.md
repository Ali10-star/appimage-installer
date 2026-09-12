# 📦 AppImage Installer

Welcome! This graphical tool helps you seamlessly integrate AppImages into your Linux Mint system. It automatically moves the AppImage to your `~/Applications` folder, makes it executable, and generates a `.desktop` shortcut so it appears properly categorized in your start menu.

---

## 📥 Step 1: Download the Tool

1. Go to the top of this GitHub page and click the green **"<> Code"** button.
2. Select **"Download ZIP"**.
3. Open your **Downloads** folder, right-click the downloaded ZIP file, and select **Extract Here**.
4. Open the newly extracted folder so you can see the files inside.

---

## 🛠️ Step 2: System Setup

To make installation as easy as possible for everyone, an automatic setup script is included.

1. Open the extracted folder in your file manager.
2. Right-click on the `install.sh` file, select **Properties**, go to the **Permissions** tab, and make sure **"Allow executing file as program"** is checked.
3. Double-click `install.sh`. 
4. If prompted, select **"Run in Terminal"**. 
5. Enter your computer password when asked (it safely installs the standard Python GUI package if missing). The window will close when finished.

*(Terminal power users: Just run `./install.sh` inside the directory)*

*Note: You can now safely delete the downloaded ZIP and extracted folder from your Downloads.*

---

## 🚀 Step 3: How to Use the App

You can now launch the app directly from your system!

1. Open your **Linux Mint Start Menu**.
2. Search for **"AppImage Installer"** and click it to open.
3. **Select your AppImage:** Click "Browse" and locate the downloaded `.AppImage` file.
4. **Name the App:** Enter the name exactly as you want it to appear in your start menu.
5. **Select a Category:** Choose the appropriate application category (e.g., Development, Game, Utility).
6. **(Optional) Add an Icon:** Browse for a `.png` or `.svg` icon file if you want a custom icon in your menu.
7. Click the green **"Install AppImage"** button.

The app will now be fully integrated into your system!
