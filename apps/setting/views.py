from django.shortcuts import render
from apps.setting.models import Setting , Achievements
from apps.products.models import Products
# Create your views here.
def index(request):
    achievements = Achievements.objects.latest('id')
    setting = Setting.objects.latest('id')
    products = Products.objects.all()

    return render(request,'index.html', locals())    