from django.shortcuts import render, redirect
from django.views import View
from app1.models import Ombor, Client, Product
from .models import Stats

class StatsView(View):
    def get(self, request):
        stats = Stats.objects.all()
        o = Ombor.objects.get(user=request.user)
        clients = Client.objects.filter(ombor=o)
        products = Product.objects.filter(ombor=o)
        return render(request, 'stats.html', {"all_stats":stats, "products":products, "clients":clients})
    def post(self, request):
        m = request.POST['miqdor']
        n = request.POST['nasiya']
        p = request.POST["product"]
        c = request.POST["client"]
        Stats.objects.create(
            product=Product.objects.get(id=p),
            client=Client.objects.get(id=c),
            sanasi=request.POST['sana'],
            miqdor=m,
            umumiy_summa=request.POST['summa'],
            nasiya=n,
            tolandi=request.POST['tolandi'],
            ombor=Ombor.objects.get(user=request.user)
        )
        pro = Product.objects.get(id=p)
        pro.miqdor = int(pro.miqdor) - int(m)
        pro.save()
        cl = Client.objects.get(id=c)
        cl.qarz = int(cl.qarz) + int(n)
        cl.save()
        return redirect("stats")

class StatsUpdate(View):
    def get(self, request, pk):
        return render(request, 'stats_update.html')


