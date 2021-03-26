from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from visitors.models import Visitor


def index(request):
    visitors = Visitor.objects.order_by(
        '-arrival_time'
    )
    visitor_wait = visitors.filter(
        status="AGUARDANDO"
    )
    visitor_visiting = visitors.filter(
        status="EM_VISITA"
    )
    visitor_finish = visitors.filter(
        status="FINALIZADO"
    )
    visitors_month = visitors.filter(
        arrival_time__month=timezone.now().month
    )

    context = {
        'visitors': visitors,
        'visitor_wait': visitor_wait.count(),
        'visitor_visiting': visitor_visiting.count(),
        'visitor_finish': visitor_finish.count(),
        'visitors_month': visitors_month.count(),
    }
    return render(request, 'index.html', context)