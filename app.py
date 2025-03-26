from fastapi import FastAPI
from lenght import router as lenght_router
from weight import router as weight_router

app = FastAPI()

app.include_router(lenght_router)
app.include_router(weight_router)
