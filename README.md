# Ex.05 Design a Website for Server Side Processing
## Date:5/10/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

```
math.html

<html>
<head>
<style>
body{
    background-color:pink;
}
.formelt{
    color:black;
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
}
h1{
    color:purple;
    text-align: center;
    padding-top: 20px;
}
</style>
</head>
<body>
<div class="edge">
<div class="box">
<h1>BMI Calculation (BMI = w / h^2 )</h1>
<form method="POST">
    {% csrf_token %}
    <div class="formelt">
        weight (w): <input type="text" name="weight" value="{{w}}">(in kg)<br/>
    </div>
    <div class="formelt">
        height (h): <input type="text" name="height" value="{{h}}">(in m)<br/>
    </div>
    <div class="formelt">
    <input type="submit" value="Calculate"><br/>
    </div>
    <div class="formelt">
        BMI : <input type="text" name="BMI" value="{{BMI}}">(in kg/m^2 )<br/>
    </div>
</form>
</div>
</div>
</body>
</html>



views.py

from django.shortcuts import render

def BMIcalc(request):
    context = {}
    context['BMI'] = "0"
    context['w'] = "0"
    context['h'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        w = request.POST.get('weight', '0')
        h = request.POST.get('height', '0')

        print('weight =', w)
        print('height =', h)
        BMI = (int(w) ) / (float(h)**2)

        context['BMI'] = BMI
        context['w'] = w
        context['h'] = h

        print('BMI =', BMI)

    return render(request, 'mathapp/math.html', context)



urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BMI/', views.BMIcalc, name="BMIcalc"),
    path('', views.BMIcalc, name="BMIcalcroot"),  
]






```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (39).png>)
## HOMEPAGE:
![alt text](<Screenshot (38).png>)
## RESULT:
The program for performing server side processing is completed successfully.
