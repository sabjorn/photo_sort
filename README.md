# Photo Sort
## About
A simple tool for normalizing the organization of photos through a date based hierarchy.

The date created metadata of a photo is used to define a folder structure:

```
YY
- MM
-- DD
```

The name of the file will be:

```
YY-MM-DD-HH.MM.SS.MS.<filetype>
```

**NOTE**: this script creates symlinks and does not modify the original files

## Future Development
Getting the camera 'Model' from the metadata of images is ideal for adding to the image filename. However, the easiest way to do this is with `PIL` (see [this](https://faun.pub/making-an-image-metadata-extractor-in-python-40d54f9e9f40) guide) but external dependencies are not ideal.

