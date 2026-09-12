#!/usr/bin/env python3
import os
import shutil
import stat
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def browse_appimage():
    path = filedialog.askopenfilename(
        title="Select AppImage",
        filetypes=[("AppImage Files", "*.AppImage *.appimage"), ("All Files", "*.*")],
    )
    if path:
        source_var.set(path)
        # Auto-fill the app name based on the filename if it's currently empty
        if not name_var.get():
            base_name = os.path.basename(path)
            name_without_ext = os.path.splitext(base_name)[0]
            name_var.set(name_without_ext)


def browse_icon():
    path = filedialog.askopenfilename(
        title="Select Icon (Optional)",
        filetypes=[("Image Files", "*.png *.svg *.xpm"), ("All Files", "*.*")],
    )
    if path:
        icon_var.set(path)


def install_appimage():
    source_path = source_var.get()
    app_name = name_var.get().strip()
    category = category_var.get()
    icon_path = icon_var.get()

    if not source_path or not os.path.exists(source_path):
        messagebox.showwarning("Missing Input", "Please select a valid AppImage file.")
        return

    if not app_name:
        messagebox.showwarning(
            "Missing Input", "Please enter a name for the application."
        )
        return

    # Define standard installation paths
    applications_dir = os.path.expanduser("~/Applications")
    desktop_dir = os.path.expanduser("~/.local/share/applications")

    # Ensure directories exist
    os.makedirs(applications_dir, exist_ok=True)
    os.makedirs(desktop_dir, exist_ok=True)

    # 1. Copy the file
    filename = os.path.basename(source_path)
    dest_path = os.path.join(applications_dir, filename)

    try:
        shutil.copy2(source_path, dest_path)
    except Exception as e:
        messagebox.showerror("Copy Error", f"Failed to copy AppImage:\n{e}")
        return

    # 2. Make it executable
    try:
        # Fetch current permissions and add executable flags
        st = os.stat(dest_path)
        os.chmod(dest_path, st.st_mode | stat.S_IEXEC)
    except Exception as e:
        messagebox.showerror(
            "Permission Error", f"Failed to make file executable:\n{e}"
        )
        return

    # 3. Create the .desktop shortcut
    # Generate a safe filename for the .desktop file
    safe_name = "".join(c if c.isalnum() else "_" for c in app_name).lower()
    desktop_file_path = os.path.join(desktop_dir, f"{safe_name}_appimage.desktop")

    # Use a generic icon if none is provided
    final_icon = icon_path if icon_path else "application-x-executable"

    desktop_entry = f"""[Desktop Entry]
Name={app_name}
Exec="{dest_path}"
Icon={final_icon}
Type=Application
Categories={category};
Terminal=false
"""
    try:
        with open(desktop_file_path, "w") as f:
            f.write(desktop_entry)

        # Make the .desktop file executable (required by some desktop environments)
        os.chmod(desktop_file_path, os.stat(desktop_file_path).st_mode | stat.S_IEXEC)

        messagebox.showinfo(
            "Success",
            f"{app_name} installed successfully!\n\nYou can now find it in your application menu under {category}.",
        )

        # Clear inputs for the next installation
        source_var.set("")
        name_var.set("")
        icon_var.set("")

    except Exception as e:
        messagebox.showerror(
            "Shortcut Error", f"Failed to create desktop shortcut:\n{e}"
        )


# --- GUI Setup ---
root = tk.Tk()
root.title("AppImage Installer")
root.geometry("500x420")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# 1. Source AppImage
tk.Label(main_frame, text="1. Select AppImage File:", font=("bold")).pack(
    anchor=tk.W, pady=(0, 5)
)
source_var = tk.StringVar()
source_frame = tk.Frame(main_frame)
source_frame.pack(fill=tk.X, pady=(0, 15))
tk.Entry(source_frame, textvariable=source_var).pack(
    side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5)
)
tk.Button(source_frame, text="Browse", command=browse_appimage).pack(side=tk.LEFT)

# 2. App Name
tk.Label(main_frame, text="2. Application Name (For Menu):", font=("bold")).pack(
    anchor=tk.W, pady=(0, 5)
)
name_var = tk.StringVar()
tk.Entry(main_frame, textvariable=name_var).pack(fill=tk.X, pady=(0, 15))

# 3. Category
tk.Label(main_frame, text="3. Menu Category:", font=("bold")).pack(
    anchor=tk.W, pady=(0, 5)
)
# These are standard FreeDesktop categories ensuring cross-distro compatibility
categories = [
    "AudioVideo",
    "Development",
    "Education",
    "Game",
    "Graphics",
    "Network",
    "Office",
    "Settings",
    "System",
    "Utility",
]
category_var = tk.StringVar(value="Utility")
category_dropdown = ttk.Combobox(
    main_frame, textvariable=category_var, values=categories, state="readonly"
)
category_dropdown.pack(fill=tk.X, pady=(0, 15))

# 4. Icon (Optional)
tk.Label(main_frame, text="4. Icon Image (Optional):", font=("bold")).pack(
    anchor=tk.W, pady=(0, 5)
)
icon_var = tk.StringVar()
icon_frame = tk.Frame(main_frame)
icon_frame.pack(fill=tk.X, pady=(0, 20))
tk.Entry(icon_frame, textvariable=icon_var).pack(
    side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5)
)
tk.Button(icon_frame, text="Browse", command=browse_icon).pack(side=tk.LEFT)

# Install Button
tk.Button(
    main_frame,
    text="Install AppImage",
    command=install_appimage,
    bg="#4CAF50",
    fg="white",
    font=("bold", 10),
    pady=8,
).pack(fill=tk.X)

if __name__ == "__main__":
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
