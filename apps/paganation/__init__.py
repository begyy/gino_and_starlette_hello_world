import math
from my_app import settings
from starlette.responses import Response
import json
import typing


class PaginationResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any, request=None) -> bytes:
        # TODO ADD VALIDATE NUMBER
        return json.dumps(
            dict(
                next=self.get_next_url(request),
                previous=self.get_previous_url(request),
                results=content
            ),
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")

    def get_count(self):  # TODO ADD COUNT
        pass

    def get_next_url(self, request):
        page_size = int(request.query_params.get('page_size', settings.PAGE_SIZE))
        page = int(request.query_params.get('page', 1))
        main_url = 'localhost:8000/users/'
        return f"{main_url}?page_size={page_size}&page={page + 1}"

    def get_previous_url(self, request):
        return ""


class Page(object):

    def __init__(self, items, page, page_size, total):
        self.items = items
        self.previous_page = None
        self.next_page = None
        self.has_previous = page > 1
        if self.has_previous:
            self.previous_page = page - 1
        previous_items = (page - 1) * page_size
        # self.has_next = previous_items + len(items) < total
        # if self.has_next:
        #     self.next_page = page + 1
        self.total = total
        # self.pages = int(math.ceil(total / float(page_size)))


def paginate(query, request):
    page_size = int(request.query_params.get('page_size', settings.PAGE_SIZE))
    page = int(request.query_params.get('page', 1))
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if page_size <= 0:
        raise AttributeError('page_size needs to be >= 1')
    return query.limit(page_size).offset((page - 1) * page_size)


#     # We remove the ordering of the query since it doesn't matter for getting a count and
#     # might have performance implications as discussed on this Flask-SqlAlchemy issue
#     # https://github.com/mitsuhiko/flask-sqlalchemy/issues/100
#     total = query.order_by(None).count()
#     return Page(items, page, page_size, total)


def queryset_paginate(query, request):
    page_size = request.query_params.get('page_size', settings.PAGE_SIZE)
    page = request.query_params.get('page', 1)
    page = int(page)
    if page <= 0:
        page = 1
    queryset = query.limit(page_size).offset((page - 1) * page_size)
    return queryset
