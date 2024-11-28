from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"Вы попали yf[th на страницу администратора"}

@app.get('/user/{user_id}')
async def user(user_id: str) -> dict:
    return {"Вы вошли как пользователь №": user_id}

@app.get("/user/{username}/{age}")
async def info_user(username: str, age: int) -> dict:
    return {"Информация о пользователе. Имя:": username, "Возраст:": age}
