from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import os

###Functions
def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def browse(frame):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    load_img(frame,filename)

def load_img(frame,path):
    clear_widget(frame)
    load = Image.open(path).resize((300,300), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img_panel = Label(frame, image=render)
    img_panel.image = render
    img_panel.pack()

def openeditor():
    webbrowser.open("rule.txt")

def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def pad(pad_type,frame,row_,column_,val):
    if(pad_type == "horizontal"):
        pad_frame = Frame(frame, width=val)
        pad_frame.grid(row=row_, column=column_)
    elif(pad_type == "vertical"):
        pad_frame = Frame(frame, height=val)
        pad_frame.grid(row=row_, column=column_)

def OnDoubleClick(event):
    item = tree.selection()[0]
    img_name = tree.item(item,"text") + ".jpg"

    exist = False
    entries = os.listdir(os.getcwd() + "/Shape_collections/")
    for entry in entries:
        if(entry == img_name):
            exist = True
    
    if(exist):
        path = os.getcwd() + "/Shape_collections/" + img_name
        try:
            load_img(detection_img_frame, path)
        except BaseException:
            print("Cannot load file.")

###Code

root = Tk()
root.title("TUBES 2 AI")

###========== Upper Frame
upper_window = Frame(root)#init window
upper_window.pack(side=TOP)

###==================== Source Image Panel
source_img_lbl = Label(upper_window, text="Source Image")
source_img_lbl.grid(row=0, column=0)

source_img_frame = Frame(upper_window, height=300, width=300, bg= from_rgb((255, 255, 255)))
source_img_frame.grid(row=1, column=0)

path = os.getcwd() + "/Shape_collections/init_source.jpg"
load_img(source_img_frame,path)

pad("horizontal",upper_window,1,1,10)

###==================== Detection Image Panel
detection_img_label = Label(upper_window, text="Detection Image")
detection_img_label.grid(row=0, column=2)

detection_img_frame = Frame(upper_window, height=300, width=300, bg= from_rgb((255, 255, 255)))
detection_img_frame.grid(row=1, column=2)

path = os.getcwd() + "/Shape_collections/init_detection_img.jpg"
load_img(detection_img_frame,path)

pad("horizontal",upper_window,1,3,10)

###==================== Menu Panel
menu_frame = Frame(upper_window, width=200, height=300)
menu_frame.grid(row=1, column=4)

###==================== Generate Padding for menu frame
for i in range(2,9):
    if(i%2 == 0):
        #pad([vertical or horizontal],window,row,column,[height or width])
        pad("vertical",menu_frame,i,0,10)

###==================== Buttons
###============================== Open Image
open_img_btn = Button(menu_frame, text="Open Image", bg ="white", fg="black", width=18, command= lambda:browse(source_img_frame))
open_img_btn.grid(row=1, column=0)

###============================== Open Rules
open_rule_btn = Button(menu_frame, text="Open Rule Editor", bg ="white", fg="black", width=18, command= lambda:openeditor())
open_rule_btn.grid(row=3, column=0)

###============================== Show Rules
show_rule_btn = Button(menu_frame, text="Show Rules", bg ="white", fg="black", width=18)
show_rule_btn.grid(row=5, column=0)

###============================== Show Facts
show_facts_btn = Button(menu_frame, text="Show Facts", bg ="white", fg="black", width=18)
show_facts_btn.grid(row=7, column=0)

###============================== TreeView
menu_lbl = Label(menu_frame, text="What shape do you want")
menu_lbl.grid(row=9, column=0)

tree = ttk.Treeview(menu_frame)
tree.grid(row=10, column=0)
tree.config(height=5)

tree.insert('', '0', 'root', text="All Shapes")

tree.insert('root', '1', 'triangle', text="Triangle")
tree.insert('triangle', '0', 'triangle-var1', text="Acute Triangle")
tree.insert('triangle', '1', 'triangle-var2', text="Blunt Triangle")
tree.insert('triangle', '2', 'triangle-var3', text="Equilateral Triangle")
tree.insert('triangle', '3', 'triangle-var4', text="Right Triangle")
tree.insert('triangle', '4', 'triangle-var5', text="Isosceles Triangle")
tree.insert('triangle-var5', '0', 'triangle-var5-1', text="Taper Isosceles Triangle")
tree.insert('triangle-var5', '1', 'triangle-var5-2', text="Blunt Isosceles Triangle")

tree.insert('root', '2', 'quad', text="Quadrilateral")
tree.insert('quad', '0', 'quad-var1', text="Parallelogram")
tree.insert('quad-var1', '0', 'quad-var1-1', text="Kite")
tree.insert('quad-var1', '1', 'quad-var1-2', text="Square")
tree.insert('quad', '1', 'quad-var2', text="Trapezoidal")
tree.insert('quad-var2', '0', 'quad-var2-1', text="Isosceles Trapezoid")
tree.insert('quad-var2', '1', 'quad-var2-2', text="Right Trapezoid")
tree.insert('quad-var2', '2', 'quad-var2-3', text="Left Trapezoid")

tree.insert('root', '3', 'pentagon', text="Pentagon")
tree.insert('pentagon', '0', 'pentagon-var1', text="Irregular Pentagon")
tree.insert('pentagon', '1', 'pentagon-var2', text="Regular Pentagon")

tree.insert('root', '4', 'hexagon', text="Hexagon")
tree.insert('hexagon', '0', 'hexagon-var1', text="Irregular Hexagon")
tree.insert('hexagon', '1', 'hexagon-var2', text="Regular Hexagon")

tree.bind("<Double-1>", OnDoubleClick)

###========== Bottom Frame
bottom_window = Frame(root)
bottom_window.pack(side=BOTTOM)

###==================== Generate Padding
for i in range(0,7):
    if(i%2 == 0):
        pad("horizontal",bottom_window,1,i,10)

for i in range(0,6):
    if(i%2 == 0):
        pad("vertical",bottom_window,2,i,10)

###==================== Detection Result Panel
detection_result = Label(bottom_window, text="Detection Image")
detection_result.grid(row=0, column=1)

detection_result_frame = Frame(bottom_window, height=270, width=270, bg= from_rgb((255, 255, 255)))
detection_result_frame.grid(row=1, column=1)

###==================== Matched Facts
matched_facts = Label(bottom_window, text="Matched Facts")
matched_facts.grid(row=0, column=3)

matched_facts_frame = Frame(bottom_window, height=270, width=270, bg= from_rgb((255, 255, 255)))
matched_facts_frame.grid(row=1, column=3)

###==================== Hit Rules
hit_rules = Label(bottom_window, text="Hit Rules")
hit_rules.grid(row=0, column=5)

hit_rules_frame = Frame(bottom_window, height=270, width=270, bg= from_rgb((255, 255, 255)))
hit_rules_frame.grid(row=1, column=5)

root.mainloop()