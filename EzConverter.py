import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
print("$$$$$$$$$\\                 $$$$$$\\                                               $$\\                        \n" + 
      "$$  _____|               $$  __$$\\                                              $$ |                       \n" + 
      "$$ |     $$$$$$$$\\       $$ /  \\__|$$$$$$\\ $$$$$$$\\$$\\    $$\\ $$$$$$\\  $$$$$$\\$$$$$$\\   $$$$$$\\  $$$$$$\\  \n" + 
      "$$$$$\\   \\____$$  |      $$ |     $$  __$$\\$$  __$$\\$$\\  $$  $$  __$$\\$$  __$$\\_$$  _| $$  __$$\\$$  __$$\\ \n" + 
      "$$  __|    $$$$ _/       $$ |     $$ /  $$ $$ |  $$ \\$$\\$$  /$$$$$$$$ $$ |  \\__|$$ |   $$$$$$$$ $$ |  \\__|\n" + 
      "$$ |      $$  _/         $$ |  $$\\$$ |  $$ $$ |  $$ |\\$$$  / $$   ____$$ |      $$ |$$\\$$   ____$$ |      \n" + 
      "$$$$$$$$\\$$$$$$$$\\       \\$$$$$$  \\$$$$$$  $$ |  $$ | \\$  /  \\$$$$$$$\\$$ |      \\$$$$  \\$$$$$$$\\$$ |      \n" + 
      "\\________\\________|       \\______/ \\______/\\__|  \\__|  \\_/    \\_______\\__|       \\____/ \\_______\\__|      \n" + 
      "                                                                                                              \n" + 
      "                                                                                                              \n" + 
      "                                                                                                              \n" + 
      "                                                             $$\\      $$\\$$\\                              \n" + 
      "                                                             $$$\\    $$$ \\__|                             \n" + 
      "                                                             $$$$\\  $$$$ $$\\ $$$$$$\\  $$$$$$\\  $$$$$$\\    \n" + 
      "                                                      $$$$$$\\$$\\$$\\$$ $$ $$ $$  __$$\\$$  __$$\\$$  __$$\\   \n" + 
      "                                                      \\______$$ \\$$$  $$ $$ $$ |  \\__$$$$$$$$ $$$$$$$$ |  \n" + 
      "                                                             $$ |\\$  /$$ $$ $$ |     $$   ____$$   ____|  \n" + 
      "                                                             $$ | \\_/ $$ $$ $$ |     \\$$$$$$$\\$$$$$$$\\   \n" + 
      "                                                             \\__|     \\__\\__\\__|      \\_______|\\_______|  \n" + 
      "                                                                                                              \n" + 
      "                                                                                                              \n" + 
      "                                                                                                              ")

start = input("Do you want to start? (y/n) ")

if start == "y":
    file_path = filedialog.askopenfilename()
    print(f"Selected file path: {file_path}")

    if not file_path:
        print("No file selected")
    else:
        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            email, password = line.strip().split(":")
            username = email.split("@")[0]
            new_lines.append(f"{username}:{password}")

        new_file_path = file_path.split(".")[0] + "_username.txt"
        with open(new_file_path, "w") as f:
            f.write("\n".join(new_lines))

        print(f"Username:Password combolist saved: {new_file_path}")
elif start == "n":
    print("Exiting the program.")
else:
    print("Unrecognized response.")

input("Press enter to exit...")
