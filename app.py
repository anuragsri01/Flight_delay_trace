from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/getdelay', methods=['POST'])
def get_delay():
    if request.method == 'POST':
        result = request.form

#         # Prepare the feature vector for prediction
#         pkl_file = open('cat', 'rb')
#         index_dict = pickle.load(pkl_file)
#         new_vector = np.zeros(len(index_dict))

#         try:
#             new_vector[index_dict['DayOfWeek' + str(result['DayOfWeek'])]] = 1
#         except:
#             pass
#         try:
#             new_vector[index_dict['UniqueCarrier' + str(result['UniqueCarrier'])]] = 1
#         except:
#             pass
#         try:
#             new_vector[index_dict['Origin' + str(result['Origin'])]] = 1
#         except:
#             pass
#         try:
#             new_vector[index_dict['Dest' + str(result['Dest'])]] = 1
#         except:
#             pass
#         try:
#             new_vector[index_dict['DepTime' + str(result['DepTime'])]] = 1
#         except:
#             pass

        pkl_file = open('logmodel.pkl', 'rb')
        logmodel = pickle.load(pkl_file)
        prediction = logmodel.predict(new_vector)

        return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run()
