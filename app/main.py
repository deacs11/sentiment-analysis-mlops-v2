# app/main.py
from flask import Flask, request, jsonify, Response # <-- 1. Importa Response
from model import SentimentModel
# --- Importa le librerie di Prometheus ---
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY, CONTENT_TYPE_LATEST # <-- 2. Importa Content_Type_Latest
import time

app = Flask(__name__)
sentiment_model = SentimentModel()

# --- Definisce le metriche che si desidera tracciare ---
REQUESTS_TOTAL = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency', ['endpoint'])
PREDICTIONS_TOTAL = Counter('sentiment_predictions_total', 'Total number of sentiment predictions', ['sentiment'])

@app.route('/')
def home():
    REQUESTS_TOTAL.labels(method='GET', endpoint='/', http_status=200).inc()
    return jsonify({"message": "Sentiment Analysis API is running! Use the /predict endpoint for analysis."})

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    
    data = request.get_json(force=True)
    review_text = data.get('review')

    if not review_text:
        REQUESTS_TOTAL.labels(method='POST', endpoint='/predict', http_status=400).inc()
        return jsonify({"error": "Il campo 'review' è mancante nel JSON"}), 400

    sentiment, confidence = sentiment_model.predict_sentiment(review_text)
    PREDICTIONS_TOTAL.labels(sentiment=sentiment).inc()

    response = {
        "sentiment": sentiment,
        "confidence": confidence
    }
    
    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint='/predict').observe(latency)
    
    REQUESTS_TOTAL.labels(method='POST', endpoint='/predict', http_status=200).inc()
    return jsonify(response)

@app.route('/metrics')
def metrics():
    # Uso Response per impostare il Content-Type corretto che Prometheus si aspetta
    return Response(generate_latest(REGISTRY), content_type=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)