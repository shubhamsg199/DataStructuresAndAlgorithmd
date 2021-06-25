class Doctor:
    def __init__(self,doctorid,doctorname,deptname,consultfee,sundayavailable):
        self.doctorid = doctorid
        self.doctorname = doctorname
        self.deptname = deptname
        self.consultfee = consultfee
        self.sundayavailable = sundayavailable

class Hospital:
    def __init__(self,dlist):
        self.dlist = dlist

    def getDoctorList(self,name):
        l = []

        for i in self.dlist:
            if i.deptname.lower() == name.lower() and i.sundayavailable.lower() == "available":
                l.append(i)
        if len(l) > 0:
            return l
        else:
            return None


    def selectDoctor(self,fee):
        for i in self.dlist:
            t = 0
            if i.sundayavailable.lower() == "not available" and i.consultfee > fee:
                self.dlist.remove(i)
                t = 1
            if t>0:
                return True
            else:
                return False



if __name__ == "__main__":

    l1 = []
    for i in range(5):
        id = int(input())
        name = input()
        depname = input()
        fee = int(input())
        available = input()
        l1.append(Doctor(id,name,depname,fee,available))

    O1 = Hospital(l1)
    deptname = input()
    fee = int(input())
    obj1 = O1.getDoctorList(deptname)
    if obj1 == None:
        print("Doctor Not Found")
    else:
        for i in obj1:
            print(i.doctorid,"\n",i.doctorname,sep="")

    obj2 = O1.selectDoctor(fee)
    if obj2 ==  True:
        l1.sort(key=lambda x: x.consultfee)
        for i in O1.dlist:
            print(i.doctorid,"\n",i.doctorname,"\n",i.consultfee,sep="")
    else:
        print("Returning the original list")
        for j in O1.dlist:
            print(j.doctorid,"\n",j.doctorname,sep="")















