The NBA_stats contains code (Python and R), dataset and documentations
for the SEIS785 course project "Stories behind the NBA Stats".

The project is for exploring what are the key factors that make a team
a NBA Championship by analyzing and visualizing NBA stats from 1980 to 2009
and building models to predicate 2013 NBA Championship.

You can find details in both:
https://github.com/imsure/NBA_Stats/blob/master/project_presentation_seis785.pdf
and
https://github.com/imsure/NBA_Stats/blob/master/project-report.pdf

Before running, make sure that you have a unix-like shell, Python and R installed correctly.

To run:

execute the following command in sequence in a unix shell
(if you are a Window user, using Cygwin instead.)

chmod 755 run.sh

./run.sh

After the shell program is done, you will see a database file generated under db directory
and graphs generated under graphs directory.

To clean up the generated files:

chmod 755 cleanup.sh
./cleanup.sh
