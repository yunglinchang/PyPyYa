import pandas as pd
import re
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import Scrollbar

# %% Course search
class course:
    def __init__(self, key_word, data_path, root):
        self.key_word = key_word
        self.data_path = data_path
        self.root = root

    # Seach for course information that matches the key word
    def searchCourse(self):
        key_word = self.key_word.replace(" ", ".*")
        df = pd.read_csv(self.data_path, index_col=0)
        new_df = df
        new_df.fillna("", inplace=True)
        new_df["in_title"] = new_df["Title"].apply(
            lambda x: 1 if re.search(key_word, x) else 0
        )
        new_df["in_desc"] = new_df["Description"].apply(
            lambda x: 1 if re.search(key_word, x) else 0
        )
        title_df = new_df[new_df["in_title"] == 1]
        desc_df = new_df[new_df["in_desc"] == 1]
        result_df = title_df.append(desc_df)
        result_df = result_df
        result_df = result_df.iloc[:, :4]
        result_arr = result_df.values
        return result_arr

    # Get the search result and create the "Course" table
    def selectCourse(self, result):
        label4 = tk.Label(
            self.root, text="Course", font=("Times New Roman", 14, "bold")
        )
        label4.place(relx=0.5, rely=0.1)

        var = tk.StringVar()
        textLabel = tk.Label(self.root, textvariable=var, fg="red")
        textLabel.place(relx=0.62, rely=0.1)

        columns = ("Department", "Title", "Number", "Unit")
        tree = ttk.Treeview(
            self.root, height=17, show="headings", selectmode="browse", columns=columns
        )

        tree.column(columns[0], width=75)
        tree.column(columns[1], width=175)
        tree.column(columns[2], width=55)
        tree.column(columns[3], width=42)

        for i in columns:
            tree.heading(i, text=i)

        tree.place(relx=0.5, rely=0.13)

        i = 0

        # When the search button is clicked, reset the table
        self.delButton(tree)
        var.set("")

        # display number of match results found
        result_str = "Number of result: " + str(len(result))
        var.set(result_str)

        for item in result:
            tree.insert("", i, values=(item[0], item[1], item[2], item[3]))
            i = i + 1

    # Delete all items in the treeview
    def delButton(self, tree):
        x = tree.get_children()
        for item in x:
            tree.delete(item)

