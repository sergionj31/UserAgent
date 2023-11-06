from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse

# Create your views here.

def indexer(request):
    return render(request, 'index.html')

def infoView(request):
    user_agent = get_user_agent(request)
    return render(request, 'info.html', {'user_agent':user_agent})

def visiter(request):
    user_agent = get_user_agent(request)
    ip_client = request.META.get('REMOTE_ADDR')
    host_name = request.META.get('HTTP_HOST')

    if user_agent.is_mobile:
        info = f'Está usando un dispositivo móvil. Su host es {host_name} y su IP es {ip_client}' 
        if user_agent.is_touch_capable:
            info += ' .Su dispositivo es táctil.'
        else:
            info += ' .Su dispositivo no es táctil.'
    elif user_agent.is_tablet:
        info = f'Está usando una tableta. Su host es {host_name} y su IP es {ip_client}' 
        if user_agent.is_touch_capable:
            info += ' .Su dispositivo es táctil.'
        else:
            info += ' .Su dispositivo no es táctil.'
    elif user_agent.is_pc:
        info = f'Está usando un PC. Su host es {host_name} y su IP es {ip_client}' 
        if user_agent.is_touch_capable:
            info += ' .Su dispositivo es táctil.'
        else:
            info += ' .Su dispositivo no es táctil.'
    elif request.user_agent.is_bot:
        info = f'Está usando un bot. Su host es {host_name} y su IP es {ip_client}' 
        if user_agent.is_touch_capable:
            info += ' .Su dispositivo es táctil.'
        else:
            info += ' .Su dispositivo no es táctil.'

    return render(request, 'visit.html', {'info': info})