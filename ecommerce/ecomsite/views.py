from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from .forms import StudentForm
from django.conf import settings
 
# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
collection = db["finals"]  # Collection name
 
def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Get form data
            student_data = {
                "name": form.cleaned_data["name"],
                "age": form.cleaned_data["age"],
                "department": form.cleaned_data["department"],
            }
            # Insert into MongoDB
            collection.insert_one(student_data)
            return HttpResponse("✅ Student data saved successfully!")
    else:
        form = StudentForm()
 
    return render(request, "ecomsite/form.html", {"form": form})