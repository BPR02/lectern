# Lectern snapshot

## Resource pack

- `@resource_pack pack.mcmeta`

  <details>

  ```json
  {
    "pack": {
      "pack_format": 6,
      "description": ""
    }
  }
  ```

  </details>

### minecraft

- `@resource_pack assets/minecraft/sounds.json`

  <details>

  ```json
  {
    "block.note_block.bit_1": {
      "sounds": [
        "block/note_block/bit_1"
      ],
      "subtitle": "subtitles.block.note_block.note"
    }
  }
  ```

  </details>

- [`@sound minecraft:block/note_block/bit_1`](data:audio/ogg;base64,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AJABAMAYg5BBBiFjEEIIIYQQQggJAAAYcAAACDChDBQashIASAUAAAxSijEHpaQUKcWYcxBKSSlSijHnIJSSUsWYcxBKSam1ijHnIJSSUmudcxBKSam1GDvnIJSSUmsxhhBKSam1GGMMIZSSUmsx1lpKSam1GGvMtZSSUmsx1lprSq21GGutNeeUWmsx1lpzzgUAIDQ4AIAd2LA6wknRWGChISsBgDwAAEgpxhhjjDGlFGOMMcaYUooxxhhjjDHGGGOMMaYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHmGGOMMcYYY8w5xhhjjDnmHGOMMcacc04AAFCBAwBAgI0imxOMBBUashIACAcAAIxhzDnnIJSQSqOUcxBCKCWVVhqlnIMSQikptZY5JyWlUlJqLbbMOSkplZJSay12ElJqLaXWYqyxg5BSa6m1FmONHYRSWootxhpz7SCUklprMcZaayilpdhirLHWmkMpqbUWY60151xSai3GWmvNteeSUmsxxlprrbmn1mKssdZcc+89tRZjjbXmnHvOBQCYPDgAQCXYOMNK0lnhaHChISsBgNwAAEYpxpxzDkIIIYQQQgiVUow55xyEEEIIIYQQKqUYc845CCGEEEIIIWSMOeccdBBCCCGEEELIGHPOOQghhBBCCCGE0DnnHIQQQgghhFBCKaVzzjkHIYQQQgghhFBK5xyEEEIIIYQSSiillM45CCGEEEIIpYRSSikhhBBCCCGEEkoppZRSOgghhBBCCKWUUkoppYQQQgghhBBKKaWUUkoJIYQQQgghlFJKKaWUEkIIIYQSSimllFJKKSWEEEIIoZRSSimllFJKCCGEUkoppZRSSimllBBCKCGUUkoppZRSSikhhBJKKKWUUkoppZRSQggllFJKKaWUUkoppYQQQiillFJKKaWUUkoJIZRSSimllFJKKaWUUgAA0IEDAECAEZUWYqcZVx6BIwoZJqBCQ1YCAOEAAAAhlFJKKaWUUmokpZRSSimllFIjJaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSimllFJKKaWUUkoppZRSSqWUUkoppZRSSimllFJKKaWUUkoppQCoywwHwOgJG2dYSTorHA0uNGQl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)