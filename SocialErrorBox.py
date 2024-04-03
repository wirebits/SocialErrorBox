# SocialErrorBox
# A tool which generates error message boxes for social engineering and fun.
# Author - WireBits

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class ArduinoHIDConverter:
    @staticmethod
    def convert_to_arduino_script(arduino_mnemonic):
        conversion_rules = {
            "VAR": ArduinoHIDConverter.convert_var,
            "INF": ArduinoHIDConverter.convert_inf,
            "REDO": ArduinoHIDConverter.convert_redo,
            "SET": ArduinoHIDConverter.convert_set,
            "RUN": ArduinoHIDConverter.convert_run
        }

        parts = arduino_mnemonic.split()
        command = parts[0]

        if command in conversion_rules:
            return conversion_rules[command](parts)
        else:
            return f"Error: Invalid command '{command}'"

    @staticmethod
    def convert_var(parts):
        variable_name = parts[1]
        title_text, msg_text, button, icon = ArduinoHIDConverter.extract_params(parts[2:])
        return f"{variable_name} = MsgBox(\"{msg_text}\", {button}+{icon}, \"{title_text}\")"

    @staticmethod
    def convert_inf(parts):
        variable_name = parts[1]
        title_text, msg_text, button, icon = ArduinoHIDConverter.extract_params(parts[2:])
        return f"Do\n{variable_name} = MsgBox(\"{msg_text}\", {button}+{icon}, \"{title_text}\")\nLoop"

    @staticmethod
    def convert_redo(parts):
        iterations = int(parts[1])
        variable_name = parts[2]
        title_text, msg_text, button, icon = ArduinoHIDConverter.extract_params(parts[3:])
        loop_code = f"For i = 1 to {iterations}\n"
        loop_code += f"    {variable_name} = MsgBox(\"{msg_text}\", {button}+{icon}, \"{title_text}\")\n"
        loop_code += "Next"
        return loop_code

    @staticmethod
    def convert_set(parts):
        variable_name = parts[1]
        return f"Dim {variable_name}\nSet {variable_name} = WScript.CreateObject(\"WScript.Shell\")"

    @staticmethod
    def convert_run(parts):
        box_var = parts[1]
        variable_name = parts[2]
        script = parts[3:]
        execute_script = " ".join(script)
        return f"If {box_var} = 1 Then\n    {variable_name}.Run \"{execute_script}\", 1, True\nEnd If"

    @staticmethod
    def extract_params(params):
        title_text = ""
        msg_text = ""
        button = ""
        icon = ""

        for i in range(0, len(params), 2):
            key = params[i]
            value = params[i+1]
            if key == "TITLE":
                title_text = value
            elif key == "MSG":
                msg_text = value
            elif key == "BUTTON":
                button = value
            elif key == "ICON":
                icon = value

        return title_text, msg_text, button, icon

class ArduinoHIDMain:
    def __init__(self, main_window):
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        self.main_window.title("SocialErrorBox")
        self.main_window.resizable(0, 0)

        main_split_frame = ttk.Frame(self.main_window)
        main_split_frame.pack(side="top", fill="both", expand=True)

        self.mnemonic_frame = tk.Text(main_split_frame, font='courier 10', fg='black')
        self.mnemonic_frame.pack(side="left", fill="both", expand=True)
        self.mnemonic_frame.insert(tk.END, "Enter your mnemonic")

        self.arduino_frame = tk.Text(main_split_frame, font='courier 10', fg='black')
        self.arduino_frame.pack(side="right", fill="both", expand=True)
        self.arduino_frame.insert(tk.END, "Your VB script")

        self.mnemonic_frame.bind("<FocusIn>", self.clear_placeholder)
        self.mnemonic_frame.bind("<Button-1>", self.disable_convert_button)

        buttons_frame = ttk.Frame(self.main_window)
        buttons_frame.pack(side="top", fill="x")

        self.convert_button = ttk.Button(buttons_frame, text="Convert", command=self.convert_text, state=tk.DISABLED)
        self.convert_button.pack(side="left", padx=5, pady=5)

        reset_button = ttk.Button(buttons_frame, text="Reset", command=self.reset_all)
        reset_button.pack(side="left", padx=5, pady=5)

        save_button = ttk.Button(buttons_frame, text="Save", command=self.save_file)
        save_button.pack(side="left", padx=5, pady=5)

        exit_button = ttk.Button(buttons_frame, text="Exit", command=self.exit_window)
        exit_button.pack(side="right", padx=5, pady=5)

    def clear_placeholder(self, event):
        if event.widget.get(1.0, tk.END).strip() == "Enter your mnemonic":
            event.widget.delete(1.0, tk.END)

    def disable_convert_button(self, event):
        self.convert_button.configure(state=tk.NORMAL)

    def convert_text(self):
        mnemonic_script = self.mnemonic_frame.get(1.0, tk.END).strip()
        if not mnemonic_script:
            self.arduino_frame.delete(1.0, tk.END)
            self.arduino_frame.insert(tk.END, "Enter some mnemonics to convert!")
        else:
            mnemonics = ""
            for line in mnemonic_script.splitlines():
                converted_line = ArduinoHIDConverter.convert_to_arduino_script(line.strip())
                mnemonics += converted_line + '\n'
            self.arduino_frame.delete(1.0, tk.END)
            self.arduino_frame.insert(tk.END, mnemonics)
            self.arduino_frame.mark_set(tk.INSERT, "end-1c linestart")

    def reset_all(self):
        self.mnemonic_frame.delete(1.0, tk.END)
        self.mnemonic_frame.insert(tk.END, "Enter your mnemonic")
        self.arduino_frame.delete(1.0, tk.END)
        self.arduino_frame.insert(tk.END, "Your VB script")
        self.convert_button.configure(state=tk.DISABLED)

    def exit_window(self):
        self.main_window.destroy()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[('VBScript Files', '*.vbs')], defaultextension='.vbs')
        if not file_path:
            return
        with open(file_path, 'w') as file:
            file.write(self.arduino_frame.get(1.0, tk.END))

main_window = tk.Tk()
app = ArduinoHIDMain(main_window)
main_window.mainloop()