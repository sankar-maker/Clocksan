# -*- mode: python ; coding: utf-8 -*-

from kivymd import hooks_path as kivymd_hooks_path
from  PyInstaller.utils.hooks import (collect_data_files, collect_submodules)

kivy_md= collect_submodules('kivymd')
plyer_m=collect_submodules('plyer')
hid_mod=kivy_md+plyer_m

block_cipher = None


a = Analysis([r'C:\Users\dima\Downloads\timer\timer.py'],
             pathex=[r'C:\Users\dima\Downloads\timer'],
             binaries=[],
             datas=[],
             hiddenimports=hid_mod,
             hookspath=[kivymd_hooks_path,  ],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          Tree(r"C:\Users\dima\AppData\Local\Programs\Python\Python39\share\glew\bin"),
          Tree(r'C:\Users\dima\AppData\Local\Programs\Python\Python39\share\sdl2\bin'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          #*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          [],
          name='SanClock',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon=r'C:\Users\dima\Downloads\timer\clock, date, time icon icon.ico')
