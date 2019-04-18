git checkout -b temp

make html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*.html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*/*.html
perl -pi -e 's/<h2>blogroll</<h2>links</g' output/*/*/*.html

perl -pi -e 's/<h2>social</<h2>associates</g' output/*.html
perl -pi -e 's/<h2>social</<h2>associates</g' output/*/*.html
perl -pi -e 's/<h2>social</<h2>associates</g' output/*/*/*.html

ghp-import output/ -p -f -r https://github.com/open-science-frankfurt/open-science-frankfurt.github.io.git  -b master
git rm -f __pycache__/pelicanconf.cpython-36.pyc

git checkout master
git branch -D temp

git fetch origin
git reset --hard origin/master
