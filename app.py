from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/greet")
def greet():
    return {"Message":"Hello mr toast man"}




# Mangum adapts FastAPI (an ASGI app) to the event/response shape
# AWS Lambda expects. This is the only Lambda-specific line in the app.
handler = Mangum(app)