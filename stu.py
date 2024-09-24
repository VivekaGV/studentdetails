class student:
    def __init__(self, name, reg, m1, m2, m3):
        self.name = name
        self.reg = reg
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        a = int((m1 + m2 + m3) / 3)
        avgm[reg] = a

    def rank(self):
        print("Student's Average Marks and Ranks")
        i = 0
        rank = 1
        temp = ()
        while i < n:
            print()
            keymax = max(zip(avgm.values(), avgm.keys()))
            print("Rank=", rank, end=" ")
            print("(Average marks and USN)=", keymax)
            a = keymax[1]
            del avgm[a]
            rank += 1
            i += 1


n = int(input("Enter number of students:"))
stud = {}
avgm = {}
m = []

for a in range(n):
    if a==0:
      name = input("Enter Student Name:")
    else:
        name = input("Enter Next Student Name:")
    reg = input("Enter a Student USN:")
    m1 = int(input("Enter marks1:"))
    m2 = int(input("Enter marks2:"))
    m3 = int(input("Enter marks3:"))
    st = student(name, reg, m1, m2, m3)
    stud[reg] = st
    st.avg()
st.rank()
