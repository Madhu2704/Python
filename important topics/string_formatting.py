

from icecream import ic

ic.configureOutput(includeContext=True)


def stringFormatType1(name: str, age: int, gpa: float) -> str:
    return 'Hello %s your age is %d with GPA : %0.1f' % (name, age, gpa)


def stringFormatType2(name: str, age: int, gpa: float) -> tuple:
    case1 = 'Hello {0} your age is {1} with GPA : {2:0.1f}'.format(
        name, age, gpa)
    case2 = 'Hello {candidate_name} your age is {candidate_age} with GPA : {candidate_gpa:0.1f}'.format(
        candidate_name=name, candidate_age=age, candidate_gpa=gpa)
    return (case1, case2)


def stringFormatType3(name: str, age: int, gpa: float) -> tuple:
    case1 = f'Hello {name} your age is {age} with GPA : {gpa:0.1f}'
    case2 = f'Hello {name} your age is {age} with GPA : {gpa:{0}.{3}}'
    case3 = f'Hello {name} your actual age is {(lambda no:no*3)(age)}'
    return (case1, case2, case3)


if __name__ == '__main__':
    name, age, gpa = "Madhu", 24, 4.0

    # String Format Type 1 usiing %
    ic(stringFormatType1(name, age, gpa))
    # String Format Type 2 using .format()
    ic(stringFormatType2(name, age, gpa))
    # String Format Type 3 using f string literal
    ic(stringFormatType3(name, age, gpa))
