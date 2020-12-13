# PyPyYa
**Your career service from coursework to dream work!**

Nowadays, students ranging from bachelors to more advanced degrees often face a common problem in the job market. There is an information gap between what they have learned and what the job market looks for. In most instances, students lack the key skills that would harm their qualifications for their dream jobs! They also have no idea about career tendency. Life is a one-way journey. What if there is a system that maps out all the must-take courses at your university for the job and tells you how to match your abilities to the actual labor market? You could take a guide, and that is us!

**Introducing--PyPyYa!**

## Demo
Video: https://youtu.be/SyYz-tfTMEI


![alt text](https://github.com/yunglinchang/PyPyYa/blob/master/demo/demo.jpg?raw=true)

## The Team--Group 10:
* **CEO**: Jack Chang   |  yunglinc@andrew.cmu.edu
* **COO**: Crystal Chen |  yiwenc2@andrew.cmu.edu 
* **CTO**: Yumin Chen   |  yuminc@andrew.cmu.edu 
* **CFO**: Siqin Deng   |  siqideng@andrew.cmu.edu

## Structure:
```
.
├── README.md
├── .DS_Store
├── .gitattributes
├── LICENSE
├── data
│   ├── DataAnalyst.csv           
│   ├── DataEngineer.csv             
│   ├── DataScientist.csv      
│   ├── Labor_statistics.csv
│   └── course_clean.csv
├── requirement.txt           
└── scripts
    ├── course_description.py
    ├── Course_GUI.py
    ├── get_sched_table.py
    ├── jobindustry_GUI.py
    ├── main.py
    └── merge_xls.py
```


## Setup:
1. Clone the PyPyYa repository
```
git clone https://github.com/yunglinchang/PyPyYa.git
```
2. Change directory to PyPyYa folder
```
cd PyPyYa
```
3. Setup and install all the dependencies
```
pip install –r requirements.txt
```
Note: The version of the dependencies used are recorded in the requirements.txt document.
* beautifulsoup4==4.8.0
* matplotlib==3.1.3
* nltk==3.4.5
* numpy==1.18.5
* pandas==0.25.3
* Pillow==6.2.0
* regex==2020.11.13
* seaborn==0.10.1
* selenium==3.141.0
* wordcloud==1.7.0

If pip install does not work for you, you could try utilizing the conda installation with Anaconda.
```
conda install --yes --file requirements.txt
```
4. Run the Python file in terminal
```
python3 ./scripts/main.py
```


## Data Source:
* **DataAnalyst.csv**: job data from [picklesueat/data_jobs_data](https://github.com/picklesueat/data_jobs_data)
* **DataEngineer.csv**: job data from [picklesueat/data_jobs_data](https://github.com/picklesueat/data_jobs_data)
* **DataScientist.csv**: job data from [picklesueat/data_jobs_data](https://github.com/picklesueat/data_jobs_data)
* **Labor_statistics.csv**: scraped from [U.S. Bureau of Labor Statistics](https://data.bls.gov/projections/nationalMatrix?queryParams=15-2098&ioType=o) using jobindustry_GUI.py
* **course_clean.csv**: scraped from [Carnegie Mellon University - Schedule of Classes](https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/search) using course_description.py and get_sched_table.py, and integrated with merge_xls.py

## Python file:
* **course_description.py**: Scrape course description data from Schedule of Classes(SOC).
* **Course_GUI.py**: Provide user interface of PaPaYa.
* **get_sched_table.py**: Scrape course schedule data from SOC.
* **jobindustry_GUI.py**: Read data from job search csv file and scrap data from U.S. Labor Statisticts. Convert the data into bar/plot graph and Data Frame table. 
* **main.py**: Main python file to execute all the other python files.
* **merge_xls.py**: Merge course description and schedule data on course ID and integrate department information.

## License
MIT License

Copyright (c) [2020] [Yung-Lin Chang, Crystal Chen, Yumin Chen, Siqin Deng]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You must write exactly ONE "README" file, submitted as a PDF, MS-Word, or .txt file, that gives us instructions on how to install and run your project, including installing any additional Python modules beyond what Anaconda provides; setting environment variables (please avoid if possible); obtaining an API key; or the like.  (If your project requires packages/modules other than what Anaconda provides, tell us what we need to do MANUALLY to install those: do not auto-install those within your project: it's too hard for us to un-install things that were auto-installed.)  Include the names and email addresses of all Group members in the "README" file. Give us screen shots to look at, when that would be helpful.  DO NOT write a "README" file that refers us to other "README" files elsewhere.  To repeat: ONE "README" file only, submitted as a PDF, MS-Word, or .txt file.
