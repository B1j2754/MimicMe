import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
import sv_ttk
import darkdetect

# Import relavent data from indices.py for meshes
from indices import MESH_CONNECTIONS, PALETTES

# Pull in values from config
import config

def window_tk(q):
    print("ran tk")
    root = tk.Tk()
    root.title("Face Mesh Avatar GUI")
    root.geometry("400x1000")
    
    # Create a main frame
    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Add a Canvas widget
    canvas = tk.Canvas(main_frame)
    canvas.pack(side="left", fill="both", expand=True)

    # Add a vertical scrollbar to the Canvas
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the Canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    def _canvas_config(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>", _canvas_config)

    # Create a frame inside the Canvas
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Function to open the color picker and update the label color
    def _pick_color(label, i):
        """
        Allows user to pick a color and updates the label's background and configuration values

        Parameters:
        - label (tkinter.Label): The label widget to update with the selected color
        - i (int): Index of the configuration value to update

        Returns:
        - None
        """
        color_code = colorchooser.askcolor(title="Choose color", initialcolor=label.cget("background"))
        if color_code[1]: 
            label.config(background=color_code[1])
            config.values[i][1] = color_code[0][::-1]  # Update the values dictionary with the selected color (rgb --> bgr format)
            # Update features
            _update_features(q)

    # Function to update features and push to the queue
    def _update_features(q):
        """
        Updates feature data based on configuration and sends it to a queue for use in another thread

        Parameters:
        - q (queue.Queue): Queue to store the updated features data

        Returns:
        - None
        """
        u_feature_data = []
        for i in config.values:
            if config.values[i][0].get():  # If checkbox is selected
                u_feature_data.append((i, config.values[i][1]))

        # Format features data for the cv2 thread
        updated_features = [(item[0], item[1], MESH_CONNECTIONS[item[0]]) for item in u_feature_data]
        
        # Send updated features to the queue
        q.put(updated_features)

    # Function to convert (r,g,b) to hex
    def _from_rgb(rgb):
        """
        Converts an RGB color tuple to its hexadecimal string representation.

        Parameters:
        - rgb (tuple): A tuple containing red, green, and blue values (int, 0-255).

        Returns:
        - output (str): The hexadecimal string representation of the color.
        """
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'


    labels = []
    # Create rows with checkbox, color picker button, and display label
    for i in MESH_CONNECTIONS.keys():
        # Create a frame for each row
        row_frame = ttk.Frame(scrollable_frame)
        row_frame.pack(fill="x", pady=2, padx=5)  # Fill horizontally, with padding

        # Initialize the value with a boolean and default color
        config.values[i] = [tk.BooleanVar(value=True), (255, 255, 255)]
        checkbox = ttk.Checkbutton(row_frame, text=i, variable=config.values[i][0])
        checkbox.pack(side="left", padx=5)

        # Color display label
        color_label = ttk.Label(row_frame, text="", background="white", width=15)
        color_label.pack(side="right", padx=5)
        color_label.config

        # Save label for later updates with presets
        labels.append(color_label)

        # Create the color picker button function
        def _pick_color_for_label(i=i, color_label=color_label):
            _pick_color(color_label, i)

        color_button = ttk.Button(row_frame, text="Pick a color", command=_pick_color_for_label, style='Accent.TButton')
        color_button.pack(side="right", padx=5)

    # Create a label to denote the dropdown selection for color presets
    preset_label = ttk.Label(scrollable_frame, text="Color Presets", background="black", width=15, justify="right", font="bold")
    preset_label.pack(fill="x", pady=2, padx=5)

    # Create callback function for dropdown
    def apply_preset(preset):
        # Update the values dictionary with the selected color (rgb format)
        for i, lbl in zip(config.values,labels):
            if i in PALETTES[preset]:
                config.values[i][0].set(True)
                config.values[i][1] = PALETTES[preset][i]

                lbl.config(background=_from_rgb(config.values[i][1][::-1]))
        
        # Update features
        _update_features(q)

    # Create the dropdown selection function
    options = ["None"] + list(PALETTES.keys())
    dropdown_default = tk.StringVar() 
    dropdown_default.set("None") 
    pallete_dropdown = ttk.OptionMenu(scrollable_frame, dropdown_default, *options, command=apply_preset)
    pallete_dropdown.pack(fill="x", pady=2, padx=5)

    # Function to periodically check the queue
    def loop_update():
        _update_features(q)
        # Schedule the next check
        root.after(200, loop_update)  # Check every 100ms

    # Start checking the queue
    loop_update()

    # Handle closing the window
    def on_close():
        root.destroy()
        print("TK - Done!")
    
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Set theme to dark Sun-Valley (https://github.com/rdbende/Sun-Valley-ttk-theme)
    sv_ttk.set_theme(darkdetect.theme())

    # Start the Tkinter event loop
    root.mainloop()