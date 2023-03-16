from django.shortcuts import render

# Create your views here.

def math_modul(request):
    mylist = request.POST.get('mylist')
    if not mylist:
        newlist = []
    else:
        mylist = mylist.split(' ')
        newlist = []
        for i in mylist:
            if int(i) % 2 == 0:
                newlist.append(int(i))
# -------------------------------------------------------------
    n = request.POST.get('n')
    if not n:
        fact = 0
    else:
        fact = 1
        for i in range(1, int(n) + 1):
            fact *= i
# -------------------------------------------------------------

    number1 = request.POST.get('number1')
    number2 = request.POST.get('number2')
    result = []
    if not number1 or not number2:
        result = []
    else:
        for i in range(int(number2), int(number1) + 1):
            if i % int(number2) == 0:
                result.append(i)
# -------------------------------------------------------------

    list1 = request.POST.get('list1')
    list2 = request.POST.get('list2')
    list_ = []
    if not list1 or not list2:
        list_ = []
    else:
        list1 = list1.split(' ')
        list2 = list2.split(' ')
        for i, j in zip(list1, list2):
            if int(i) > int(j):
                list_.append(int(i))
            else:
                list_.append(int(j))
# -------------------------------------------------------------
    number = request.POST.get('fib')
    if not number:
        res = 0
    else:
        n1 = 0
        n2 = 1
        if int(number) == 0:
            res = n1
        elif int(number) > 0:
            count = 0
            r = []
            while n1 != int(number):
                count += 1
                r.append(str(count))
                n1, n2 = n2, n1 + n2
                if n1 > int(number):
                    res = 'no fib'
                    return render(request, 'main/math_modul.html', context={
                'newlist':newlist,
                'fact':fact,
                'result':result,
                'list_':list_,
                'res':res
                    })
            res = ' '.join([i for i in r])
                
        else:
            res = 'no fib'

# -------------------------------------------------------------

    return render(request, 'main/math_modul.html', context={
            'newlist':newlist,
            'fact':fact,
            'result':result,
            'list_':list_,
            'res':res
        })


