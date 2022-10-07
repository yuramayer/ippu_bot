from docx import Document
from docx.shared import Pt
import os.path
from data.config import DOC_PATH, RES_PATH


def add_to_docx(name, sex, course, form_type, level, base, year, birth, program):

    document = Document(f'{DOC_PATH}')

    if sex == 'Мужской':
        sex_1 = 'он'
        sex_2 = 'обучающимся'
        sex_3 = 'Зачислен'
    elif sex == 'Женский':
        sex_1 = 'она'
        sex_2 = 'обучающейся'
        sex_3 = 'Зачислена'

    if form_type == 'Очная':
        form_type_1 = 'очной'
    elif form_type == 'Заочная':
        form_type_1 = 'заочной'
    elif form_type == 'Очно-заочная':
        form_type_1 = 'очно-заочной'

    if level == 'Магистратура':
        level_1 = 'магистратуры'
        level_2 = '40.04.01'
        specialization = 'направлению подготовки'
    elif level == 'Бакалавриат':
        level_1 = 'бакалавриата'
        level_2 = '40.03.01'
        specialization = 'направлению подготовки'
    elif level == 'Специалитет':
        level_1 = 'специалитета'
        level_2 = '40.05.01'
        specialization = 'специальности'

    if base == 'Бюджет':
        base_1 = 'бюджетной'
    elif base == 'Коммерция':
        base_1 = 'платной'

    first_par = f"Выдана {name}, {birth} года рождения, в том, " \
                f"что {sex_1} является {sex_2} {course} курса {form_type_1} формы обучения " \
                "Института публичного права и управления ФГБОУ ВО " \
                "«Московский государственный юридический университет имени О.Е. Кутафина " \
                "(МГЮА)» и обучается по основной профессиональной образовательной программе " \
                f"высшего образования – программе {level_1} по {specialization} {level_2} {program}."

    sec_par = f'Обучается на {base_1} основе.'

    third_par = f'Начало обучения с 01 сентября {year} года.'

    fourth_par = f'{sex_3} приказом от _______________ года № ____.'

    fifth_par = 'Предполагаемый срок окончания обучения ___________________.'

    for p in document.paragraphs:
        if 'FIRST_PAR' in p.text:
            p.text = first_par
        elif 'SEC_PAR' in p.text:
            p.text = sec_par
        elif 'THIRD_PAR' in p.text:
            p.text = third_par
            p.style = document.styles['Normal']
        elif 'FOURTH_PAR' in p.text:
            p.text = fourth_par
        elif 'FIFTH_PAR' in p.text:
            p.text = fifth_par


    document.save(f'{RES_PATH}')

