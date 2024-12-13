# Thumbny
A social media simple thumbnails creator

# Command Examples


Help command:
```bash
thumbnails-generator --help
usage: thumbnails-generator [-h] {create,delete,generate,templates} ...

positional arguments:
  {create,delete,generate,templates}
    create              Create a new template
    delete              Delete a template
    generate            Generate a thumbnail
    templates           List all templates

options:
  -h, --help            show this help message and exit
```

Create a template:
```bash
thumbnails-generator create \
'{
    "key": "youtube",
    "name": "sample thumbnail",
    "width": 1280,
    "height": 720,
    "background-color": "#ffffff",
    "text": [
        {
            "key": "title"
            "content": "Sample",
            "position": {
                "key": "relative|fixed",
                "value": "top-center|x,y"
            },
            "alignment": "center",
            "font-color": "#333333",
            "font-size": "36",
            "font-family": "Arial"
        }
    ]
}'
```

Use a template:
```bash
thumbnails-generator generate \
'
{
  "template_key": "youtube",
  "text": [
    {
      "key": "title",
      "value": "Hello YouTube"
    }
  ]
}
'
```

To remove a template:
```bash
thumbnails-generator delete '{"name": "template-name"}'
```

To list all templates:
```bash
thumbnails-generator templates
```
