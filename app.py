from fastapi import FASTAPI
from mangum import Mangum

app = FASTAPI(title="MyFlow",version= "0.1.0")

app.get("/health")
def health():
    return {"status":"ok"}



handler = Mangum(app)