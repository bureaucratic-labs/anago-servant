"""Configuration variables required to run."""
import os
import typing
import sentry_sdk

MODEL_PARAMS_PATH: str = os.environ['MODEL_PARAMS_PATH']
MODEL_PREPROCESSOR_PATH: str = os.environ['MODEL_PREPROCESSOR_PATH']
MODEL_WEIGHTS_PATH: str = os.environ['MODEL_WEIGHTS_PATH']
SENTRY_DSN: typing.Optional[str] = os.environ.get('SENTRY_DSN')

sentry_sdk.init(SENTRY_DSN)
