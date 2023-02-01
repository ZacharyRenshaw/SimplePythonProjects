import sys
import clipboard
import json
import os

dirname = os.path.dirname(__file__)
SAVED_DATA = os.path.join(dirname, "clipboard.json")

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
    
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
        
def run_functionality(command):
    data = load_data(SAVED_DATA)
    if command == "help":
        print("""\
              Save   - Save your current clipboard
              Load   - Load a clipboard item
              List   - List all saved items
              Delete - Delete a clipboard key
              Now    - Check current clipboard
              [None] - Prompts a command""")
    elif command == "save":
        key = input("Enter a key: ")
        if key == "":
            print("Command Canceled.")
            return
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key == "":
            print("Command Canceled.")
            return
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist!")
    elif command == "delete":
        key = input("Enter a key to delete: ")
        if key == "":
            print("Command Canceled.")
            return
        if key in data:
            data.pop(key, None)
            save_data(SAVED_DATA, data)
            print(f"The key of {key} was deleted.") 
        else:
            print("Key does not exist!")    
    elif command == "list":
        if len(data) > 0:
            for key in data:
                print("Key:", key, "- Output:", data[key])
        else:
            print("No saved keys.")
    elif command == "now":
        print(clipboard.paste())
    else:
        print("Unknown Command")
                
if len(sys.argv) == 2:
    command = sys.argv[1].lower()
    run_functionality(command)
elif len(sys.argv) == 1:
    command = input("Enter a command (Save, Load, List, Delete, Now, Help): ")
    run_functionality(command.lower())
else:
    print("Please type in exactly one command or leave blank.")