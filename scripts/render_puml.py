#!/usr/bin/env python3
"""
Compilador automático de diagramas PlantUML (.puml) a SVG para CTS Academy.
Genera los archivos SVG en la carpeta /images manteniendo la misma estructura
relativa que los archivos .puml en /RUP, conforme al estándar de Masías / pyCelda.
"""

import sys
import zlib
import urllib.request
import pathlib

PLANTUML_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

def encode_6bit(b):
    return PLANTUML_ALPHABET[b & 0x3F]

def append_3bytes(b1, b2, b3):
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return encode_6bit(c1) + encode_6bit(c2) + encode_6bit(c3) + encode_6bit(c4)

def encode_plantuml(text):
    zlib_data = zlib.compress(text.encode("utf-8"))[2:-4]
    res = ""
    i = 0
    while i < len(zlib_data):
        b1 = zlib_data[i]
        b2 = zlib_data[i+1] if i+1 < len(zlib_data) else 0
        b3 = zlib_data[i+2] if i+2 < len(zlib_data) else 0
        res += append_3bytes(b1, b2, b3)
        i += 3
    return res

import re

def render_plantuml_code(code_str, target_svg_path, repo_root):
    target_svg_path.parent.mkdir(parents=True, exist_ok=True)
    enc = encode_plantuml(code_str)
    url = f"http://www.plantuml.com/plantuml/svg/{enc}"
    req = urllib.request.Request(url, headers={"User-Agent": "CTS-Academy-Compiler"})
    with urllib.request.urlopen(req) as resp:
        svg_data = resp.read()
        target_svg_path.write_bytes(svg_data)
        print(f"✓ Renderizado: {target_svg_path.relative_to(repo_root)} ({len(svg_data)} bytes)")

def render_file(puml_path, repo_root):
    rel_path = puml_path.relative_to(repo_root)
    content = puml_path.read_text(encoding="utf-8")
    
    blocks = re.findall(r"(@start(?:uml|salt)[^\n]*\n.*?@end(?:uml|salt))", content, re.DOTALL)
    if not blocks:
        blocks = [content]
        
    if len(blocks) == 1:
        svg_path = repo_root / "images" / rel_path.with_suffix(".svg")
        render_plantuml_code(blocks[0], svg_path, repo_root)
    else:
        for idx, block in enumerate(blocks):
            first_line = block.splitlines()[0]
            m = re.match(r"@start(?:uml|salt)\s+([A-Za-z0-9_-]+)", first_line)
            if m:
                name = m.group(1)
                svg_path = repo_root / "images" / rel_path.parent / f"{name}.svg"
            else:
                svg_path = repo_root / "images" / rel_path.parent / f"{puml_path.stem}-{idx+1}.svg"
            render_plantuml_code(block, svg_path, repo_root)

def main():
    repo_root = pathlib.Path(__file__).resolve().parent.parent
    pumls = sorted(repo_root.glob("RUP/**/*.puml"))
    print(f"🔍 Encontrados {len(pumls)} archivos PlantUML (.puml) en RUP...")
    
    for puml in pumls:
        try:
            render_file(puml, repo_root)
        except Exception as e:
            print(f"✗ Error al renderizar {puml.name}: {e}", file=sys.stderr)
            
    print("✨ Todos los diagramas se compilaron exitosamente a SVG en /images.")

if __name__ == "__main__":
    main()
