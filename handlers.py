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

router = Router()



@router.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer(f'привет {msg.from_user.full_name}', reply_markup=kb.menu_reply)


@router.message(F.text.lower() == "меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
    
@router.message(F.text.lower() == "какой то текст")
async def menu(msg: Message):
    await msg.answer('какой то ответ')
    
    
@router.callback_query(F.data == "generate_text") #ввод с клавы
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.text_prompt)
    await clbck.message.edit_text(text.gen_text)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_kb)


@router.message(Gen.text_prompt)
async def generate_text(msg: Message, state: FSMContext):
    prompt = msg.text
    mesg = await msg.answer(text.gen_wait)
    res = await utils.return_text(prompt)
    if not res:
        return await mesg.edit_text(text.gen_error, reply_markup=kb.iexit_kb)
    await mesg.edit_text(res[0] + text.text_watermark, disable_web_page_preview=True)


@router.message()
async def cmd_start(msg: types.Message):
    await msg.answer('press start', reply_markup=kb.start)