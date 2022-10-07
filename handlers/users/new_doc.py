from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from data.config import RES_PATH
from keyboards.default import sex_kb, course_kb, type_kb, level_kb, base_kb, program_kb, no_kb
from keyboards.checking import answers
from loader import dp
from states import new_user

from backend.docx_editor import add_to_docx
from backend.variable_checker import vars_from_dict



@dp.message_handler(Command('new_doc'), state='*')
async def start_new_doc(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Пожалуйста, отправьте своё имя в <b>дательном падеже</b>\n\n'
                         '<i><b>Например:</b></i>\n'
                         '👉🏻 <i><b>Кому?</b> Краснову Илье Владимировичу</i>\n'
                         '👉🏻 <i><b>Кому?</b> Небелой Марии Игоревне</i>', reply_markup=no_kb)

    await new_user.name.set()


@dp.message_handler(state=new_user.name)
async def get_sex(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer('Выберите свой <b>пол</b> с помощью кнопок ниже:', reply_markup=sex_kb)
    await new_user.sex.set()


@dp.message_handler(state=new_user.sex)
async def get_course(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in answers.sex_keyboard:
        await message.answer('<i>Пожалуйста, воспользуйся специальными кнопками 🥺</i>', reply_markup=sex_kb)
        return
    await state.update_data(sex=answer)
    await message.answer('Выберите свой <b>курс</b> также с помощью кнопок ниже:', reply_markup=course_kb)
    await new_user.course.set()


@dp.message_handler(state=new_user.course)
async def get_type(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in answers.course_keyboard:
        await message.answer('<i>Пожалуйста, воспользуйся специальными кнопками 🥺</i>', reply_markup=course_kb)
        return
    await state.update_data(course=answer)
    await message.answer('Выберите свою <b>форму обучения</b> с помощью специальных кнопок:', reply_markup=type_kb)
    await new_user.type.set()


@dp.message_handler(state=new_user.type)
async def get_level(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in answers.type_keyboard:
        await message.answer('<i>Пожалуйста, воспользуйся специальными кнопками 🥺</i>', reply_markup=type_kb)
        return
    await state.update_data(type=answer)
    await message.answer('Выберите <b>уровень получаемого образования</b> с помощью кнопок:', reply_markup=level_kb)
    await new_user.level.set()


# new handler (program)

@dp.message_handler(state=new_user.level)
async def get_program(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in answers.level_keyboard:
        await message.answer('<i>Пожалуйста, воспользуйся специальными кнопками 🥺</i>', reply_markup=level_kb)
        return
    await state.update_data(level=answer)
    await message.answer('Пожалуйста, укажите <b>название программы</b> с помощью специальных кнопок:', reply_markup=program_kb)
    await new_user.program.set()

# the end of the new handler


@dp.message_handler(state=new_user.program)
async def get_base(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in answers.program_keyboard:
        await message.answer('<i>Пожалуйста, воспользуйся специальными кнопками 🥺</i>', reply_markup=program_kb)
        return
    await state.update_data(program=answer)
    await message.answer('Выберите <b>основу обучения</b> с помощью специальных кнопок:', reply_markup=base_kb)
    await new_user.base.set()


@dp.message_handler(state=new_user.base)
async def get_year(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in answers.base_keyboard:
        await message.answer('<i>Пожалуйста, воспользуйся специальными кнопками 🥺</i>', reply_markup=base_kb)
        return
    await state.update_data(base=answer)
    await message.answer('В каком году вы <b>поступили в Университет</b>?\n\n'
                         '<i>Важно! Год должен быть только <b>в виде числа</b></i>\n\n'
                         '<i><b>Например:</b></i>\n'
                         '👉🏻 <i>2020</i>\n'
                         '👉🏻 <i>2019</i>', reply_markup=no_kb)
    await new_user.year.set()

# new handler

@dp.message_handler(state=new_user.year)
async def get_birth(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(year=answer)
    await message.answer('Когда вы <b>родились</b>?\n\n'
                         '<i>Важно! Дата должна быть только <b>в виде ДАТА.МЕСЯЦ.ГОД</b></i>\n\n'
                         '<i><b>Например:</b></i>\n'
                         '👉🏻 <i>01.01.1995</i>\n'
                         '👉🏻 <i>12.05.2000</i>', reply_markup=no_kb)
    await new_user.birth.set()

# end of the handler



@dp.message_handler(state=new_user.birth)
async def finish(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(birth=answer)

    data = await state.get_data()

    await message.answer('Одну минуточку... 🤔')

    student_vars = vars_from_dict(data)
    add_to_docx(*student_vars)

    await message.answer('Справка готова! ✨\n\n'
                         '❗️ Пожалуйста, отправьте её своему инспектору за подписью!')
    await message.answer_document(open(f'{RES_PATH}', 'rb'))

    await state.finish()

    await message.answer('<i>Оформить справку ещё раз:</i> <b>/new_doc</b>')
