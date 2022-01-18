from tkinter import *
import random
from PIL import ImageTk, Image
# python image library
root = Tk()

root.title("Endless Dice Game")
root.geometry("600x400")

root.configure(background = "yellow2")

i1 = Image.open("pokeball.png")
i1 = i1.resize((100,100),Image.ANTIALIAS)
img = ImageTk.PhotoImage(i1)
img1 = ImageTk.PhotoImage(Image.open ("abra.jpg"))
img2 = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
img3 = ImageTk.PhotoImage(Image.open ("charmender.jpg"))
img4 = ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
img5 = ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
img6 = ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
img7 = ImageTk.PhotoImage(Image.open ("meowth.jpg"))
img8 = ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
img9 = ImageTk.PhotoImage(Image.open ("paras.jpg"))
img10 = ImageTk.PhotoImage(Image.open ("persion.jpg"))
img11 = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
img12 = ImageTk.PhotoImage(Image.open ("ratata.jpg"))
img13 = ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
player1score = 0;
player2score = 0;
dice = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13]
dice_number= [10,30,30,50,20,20,20,30,20,30,150,30,30]

def player1roll():
    global player1score
    r1 = random.randint(0,12)
    print(r1)
    p1 = dice[r1]
    print(dice_number[r1])
    Pokemon['image'] = p1
    random_dice_label["text"] = "Player 1 Pokemon is : " + str(dice_number[r1])
    player1score = player1score + dice_number[r1]
    player_1_score["text"] = str(player1score)

player1 = Label(root, text = 'Player 1', bg = "royal blue", fg = 'white')
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

def player2roll():
    global player2score
    r1 = random.randint(0,12)
    print(r1)
    p2 = dice[r1]
    print(dice_number[r1])
    Pokemon['image'] = p2
    random_dice_label["text"] = "Player 2 Pokemon is : " + str(dice_number[r1])
    player2score = player2score + dice_number[r1]
    player_2_score["text"] = str(player2score)

place2 = Label(root, text = 'Player 2', bg = 'royal blue', fg = 'white')
place2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score =  Label(root, bg = 'royal blue', fg = 'white')
player_1_score.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score = Label(root, bg = 'royal blue', fg = 'white')
player_2_score.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = 'chocolate1', fg = 'white')
random_dice_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

Pokemon = Label(root)
Pokemon.place(relx = 0.5, rely = 0.5, anchor = CENTER)

player1_btn = Button(root, image = img, command = player1roll)
player1_btn.place(relx = 0.1, rely = 0.7, anchor = CENTER)

player2_btn = Button(root, image = img, command = player2roll)
player2_btn.place(relx = 0.9, rely = 0.7, anchor = CENTER)

root.mainloop()