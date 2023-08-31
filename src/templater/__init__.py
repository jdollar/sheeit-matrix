from datetime import datetime
import random
from pyhtml2pdf import converter
import os
from pathlib import Path
import typer
from jinja2 import Environment, FileSystemLoader
from typing_extensions import Annotated

def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        chunk = l[i:i + n]
        # pad the array with empty strings
        # if we don't have enough
        chunk = chunk + ([''] * (n - len(chunk)))
        yield chunk

def main(
    template: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True
        )
    ],
    count: Annotated[
        int,
        typer.Option(
            min=0,
            help="Number of QR codes to generate",
        )
    ],
    code: Annotated[
        int,
        typer.Option(min=0, max=999)
    ],
    violation: Annotated[
        int,
        typer.Option(min=0, max=999)
    ],
    date: Annotated[datetime, typer.Option(formats=['%Y%m%d'])] = datetime.now(),
    cle: Annotated[int, typer.Option(min=0, max=999)] = 0,
):
    environment = Environment(loader=FileSystemLoader(template.cwd()))
    environment.globals.update(divide_chunks=divide_chunks)
    templateFile = environment.get_template(template.name)

    already_created = set()
    qr_codes = list()
    for _ in range(count):
        serial_number = ""
        while serial_number == "" or serial_number in already_created:
            rando = random.randrange(100000, 900000)
            code_str = str(code).zfill(3)
            violation_str = str(violation).zfill(3)
            cle_str = str(cle).zfill(3)
            serial_number = f"{date.strftime('%Y%m%d')}{code_str}{violation_str}{cle_str}{rando}"

        already_created.add(serial_number)

        qr_codes.append({
            'serial_number': serial_number
        })

    output_html_file = "test.html"
    with open(output_html_file, mode="w", encoding="utf-8") as html_file:
        content = templateFile.render(qr_codes=qr_codes)
        html_file.write(content)

    output_pdf_file = "test.pdf"
    converter.convert(f"file:///{os.path.abspath(output_html_file)}", output_pdf_file)

def templater():
    typer.run(main)
