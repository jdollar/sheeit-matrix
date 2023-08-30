Need to have chrome installed

Running for development:
```bash
pip install --upgrade build
pip install --editable .
python -c "import templater"
```

You then should be able to run the following command:
```bash
templater --help
templater --template=test.html.j2 --count=2
```

Any changes you make to the source files will then be reflected when rerunning the commands above

