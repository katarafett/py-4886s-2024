# Multifile Programs

The VEX Python VSCode extension doesn't support multifile projects. To use
multifile projects anyway, I've created a script that will dump all the text
from a set of files into one titled `main.py`.

To use:  
1. List all the source files _in order_, from top to bottom, in `all-files.text`
2. List all the standard libraries to include in `/include/imports.py`
3. Make the script `python-concat.sh` executable with `chmod +x`
4. Run the script `python-concat.sh`

Important Notes:  
- Any user-defined modules must be imported with:
```py
from module_name import *
```

- Standard libraries must much the format in `/include/imports.py`. e.g. if
`import vex` is used in `imports.py`, `import vex` should also be used in
`main.py`.

# Other Stuff

For the most part, this is basic boilerplate code that every VRC team should 
have. The interesting stuff is in `/src/pid.py` and `/src/movement.py`. They 
have the PID class and functions for consistent, fast driver-control functions.
