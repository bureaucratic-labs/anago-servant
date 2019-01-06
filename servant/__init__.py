"""HTTP API for NER models."""
from anago import Sequence

from aiohttp import web
from aiohttp_swagger import setup_swagger
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from servant import settings
from servant.routes import index


async def swagger(app):
    """Setups online documentation for API."""
    setup_swagger(
        app=app, swagger_url='/api/docs', swagger_info=app['swagger_dict']
    )


async def setup_api_schema(app):
    """Setups API schema."""
    setup_aiohttp_apispec(
        app=app, title='Servant Documentation', version='v1', url='/api/schema'
    )


async def create_app():
    """Create aiohttp application for whole project."""
    app = web.Application()
    app['model'] = Sequence.load(
        settings.MODEL_WEIGHTS_PATH,
        settings.MODEL_PARAMS_PATH,
        settings.MODEL_PREPROCESSOR_PATH,
    )
    app.router.add_post('/api/v1/recognize', index)
    app.middlewares.append(validation_middleware)
    await setup_api_schema(app)
    app.on_startup.append(swagger)
    return app
