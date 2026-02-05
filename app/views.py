from django.shortcuts import render

# Create your views here.
def calculator(request):
    result=''
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operater = request.POST.get('operater')
            if operater == '+':
                result = num1 + num2
            elif operater == '-':
                result = num1 - num2
            elif operater == '*':   
                result = num1 * num2
            elif operater == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Error: Division by zero'
        except:
                result = 'Error: Invalid input'
    return render(request, 'calculator.html', {'result': result})   
