#!/usr/bin/env python
# coding: utf-8

import os
import click
import uuid
import subprocess

BASE_DIR = os.getcwd()
TMP_DIR = '/tmp'


@click.group()
def cli():
    pass


@cli.command()
@click.argument('project')
def init(project):
    tmp_venv = os.path.join(TMP_DIR, uuid.uuid1().hex)
    tmp_pip = os.path.join(tmp_venv, 'bin/pip')
    tmp_django_admin = os.path.join(tmp_venv, 'bin/django-admin.py')

    project_dir = os.path.join(BASE_DIR, project)
    project_source_dir = os.path.join(project_dir, project)
    project_venv = os.path.join(project_dir, '.venv')
    project_pip = os.path.join(project_venv, 'bin/pip')

    starter_tpl_dir = os.path.join(TMP_DIR, uuid.uuid1().hex)
    dev_requirements = os.path.join(starter_tpl_dir, 'requirements/dev.txt')
    tpl_requirements = os.path.join(starter_tpl_dir, 'requirements')
    tpl_source = os.path.join(starter_tpl_dir, 'source')
    tpl_gitignore = os.path.join(starter_tpl_dir, 'gitignore.example')
    drf_settings = os.path.join(starter_tpl_dir, 'drf_settings.py')

    project_gitignore = os.path.join(project_dir, '.gitignore')
    project_current_settings = os.path.join(project_source_dir, 'settings.py')
    project_settings_dir = os.path.join(project_source_dir, 'settings')
    project_settings = os.path.join(project_settings_dir, 'settings.py')

    # clone django starter kit template
    subprocess.call(['git', 'clone', 'https://github.com/runforever/django-starter-template.git', starter_tpl_dir])

    # create virtualenv
    subprocess.call(['virtualenv', tmp_venv])
    subprocess.call([tmp_pip, 'install', 'Django==1.10.4', '-i', 'https://pypi.mirrors.ustc.edu.cn/simple'])

    # create django project
    subprocess.call([tmp_django_admin, 'startproject', project])
    subprocess.call(['virtualenv', project_venv])
    subprocess.call([project_pip, 'install', '-r', dev_requirements, '-i', 'https://pypi.mirrors.ustc.edu.cn/simple'])

    # copy requiremnts to project
    subprocess.call(['cp', '-r', tpl_requirements, project])

    # copy source to project
    subprocess.call('cp -r {src}/* {dest}'.format(src=tpl_source, dest=project_source_dir), shell=True)

    # copy gitignore to project
    subprocess.call(['cp', tpl_gitignore, project_gitignore])

    # append django restframework settings
    subprocess.call(['mv', project_current_settings, project_settings])
    with open(project_settings, 'a') as settings_file:
        subprocess.call(['cat', drf_settings], stdout=settings_file)

    # rm tmp file
    subprocess.call(['rm', '-rf', starter_tpl_dir])
    subprocess.call(['rm', '-rf', tmp_venv])
