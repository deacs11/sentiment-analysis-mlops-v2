# app/model.py
import pickle
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentModel:
    def __init__(self, model_path="sentimentanalysismodel.pkl"):
        script_dir = os.path.dirname(__file__)
        abs_model_path = os.path.join(script_dir, model_path)
        
        try:
            with open(abs_model_path, 'rb') as f:
                self.model = pickle.load(f)
            logging.info(f"Modello caricato con successo da {abs_model_path}")
        except Exception as e:
            logging.error(f"ERRORE CRITICO DURANTE IL CARICAMENTO DEL MODELLO: {e}")
            self.model = None


    def predict_sentiment(self, text):
        if self.model is None:
            logging.warning("Tentativo di predizione fallito: il modello non è caricato.")
            return "error", 0.0

        try:
            # Il modello si aspetta una lista e restituisce una lista, quindi prendo il primo elemento.
            prediction = self.model.predict([text])
            sentiment = prediction[0]
            
            logging.info(f"Output del modello per '{text[:30]}...': [{sentiment}]")

            # Non ho più bisogno di mappatura. Uso l'output diretto.
            # Aggiungo una confidenza fittizia come richiesto dal formato della risposta.
            confidence = 0.98 
            
            return sentiment, confidence

        except Exception as e:
            logging.error(f"ERRORE DURANTE LA PREDIZIONE per il testo '{text[:30]}...': {e}")
            return "error", 0.0