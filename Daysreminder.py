'''
names = ["nanda", "usha", "udi", "rithi", "et cetra"]
del names[2:3]
print(names)
del names[1]
print(names)
names.remove("et cetra")
print(names)
names.append("soma")
print(names)
names.insert(2, "pammi")
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.reverse()
print(names)

name = ["nanda", "usha", "udi", "rithi", "et cetra"]
newname = name.pop()
print(name)
print(newname)
newname = name.pop(3)
print(newname)
'''
'''
#copy module - deepcopy

import copy
ex_1 = [1, 2, 3]
ex_2 = copy.deepcopy(ex_1)
print(ex_1)
print(ex_2)
'''


def get_reminder(filepath = "files/reminder.txt"):
    with open(filepath, 'r') as f_local:
        reminder_local =f_local.readlines()
    return reminder_local


def write_reminder(reminder_arg, filepath = "files/reminder.txt"):
    with open(filepath, 'w') as file:
        file.writelines(reminder_arg)



import functions
import FreeSimpleGUI as fsg
label = fsg.Text("enter today's reminder")
input_box = fsg.InputText(tooltip="enter reminder", key="reminder")
add_button = fsg.Button("add")
lists_box = fsg.Listbox(values=get_reminder(), key="reminders",
                        enable_events=True, size=[45, 10])

window = fsg.Window("Days-reminder",layout=[[label], [input_box, add_button], [lists_box]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            reminders = get_reminder()
            new_reminder = values['reminder'] + "\n"
            reminders.append(new_reminder)
            write_reminder(reminders)
            window['reminders'].update(values=reminders)
        case fsg.WIN_CLOSED:
            break
window.close()
