import json
import datetime
import time

class item():
    def __init__(self, name, content, date):
        self.name = name
        self.content = content
        self.date = date
    
    def get_name(self):
        return self.name
    
    def get_content(self):
        return self.content
    
    def get_date(self):
        return self.date

def load_json():
    try:
        with open("todo.json", "r") as f:
            return json.load(f)
    except:
        return {}

def menu():
    load_json()
    slow_text("To Do List\nPython Text Based App\n")
    navigation()

def navigation():
    slow_text("\nNAVIGATION:\nAdd Item, A\nView Items, V\nDelete Items, D\nChoose a navigation option")
    nav_Input = input(">>\n")

    if nav_Input == "A":
        add_Item()
    elif nav_Input == "V":
        view_Items()
    elif nav_Input == "D":
        delete_Item()
    else:
        slow_text("Invalid Input, Please try again.")
        navigation()

def save_Item(data):
    with open("todo.json", "w") as f:
        json.dump(data, f)

def add_Item():
    todos = load_json()
    slow_text("\nEnter item name")
    name = input("\n>> ")
    slow_text("\nEnter content")
    content = input("\n>> ")
    slow_text("\nEnter task deadline")
    year = int(input("\nYear >> "))
    month = int(input("Month >> "))
    day = int(input("Day >> "))
    date = [day,month,year]
    current_item = item(name,content,date)
    values = {"content": current_item.get_content(),"date": current_item.get_date()}
    todos[current_item.get_name()] = values
    save_Item(todos)

def view_Items():
    data = load_json()
    
    for i in data:
        content = data[i]["content"]
        date = datetime.date(data[i]["date"][2],data[i]["date"][1],data[i]["date"][0])
        slow_text(f"{i} | {content}\nDeadline:{date}\n")

def delete_Item():
    data = load_json()

    slow_text("\nEnter name of item to delete")
    name = input("\n>> ")

    try:
        del data[name]
        save_Item(data)
        slow_text("Item Deleted")
    except:
        slow_text("Item does not exist.")


def slow_text(text):
    text = list(text)
    for i in text:
        print(i, end="", flush = True)
        time.sleep(0.025)

menu()

# Next add -
# Expiration to items
# Ability to tick off items