#!/usr/bin/env python3
"""Fold the Power Drive (CD32) findings into the shared checklist.

Same contract as every patch script in this directory: every anchor is
asserted UNIQUE before anything is written, and if any anchor is missing or
ambiguous the script writes nothing at all and says which one failed.  The
section 10 column is NOT here: it went in through `addcolumn.py` with
`column-powerdrive.py` (33 rows widened 20 -> 21, none empty).

Usage: python tools/patch-powerdrive.py cd32-platform-notes.md
"""
import sys, io

EDITS = []


def edit(name, old, new):
    EDITS.append((name, old, new))


# ---------------------------------------------------------------- header
edit("intro: disc count",
"""next and added to by each. It currently rests on **nineteen discs**, so much of
it is still marked with the title it came from: treat it as a list of things to
*test*, not a list of things that are true of the format.""",
"""next and added to by each. It currently rests on **twenty discs**, so much of
it is still marked with the title it came from: treat it as a list of things to
*test*, not a list of things that are true of the format.""")

edit("intro: the twentieth",
"""dates. See sections 1, 8, 9 and 10, and open item 41.""",
"""dates. See sections 1, 8, 9 and 10, and open item 41.

And the twentieth is the **fourth disc stamped on the afternoon of 21 December
1992** — and the first that shares its mastering house with one of the other
three: Rob Northen Computing, ISOCD 1.04 and the same 50.000000-MiB hole as
Myth. It carries a *second* day fourteen seconds after the first, and 161 of
its 162 directory records have an even second, which is a FAT file system's
signature and the first time the file clock and the mastering clock could be
told apart on one of these discs. It is also the disc on which the **Akiko C2P
column was checked in the form that could have hidden a positive** — the
register-relative `$38(a5)` after a `lea $B80000,a5` — with a walker from the
load site rather than a byte scan, and stayed at zero: the twentieth negative,
and the first one earned. See sections 3, 4, 10 and 11.""")

edit("disc list: add the twentieth row",
"""| [Alfred Chicken](https://github.com/vs-sr-dev/cd32-alfredchicken-doc) | **1993** | Twilight for Mindscape, UK — the **first di""",
"""| [Power Drive](https://github.com/vs-sr-dev/cd32-powerdrive-doc) | **1994/1995** | Denton Designs (named only as a rendered logo) / US Gold, UK — one `MODE1/2352` track, **38,133 sectors of which 68.39 % are zero**, a **50.000000-MiB hole at the same LBA as Myth's**, the same preparer and tool as Myth, and a PVD date of 1992-12-21 that the `.TM` block's © 1993 falsifies: **the fourth disc with that afternoon**, with a second day fourteen seconds after the first and **161 of 162 records stamped with even seconds** (FAT). 161 files, **135 RNC ProPack 1 closing 135 of 135**, and **89.73 % of the file bytes are six cars in 583 headerless frames of 240 × 150 × 5 planes with a 32-colour palette each**, dated December 1994, closed by lag measurement and a render the owner recognised. A 440-byte hunk reads a 99 KB raw loader through `dos.library` — twice — which copies itself to $28000 and carries a CD driver assembled twice, a floppy MFM encoder, an `RDSK` parser and an I²C EEPROM driver; **Akiko drives the CD (4 of 20) and the NVRAM (2 of 20) through base registers, and the C2P port is untouched (0 of 20) in the register-relative form too**. Five languages as five pointers per menu record, 121 records; two Oktalyzer players with 27 `.WAV`-named samples inside; a PC's PKZIP whose two members are the disc's own files |
| [Alfred Chicken](https://github.com/vs-sr-dev/cd32-alfredchicken-doc) | **1993** | Twilight for Mindscape, UK — the **first di""")

# ---------------------------------------------------- section 2: .TM count
edit("section 2: .TM disc count",
"""**All three SHA-1s match, byte for byte, on seventeen of the eighteen CD32-era
discs**""",
"""**All three SHA-1s match, byte for byte, on eighteen of the nineteen CD32-era
discs** ([Power Drive] the eighteenth, reached through the `TM` tag at PVD byte
888 with constant 0x0014, length 2,048, LBA 21)""")

