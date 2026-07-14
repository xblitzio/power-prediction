This is a full-stack machine learning web application that predicts the net hourly electrical energy output of a Combined Cycle Power Plant (CCPP).

The model takes four environmental variables as input: temperature, exhaust vacuum, ambient pressure, and relative humidity, and predicts the predicted power output.

### Tech Stack
- Machine Learning: Python, Scikit-Learn, Pandas, NumPy
- Backend: Flask
- Frontend: HTML5, CSS3

### Project Structure
- model_training.py: The script used to load the CCPP dataset, train a Multiple Linear Regression model, and save it as a pickle file.
- model.pkl: The serialized, trained machine learning model.
- app.py: The Flask web server that handles routing, processes user input, and returns predictions.
- templates/index.html: The frontend user interface with built-in input validation and styling.
