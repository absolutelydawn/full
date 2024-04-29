from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/')
async def health_check():
    return "OK"

@app.get('/getcsv')
async def getcsv():
    csv_file = 'data.csv'

    df = pd.read_csv(csv_file)
    dict_data = df.to_dict()

    return dict_data