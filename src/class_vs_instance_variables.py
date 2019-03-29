class BestCourse:
    website = "http://test.com"

    def __init__(self, name):
        self.name = name

course = BestCourse("Learn Python")
learn_command_line = BestCourse("Learn Command Line")

print(course.name)
print(BestCourse.website)

print(learn_command_line.name)  #Object
print(BestCourse.website)       #Class
