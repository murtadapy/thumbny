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
--name template-name \
--size 1280x720 \
--background-color #FFFFFF \
--color #000000 \
--font-family /path/to/font.ttf
```
* Only name is required

Use a template:
```bash
thumbnails-generator generate \ 
--template-name template-name \
--title title on the thumbnail \
--output /path/to/output/folder
```
* Only template-name and title are required

To remove a template:
```bash
thumbnails-generator delete --name template-name
```

To list all templates:
```bash
thumbnails-generator templates
```
