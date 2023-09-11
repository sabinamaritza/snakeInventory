from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Corn Snake',
        'price': 20000,
        'amount': 7,
        'description': 'snakey'
    }

    return render(request, "main.html", context)