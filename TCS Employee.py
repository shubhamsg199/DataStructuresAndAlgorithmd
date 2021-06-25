class Employee:
    def __init__(self, name, id, age, gender):
        self.ename = name
        self.eid = id
        self.eage = age
        self.egender = gender


class Organisation():
    def __init__(self,oname, elist):
        self.oname = oname
        self.elist = elist

    def addEmployee(self,name,id,age,gender):
        e = Employee(name,id,age,gender)
        self.elist.append(e)

    def getEmployeeCount(self):
        return len(self.elist)

    def findEmployeeAge(self,id):
        age = -1
        for e in self.elist:
            if e.eid == id:
                age = e.age
                break
        return age

    def countEmployees(self,age):
        count = 0
        for e in self.elist:
            if e.age > age:
                count +=1
        return count


if __name__ == '__main__':
    elist=[]
    o = Organisation('XYZ',elist)
    n=int(input())
    for i in range(n):
        ename=input()
        eid=int(input())
        eage=int(input())
        egender=input()
        o.addEmployee(ename,eid,eage,egender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))