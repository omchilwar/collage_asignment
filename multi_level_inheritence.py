class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_info(self):
        print(f"person age:{self.age}")
        print(f"person name:{self.name}")    
class employee(person):
    def __init__(self, name, age,employee_id,salerry):
        super().__init__(name, age) 
        self.employee_id=employee_id
        self.salerry=salerry

    def employee_info(self):
        print(f"employee id : {self.employee_id}")           
        print(f"employee salerry : {self.salerry}")   

class manager(employee,person):
    def __init__(self, name, age, employee_id, salerry,dep):
        super().__init__(name, age, employee_id, salerry)
        self.dep=dep
    def manager_info(self):
        self.person_info()
        self.employee_info()
        print(f"department : {self.dep}")
    def leave_approval(self):
        print(f"{self.name} needs a leave approval")      

m1=manager("jon",34,"MIO002",100000,"CS")
m1.manager_info()
m1.leave_approval()
          