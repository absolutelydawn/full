from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/uid")
async def receive_uid(request: Request):
    data = await request.json()
    uid = data.get("uid")
    print(f"Received UID: {uid}")
    return {"status": "success", "uid": uid}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
