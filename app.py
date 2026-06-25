from flask import Flask, request , url_for , render_template
import joblib
model = joblib.load(r'C:\Users\user\OneDrive\Desktop\Data Science\Student-Performance-Predictor\model\student_model.lb')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/history')
def history():
    return render_template('history.html')
@app.route('/project',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age	 = request.form['age']
        gender = request.form['gender']
        school_type	 = request.form['school_type']
        parent_education	 = request.form['parent_education']
        study_hours	 = request.form['study_hours']
        attendance_percentage	 = request.form['attendance_percentage']
        internet_access	 = request.form['internet_access']
        travel_time	 = request.form['travel_time']
        extra_activities	 = request.form['extra_activities']
        study_method	 = request.form['study_method']

        gender_dict = {'Male':0,'Female':1,'Others':2}
        gender = gender_dict.get(gender)

        school_dict = {'Public':0, 'Private':1}
        school_type = school_dict.get(school_type)

        parent_dict = {'Post Graduate':0, 'Graduate':1, 'High School':2, 'No Formal':3, 'Diploma':4, 'Phd':5}
        parent_education = parent_dict.get(parent_education)

        internet_dict = {'Yes':0,'No':1}
        internet_access = internet_dict.get(internet_access)

        travel_dict = {'Less than 15 min':0, 'Greater than 60 min':1, '15-30 min':2, '30-60 min':3}
        travel_time = travel_dict.get(travel_time)

        extra_activity_dict = {'Yes':0,'No':1}
        extra_activities = extra_activity_dict.get(extra_activities)

        study_method_dict = {'Notes':0, 'Textbook':1, 'Group Study':2, 'Coaching':3, 'Mixed':4, 'Online Videos':5}
        study_method = study_method_dict.get(study_method)

        pred = model.predict([[age,gender,school_type	,parent_education,study_hours	,attendance_percentage,internet_access	,travel_time,extra_activities,study_method]])
        print('prediction :->>>',age,gender,school_type	,parent_education,study_hours	,attendance_percentage,internet_access	,travel_time,extra_activities,study_method)
        final = round(pred[0])
    return render_template('project.html',prediction = final)

if __name__ == '__main__':
    app.run(debug=True)