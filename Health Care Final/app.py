from flask import Flask, render_template, request, url_for, request
from predict_disease import Predict
from description_prediction import Description
from precaution_detection import Precaution
from hospitals import Hospitals
from twilio.rest import Client
import datetime
from sending_mail import send_email

app = Flask(__name__,template_folder='templates',static_folder = 'static')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# message intergation using Twilio
account_sid = "AC5ce8ed9f834ac8111cf955d00ed9fe87"
auth_token = "50d952238749f38da7da1413fff96500"

client = Client(account_sid, auth_token)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# user info
user_info = []
hosp_name = []

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# user choices while choosing symptoms
symptoms = ['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
            'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
            'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
            'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
            'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
            'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
            'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
            'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
            'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
            'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
            'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
            'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
            'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
            'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
            'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
            'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
            'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
            'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
            'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
            'yellow_crust_ooze']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

@app.errorhandler(404)
def not_found(e):
    return(render_template("404.html"))

@app.route('/')
def index():
    return render_template('index.html')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

@app.route('/register' , methods = ['GET', 'POST'])
def register():
    return render_template('register.html')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# this happens when you submit the registeration form
# and takes you to symptoms's page
@app.route('/registerd_succesfully' , methods = ['GET', 'POST'])
def disease_prediction():

    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        mobile_no = request.form['mobile']
        pincode = request.form['pincode']
        gender = request.form['gender']

        username = first_name + ' ' + last_name
        user_email = email
        user_number = mobile_no
        user_pincode = pincode
        user_gender = gender

        user_info.append(username)
        user_info.append(user_email)
        user_info.append(user_number)
        user_info.append(user_pincode)
        user_info.append(user_gender)

        #print(user_info[1])
        send_email(user_info[1])

        # go to next section: i.e. prediction page
        return render_template('disease-prediction.html', symptoms=sorted(symptoms))

    return render_template('register.html')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


@app.route('/diseases_detected' , methods = ['GET', 'POST'])
def diseases_detected():
    
    if request.method == 'POST':

        symptom1 = request.form['Symptom_1']
        symptom2 = request.form['Symptom_2']
        symptom3 = request.form['Symptom_3']
        symptom4 = request.form['Symptom_4']
        symptom5 = request.form['Symptom_5']

        if symptom3 == 'Choose':
            symptom3 = 0

        if symptom4 == 'Choose':
            symptom4 = 0

        if symptom5 == 'Choose':
            symptom5 = 0

        global predicted_disease

        predict = Predict(symptom1,symptom2, symptom3, symptom4, symptom5)
        predicted_disease = predict.symptom_predicition()
        predicted_disease = predicted_disease[0]
        #print(predicted_disease)

        

        dis = Description(f'{predicted_disease}')
        txt = dis.display()
        print(txt)

        dis2 = Precaution(f'{predicted_disease}')
        txt2 = dis2.display()
        print(txt2)
        
        return render_template('result.html', predicted_disease=predicted_disease, txt=txt, txt2=txt2)

    return render_template('disease-prediction.html', symptoms=sorted(symptoms))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


@app.route('/result' , methods = ['GET', 'POST'])
def result():
    return render_template('result.html')


@app.route('/hospital' , methods = ['GET', 'POST'])
def hospital():
    
    user_pincode = user_info[3]
    print(user_pincode)
    hos = Hospitals(user_pincode)
    available_hospitals = hos.list_hospitals()

    #print(available_hospitals)

    return render_template('hospital.html', available_hospitals=available_hospitals)

@app.route('/<hospital_name>', methods = ['GET', 'POST'])
def book_appointment(hospital_name):
    
    hosp_name.append(hospital_name)
    #hosp_name.remove('favicon.ico')
    
    if 'favicon.ico' in hosp_name:
        hosp_name.remove('favicon.ico')

    #print(hospital_name)
    print(hosp_name)

    if user_info is not None:
        username = user_info[0]
        email = user_info[1]
        number = user_info[2]

    return render_template('book-app.html', hospital_name=hospital_name, username=username, email=email, number=number)


@app.route('/thankyou')
def thankyou():
    return(render_template('thankyou.html'))

@app.route('/booking_done', methods = ['GET', 'POST'])
def booking():

    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']

        new_date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%y')
    
        #print(new_date)
        #print(time)

        body_txt = f'''\n\nHey {user_info[0]}, Welcome to MED LYFE 24/7 !!!\n\nOur system has predicted that you are most likely suffering from {predicted_disease}.\n\nYour appoinment has been booked at {hosp_name[0]}\n\nDate: {new_date}\nTiming: {time}\n\nContact Us +1234567'''

        message = client.messages.create(
                              body= body_txt,
                              from_='+17813437199',
                              to='+91'+user_info[2]
                          )
        
        print(message.sid)

        # then empty the user list
        del user_info[:]
        del hosp_name[:]

        return(render_template('thankyou.html'))

    return render_template('book-app.html')


if __name__ == "__main__" :
    app.run(debug = True)