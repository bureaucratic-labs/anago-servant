"""Module where views are defined."""
from typing import List

from razdel import tokenize as tokenize_

from aiohttp import web
from aiohttp_apispec import docs, use_kwargs, marshal_with

from servant.schema import RequestSchema, ResponseSchema


def tokenize(text) -> List[str]:
    """Tokenize (split on words) given text."""
    return [
        token for _, _, token in tokenize_(text)
    ]


@docs(tags=['Named entity recognition'], description='Endpoint, that does entity recognition.')
@use_kwargs(RequestSchema(strict=True))
@marshal_with(ResponseSchema(), 200)
async def index(request):
    """Endpoint, that does entity recognition."""
    text = request['data']['text']
    model = request.app['model']
    if text:
        result = model.analyze(text, tokenizer=tokenize)
    else:
        result = {}
    return web.json_response(result)
