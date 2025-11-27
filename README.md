# MPO-to-SBS3D
A script for converting (sub)directories with stereo 3D .MPO files to side-by-side .JPGs suited for cross-eye 3d viewing.
Made with the Nintendo 3DS in mind but probably also works on other sources. If an .MPO from another source gives an inverted or not working 3d effect, first try swapping the left and right image in the code.

This script maintains the original file structure in the result directory and copies the exif data from the original files. 
This is an example if when run from the N3DS SD card:
```bash
└── SD
    ├── MPO-SBS3D.py
    └── DCIM
       ├── 101NIN03
       │   ├── HNI_0001.MPO
       │   ├── HNI_0001.JPG (not side-by-side)
       │   ├── HNI_0002.MPO
       │   ├── HNI_0002.JPG (not side-by-side)
       │   └── ...
       └── 102NIN03
           ├── HNI_0001.MPO
           ├── HNI_0001.JPG (not side-by-side)
           └── ...
```
Running the script gives 
```bash
└── SD
    ├── MPO-SBS3D.py
    ├── DCIM
    │    └── ...
    └── DCIM-SBS
       ├── 101NIN03
       │   ├── HNI_0001.JPG (side-by-side 3d)
       │   ├── HNI_0002.JPG (side-by-side 3d)
       │   └── ...
       └── 102NIN03
           ├── HNI_0001.JPG (side-by-side 3d)
           └── ...
```

Valid command line arguments are:
```bash
-s <source_dir>          default: ./DCIM
-d <destination_dir>     default: ./DCIM-SBS
```


A few examples of what a resulting file could look like. To see the 3D effect, cross your eyes and try to make the two sides overlap.
![Young deer with its head through a fence](examples/HNI_0004.JPG)
![Small frog statues in a stack of cups](examples/HNI_0078.JPG)
![View of a japanese shrine](examples/HNI_0081.JPG)