# ---------------------------------------------------- section 3: the fourth disc
edit("section 3: the fourth disc",
"""Three discs now show a
clustered start. **On the fourth, look for the first bulk write near 15:1x and
let the rest of the session run where it likes.**""",
"""Three discs now show a
clustered start. **On the fourth, look for the first bulk write near 15:1x and
let the rest of the session run where it likes.**

**THE FOURTH DISC, AND IT ANSWERS THE TEST — THEN ADDS A DAY.** [Power Drive]
(US Gold, prepared by Rob Northen Computing with ISOCD 1.04, the same preparer
and the same 50.000000-MiB hole as [Myth]) carries the afternoon on **145 of
its 161 files**: PVD 1992-12-21 **15:14:49**, root record **15:12:16**, and
the first bulk write — 49 stage backdrops in forty seconds — at
**15:19:00–15:19:40**, inside the window as predicted. The rest of the day runs
where it likes: `astpal.bin` 16:05:14, `walt.rnc` 17:32:22, the `s/` directory
**19:17:20**. And that is the proof from inside the image that the other three
could not give: **a volume whose PVD says 15:14:49 indexes a directory record
of 19:17:20 the same day.** One clock cannot do that. Uptime-as-time-of-day
can, and every stamp on the disc fits it.

What the hypothesis as written did not predict: **a second day**. 92 files are
stamped 1992-12-22 from **15:08:38**, and the first stamp of 1992-12-21 is
**15:08:24** — fourteen seconds apart in time of day. Two boots of the same
machine, the date advanced by one between them. A fixed stored base does not
advance; a base restored from the boot volume after a session that left
something dated a day later would. The mechanism is not in the bytes; the
fourteen seconds are. **On the fifth disc with this afternoon, look for whether
the day advances between sessions, and by how much.**

**And a witness nobody had asked for: the seconds.** 161 of Power Drive's 162
directory records carry an **even** second. AmigaDOS stamps in 1/50 s and has
no parity; MS-DOS/FAT stamps in two-second units and cannot be odd. The one
odd record is the PKZIP archive (15:12:01), written fifteen seconds before the
root record, and the PVD's 15:14:49 is odd too. So the *files* came with FAT
stamps and the *mastering* stamps are the Amiga's — the first disc on which the
two clocks can be told apart. It is this disc's, not the afternoon's: the
1992-12-21 stamps the three other repositories quote are odd freely (Banshee
25 even against 16 odd, Marvin 6 against 4, Myth's `15:12:38`, `15:13:51`,
`17:10:58`). **Count the seconds' parity on every disc from now on**: it costs
one `awk`, and it says which side of a PC the tree passed.""")

# ---------------------------------------------------- section 4: Akiko table
edit("section 4: Akiko table recounted to twenty",
"""| | Discs using it | Which |
|---|---:|---|
| `$00B80000` as a **pointer load** — driving the drive | **3 of 17** | [Dragonstone], [Universe], **[Myth]** |
| `$00B80030` — the **I²C port to the CD32's serial EEPROM** | **1 of 17** | **[Universe]** |
| `$00B80038` / `$00B8003C` — the **C2P port** | **0 of 17** | none |
| `$C0DE0000` — the identification constant | **0 of 17** | none |

*(These denominators were stale at "14" for three discs. They are recounted
here against the nineteen discs in the list at the top of this document, and
the lesson is the general one: **re-read the counts you quote, not only the ones
you add**.)*""",
"""| | Discs using it | Which |
|---|---:|---|
| `$00B80000` as a **pointer load** — driving the drive | **4 of 20** | [Dragonstone], [Universe], [Myth], **[Power Drive]** |
| `$00B80030` — the **I²C port to the CD32's serial EEPROM** | **2 of 20** | [Universe], **[Power Drive]** |
| `$00B80038` / `$00B8003C` — the **C2P port** | **0 of 20** | none |
| `$C0DE0000` — the identification constant | **0 of 20** | none — [Power Drive] has six as bitmap bytes inside `*dat.bin`, named as the false positive |

*(These denominators were stale at "14" for three discs, then at "17" for two
more — the table said "of 17" beside a sentence saying it had been recounted
against nineteen. They are recounted here against the twenty discs in the list
at the top of this document, and the lesson is the general one, twice: **re-read
the counts you quote, not only the ones you add**.)*

**THE FOURTH LOOK — THE C2P COLUMN CHECKED IN THE FORM THAT COULD HAVE HIDDEN
IT.** Every zero in the third row above was an *absolute* zero: no instruction
with the operand `$00B80038` or `$00B8003C`. But three of the four drive-drivers
load `$B80000` into a base register, and from then on the C2P port is
**`$38(a5)`** — a 16-bit displacement, invisible to any scan for the four
bytes. [Power Drive]'s `akiko2.py --follow` walks the code from each Akiko load
the byte scan finds: linear flow, `bsr`/`Bcc`/`DBcc`/`bra` targets, `jsr d16(pc)`,
and `jsr abs.l` inside the loaded image (`--base`), until `rts`, an indirect
jump, or the first instruction that writes the base register (`lea $440(a5),a5`,
a `movem.l (a7)+` restore), and reports every access through that register as
the absolute Akiko address it reaches. Its selftest carries the controls: a
`move.l d0,$38(a5)` after `lea $B80000,a5` must be found; the same access in a
`bsr` target placed *after* the caller's `rts` must be found (a linear sweep
misses it, and that is the shape of the driver); after a table step or a
restore it must not be. On Power Drive's loader the walk from the a5 loads
reaches `$04 $08 $10 $14 $18 $19 $1A $1D $1F $20 $24` and nothing else — 46
and 45 accesses, and 32 dispatch-table handlers closed by hand — and the 94
`$38`/`$3C` displacements on *any* register all close on something that is not
Akiko (80 on the driver's variable block, 4 in a floppy MFM encoder where `$38`
is a sector's data checksum, 10 in data). **Run `--follow` on Dragonstone,
Universe and Myth**: their zeros are still absolute zeros until it has.""")

