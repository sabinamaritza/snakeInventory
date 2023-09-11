from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Corn Snake',
        'price': 1000000,
        'amount': 7,
        'description': 'Corn Snake\nMorph: Anery\nSex: Male'
    }

    return render(request, "main.html", context)