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
        pass
    elif nav_Input == "D":
        pass
    else:
        slow_text("Invalid Input, Please try again.")
        navigation()

def add_Item():
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

    with open("todo.json", "w") as f:
        todos = load_json()
        values = {"content": current_item.get_content(),"date": current_item.get_date()}
        todos[current_item.get_name()] = values
        json.dump(todos, f)


def slow_text(text):
    text = list(text)
    for i in text:
        print(i, end="", flush = True)
        time.sleep(0.025)

menu()