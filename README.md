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

## Issues
Collisions happen frequently because the minimum time resolution for metadata is seconds. Two images take within the same second will receieve the same filename (collision). The original filename is hashed and added to the image name but that doesn't help when the original filenames are the same.

### Solutions
* unique IDs may be possible from `exif` library to prevent collisions, or;
* if collision, hash the full file and compare, if they are the same then ignore

## Future Development
* Getting the camera 'Model' from the metadata of images is ideal for adding to the image filename. However, the easiest way to do this is with `PIL` (see [this](https://faun.pub/making-an-image-metadata-extractor-in-python-40d54f9e9f40) guide) but external dependencies are not ideal.
