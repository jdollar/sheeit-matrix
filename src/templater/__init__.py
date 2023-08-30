from datetime import datetime
import random
from pyhtml2pdf import converter
import os
from pathlib import Path
from typing import Optional
import typer
from jinja2 import Environment, FileSystemLoader
from typing_extensions import Annotated

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
    count: Annotated[int, typer.Option(min=0)],
    code: Annotated[int, typer.Option(min=0, max=999)],
    violation: Annotated[int, typer.Option(min=0, max=999)],
    date: Annotated[datetime, typer.Option(formats=['%Y%m%d'])] = datetime.now(),
    cle: Annotated[int, typer.Option(min=0, max=999)] = 0,
):
    environment = Environment(loader=FileSystemLoader(template.cwd()))

    template = environment.get_template(template.name)

    already_created = set()
    qr_codes = list()
    for _ in range(count):
        serial_number = ""
        while serial_number == "" or serial_number in already_created:
            rando = random.randrange(100000, 900000)
            serial_number = f"{date.strftime('%Y%m%d')}{code}{violation}{cle}{rando}"

        already_created.add(serial_number)

        qr_codes.append({
            'serial_number': serial_number
        })

    output_html_file = "test.html"
    with open(output_html_file, mode="w", encoding="utf-8") as html_file:
        content = template.render(qr_codes=qr_codes)
        html_file.write(content)
        print(f"Wrote { output_html_file }")

    output_pdf_file = "test.pdf"
    converter.convert(f"file:///{os.path.abspath(output_html_file)}", output_pdf_file)

def templater():
    typer.run(main)
