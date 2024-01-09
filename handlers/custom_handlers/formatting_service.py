from typing import Dict, List

from site_API.utils import site_api_handler

service_dict = site_api_handler._make_response()



def formatting(service_name: str, start_dict : Dict = service_dict):
    current_start_dict = start_dict[service_name]
    add_service = dict()
    format_service = dict()
    for service, cost in current_start_dict.items():
        if "+" in cost:
            add_service[service] = cost
            continue
        if "/" in cost:
            cost = cost[:cost.index("/")]
        if "-" in cost:

            cost = cost[:cost.index("-")]
        if "₽" in cost:
            cost = cost[:cost.index("₽")]
        format_service[service] = int(cost)

    format_service = dict(sorted(format_service.items(), key=lambda x: x[1]))
    return format_service, add_service, current_start_dict

