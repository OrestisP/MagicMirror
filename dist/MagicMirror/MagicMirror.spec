from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\Orestis\\Documents\\1. UDEMY COURSES\\19.Ardit_course_OOP\\Mirror'],
             binaries=[],
             datas=[('images\*.png', '.\png')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['docxtpl', 'PyDrive','python-docx', 'google-api-core','google-api-python-client',
                       'google-auth-httplib2', 'google-auth-oauthlib', 'googleapis-common-protos'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='MagicMirror',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='mirror.ico')
coll = COLLECT(exe, Tree('D:\\Orestis\\Documents\\1. UDEMY COURSES\\19.Ardit_course_OOP\\Mirror'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='MagicMirror')
