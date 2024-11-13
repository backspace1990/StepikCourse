from fastapi import FastAPI
import uvicorn


app = FastAPI(title="FastAPI Stepik Courses")



#@app.get("/")
#async def root():
#    return {"message": "Beni bitir"}
@app.get("/get_hotels")
def get_hotels():
    return "5 Yildizli Antalya oteli"



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)