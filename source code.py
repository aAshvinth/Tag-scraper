import requests
from bs4 import BeautifulSoup
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def scrap_tags():
    #Gets the "keywords and "title" from the url
    url = entry.get()
    return_value = requests.get(url)

    if return_value.status_code == 200:
        html = return_value.content
        soup = BeautifulSoup(html, "html.parser")
        keywords = soup.find("meta", attrs={"name": "keywords"})
        title = soup.find("meta", attrs={"property": "og:title"})
        now = datetime.now()
        Time = now.strftime("%Y-%m-%d %H:%M:%S")
        if title:
            title = title["content"]
            keywords = keywords["content"].split(",")
            with open("Tags.txt", "a") as file:
                file.write(" " + "\n")
                file.write(
                    "-------------------------------------------------------------------------------------------\n"
                )
                file.write(Time + " \n")
                file.write("Video Title= " + title + "\n")
                file.write("Tags for the video " + url + " = " + "\n")
                for keyword in keywords:
                    file.write(", " + keyword + "\n")
                file.write("-------------------------------------------------------------------------------------------\n")
                file.write(" " + "\n")
                
            # displays the scrapped datat 
            tags_text.delete('1.0', tk.END)
            tags_text.insert(tk.END,"(Tags are stored in Tags.txt)"+"\n"+ "Tags for the video '" + title + "': \n\n" +', '.join(keywords))
        else:
            messagebox.showerror("Error", "Data for the url not found.")
    else:
        messagebox.showerror("Error", "Invalid URL")

root = tk.Tk()
root.geometry("500x500")
root.title("Get Video Tags")

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame, width=50)
entry.pack()

button = tk.Button(frame, text="Fetch", command=scrap_tags)
button.pack()
url_text = tk.Label(frame, text="Enter the URL above ^^^")
url_text.pack(side=tk.LEFT)

#Displays the tags in the windows
tags_text = tk.Text(root, height=20, width=70)
tags_text.pack()

root.mainloop()
