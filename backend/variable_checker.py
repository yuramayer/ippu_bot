
def vars_from_dict(d):
    name = d.get('name', '[ФИО]')
    sex = d.get('sex', '[ПОЛ]')
    course = d.get('course', '[КУРС]')
    student_type = d.get('type', '[ФОРМА_ОБУЧЕНИЯ]')
    level = d.get('level', '[УРОВЕНЬ_ОБРАЗОВАНИЯ]')
    base = d.get('base', '[ОСНОВА_ОБУЧЕНИЯ]')
    year = d.get('year', '[ГОД]')
    birth = d.get('birth', '[ДАТА_РОЖДЕНИЯ]')
    program = d.get('program', '[НАЗВАНИЕ_ПРОГРАММЫ]')

    return name, sex, course, student_type, level, base, year, birth, program


