from collections import namedtuple

Answers = namedtuple('Answers', ['sex_keyboard', 'course_keyboard',
                                 'type_keyboard', 'level_keyboard',
                                 'base_keyboard', 'program_keyboard'])

answers = Answers(['Мужской', 'Женский'], ['1', '2', '3', '4', '5'],
                  ['Очная', 'Заочная', 'Очно-заочная'], ['Бакалавриат', 'Магистратура', 'Специалитет'],
                  ['Бюджет', 'Коммерция'], ['Обеспечение безопасности', 'Гос. и мун. управление', 'Юриспруденция'])
