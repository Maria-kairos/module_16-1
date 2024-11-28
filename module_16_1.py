from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def user(user_id: str):
    return {'message': f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def info_user() -> dict:
    return {'message': "Информация о пользователе. Имя: <username>, Возраст: <age>"}
