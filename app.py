from fastapi import FastAPI

app = FastAPI(title="Dockerized Backend Service")

@app.get("/")
def home():
    return {
        "message": "Backend service is running successfully!",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI Backend"
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Rahul",
        "department": "Computer Science"
    }

@app.get("/calculate/{price}/{quantity}")
def calculate_total(price: float, quantity: int):
    return {
        "price": price,
        "quantity": quantity,
        "total": price * quantity
    }