all:
	make check-py35
	make notebooks-html
	make notebooks-pdf

docker-all:
	make docker-build
	make docker-check-py35
	make docker-html
	make docker-pdf
	make docker-nbval

jb-html:
	jupyter-book build .

jb-latex:
	jupyter-book build . --builder pdflatex

notebooks-pdf: *-*.ipynb static/latex_template.tplx
	@echo "Attempting to create combined.pdf from notebooks"
	python3 -m bookbook.latex --pdf --template static/latex_template.tplx
	@mkdir -p pdf
	mv -v combined.pdf pdf/Introducao-Python-para-Ciencias-Computacionais-Engenharia.pdf
	make version && mv -v version.txt pdf

notebooks-html: check-py35
	@echo "Attempting to create html version (in ./html)"
	python3 -m bookbook.html
	@echo "Output stored in html/*html; start with html/index.html"
	make version && mv -v version.txt html

check-py35:
	@echo "Checking Python version is >= 3.5"
	@python3 -c "import sys; assert sys.version_info[0] >= 3"
	@python3 -c "import sys; assert sys.version_info[1] >= 5"
	@echo "        (ok)"

version:
	echo "Last compiled: `date`" > version.txt
	echo " " >> version.txt
	echo "Last commit:" >> version.txt
	git log HEAD -1	 >> version.txt

nbval:
	py.test -v --nbval --sanitize-with static/nbval_sanitize.cfg *.ipynb

clean:
	rm -rf *.aux *.out *.log combined_files hello.txt hello.py pylabimshow* myplot* myfile* data.mat test.txt vectools.py module1.py pylabhistogram.pdf


# To use Docker container for building and testing

# build docker image locally, needs to be done first
docker-build:
	cd tools/docker && docker build -t python4compscience .

# build pdf and html through container
docker-html:
	docker run -v `pwd`:/io python4compscience make notebooks-html

docker-pdf:
	docker run -v `pwd`:/io python4compscience make notebooks-pdf

docker-nbval:
	docker run -v `pwd`:/io python4compscience make nbval

docker-check-py35:
	docker run -v `pwd`:/io python4compscience make check-py35
