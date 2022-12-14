# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Renge_classroom.pyw'],
    pathex=['./modules/'],
    binaries=[],
    datas=[('./assets/character_keys/hiragana.json', 'character_sets'), ('./assets/renge_pics/renge_dying_inside.png', 'pictures'), ('./assets/renge_pics/renge_regular.png', 'pictures'), ('./assets/renge_pics/renge_welcome.png', 'pictures'), ('./assets/renge_pics/renge_cheerful.png', 'pictures'), ('./assets/renge_pics/renge_disappointed.png', 'pictures'), ('./assets/renge_pics/renge_disgusted.png', 'pictures'), ('./assets/renge_pics/renge_intrigued.png', 'pictures'), ('./assets/renge_pics/renge_cheerful.png', 'pictures')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Renge_classroom',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Renge_classroom',
)
