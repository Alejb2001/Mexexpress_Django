from django.shortcuts import render
from django.http import HttpResponse
from shopApp.models import Product, Contact

# Views de index.html
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        "user": "guest",
        "message": "Hola",
        "special_offers": special_offers,
        "product_list": product_list,
        "special_offers_2": [
            {
                "name": "Mascarilla hidratante de Sávila",
                "cost": 14.00,
                "img": "shopApp/img/img_mascarilla.jpg",
            },
            {
                "name": "Consola de videojuegos portátil XE150",
                "cost": 450.00,
                "img": "shopApp/img/img_consola2.jpg",
            },
            {
                "name": "Reloj de pulsera gótico de Snoopy",
                "cost": 160.00,
                "img": "shopApp/img/img_reloj_snoopy.jpg",
            },
            {
                "name": "Camisa para caballero de algodón",
                "cost": 200.00,
                "img": "shopApp/img/img_camisa_caballero_algodon.jpg",
            },
            {
                "name": "Peluche de Batman tamaño real",
                "cost": 2000.00,
                "img": "shopApp/img/img_peluche_batman.jpg",
            },
            {
                "name": "Flauta peruana de cerámica",
                "cost": 250.00,
                "img": "shopApp/img/img_flauta_peruana.jpg",
            },
            {
                "name": "Miniatura de 40k",
                "cost": 100.00,
                "img": "shopApp/img/img_miniatura_40k.jpg",
            }
        ]
    }
    return render(request, "shopApp/index.html", context=my_context)

# Views de about.html
def about(request):
    contact_list = Contact.objects.filter(active=True) 
    return render(request, "shopApp/about.html", {'contact_list': contact_list})