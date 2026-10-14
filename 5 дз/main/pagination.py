from rest_framework import PAgeNumberPagination
class ZonePagination(PAgeNumberPagination):
    page_size=4
    page_size_query_param='size'

    max_page_size=50
    page_query_param='page'