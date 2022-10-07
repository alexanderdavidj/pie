# pie

pie is a tool for easy pixel color extraction made in Python

## Install

```bash
python3 -m pip install git+https://github.com/alexzerozeroone/pie
```

## Usage

- -h, --help
  
  - Print help message

- -f, --file [filename.png]
  
  - Path of the image file to process
    
    - **REQUIRED**

- -o, --out [filename.txt]
  
  - Name of the output processed file
    
    - **Default** ("pixel.txt")

- -d, --div [divider]
  
  - Pixel string divider
    
    - **Default** ("-")
  
  - Example (-)
    
    - [0, 0, 0, **"55-299"**]

- -s, --size
  
  - Include image dimensions in the processed file
    
    - **Default** (false)
  
  - Example (true)
    
    - [**[170,170]**,[0, 0, 0, "0-0"], ...]

- -c, --compress
  
  - Compress processed file by removing whitespace
    
    - **Default** (false)
  
  - Example (both)
    
    - Compressed (489 KB with 6KB 170x170 PNG)
      
      - [[0,0,0,"0-0"],[0,0,0,"0-1"],[0,0,0,"0-2"],...]
    
    - Uncompressed (602 KB with 6KB 170x170 PNG)
      
      - [[0, 0, 0, "0-0"], [0, 0, 0, "0-1"], [0, 0, 0, "0-2"], ...]

- -v, --verbose
  
  - Log details about what the code is currently doing
    
    - **Default** (false)
  
  - Example (both)
    
    - Verbose output
      
      - ```
        [ppy] Adding image dimensions to processed file
        [ppy] Creating pixels array
        [ppy] Created pixels array with 28,900 pixels
        [ppy] Creating file pixel.txt
        [ppy] Compressing processed file
        [ppy] Wrote and compressed file content
        [ppy] Processed file is ready
        [ppy] Processed file came out to 489.3 KB
        ```
    
    - Non-verbose output
      
      - ```
        
        ```

- --version
  
  - Print current program version
