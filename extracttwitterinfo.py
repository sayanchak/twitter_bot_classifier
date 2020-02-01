import tweepy
from tkinter import *
from tkinter import ttk


api_key = 'qbIsaXtZI5Lonofq2sj4NlUa5'
secret_key = 'exsK4pzO7VDNIK02yTXEFVfTNmJC2HmWmycijqOhh2EuNKCr0d'
auth = tweepy.OAuthHandler(api_key, secret_key)
api = tweepy.API(auth)

user_info = api.get_user('nichememer')
global created_at
global follower_count
global friends_count
global listed_count
global favorites_count
global statuses_count
global verified
global default_profile
global default_profile_image
created_at = user_info.created_at
follower_count = user_info.followers_count
friends_count = user_info.friends_count
listed_count = user_info.listed_count
favorites_count = user_info.favourites_count
statuses_count = user_info.statuses_count
verified = user_info.verified
default_profile = user_info.default_profile
default_profile_image = user_info.default_profile_image


root = Tk()
root.geometry("500x300")

data = [["created_at", str(created_at)],
        ["follower_count", str(follower_count)],
        ["friends_count", str(friends_count)],
        ["listed_count", str(listed_count)],
        ["favorites_count", str(favorites_count)],
        ["statuses_count", str(statuses_count)],
        ["verified", str(verified)],
        ["default_profile", str(default_profile)],
        ["default_profile_image", str(default_profile_image)]]


frame = Frame(root)
frame.pack()

tree = ttk.Treeview(frame, columns=(1,2), height=9, show="headings")
tree.grid(row=1, column=1)
tree.heading(1, text="Model Variables")
tree.heading(2, text="User Data")
tree.column(1, width=150)
tree.column(2, width=150)
for val in data:
    tree.insert('', 'end', values=(val[0], val[1]))
root.mainloop()