<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Get latest sources:](#get-latest-sources)
- [Change version in version.py](#change-version-in-versionpy)
- [Update ChangeLog:](#update-changelog)
- [Update NEWS from ChangeLog. Then:](#update-news-from-changelog-then)
- [Make sure pyenv is running and check newer versions](#make-sure-pyenv-is-running-and-check-newer-versions)
- [Switch to python-2.4, sync that up and build that first since it creates a tarball which we don't want.](#switch-to-python-24-sync-that-up-and-build-that-first-since-it-creates-a-tarball-which-we-dont-want)
- [Update NEWS from master branch](#update-news-from-master-branch)
- [Check against all versions](#check-against-all-versions)
- [Make packages and tag](#make-packages-and-tag)
- [Upload single package and look at Rst Formating](#upload-single-package-and-look-at-rst-formating)
- [Upload rest of versions](#upload-rest-of-versions)
- [Push tags:](#push-tags)
- [Check on a VM](#check-on-a-vm)

<!-- markdown-toc end -->

# Get latest sources:

    git pull

# Change version in VERSION.py

    $ emacs loctraceback/version.py
    $ source loctraceback/version.py
    $ echo $__version__
    $ git commit -m"Get ready for release $__version__" .


# Update ChangeLog:

    $ make ChangeLog

#  Update NEWS from ChangeLog. Then:

    $ emacs NEWS
    $ make check
    $ git commit --amend .
    $ git push   # get CI testing going early
    $ make check

# Make sure pyenv is running and check newer versions

    $ pyenv local && source admin-tools/check-versions.sh

# Update NEWS from master branch

    $ git commit -m"Get ready for release $VERSION" .

# Make packages and tag

    $ . ./admin-tools/make-dist.sh
    $ git tag release-${__version__}

# Upload single package and look at Rst Formating

    $ twine upload dist/loctraceback-${__version__}-py3.3.egg

# Upload rest of versions

    $ twine upload dist/loctraceback-${__version__}*

# Push tags:

    $ git push --tags

# Check on a VM

    $ cd /virtual/vagrant/virtual/vagrant/ubuntu-zesty
	$ vagrant up
	$ vagrant ssh
	$ pyenv local 3.5.2
	$ pip install --upgrade loctraceback
	$ exit
	$ vagrant halt
