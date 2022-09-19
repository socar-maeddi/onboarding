from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

cars_db = [
    {"car_id": 1, "car_name": "a", "car_num": 111, "createdat": datetime.now()},
    {"car_id": 2, "car_name": "b", "car_num": 222, "createdat": datetime.now()},
    {"car_id": 3, "car_name": "c", "car_num": 333, "createdat": datetime.now()},
    {"car_id": 4, "car_name": "d", "car_num": 444, "createdat": datetime.now()}
    
]

@app.get("/")
def root():
    text = """
    과제 1: FastAPI를 활용하여 간단한 App 띄우기
    """
    return text

@app.get("/cars")
def get_car() -> list:
    return cars_db

@app.get("/cars/{car_id}")
def get_car_info(car_id: int) -> dict:
    for car_info in cars_db:
        if car_info["car_id"] == car_id:
            return car_info
    
    return {"message": "no data"}


@app.post("/cars")
def add_car(car_id: int, car_name: str, car_num: int):
    new_info = {"car_id": car_id, "car_name": car_name, "car_num": car_num, "createdat": datetime.now()}
    try:
        cars_db.append(new_info)
        return True
    except:
        return False

