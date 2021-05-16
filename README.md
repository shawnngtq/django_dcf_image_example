# Django Crispy Form ImageField example

I notice some issue using django-crispy-form (dcf), details of issue: <https://github.com/django-crispy-forms/django-crispy-forms/issues/1160>

Here is a basic example of dcf with Django ImageField

## Main Python Packages

- python: 3.9
- django: 3.2
- django-crispy-form: 1.11.2
- Template pack: Bootstrap4

## Python Setup

```bash
# since I am not sure which Python manager you are using, bash script is universal
# 1st activate your environment (conda / venv)
# execute this bash script that installs required python packages
./install_packages.sh

# django
./manage runserver
./manage migrate
./manage createsuperuser

# to test the problem
# go 127.0.0.1:<port>/person/create and upload > 1 images by clicking `Add more image`, you will see missing the filename
```

## Problem

I noticed that:

1. When there is multiple image inline formsets, the filenames do not appear after upload, but the files there because it will appear in database table once the form is submitted
1. ImageField's `ClearableFileInput` do not follow the layout defined

![image1](img/image1.png)

If there is only single image inline formset, filename appear just fine.

![image2](img/image2.png)

In this image, you see 2 image upload, both with `---`, but I have already uploaded 2 images, thus problem 1.

![image3](img/image3.png)

Same example as previous image, both with `---`, but when hover, you will see the filename.

If you refer to `person/forms.py`, you see that I have defined the layout, `is_primary` field should be before image field, but that is not the html generated, thus problem 2
