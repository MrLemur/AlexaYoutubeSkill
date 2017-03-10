# AlexaYoutubeSkill
Simple Alexa skill to return first result of YouTube search query and play on a smart TV.

## Prerequisites
* flask framework
* flask-ask
* Google API Key
* HTTPS enabled server (I do a reverse proxy from my VPS to my Rapsberry Py)
* Device on the same network as the smart TV

## Invocation name
youtube

## Intent setup
```json
{
  "intents": [
    {
      "intent": "PlayYoutube",
      "slots": [
        {
          "name": "Query",
          "type": "QUERY"
        }
      ]
    }
]
}
```

## Custom Slot Type setup
Name: **Query**

Values:
```
bread
none left
small big red
red black blue ticket
```

## Utterances
```
PlayYoutube {Query}
PlayYoutube to play {Query}
PlayYoutube to find {Query}
```

