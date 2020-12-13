from jobindustry_GUI import *
from Course_GUI import *

# %% Exit the search window
def exit_program(root):
    root.destroy()


# %% Search event
def searchConduct(root, key_word):
    # Get the input key word
    key = key_word.get()
    p1 = "./data/"
    p2 = "./data/course_clean.csv"
    other_sw = [
        "race",
        "color",
        "gender",
        "disability",
        "sexual",
        "religion",
        "attorney",
        "status",
        "employer",
        "employment",
        "opportunities",
        "opportunity",
        "consideration",
        "origin",
        "year",
        "years" "equal",
    ]
    # Declare a jobindustry object
    j = jobindustry(p1, key, root)
    df, table_ = j.read_data()
    j.process_data(df)
    new_df = j.map_industry_return_df(df, table_)
    phrase_df = j.find_phrase(new_df)
    # Display the bar plot
    j.barplot_loc_sal(phrase_df)
    # Display the distribution plot
    j.distplot_salary(phrase_df)
    # Display the wordcloud
    j.wordcloud_ngrams(phrase_df, other_sw)
    # Declare a course object
    c = course(key, p2, root)
    result = c.searchCourse()
    # Display the course search result
    c.selectCourse(result)
    # Display related industry prospect
    j.nt_summary(phrase_df)


# %% main window layout
def window_layout(root):
    # Create and place the title line
    theme = tk.Label(
        root, text="PyPyYa", fg="orange", font=("Times New Roman", 16, "bold")
    )
    theme.place(relx=0.5, rely=0.03, anchor="center")

    # Create and place the search line
    tk.Label(root, text="ENTER KEYWORD:", font=("Times New Roman", 16, "bold")).place(
        relx=0.03, rely=0.05, anchor="nw"
    )
    key = tk.StringVar()
    entry_key_word = tk.Entry(root, width=40, textvariable=key)
    entry_key_word.place(relx=0.25, rely=0.05)
    # Search button
    btn_search = tk.Button(
        root, text="Search", command=lambda: searchConduct(window, key)
    )
    btn_search.place(relx=0.87, rely=0.05, anchor="ne")

    # Exit button
    btn_exit = tk.Button(
        root, text="Exit", width=6, command=lambda: exit_program(window)
    )
    btn_exit.place(relx=0.95, rely=0.05, anchor="ne")


# %%
if __name__ == "__main__":
    window = tk.Tk()
    window.title("PyPyYa")
    window.geometry("735x650")
    warnings.filterwarnings("ignore")
    window_layout(window)
    window.mainloop()
