
class StudentData():
    def __init__(self, name, english, math) -> None:
        self.name = name,
        self.english = english
        self.math = math
    
    def show_means(self):
        mean = (self.english + self.math) / 2
        print(mean)

if __name__ == '__main__':
    s1 = StudentData("Suzuki", 60, 60)
    s1.show_means()
    