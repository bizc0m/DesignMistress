from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAPSULE = Path(__file__).resolve().parent
DIST = CAPSULE / "dist"
SOURCES = {
    ROOT / "index.html": (DIST / "apps" / "designmistress.html", ()),
    ROOT / "NameTent" / "index.html": (
        DIST / "apps" / "nametent.html",
        ((b'href="./index.html"', b'href="./nametent.html"'),),
    ),
    ROOT / "NameTent" / "price-tents.html": (
        DIST / "apps" / "price-tents.html",
        ((b'href="./index.html"', b'href="./nametent.html"'),),
    ),
}


def build():
    missing = [str(source) for source in SOURCES if not source.is_file()]
    if missing:
        raise SystemExit("Sources manquantes pour assembler la capsule :\n- " + "\n- ".join(missing))
    (DIST / "apps").mkdir(parents=True, exist_ok=True)
    (DIST / "index.html").write_bytes((CAPSULE / "index.html").read_bytes())
    for source, (target, replacements) in SOURCES.items():
        content = source.read_bytes()
        for old, new in replacements:
            if old not in content:
                raise SystemExit(f"Lien attendu introuvable dans {source}: {old.decode()}")
            content = content.replace(old, new)
        target.write_bytes(content)
    print("Capsule prête :", DIST)
    for path in [DIST / "index.html", *sorted((DIST / "apps").glob("*.html"))]:
        print(f"  {path.name}: {path.stat().st_size:,} octets")


if __name__ == "__main__":
    build()
