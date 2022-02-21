import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist

# Comment added according to instructions

app = FastAPI(title="Predicting Wine Class with batching")

# Open classifier in global scope
# Change in comment
<<<<<<< HEAD
# Change is made as a comment
with open("models/wine.pkl", "rb") as file:
=======
with open("models/wine-95-fixed.pkl", "rb") as file:
>>>>>>> 128c44d746747739fda76b855295aba9acb3c2b2
    clf = pickle.load(file)


class Wine(BaseModel):
    batches: List[conlist(item_type=float, min_items=13, max_items=13)]


@app.post("/predict")
def predict(wine: Wine):
    batches = wine.batches
    np_batches = np.array(batches)
    pred = clf.predict(np_batches).tolist()
    return {"Prediction": pred}
