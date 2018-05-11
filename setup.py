# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('autoLotus5.py')]

options = {
    'build_exe': {
        'include_msvcr': True,
    }
}
setup(name='LotusAuto',
      version='0.0.5',
      description='AutoLotus FKU',
      executables=executables,
      options=options)