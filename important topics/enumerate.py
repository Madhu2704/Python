

from icecream import ic

ic.configureOutput(includeContext=True)

SPORTS_PERSONS = ['Virat Kohli', 'Dhoni',
                  'Ronaldo', 'Messi', 'Smith', 'kane Williamson']


def forLoopOfEnum(ENUM_OF_SPORTS_PERSON) -> object:
    for obj in ENUM_OF_SPORTS_PERSON:
        print(obj)
    return ENUM_OF_SPORTS_PERSON


def trimingEnum() -> object:
    # 2nd Aurgument in enumerate function gives us the extra edge
    # to start the index from 3 instead of 0
    ENUM_OF_SPORTS_PERSON = enumerate(SPORTS_PERSONS, 3)
    for index, value in ENUM_OF_SPORTS_PERSON:
        print(index, value)
    return ENUM_OF_SPORTS_PERSON


if __name__ == '__main__':
    # creating enumerate obj
    ENUM_OF_SPORTS_PERSON = enumerate(SPORTS_PERSONS)
    print(f'Type of ENUM:{type(ENUM_OF_SPORTS_PERSON)}')
    print(ENUM_OF_SPORTS_PERSON)
    ic(forLoopOfEnum(ENUM_OF_SPORTS_PERSON))
    ic(trimingEnum())
