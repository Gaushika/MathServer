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

