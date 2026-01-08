from fastapi import FastAPI

app = FastAPI(title="ShubhSay API")

@app.get("/")
def root():
    return {"message": "ShubhSay backend is running 🚀"}
