from django.http import HttpRequest

HEADER_LINKS_LIST = [
    {"name": "Головна", "url_name": "main:index"},
    {"name": "Всі колекції", "url_name": "products:list"},
    {"name": "Твій дизайн", "url_name": "products:custom-design"},
]


def header_links(request: HttpRequest) -> dict[str, list[dict[str, str]]]:
    return {"header_links": HEADER_LINKS_LIST}
