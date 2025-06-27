from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    text_prompt = State()
    img_prompt = State()
    
class Register(StatesGroup):
    name = State()
    age = State()
    number = State()
    passs = State()