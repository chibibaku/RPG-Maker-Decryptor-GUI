import json, binascii, os, sys
import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as messagebox

class utils():
    def __init__(self):
        pass

    def xor(self, data, key): #XOR Encryption/Decryption
        return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 

    def getKey(self, path:str):
        f = open(path, 'rb')
        data = json.loads(f.read())
        key = data["encryptionKey"] #This is the name of the dict key
        # print('The key is: '+key)
        return key
    
    def getFilename(self, path): #Change the extension for the consequent
        if path.endswith(".rpgmvo"):
            return path[:-7]+".ogg"
        elif path.endswith(".rpgmvm"):
            return path[:-7] + ".m4a"
        elif path.endswith(".rpgmvp"):
            return path[:-7] + ".png"
        elif path.endswith(".png_"):
            return path[:-5]+".png"
        elif path.endswith(".ogg_"):
            return path[:-5]+".ogg"
        else:
            messagebox.showerror("Error", "The file format selected is not supported.")
            exit()

    def getFileDecrypted(self, path, key, output): #Decrypt the file
        file = open(path, "rb").read()
        file = file[16:]
        text1 = bytearray(file[:16])
        text2 = self.xor(text1, key)
        file = file[16:]

        dirPath = self.getFilename(path)
        newFile = os.path.basename(dirPath) #get filename

        open(output+'/'+newFile, "wb").write(text2 + file) #Create the file
            

class Application():
    def __init__(self, root):
        self.utils = utils()
        self.root = root
        self.root.title("Decrypter")
        self.root.geometry("800x500")

        self.game_dir_path = None

        # Frames for horizontal layout
        self.game_dir_frame = tk.Frame(self.root)
        self.target_file_frame = tk.Frame(self.root)
        self.output_dir_frame = tk.Frame(self.root)
        self.get_key_frame = tk.Frame(self.root)
        self.buttons_frame = tk.Frame(self.root)

        # Game directory
        self.game_dir_label = tk.Label(self.game_dir_frame, text="Game Directory")
        self.game_dir_path_label = tk.Label(self.game_dir_frame, text="")
        self.game_dir_button = tk.Button(self.game_dir_frame, text="Select", command=self.select_game_dir)

        self.game_dir_label.pack(side='left', padx=5)
        self.game_dir_path_label.pack(side='left', padx=5)
        self.game_dir_button.pack(side='left', padx=5)
        self.game_dir_frame.pack(pady=5)

        # Target file
        self.target_file_label = tk.Label(self.target_file_frame, text="Target File")
        self.target_file_path_label = tk.Label(self.target_file_frame, text="")
        self.target_file_button = tk.Button(self.target_file_frame, text="Select", command=self.select_target_file)

        self.target_file_label.pack(side='left', padx=5)
        self.target_file_path_label.pack(side='left', padx=5)
        self.target_file_button.pack(side='left', padx=5)
        self.target_file_frame.pack(pady=5)

        # Output directory
        self.output_dir_label = tk.Label(self.output_dir_frame, text="Output Directory")
        self.output_dir_path_label = tk.Label(self.output_dir_frame, text="")
        self.output_dir_button = tk.Button(self.output_dir_frame, text="Select", command=self.select_output_dir)

        self.output_dir_label.pack(side='left', padx=5)
        self.output_dir_path_label.pack(side='left', padx=5)
        self.output_dir_button.pack(side='left', padx=5)
        self.output_dir_frame.pack(pady=5)

        # Get key
        self.key_label = tk.Label(self.get_key_frame, text="Key")
        self.get_key_button = tk.Button(self.get_key_frame, text="Get Key", command=self.get_key)
        self.key_label.pack(side='left', pady=5)
        self.get_key_button.pack(side='left', pady=5)
        self.get_key_frame.pack(pady=5)

        # Decrypt and Quit
        self.decrypt_button = tk.Button(self.buttons_frame, text="Decrypt", command=self.execute_decryption)
        self.quit_button = tk.Button(self.buttons_frame, text="Quit", command=self.root.quit)
        self.decrypt_button.pack(side='left', padx=20)
        self.quit_button.pack(side='left', padx=20)
        self.buttons_frame.pack(pady=10)

    def select_game_dir(self):
        base_dir = os.path.dirname(sys.executable)
        self.game_dir_path = tkfd.askdirectory(initialdir=base_dir)
        self.game_dir_path_label.config(text=self.game_dir_path)

    def select_target_file(self):
        self.target_file_path = tkfd.askopenfilenames()
        self.target_file_path_label.config(text='\n'.join(self.target_file_path))

    def select_output_dir(self):
        base_dir = os.path.dirname(sys.executable)
        self.output_dir_path = tkfd.askdirectory(initialdir=base_dir)
        self.output_dir_path_label.config(text=self.output_dir_path)
    
    def get_key(self):
        if not self.game_dir_path:
            messagebox.showerror("Error", "Please select the game directory.")
            return
        self.key = self.utils.getKey(self.game_dir_path + '/data/System.json')
        self.key_label.config(text="Key: " + self.key)

    def execute_decryption(self):
        if not self.game_dir_path or not self.target_file_path or not self.output_dir_path:
            messagebox.showerror("Error", "Please select all the required paths.")
            return
        try:
            for path in self.target_file_path:
                self.utils.getFileDecrypted(path, bytearray(binascii.unhexlify(self.key)), self.output_dir_path)
            messagebox.showinfo("Success", "Files decrypted successfully.")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while decrypting the files.\n"+str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()