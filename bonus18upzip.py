import FreeSimpleGUI as sg
from unzipcodes import extract_zip

sg.theme('DarkAmber')

label1 = sg.Text("select archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose", key="archive")

label2 = sg.Text("select destination dir")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose", key="folder")

extract_button = sg.Button("extract")
output_label = sg.Text(key="output")

window = sg.Window("Zip Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_zip(archivepath, dest_dir)
    window["output"].update(value="zip extraction completed")
window.read()
window.close()