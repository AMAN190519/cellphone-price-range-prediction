from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form inputs (ensure keys match your index.html)
        features = [
            int(request.form['battery_power']),
            int(request.form['blue']),
            float(request.form['clock_speed']),
            int(request.form['dual_sim']),
            int(request.form['fc']),
            int(request.form['four_g']),
            int(request.form['int_memory']),
            float(request.form['m_dep']),
            int(request.form['mobile_wt']),
            int(request.form['n_cores']),
            int(request.form['pc']),
            int(request.form['px_height']),
            int(request.form['px_width']),
            int(request.form['ram']),
            int(request.form['sc_h']),
            int(request.form['sc_w']),
            int(request.form['talk_time']),
            int(request.form['three_g']),
            int(request.form['touch_screen']),
            int(request.form['wifi'])
        ]

        # Convert to NumPy array and scale
        input_array = np.array([features])
        scaled_input = scaler.transform(input_array)  # apply trained scaler

        # Make prediction
        prediction = model.predict(scaled_input)[0]

        return render_template('index.html', prediction_text=f"Predicted Price Range: {prediction}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error during prediction: {e}")

if __name__ == "__main__":
    app.run(debug=True)
