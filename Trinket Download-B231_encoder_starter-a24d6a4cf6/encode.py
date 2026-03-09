#   encode.py 6-10-24
#   Note this will not run in the code editor and must be downloaded
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image

BLOCK_SIZE = 21 # default turtle size
TRTL_START_LOC = 220 

message = "change me"

characters_as_ints = []
for cha in message:
  characters_as_ints.append(ord(cha))

characters_as_bits = []
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))

bits_as_ints = []
for index in range(0,len(characters_as_bits)):
  for bit in characters_as_bits[index]:
    bits_as_ints.append(bit)

screen = trtl.getscreen()
screen.setup(1.0, 1.0, startx=0, starty=0)

painter = trtl.Turtle()
painter.penup()
painter.speed(0)
painter.shape("square")
painter.goto(-TRTL_START_LOC, TRTL_START_LOC)
painter.color("red")
painter.stamp()

painter.color("blue")
index = 0
while index < len(bits_as_ints):
  painter.forward(BLOCK_SIZE)
  if index % 8 == 0:
    painter.goto(-TRTL_START_LOC, painter.ycor()-BLOCK_SIZE)
  if bits_as_ints[index] == '1':
    painter.stamp()
  index += 1

screen.setup(1.0, 1.0)

def create_image():
  root = trtl.getcanvas().winfo_toplevel()
  x0 = root.winfo_rootx()
  y0 = root.winfo_rooty()
  x1 = x0 + root.winfo_width()
  y1 = y0 + root.winfo_height()
  painter.hideturtle()
  ImageGrab.grab().crop((x0, y0, x1, y1)).save("output.png")

try:
  create_image()
  tk.messagebox.showinfo(message="Your screenshot was captured in the output.png file.")
except:
  tk.messagebox.showinfo(message="Take a manual sreenshot of the encoding.\nSave/rename the file to \"output\".\nClose the window when done.")
  trtl.mainloop()

answer = tk.messagebox.askyesno(message="Is your output file correct?")
if not answer: 
  tk.messagebox.showinfo(message="Take a manual sreenshot of the encoding.\nSave/rename the file to \"output.png\".\nClose the window when done.")
  trtl.mainloop()