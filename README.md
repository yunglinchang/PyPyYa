# PyPyYa
**Your career service from coursework to dream work!**

Nowadays, students ranging from bachelors to more advanced degrees often face a common problem in the job market. There is an information gap between what they have learned and what the job market looks for. In most instances, students lack the key skills that would harm their qualifications for their dream jobs! They also have no idea about career tendency. Life is a one-way journey. What if there is a system that maps out all the must-take courses at your university for the job and tells you how to match your abilities to the actual labor market? You could take a guide, and that is us!

**Introducing--PyPyYa!**

## Demo
![alt text](https://github.com/yunglinchang/PyPyYa/blob/master/demo.jpg?raw=true)

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
│   └── csv
├── requirement.txt           
└── scripts
    ├── course_description.py
    ├── Course_GUI.py
    ├── jobindustry_GUI.py
    └── main.py
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