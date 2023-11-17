
class Stud():
    happy = 10
    def __init__(self, name):
        self.name = name
        self.happy = Stud.happy
        self.progress = 10

st1 = Stud('Nik')
st2 = Stud('Kat')


print()
print(st1.name, st2.name)
