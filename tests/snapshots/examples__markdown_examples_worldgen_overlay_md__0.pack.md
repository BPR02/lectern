# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 48,
    "description": ""
  },
  "overlays": {
    "entries": [
      {
        "formats": {
          "min_inclusive": 48,
          "max_inclusive": 48
        },
        "directory": "overlay_48"
      }
    ]
  }
}
```

### demo

`@dimension demo:demo`

```json
{
  "type": "demo:in-the-base-pack",
  "generator": {
    "type": "minecraft:debug"
  }
}
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@dimension demo:demo`

```json
{
  "type": "demo:in-the-overlay-pack",
  "generator": {
    "type": "minecraft:debug"
  }
}
```

`@endoverlay`
