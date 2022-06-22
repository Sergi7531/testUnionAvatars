from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def return_asInfo_With_AS_Number(request, as_number):
    
    from asAPI.models import ASInformation
    
    import json
    
    json_return_info = {}
    
    return JsonResponse(list(ASInformation.objects.filter(as_number=as_number).values()), safe=False)


def return_asInfo_With_IP(request, ip_address1, ip_address2, ip_address3, ip_address4):
    
    from asAPI.models import ASInformation
        
    json_return_info = {}
    
    ip_address = str(ip_address1) + "." + str(ip_address2) + "." + str(ip_address3) + "." + str(ip_address4)
    
    for info in list(ASInformation.objects.all()):        
        # Split range_start and range_end into 4 parts (separated by '.'):
        
        range_start_parts = info.range_start.split('.')
        range_end_parts = info.range_end.split('.')
        
        # Split ip_address into 4 parts (separated by '.'):
        
        ip_address_parts = ip_address.split('.')
        
        # Check if ip_address is in range_start and range_end:
        
        leave = False
        
        for i in range(4):
            if int(range_start_parts[i]) > int(ip_address_parts[i]):
                leave = True
                break
            
            if int(range_end_parts[i]) < int(ip_address_parts[i]):
                leave = True
                break
            
        import json
        
        if not leave:
            json_return_info = ASInformation.objects.filter(id=info.id).values()
            break
        
    return JsonResponse(list(json_return_info), safe=False)