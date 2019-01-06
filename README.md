# Servant

![HTTP API for NER models](https://i.imgur.com/JJchpFe.png)

HTTP API for NER models (actually, HTTP interface for [anago](https://github.com/Hironsan/anago))


# Configuration

```bash
$ export MODEL_PARAMS_PATH=/path/to/params.h5
$ export MODEL_PREPROCESSOR_PATH=/path/to/preprocessor.pickle
$ export MODEL_WEIGHTS_PATH=/path/to/weights.h5
```

# Start

```bash
$ gunicorn servant:create_app --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornUVLoopWebWorker --reload --workers 1
```
