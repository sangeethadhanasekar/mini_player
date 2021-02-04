import PySimpleGUI as sg
import sqlite3
conn=sqlite3.connect('reminder2.db')
c=conn.cursor()

def update_UI():
    
        window.FindElement('taskname').Update(value="")
        window.FindElement('dated').Update(value="")
        window.FindElement('drop_down').Update(value="")
        window.FindElement('check1').Update(value="")


def add_work(values):
    
    insert_query="""INSERT INTO 'tasks'('completion','taskname','duedate','priority')VALUES(?,?,?,?)"""
    count=c.execute(insert_query,(values['check1'],values['taskname'],values['dated'],values['drop_down']))
    conn.commit()
    for row in c.execute('SELECT *  FROM tasks '):
       #print(type(row))
       row=c.execute('SELECT * FROM tasks')
       #print(row)
       #rowtask.append(list(row))
       window.FindElement('list_box').Update([])
       window.FindElement('list_box').Update(values=row)
    update_UI()   
       
       
def edit_work(event,values):
    print(event,values)
    edit_value=list(values['list_box'][0])
    print("edit_value",edit_value)
            
    if event=='edit_work' or values['list_box']!="":
        print("exit_executed")
        edit_value=list(values['list_box'][0])
        print("edit_value",edit_value)
        
        check_box=bool(edit_value[0])
        edit_taskname=str(edit_value[1])
        edit_date=edit_value[2]
        edit_drop=edit_value[3]
        window.FindElement('taskname').Update(value=edit_taskname)
        window.FindElement('dated').Update(value=edit_date)
        window.FindElement('drop_down').Update(value=edit_drop)
        window.FindElement('check1').Update(value=check_box)
        delete_query="""DELETE  FROM tasks WHERE taskname=?"""
        c=conn.cursor()
        c.execute(delete_query,(edit_taskname,))
        conn.commit()
        window.FindElement('edit_work').Update("Save")
        if window.FindElement('edit_work').GetText() == 'Save':
                    edit_query="""INSERT INTO 'tasks'('completion','taskname','duedate','priority')VALUES(?,?,?,?)"""
                    c=conn.cursor()
                    c.execute(edit_query,(values['check1'],values['taskname'],values['dated'],values['drop_down']))
                    conn.commit()
                    window.FindElement('list_box').Update([])
                    for row in c.execute('SELECT *  FROM tasks '):
                             row=c.execute('SELECT * FROM tasks')
                             window['list_box'].Update(values=row)
                             window.FindElement('edit_work').Update("Edit")
                             update_UI()   



        
        
         
       




def delete_work(values):
    try:
        if values['list_box'][0]!=[]:
                   rowtask=[]
                   delete_value=values['list_box'][0]
                   delete_val=delete_value[1]
    #delete_completion=delete_value[0]
    #delete_duedate=delete_value[2]
    #delete_priority=delete_value[3]
    #print(delete_value)
    #window.FindElement('dated').Update(value=delete_completion)
    #print(delete_val)
    #print(delete_duedate)
    #print(delete_priority)
    
                   delete_query="""DELETE  FROM tasks WHERE taskname=?"""
                   c=conn.cursor()
                   c.execute(delete_query,(delete_val,))
                   conn.commit()
                   update_UI()   

    #update()
                   window.FindElement('list_box').Update([])
                   for row in c.execute('SELECT *  FROM tasks '):
                                     rowtask.append(row)
                                     window['list_box'].Update(values=rowtask)
    
    except:
        print("indentation error")
        
   









    
       
rowtask=[]                     

layout=[
    [sg.Text("Enter the task:",font=("Arial",14)),sg.InputText("",font=("Arial",14), size=(20,1),key="taskname"),
     sg.Button("open",font=("Arial",12),key="open_work")],
     [sg.Button("add",font=("Arial",12),key="add_work"),
      sg.Button("Edit",font=("Arial",12),key="edit_work"),
     sg.Button("Delete",font=("Arial",12),key="delete_work"),sg.Checkbox("completed",font=("Arial",12),size=(10,20),key="check1")],
      [sg.Text("select the priority:",font=("Arial",14)),sg.InputCombo(['very_imp','imp','later'],size=(9,0),key="drop_down"),sg.Text("deadline date:",font=("Arial",12)),sg.InputText("",font=("Arial",12),size=(9,1),key="dated")],
     [sg.Listbox(values=[],font=("Arial",14),size=(40,10),select_mode='single',change_submits=True,key="list_box")]]     
                                                                      
window=sg.Window('TO_DO_LIST',layout,finalize=True)

def open_work():
   for row in c.execute('SELECT *  FROM tasks '):                  
       rowtask.append(list(row))
       window.FindElement('list_box').Update(values=rowtask)

    
while True: 
        event,values=window.Read()
        conn.commit()
        if event is None:
           print("overrrrrrrr")
        elif event=="open_work":
             open_work()
             window.FindElement('open_work').Update("opened")
             window.FindElement('open_work').Update(disabled=True)
            
             
        elif event=="add_work":
            add_work(values)

            
        elif event=="edit_work":
            print(event,values)
            if window.FindElement('edit_work').GetText() == 'Edit':
                    edit_work(event,values)
                
        elif event=="delete_work":
            delete_work(values)

        else:
            pass


            
