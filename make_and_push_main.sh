make html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*.html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*/*.html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*/*/*.html

perl -pi -e 's/<h2>social</<h2>associates</g' output/*.html
perl -pi -e 's/<h2>social</<h2>associates</g' output/*/*.html
perl -pi -e 's/<h2>social</<h2>associates</g' output/*/*/*.html

#ghp-import output/ -p
ghp-import output/ -p -f -r https://github.com/open-science-frankfurt/open-science-frankfurt.github.io.git  -b master
