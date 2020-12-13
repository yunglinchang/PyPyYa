from jobindustry_GUI import *
from Course_GUI import *
import os
import sys

sys.path.append(os.path.abspath(os.path.join('.', 'data')))

# %% Exit the search window
def exit_program(root):
    root.destroy()
    
# %% Search event
def searchConduct(root,key_word):
    # Get the input key word
    key = key_word.get()
    
    p1= os.path.abspath(os.path.join('.', 'data'))
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
    # frame_first_center=Frame(root,width=700,height=30)
    # frame_first_center.grid(row=0, column=0,columnspan=10,padx=5)
    theme = tk.Label(root,text='PyPyYa',fg="orange",font=("Times New Roman",16,"bold"))
    theme.place(x=300,y=5)
    
    # Create and place the search line
    #frame_second_center=Frame(root,width=700,height =30)
    #frame_second_center.grid(row=1, column=0,columnspan=20,padx=5)
    tk.Label(root, text='Key word:',font=("Times New Roman",12)).place(x=5,y=30)
    key = tk.StringVar()
    entry_key_word = tk.Entry(root, width=50,textvariable=key)
    entry_key_word.place(x=80,y=30)
    # Search button
    btn_search = tk.Button(root, text='Search', 
                          command=lambda: searchConduct(window,key))
    btn_search.place(x=450,y=30)
    
    # Exit button
    btn_exit = tk.Button(root, text = 'Exit', width = 6,
                         command=lambda:exit_program(window))
    btn_exit.place(x=500,y=30)
    
    #frame_first_center.grid_propagate(0)
    #frame_second_center.grid_propagate(0)
    
# %% 
if __name__ == "__main__":
    window = tk.Tk()
    window.title("PyPyYa")
    window.attributes('-fullscreen', True)
    warnings.filterwarnings('ignore')
    window_layout(window)   
    window.mainloop()

