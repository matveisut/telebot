from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from aiogram import flags
from aiogram.fsm.context import FSMContext
import utils
from states import Gen
from aiogram.types.callback_query import CallbackQuery  # Вот этого.
import kb
import text
from states import Register

router = Router()



@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer(f'привет {msg.from_user.full_name}', reply_markup=kb.menu_reply)


@router.message(F.text.lower() == "какой то текст")
async def menu(msg: Message):
    await msg.answer('какой то ответ')


@router.message(F.text.lower() == "клавиатура")
async def menu(msg: Message):
    await msg.answer('клаиватура', reply_markup=kb.menu)
    

@router.callback_query(F.data == "callback_q") #ввод с клавы
async def q_window(callback: CallbackQuery, state: FSMContext):
    
    
    await callback.answer('вы выбрали окошко_q')
    await callback.message.answer('окошко_q')
    await state.set_state(Gen.text_prompt)
    


@router.message(Command("register"))
async def register(msg: Message, state: FSMContext):
    await state.set_state(Register.name)
    await msg.answer('введи имя', reply_markup=types.ReplyKeyboardRemove())

@router.message(Register.name)
async def register(msg: Message, state: FSMContext):
    
    await state.update_data(name = msg.text)
    await state.set_state(Register.age)
    await msg.answer('возраст')
    
@router.message(Register.age)
async def register(msg: Message, state: FSMContext):
    
    await state.update_data(age = msg.text)
    await state.set_state(Register.number)
    await msg.answer('введи номер',reply_markup = kb.get_number)


@router.message(Register.number, F.contact)
async def register(msg: Message, state: FSMContext):

    await state.update_data(number = msg.contact.phone_number)
    data = await state.get_data()
    await msg.answer(f"имя :{data['name']}, возраст: {data['age']}, номер: {data['number']}", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
    
@router.message()
async def start_handler(msg: types.Message):
    await msg.answer(f'нажми старт', reply_markup=kb.start)

@router.message(Command("я сосу яйца"))
async def start_handler(msg: types.Message):
    await msg.answer(f'привет, соси яйца')