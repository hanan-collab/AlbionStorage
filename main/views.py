from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'accountID': 'RigenMengaji',
        'balance' : '15000000',
        'item' : 'Cursed Staff',
        'description': 'The Adept\'s Great Cursed Staff is a Tier 4 Cursed Staff which may be obtained by crafting or via the Market Place',
        'itemPower' : '800',
        'tier' : '4',
        'amount' : '1',
        'place' : 'Lymhurst Bank',
        'price' : '2000'


    }

    return render(request, "main.html", context)
