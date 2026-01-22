import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Temporary Data Store
stats_db = {"opened": 0, "closed": 0, "history": []}

# AI Model Logic
class MLTicketSystem:
    def __init__(self):
        data = [("system crash", "Software"), ("wifi slow", "Network"), ("virus", "Security")] * 10
        self.df = pd.DataFrame(data, columns=['text', 'category'])
        self.pipeline = Pipeline([('tfidf', TfidfVectorizer()), ('clf', SVC(probability=True))])
        self.pipeline.fit(self.df['text'], self.df['category'])

    def predict(self, text):
        cat = self.pipeline.predict([text])[0]
        conf = np.max(self.pipeline.predict_proba([text])[0])
        return str(cat), round(float(conf), 2)

engine = MLTicketSystem()

@app.post("/process_ticket")
async def process_ticket(req: dict):
    text = req.get('text', '').strip()
    # Duplicate Check
    for t in stats_db["history"]:
        if t['input_text'].lower() == text.lower() and t['status'] == "Open":
            raise HTTPException(status_code=400, detail=f"Duplicate issue raised at {t['created_at']}")

    cat, conf = engine.predict(text)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket = {"id": f"TIC-{datetime.now().strftime('%M%S')}", "input_text": text, "issue_type": cat, "confidence": conf, "status": "Open", "created_at": ts}
    stats_db["opened"] += 1
    stats_db["history"].append(ticket)
    return ticket

@app.post("/close_ticket/{t_id}")
async def close_ticket(t_id: str):
    for t in stats_db["history"]:
        if t["id"] == t_id:
            t["status"] = "Closed"
            stats_db["opened"] -= 1
            stats_db["closed"] += 1
            return {"msg": "success"}
    return {"msg": "not found"}

@app.get("/get_all_stats")
async def get_all_stats():
    return stats_db

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
