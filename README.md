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
$ gunicorn servant:create_app --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornUVLoopWebWorker --workers 1
```

# Example

Request:

```bash
$ curl -X POST "http://localhost:8080/api/v1/recognize" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"text\": \"Собственник,сдам комнату 18 кв. м в трёхкомнатной квартире,метро Московская,Пулковское шоссе 13 к.1,со всеми удобствами (бытовая техника,раздельный санузел, ремонт.мебель,wi-fi),2 остановки от метро.Обращаться мужчинам,можно студентам.Стоимость 13250(всё включено)т. 89111347252 Светлана Павловна.\"}"
```

Response:

```json
{
  "words": [
    "Собственник", ",", "сдам", "комнату", "18", "кв", ".", "м", "в", "трёхкомнатной", "квартире", ",", "метро", "Московская", ",", "Пулковское", "шоссе", "13", "к", ".", "1", ",", "со", "всеми", "удобствами", "(", "бытовая", "техника", ",", "раздельный", "санузел", ",", "ремонт", ".", "мебель", ",", "wi-fi", ")", ",", "2", "остановки", "от", "метро", ".", "Обращаться", "мужчинам", ",", "можно", "студентам", ".", "Стоимость", "13250", "(", "всё", "включено", ")", "т", ".", "89111347252", "Светлана", "Павловна", "."
  ],
  "entities": [
    {
      "text": "18 кв . м",
      "type": "footage",
      "score": 1,
      "beginOffset": 4,
      "endOffset": 8
    },
    {
      "text": "трёхкомнатной квартире",
      "type": "apt_footage",
      "score": 1,
      "beginOffset": 9,
      "endOffset": 11
    },
    {
      "text": "метро Московская",
      "type": "metro",
      "score": 1,
      "beginOffset": 12,
      "endOffset": 14
    },
    {
      "text": "Пулковское шоссе 13 к . 1",
      "type": "address",
      "score": 1,
      "beginOffset": 15,
      "endOffset": 21
    },
    {
      "text": "мебель",
      "type": "feature",
      "score": 1,
      "beginOffset": 34,
      "endOffset": 35
    },
    {
      "text": "wi-fi",
      "type": "feature",
      "score": 1,
      "beginOffset": 36,
      "endOffset": 37
    },
    {
      "text": "13250",
      "type": "price",
      "score": 1,
      "beginOffset": 51,
      "endOffset": 52
    },
    {
      "text": "89111347252",
      "type": "phone",
      "score": 1,
      "beginOffset": 58,
      "endOffset": 59
    },
    {
      "text": "Светлана",
      "type": "name",
      "score": 1,
      "beginOffset": 59,
      "endOffset": 60
    }
  ]
}
```
