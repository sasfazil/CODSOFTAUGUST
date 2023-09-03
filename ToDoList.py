class ToDoList:
    def __init__(self):
        self.document = []
    
    def add_tasks(self,task):
        self.document.append({"task":task,"done":False})
    
    def view_tasks(self):
        if not self.document:
            print("No tasks in ToDoList")
        else:
            for index, task_info in enumerate(self.document,1):
                if task_info["done"] == True:
                    status = "Done"
                else:
                    status = "Not Done"
                print("{}. {} - {}".format(index,task_info["task"],status))
    
    def update_task(self,index):
        if len(self.document) > 0:
            
            if 0 < index <= len(self.document) and self.document[index-1]["done"] == False:
                
                self.document[index-1]["done"] = True
                print("Your Task has been Modified")
                
            elif 0 < index <= len(self.document) and self.document[index-1]["done"] == True:
                
                self.document[index-1]["done"] = False
                print("Your Task has been Modified")
                
            else :
                print("Give The proper index")
        else:
            print("No tasks are present in the To Do List to modify")
     
    
    
def main():
    to_do_list = ToDoList()
    while True:
        print("\n{}\nTo Do List: \n{}\n".format("-"*10,"-"*10))
        print("1.Add task")
        print("2.View Tasks")
        print("3.Update Tasks")
        print("4.Quit\n")
        person_input = input("Select the operations from above: ")
        
        if person_input == "1":
            person_task = input("Enter Your Task: ")
            to_do_list.add_tasks(person_task)
            print("Successfully saved your Task...")
        elif person_input == "2":
            to_do_list.view_tasks()
        elif person_input == "3":
            to_do_list.view_tasks()
            modify_tasks = int(input("Which task you want to update: "))
            to_do_list.update_task(modify_tasks)
        elif person_input == "4":
            print("Quitting from To Do List....")
            break
        else:
            print("Enter a valid input")
        
        
main()