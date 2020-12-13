from jobindustry_GUI import *
from Course_GUI import *


# %% Exit the search window
def exit_program(root):
    root.destroy()
    
# %% Search event
def searchConduct(root,key_word):
    # Get the input key word
    key = key_word.get()
    
    p1=r'./data/'
    p2='./data/course_clean.csv'
    other_sw = ['race', 'color', 'gender','disability', 'sexual', 'religion', 'attorney', 'status', 'employment', 'opportunities', 'consideration', 'equal']
    # Declare a jobindustry object
    j = jobindustry(p1, key)
    df,table_ = j.read_data()
    j.process_data(df)
    new_df= j.map_industry_return_df(df,table_)
    phrase_df = j.find_phrase(new_df)
    # Display the bar plot
    j.barplot_loc_sal(root,phrase_df)
    # Display the distribution plot
    j.distplot_salary(root,phrase_df)
    # Display the wordcloud
    j.wordcloud_ngrams(root,phrase_df, other_sw)
    # Declare a course object
    c = course(key,p2,root)
    result = c.searchCourse()
    # Display the course search result
    c.selectCourse(result)
    # Display related industry prospect
    j.nt_summary(root,phrase_df)

# %% main window layout
def window_layout(root):
     # Create and place the title line
    frame_first_center=Frame(root,width=700,height=30)
    frame_first_center.grid(row=0, column=0,columnspan=10,padx=5)
    theme = tk.Label(frame_first_center,text='PyPyYa',fg="orange",font=("Times New Roman",16,"bold"))
    theme.place(x=300,y=5)
    
    # Create and place the search line
    frame_second_center=Frame(root,width=700,height =30)
    frame_second_center.grid(row=1, column=0,columnspan=20,padx=5)
    tk.Label(frame_second_center, text='Key word:',font=("Times New Roman",12)).grid(row=1, column=0,columnspan=2,sticky = tk.W)
    key = tk.StringVar()
    entry_key_word = tk.Entry(frame_second_center, width=70,textvariable=key)
    entry_key_word.grid(row=1, column = 2,columnspan=6,padx=5)
    # Search button
    btn_search = tk.Button(frame_second_center, text='Search', 
                          command=lambda: searchConduct(window,key))
    btn_search.grid(row=1, column=8,padx=5)
    
    # Exit button
    btn_exit = tk.Button(frame_second_center, text = 'Exit', width = 6,
                         command=lambda:exit_program(window))
    btn_exit.grid(row=1, column=9)
    
    frame_first_center.grid_propagate(0)
    frame_second_center.grid_propagate(0)
    
# %% 
if __name__ == "__main__":
    window = tk.Tk()
    window.title("PyPyYa")
    window.attributes('-fullscreen', True)
    warnings.filterwarnings('ignore')
    window_layout(window)   
    window.mainloop()

