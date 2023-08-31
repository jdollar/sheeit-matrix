# Sheeit Matrix

## Pre-requisites
* Need to have chrome installed

## Downloading

You may not need to build this binary yourself. Refer to the github release page
to see if a version for your operating system is available for use: https://github.com/jdollar/html-pdf-templater/releases

Just extract the binary from the release and run it directly in the command line `./templater`

## Running

To see what you can provide the application you can reference the `--help` command:
```bash
Usage: templater [OPTIONS]

Options:
  --template FILE                 Path to the template file to use to generate
                                  the QR codes. Must be a jinja2 template
                                  file.  [required]
  --count INTEGER RANGE           Number of QR codes to generate  [x>=0;
                                  required]
  --code INTEGER RANGE            [0<=x<=999; required]
  --violation INTEGER RANGE       [0<=x<=999; required]
  --date [%Y%m%d]                 [default: 2023-08-30 23:48:29.243064]
  --cle INTEGER RANGE             [default: 0; 0<=x<=999]
  --qr-codes-per-page INTEGER RANGE
                                  The number of qr codes to stick on a page.
                                  Note, this number can shrink or grow
                                  depending on the size of each individual
                                  block housing the qr code in the template.
                                  [default: 9; x>=0]
  --html-output FILE              Path to the output html file. Primarily used
                                  for debugging.  [default:
                                  dist/2023-08-30-23-48-29.html]
  --pdf-output FILE               Path to the output pdf file.  [default:
                                  dist/2023-08-30-23-48-29.pdf]
  --assets-directory DIRECTORY    Path to any assets you want to include in
                                  the template.  [default: assets]
  --help                          Show this message and exit.
```

An example usage of the binary would be something akin to this:
```bash
templater --template ./default.html.j2 --count=5 --code 223 --violation 888
```

## Development

Running for development:
```bash
# Download all the necessary dependencies
pip install -r requirements.txt

# Run the templater
python src/templater.py
```

Any changes you make to the python file will immediately be reflected:
```bash
python src/templater.py --help
python src/templater.py --template=default.html.j2 --count=2 --code=22 --violation=333
```


## Building a binary for distribution

For building a binary that is a single file other people can run you can utilize pyinstaller
```bash
pip install -r requirements.txt
pip install --upgrade pyinstaller
pyinstaller src/templater.py --onefile
```

This will generate a binary in the `dist/` directory with the name `templater` that you can share and run.
With this, you should note, it may be beneficial to pass the template "default.html.j2" along with the binary


