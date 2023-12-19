from flask import Flask, render_template,url_for, request,send_from_directory  # Added 'request' import
import pickle

app = Flask(__name__)

# Open the file and load the model
with open('C:/Users/prashanth/OneDrive/Desktop/vamshimp/Training Files/svm.pkl', 'rb') as file:
    model = pickle.load(file)

    
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == "POST":
        
        pr_rating = request.form['pr_rating']
        cl_rating = request.form['cl_rating']
        total_score = int(request.form['pr_score']) + int(request.form['cl_score'])
        # Define your model and load it here
        # model = load_model()  # You should load your trained model here

        if (pr_rating == '2' or cl_rating == '2') and total_score >= 70:
            prediction = 'F'

        elif (pr_rating == '3' and cl_rating == '3') and 70 <= total_score <= 72:
            prediction = 'PF'

        elif (pr_rating == 'S' and cl_rating == 'S') and 29 <= total_score <= 36:
            prediction = 'PF'

        elif (pr_rating == '6' and cl_rating == '6'):
            prediction = 'NF'

        elif (pr_rating == '5' and cl_rating == '5') and 29 <= total_score <= 36:
            prediction = 'NF'

        elif total_score > 72:
            prediction = 'Some_Result'  # Define what to do when the total score is greater than 72.

        elif total_score < 29:
            prediction = 'NF'

        elif 29 <= total_score <= 72:
            X = [[int(pr_rating), int(cl_rating), int(request.form['pr_score']), int(request.form['cl_score'])],
            prediction == model.predict(X)[0]]

        else:
            prediction = 'Unknown'

        return render_template('result.html', prediction=prediction, total_score=total_score)
    else:
        return render_template('predict.html')

# @app.route('/result')
# def result():
#     # You can pass any necessary data to the result.html template here
#     prediction = "Your Prediction"
#     total_score = 100
#     return render_template('result.html', prediction=prediction, total_score=total_score)

if __name__ == '__main__':
    app.run(debug=True)
