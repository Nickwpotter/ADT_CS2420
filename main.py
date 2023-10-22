from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.value.grade() * course.value.credit_hr()
        credits += course.value.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, len(lyst)  - 1):
        if lyst[i].value > lyst[i + 1].value:
            return False
    return True

def main():
    slist = SList()
    slist.insert(value= Course(number=2))
    slist.insert(value=Course(number=3))
    slist.insert(value=Course())
    slist.insert(value=Course())
    slist.insert(value=Course())
    
    gpa = calculate_gpa(slist)
    print(gpa)

    sorted = is_sorted(slist)
    print(sorted)


if __name__ == "__main__":
    main()