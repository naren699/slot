from django.shortcuts import render

# Create your views here.


def home(request):
    # Time table data
    timetable = {
        "Monday": ["FREE SLOT", "BEEE", "", "STATS", "FREE SLOT"],
        "Tuesday": ["Free Slot", "OS", "Lunch", "DBMS", "FREE SLOT"],
        "Wednesday": ["FREE SLOT", "OS", "Lunch", "MENTOR MEET", "FWAD"],
        "Thursday": ["C", "STATS", "Lunch", "PHYSICS", "REASONING"],
        "Friday": ["C", "FWAD", "Lunch", "PHYSICS", "BEEE"]
    }

    subjects = [
        {"code": "19AI414", "name": "Fundamentals of Web Application Development "},
        {"code": "19EE305", "name": "Basic Electrical Electronics and Measurement Engineering"},
        {"code": "19PH814", "name": "Physics for Quantum Computing"},
        {"code": "19CS404", "name": "DataBase Management Systems and its Applications"},
        {"code": "19MA211", "name": "Statistics and Numerical Methods"},
        {"code": "19EY702", "name": "Reasoning Ability"},
        {"code": "19CS405", "name": "Operating Systems"},
        {"code": "19AI304", "name": "C programming"}
    ]

    return render(request, 'home.html', {
        'timetable': timetable,
        'subjects': subjects,
    })
