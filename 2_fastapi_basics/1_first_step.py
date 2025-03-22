from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

# Run dev server with "fastapi dev <filename>"
# Run production server with "fastapi run <filename>" 