# weasyprint
WeasyPrint Convert HTML &amp; CSS into High-Quality PDFs

Read :
- [https://weasyprint.com](https://weasyprint.com)
- [https://doc.courtbouillon.org/weasyprint/v52.5/install.html](https://doc.courtbouillon.org/weasyprint/v52.5/install.html)

```bash
cat /etc/os-release
python3 --version
pip --version
python3 -m venv venv
source venv/bin/activate

sudo sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

pip install weasyprint
pip show weasyprint

# Test
# Open Python shell: 
python3

# Run the code below
import weasyprint

from weasyprint import HTML
HTML(string="<h1>Hello PDF</h1>").write_pdf("test.pdf")

# Generate your own CV
from weasyprint import HTML
HTML(filename='./cv.html').write_pdf("myCV.pdf")

# PYTHONPATH=. /usr/bin/python3 ./weasyprint_install_verification.py

```


# Latex

packages nécessaires :
```bash
tlmgr install tikz moderncv fontawesome5 xcolor enumitem ragged2e
pdflatex cv.tex
```