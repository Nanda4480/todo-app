'''

import functions
import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

window.read()
window.close()

'''
'''
import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

window.read()
window.close()
'''

import FreeSimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

label2 = sg.Text("what occupies more on earth?")
option5 = sg.Radio("land", group_id="question2")
option6 = sg.Radio("water", group_id="question2")
option7 = sg.Radio("Forest", group_id="question2")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                            [option2],
                            [option3],
                            [option4],
                           [label2], [option5], [option6], [option7]])

window.read()
window.close()