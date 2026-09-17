#!/usr/bin/env python3
"""The README half of the Power Drive fold-in: the disc table gets its
twentieth row (above James Pond 2, newest first), section 10's column count
goes to twenty, and one wrong mnemonic in the new section 10 column of the
notes is corrected (`lea $B80030,a2`, encoding 45f9, not `movea.l`).

Usage: python tools/patch-powerdrive-readme.py README.md cd32-platform-notes.md
"""
import sys, io

README_EDITS = [
 ("disc table: the twentieth row above James Pond 2",
  """| [James Pond 2: Codename RoboCod](https://github.com/vs-sr-dev/cd32-jamespond2-doc) | **1993** | Millennium Interactive""",
  """| [Power Drive](https://github.com/vs-sr-dev/cd32-powerdrive-doc) | **1994/1995** | Denton Designs / US Gold — the **fourth disc stamped on the afternoon of 21 December 1992**, by Myth's preparer with Myth's tool and Myth's 50.000000-MiB hole, and the first on which a volume cut at 15:14 indexes a directory written at 19:17 the same day; a **second day fourteen seconds after the first**, and **161 of 162 records with even seconds** — a PC's FAT between the studio and the master. One track, **68.39 % zero**; 135 RNC files closing 135 of 135; **six cars in 583 headerless frames of 240 × 150 × 5 planes with a palette each**, 89.73 % of the bytes; a 99 KB raw loader carrying a CD driver twice, a floppy MFM encoder and an `RDSK` parser; **Akiko drives the CD and the NVRAM, and the C2P port is untouched in the register-relative form too** — the twentieth negative, the first one walked from the load site. The studio's name exists only as twelve rendered logo screens |
| [James Pond 2: Codename RoboCod](https://github.com/vs-sr-dev/cd32-jamespond2-doc) | **1993** | Millennium Interactive"""),
 ("section 10: twenty columns",
  """| 10 | Baselines, disc by disc, side by side — **nineteen columns**""",
  """| 10 | Baselines, disc by disc, side by side — **twenty columns**"""),
]

NOTES_EDITS = [
 ("section 10 column: the NVRAM load is lea, not movea",
  """**the CD32 EEPROM by hand**: `movea.l #$B80030,a2` twice in `rboot.bin`'s `NVIO` module""",
  """**the CD32 EEPROM by hand**: `lea $B80030,a2` (45f9) twice in `rboot.bin`'s `NVIO` module"""),
]


def apply(path, edits):
    text = io.open(path, encoding='utf-8').read()
    bad = [(n, text.count(o)) for n, o, _ in edits if text.count(o) != 1]
    if bad:
        for n, c in bad:
            print("  anchor %-45s occurs %d times (need exactly 1)" % (n, c))
        raise SystemExit("REFUSING on %s; nothing written" % path)
    before = len(text)
    for n, o, w in edits:
        text = text.replace(o, w, 1)
        print("  applied %s" % n)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
    print("OK %s: %d -> %d bytes" % (path, before, len(text)))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    apply(sys.argv[1], README_EDITS)
    apply(sys.argv[2], NOTES_EDITS)
