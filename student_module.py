import json
import pandas as pd

def read_data(): # read json file
    with open("students.json","r") as get_data:
      data= json.load(get_data)
      return data
     
def save_data(data): #write and save json file
    stu_list = list(read_data())
    stu_list.append(data)
    with open('students.json', 'w') as save:
            stu_list = json.dump(stu_list, save, indent=4)

class Student:
    
    def __init__(self,Filepath):
        self.Filepath = Filepath
        try:
            file = open(Filepath,'r') #file reading if already exists
        except IOError:
            file = open(Filepath,'w') #file creating if not exists 
            file.write('[]')      
        
    def create(self,**kwargs): # creating data 
        save_data(kwargs)
        
    def read(self): #reading all data
        self.data = read_data() 
        for k in self.data:
               print(k)
    
    def read_single(self,id): #reading single data
        self.data = read_data()
        for i in self.data:
            if i['id'] == id:
                print(i)
                
    def update(self,id,name,rollno,age): #updating value single record
      df = pd.read_json('students.json', orient='records')
      df.loc[df['id'] == id, 'name'] = name
      df.loc[df['id'] == id, 'rollno'] = rollno
      df.loc[df['id'] == id, 'age'] = age
      df.to_json('students.json', orient='records',indent=4)     
    
    def delete(self,id): #delete single record
      df = pd.read_json('students.json', orient='records')
      df = df[df.id != id]
      df.to_json('students.json', orient='records',indent=4)

    
    def export_json(data): # importing data into file
      with open("students.json", "r") as fr, open("save_data.json", "w") as to:
          to.write(fr.read())