from django.shortcuts import redirect, render
import requests
import pickle
from sklearn.preprocessing import LabelEncoder
import numpy as np

def homepage(request):
    return render(request,"homepage.html")
        
def secondpage(request):
    model_name = pickle.load(open('jobprediction.pkl', 'rb'))
    qualification = request.GET['qualification']
    designation = request.GET['designation']
    exp = int(request.GET['exp'])
    tech1 = request.GET['tech1']
    tech2 = request.GET['tech2']
    print(qualification, designation,tech1,tech2)
            
    qualification = LabelEncoder().fit_transform([qualification])
    designation = LabelEncoder().fit_transform([designation])
    tech1 = LabelEncoder().fit_transform([tech1])
    tech2 = LabelEncoder().fit_transform([tech2])
                
    input_data = (qualification[0],designation[0],exp,tech1[0],tech2[0])
    array = np.asarray(input_data)
    data_reshaped = array.reshape(1,-1)
    prediction = model_name.predict(data_reshaped)
    print(prediction)
    if prediction[0]==0:
        answer="You are not eligible for this job"
        return render(request,"homepage.html",{"answer":answer})
    if prediction[0]==1:
        answer="Share you resume here. We'll contact you soon!"
                
    
    # if prediction[0]==0:
    #     print("You are not eligible for this job")
    # if prediction[0]==1:
    #     print("You are eligible for this job. Please share your resume on next page!")
    # listt = []
	# listt.append(float(request.GET['Nitrogen']))
	# listt.append(float(request.GET['Phosphorous']))
	# listt.append(float(request.GET['Pottasium']))
	# listt.append(float(request.GET['Temperature']))
	# listt.append(float(request.GET['Humidity']))
	# listt.append(float(request.GET['Ph']))
	# listt.append(float(request.GET['Rainfall']))
        return render(request,"secondpage.html",{"answer":answer})


# Create your views here.
