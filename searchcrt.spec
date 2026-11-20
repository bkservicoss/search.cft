# -*- mode: python ; coding: utf-8 -*-
# Build do Search.CRT para Windows (usado pelo GitHub Actions: .github/workflows/build-windows.yml)

a = Analysis(
    ['searchcrt.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/identidade/searchcrt.ico', 'assets/identidade'),
        ('assets/identidade/icone-64.png', 'assets/identidade'),
    ],
    hiddenimports=['openpyxl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # Bibliotecas pesadas que o app não usa (o .exe antigo tinha ~74 MB por causa delas)
    excludes=['pyarrow', 'matplotlib', 'scipy', 'IPython', 'jupyter', 'notebook',
              'setuptools', 'PIL', 'cryptography', 'pytest', 'streamlit', 'pymongo'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Search.CRT',
    icon='assets/identidade/searchcrt.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