# ---------------------------------------------------- section 10: intro
edit("section 10: twenty discs",
"""Nineteen discs, and they bracket the format rather than agreeing on it.""",
"""Twenty discs, and they bracket the format rather than agreeing on it.""")

# ---------------------------------------------------- section 11: step 31 grows
edit("section 11: step 31, the walk from the load",
"""    a title might park somewhere unexpected. `tools/akiko2.py` in
    cd32-universe-doc. **A negative result from a two-encoding scan is not a
    negative result.** (Section 4.)""",
"""    a title might park somewhere unexpected. `tools/akiko2.py` in
    cd32-universe-doc. **A negative result from a two-encoding scan is not a
    negative result.** (Section 4.)

    **And a negative result from an absolute scan is not a negative result
    either, once a base register holds the chip.** After `lea $B80000,a5` the
    C2P port is `$38(a5)` and no byte pattern will find it. Walk the code from
    every load site — `akiko2.py --follow [--base ADDR]` in cd32-powerdrive-doc,
    with the subroutine, table-walker and restore controls in its selftest —
    and close the `jsr (An)` dispatches it stops at by hand. [Power Drive] was
    the first disc checked this way; the three earlier drive-drivers have not
    been. (Section 4.)""")

edit("section 11: item 43",
"""    so nobody can do this from the repositories as they stand. **Re-extract
    `libs/` and `c/` from every image and hash them once**; it produces a column
    for the whole set rather than a fact about one disc.""",
"""    so nobody can do this from the repositories as they stand. **Re-extract
    `libs/` and `c/` from every image and hash them once**; it produces a column
    for the whole set rather than a fact about one disc.

43. **Does the stored-base date advance between sessions, and does the tree
    pass through FAT?** [Power Drive] has two days of the 1992-12-21 afternoon
    whose first stamps are fourteen seconds apart in time of day, and 161 of
    162 records with even seconds against three neighbours that stamp odd
    seconds freely. Two `awk` lines per disc: the first stamp of each day, and
    the parity count. The first tells whether the base is fixed or carried
    forward; the second tells whether a PC sat between the studio and the
    master. Both are cheap enough to run on every disc that has the afternoon,
    and on the ones that do not. (Section 3.)""")


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    path = sys.argv[1]
    text = io.open(path, encoding='utf-8').read()

    # ---- validate every anchor BEFORE writing anything
    bad = []
    for name, old, new in EDITS:
        n = text.count(old)
        if n != 1:
            bad.append((name, n))
    if bad:
        for name, n in bad:
            print("  anchor %-45s occurs %d times (need exactly 1)" % (name, n))
        raise SystemExit("REFUSING: %d of %d anchors are not unique; nothing written"
                         % (len(bad), len(EDITS)))
    print("all %d anchors unique" % len(EDITS))

    # ---- apply
    before = len(text)
    for name, old, new in EDITS:
        text = text.replace(old, new, 1)
        print("  applied %s" % name)

    io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
    print("OK: %d -> %d bytes (+%d)" % (before, len(text), len(text) - before))


if __name__ == '__main__':
    main()
