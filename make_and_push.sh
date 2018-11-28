make html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*.html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*/*.html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*/*/*.html

perl -pi -e 's/<h2>social</<h2>associates</g' output/*.html
perl -pi -e 's/<h2>social</<h2>associates</g' output/*/*.html
perl -pi -e 's/<h2>social</<h2>associates</g' output/*/*/*.html

ghp-import output/ -p

