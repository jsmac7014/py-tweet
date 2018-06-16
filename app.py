from tkinter import *
from tweet import *

def search():
    tweet_list.delete(0,'end')
    index = 0
    count = input_count.get()
    username = input_name.get()
    tweets = get_result(username,count).most_common()
    for tweet in tweets:
        index+=1
        tweet_list.insert(index, str(tweet[0])+":"+str(tweet[1]))


root = Tk()
root.title("Twitter Search")
root.geometry("300x400")
root.resizable(False,False)

lbl_id = Label(root, text="트위터 아이디")
lbl_id.pack()

input_name = Entry(root)
input_name.insert(0,"아이디")
input_name.pack()

input_count = Entry(root)
input_count.insert(0,"개수")
input_count.pack()

btn = Button(root, text="검색" , command=search)
btn.pack()

lbl_list = Label(root, text="결과")
lbl_list.pack()
tweet_list = Listbox()
tweet_list.config(width=30)
tweet_list.pack()

root.mainloop()