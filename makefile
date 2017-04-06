FILES :=								\
	.travis.yml							\
	apiary.apib							\
	IDB2.log							\
	models.html							\
	app/models.py 						\
	app/tests.py 						\
	UML.pdf

check:
	@not_found=0;                                 \
	for i in $(FILES);                            \
	do                                            \
		if [ -e $$i ];                            \
		then                                      \
			echo "$$i found";                     \
		else                                      \
			echo "$$i NOT FOUND";                 \
			not_found=`expr "$$not_found" + "1"`; \
		fi                                        \
	done;                                         \
	if [ $$not_found -ne 0 ];                     \
	then                                          \
		echo "$$not_found failures";              \
		exit 1;                                   \
	fi;                                           \
	echo "success";

clean-venv:
	rm -rf app/venv/

start-server:
#	python3.5 ./app/make_config.py
	bash start_server.sh

html:
	python3.5 -m pydoc -w app/models.py

log:
	git log > IDB2.log

unittest:
	# Make the config file
	python3.5 app/make_config.py && mv config.py app/
	coverage-3.5 run    --branch app/tests.py >  tests.tmp 2>&1
	coverage-3.5 report -m                      >> tests.tmp
	cat tests.tmp
	python3.5 app/tests.py
#
# test: html check
test: unittest html log check
