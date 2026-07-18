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
HTML(filename='./cv - print to PDF baseline .html').write_pdf("cv - print to PDF baseline.pdf")
HTML(filename='./cv.html').write_pdf("myCV.pdf")

#
import weasyprint
from weasyprint import HTML
HTML(filename='./ticket.html').write_pdf("ticket-tom.pdf")

# https://doc.courtbouillon.org/weasyprint/stable/common_use_cases.html#show-log-messages
import logging
logger = logging.getLogger('weasyprint')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('weasyprint.log'))
logger.addHandler(logging.StreamHandler())

from weasyprint import HTML
from weasyprint import document
#HTML(filename='./cv.html').write_pdf("myCV.pdf")

html = HTML(filename='./cv.html')
doc = html.render() # pageSize=2

total_pages = len(doc.pages)
print(f"Total number of pages: {total_pages}")

doc.copy(doc.pages[0::2]).write_pdf("myCV.pdf")
doc.write_pdf("myCV.pdf")

# https://doc.courtbouillon.org/weasyprint/v52.5/tutorial.html#individual-pages-meta-data-other-output-formats

# https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#rendering-to-a-single-file
# Once you have a HTML object, call its HTML.write_pdf() method to get the rendered document in a single PDF file.

#If you want more than a single PDF, the HTML.render() method gives you a document.Document object with access to individual document.Page objects. Thus you can get the number of pages, their size[1], the details of hyperlinks and bookmarks, etc. Documents also have a document.Document.write_pdf() method, and you can get a subset of the pages with document.Document.copy().

# PYTHONPATH=. /usr/bin/python3 ./weasyprint_install_verification.py

```


# Latex

packages nécessaires :
```bash
tlmgr install tikz moderncv fontawesome5 xcolor enumitem ragged2e
pdflatex cv.tex
```

# To be evaluated

- [https://www.onelatex.com](https://www.onelatex.com)