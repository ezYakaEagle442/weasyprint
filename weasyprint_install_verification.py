#!/usr/bin/python3

# PYTHONPATH=. /usr/bin/python3 ./weasyprint_install_verification.py

import weasyprint

from weasyprint import HTML
HTML(string="<h1>Hello PDF</h1>").write_pdf("test.pdf")