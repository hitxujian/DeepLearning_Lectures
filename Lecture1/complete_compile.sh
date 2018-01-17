# complete compile the files
# Lecture number is given as the argument
# Compile all the modules separately

if [[ "$2" == "nonstopmode" ]]; then
	pdflatex -interaction=nonstopmode -halt-on-error Lecture$1.tex
else
	pdflatex Lecture$1.tex
fi

if [[ $? == 1 ]]; then
	echo "Compilation is giving an error "
	return 1
fi

if [[ "$3" == "ref" ]]
then
	bibtex Lecture$1.aux
	pdflatex -interaction=nonstopmode Lecture$1.tex
	pdflatex -interaction=nonstopmode Lecture$1.tex
fi 

if [[ $? == 1 ]]; then
	echo "Could not link the references"
	return 1
fi

if [[ "$4" == "all-modules" ]]; then
	for i in $(ls modules)
	do
		cat modules/packages.tex modules/$i > modules/temp.tex
		echo  "\end{document}"  >> modules/temp.tex
		pdflatex -interaction=nonstopmode modules/temp.tex
		mv modules/temp.pdf modules/$i.pdf
fi


echo "Deleting the generated logs"
find . -name "*.nav" -type f -delete
find . -name "*.log" -type f -delete
find . -name "*.snm" -type f -delete
find . -name "*.aux" -type f -delete
find . -name "*.toc" -type f -delete
find . -name "*.out" -type f -delete
find . -name "*.bbl" -type f -delete
find . -name "*.blg" -type f -delete
