# Amiga CD32 / CDTV platform notes — a checklist for the next disc

A running checklist, carried from one Amiga CD documentation pipeline to the
next and added to by each. It currently rests on **nineteen discs**, so much of
it is still marked with the title it came from: treat it as a list of things to
*test*, not a list of things that are true of the format.

One of the nineteen is the **CDTV release of a title whose CD32 release is also
here**,
which is the most productive single thing that has happened to this document:
it supplied a control for claims that had been made on one disc's evidence,
and **two of them were wrong**. Both are corrected in place below, and both
corrections are marked. If you can get two releases of the same game on two
generations of the format, do that before you generalise anything.

Findings are marked:

* **[all]** — checked on every disc covered so far.
* **[N of M]** — checked on N of the M discs covered.
* *named after a disc* — seen once, not yet generalised.

And one of the nineteen is a **CD32 title whose A1200 floppy release can be
compared with it block for block**, which is the second-most productive thing
that has happened to this document: it turned the compression rule below from a
correlation across unrelated discs into a controlled experiment on one data set.

The discs are as unlike each other as CD32 titles can be — a floppy port that
uses 3 % of a CD, a disc that is 89 % Red Book audio, a disc that is 91 %
digitised speech, one that is **92 % a single file of streamed video**, one
whose whole volume is **772 sectors**, one that leaves **95 % of its volume
empty in front of the files**, one whose whole game is **2.25 MB with
nothing packed**, and one that is **99 % Red Book audio with a 918-sector data
track** — which makes the handful of things they agree on worth more
than the count suggests.

And one of the nineteen is the **second disc here from a label that already
had one**, three months apart in the same year and close enough to have shared a
build kit. It is the most productive control after the two Prey masters,
because it tested a prediction this document had been carrying for eight discs
and **the prediction was wrong**. See open item 14. **A third disc from that
same label has since arrived** — Universe, Core Design, 1994 — which turns that
one-off comparison into a three-point test, and the answer holds: see open
item 14.

And the fourteenth is the set's **first point-and-click**, which matters
because it is the first title here whose *content* is text rather than
artwork. It supplied the section 9 numbers this document had been unable to
fill in, a **bytecode interpreter** nothing in the set had shown before, and
the correction that matters most operationally — **the Akiko scan carried from
Guardian was looking at two of the eight address registers and returns a false
negative**. See section 4.

And the nineteenth is the first disc here that is **three products on one
master** — a game, a 2 m 43 s cartoon and a three-language electronic book,
offered as three branches of a shell script — which is what finally separates
"the disc" from "the title" in section 10, and moves the size band's floor for
the second time in two discs. It is also the disc where the **data-preparer
field stops being anonymous**: the man named in it wrote the boot script, signed
it in the first person, dated it, and the directory confirms all three of his
dates. See sections 1, 8, 9 and 10, and open item 41.

And the eighteenth is the **first disc here read from the physical medium
instead of from an image file**, which is the most productive single thing to
happen to this document since the two Prey masters. It settled three things no
image could: the thirteen-zero `CATALOG` four discs carry is **on the disc**, in
the subchannel, not lost by a dumper; the 32..232-sector overrun past the
declared volume is **cut into the glass master**, and is padding up to the next
track's pregap; and `MODE1/2048`, which every cue in this set asserts and no disc
had ever been checked for, is **verified** by descrambling raw sectors. It also
supplied per-track **ISRC** and real pregaps, fields the set had never read, and
a dating instrument it had no step for — **expanded RCS keywords**. See step 40
and open items 38–40.

## Discs this rests on

| Disc | Year | What it is |
|---|---|---|
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |
| [Marvin's Marvellous Adventure](https://github.com/vs-sr-dev/cd32-marvinsmarvellousadventure-doc) | 1994/1995 | Infernal Byte Systems / 21st Century, DE/UK — twelve tracks, 212 files, **nothing compressed**, 61 % of the disc used, ten libraries opened and AmigaDOS alive throughout |
| [Prey: An Alien Encounter, CD32](https://github.com/vs-sr-dev/cd32-prey-doc) | **1993** | KirkMoreno Multimedia / Almathera, UK+DK — **one track and no audio track at all**, 1,439 files, nothing compressed, 18 % of the disc used, an hour of speech streamed as 1,225 identical 60 KB files, and the only disc so far that genuinely uses AGA |
| [The Speris Legacy](https://github.com/vs-sr-dev/cd32-thesperislegacy-doc) | **1996** | Binary Emotions / Team 17, UK — one track, **no audio track**, 47 files, **0.74 % of the disc used**, Imploder-crunched at 2:1, genuine 24-bit AGA palettes in every level, and the disc that **broke this document's rule about what the `.TM` block contains** |
| [Legends](https://github.com/vs-sr-dev/cd32-legends-doc) | **1996** | Krisalis Software / Guildhall, UK — **28 audio tracks**, 111 files, **0.72 % of the disc used for the game and 88.6 % for the music**, a six-floppy A1200 game copied onto a CD with its hard-disk installer still on it, 79 files packed by a cruncher with **no magic number at all**, and a front end that re-implements `LoadSeg` |
| [Liberation: Captive II](https://github.com/vs-sr-dev/cd32-liberation-doc) | **1994** | Byte Engineers / Mindscape, UK — **the largest data track on the format so far**, 82,502 sectors, of which **91.2 % is digitised speech**; 187 files, ten audio tracks, one codec wearing RNC ProPack's magic over a different stream, a 3D engine shipped as **three separate shared libraries**, three **procedural generators the game runs as separate programs**, and a boot script that mounts a **reset-surviving RAM disk** |
| [Microcosm](https://github.com/vs-sr-dev/cd32-microcosm-doc) | **1994** | Psygnosis, UK — the **first CD32-exclusive title here**: no floppy ancestor, no A1200 fallback, AGA required. 34 files, a five-byte boot script, one Red Book track nothing plays, and **92.3 % of the data track in one 483 MB file** holding 30,707 frames of video in 261 movies, streamed with `CD_READXL` and decoded straight into eight bitplanes. Volume identifier **`CDTV_TEST`** |
| [Gloom](https://github.com/vs-sr-dev/cd32-gloom-doc) | **1995** | Black Magic Software / Guildhall, UK — **the smallest volume on the format, 772 sectors, 0.23 % of a CD**; 131 files, 115 of them packed with **CrunchMania**, no `c/` and no `libs/`, a seven-bitplane AGA display, and a real-time texture-mapped renderer whose **framebuffer is a copper list with one `MOVE` per pixel** |
| [HeroQuest II: Legacy of Sorasil](https://github.com/vs-sr-dev/cd32-heroquest2-doc) | **1994** | Gremlin Graphics, UK — a three-floppy A1200 board-game adaptation with its floppy loader intact. 97 files, five audio tracks of which the game can reach **two**, **95.4 % of the volume left empty in front of the files**, **RNC ProPack 1 wearing a rotating XOR key**, an executable that **decrunches and relocates itself in 584 bytes**, and the first master here cut with **ISOCD 1.03** |
| [Guardian](https://github.com/vs-sr-dev/cd32-guardian-doc) | **1994** | Acid Software — a **CD32-first** third-person polygon shooter, and the first genuine real-time triangle rasteriser in this set. 61 files, **none of them compressed**, 1,193 sectors, 0.40 % of a CD, twelve Red Book tracks the game plays out of the disc's own TOC. A **six-plane HUD panel stacked over a four-plane 3D view**, 24-bit colour reached through `BPLCON4`'s `BPLAM`, the pad clocked by hand on **both ports**, and a rasteriser that fills each polygon scanline with **one Blitter cookie-cut across all four interleaved planes** — so Akiko is zero again |
| [Banshee](https://github.com/vs-sr-dev/cd32-banshee-doc) | **1994** | Core Design, UK — the same label as Dragonstone and **written by a two-person Danish team**, which makes it the first same-label control here. 45 files, 37 RNC ProPack 1, 1,455 sectors, **0.44 % of a CD**; five minutes of Red Book played out of the drive; a **live developer hook in the pressed boot script**; and a 274 KB program nothing runs, holding a **640 × 512 interlaced HAM8** picture behind RNC ProPack **method 2** |
| [Fire & Ice](https://github.com/vs-sr-dev/cd32-fireandice-doc) | **1994** | Graftgold / Renegade, UK — a 1992 Amiga floppy platform game on CD32, and the **third `D J Pocock` master**. 29 files, **22 Red Book tracks** and 50:33 of music against a 1,270-sector data track; 21 files packed with **PowerPacker 2.0, the seventh cruncher here**, plus **29 more PP20 streams nested inside them that entropy cannot see**; an eight-plane dual-playfield AGA display run almost entirely from one copper list; and a floppy disk-swap prompt and a manual copy-protection prompt still in the pressed executable |
| [Universe](https://github.com/vs-sr-dev/cd32-universe-doc) | **1994** | Core Design, UK — the **third disc from this label** and the set's **first point-and-click**. 52 files, 47 RNC ProPack 1 nested **three levels deep** (342 validated streams), 2,429 sectors, **0.73 % of a CD** against **23 Red Book tracks and 40:37 of music**; **602 KB of prose in four complete languages**; a **16-opcode bytecode interpreter** with an explicit program counter; the CD-ROM *and* the CD32's serial EEPROM driven by hand through Akiko with the OS switched off; a six-plane **Extra-Half-Brite** display on AGA silicon with `FMODE = 0`; and the **fourth `D J Pocock` master**, leaving 232 sectors exactly as predicted |
| [Superfrog](https://github.com/vs-sr-dev/cd32-superfrog-doc) | **1994** | Team 17, UK — a 1993 floppy platformer, and the set's only **compilation**: Superfrog is 50.5 % of the bytes against a *Super Stardust* demo at 39.6 % and an *Arcade Pool* demo at 7.4 %, so most questions get asked three times on one master. 221 files, **no audio track**, 4,164 sectors, **1.26 % of a CD**. **96 Imploder files, 158 validated streams at depth 2**, and the game alone is **13,336,690 bytes resident — 0.64 % past Marvin's ceiling** while its on-disc 4.10 MB sits well inside the band, so the two readings disagree for the first time. The **cruncher follows the label** and the **`.TM` block follows the tool**, both predicted in writing and pointing opposite ways, with the mechanism on the disc: preparer `Kenny Grant` is a **third** preparer pattern and `s/T17Menu`'s `$VER:` names him as the menu's author. The **1993 three-floppy layout is recovered byte-exact** from the CD binary, the music is **37 The Player modules** in a fifth place the checklist did not list, and the manual is a **markup language shipped in source** with a doubled paste in the English original |
| [Gunship 2000](https://github.com/vs-sr-dev/cd32-gunship2000-doc) | **1994** | MicroProse — the **first flight simulator** here and the **first non-British publisher**, so the first test of whether ISOCD mastering practice follows the label. 140 files, five Red Book tracks, and the **second-largest data track in the set** at 157.84 MB — of which **63.4 % is a hole of exactly 100 MiB of zeros** and 86.9 % of the file bytes are CDXL video, leaving a 7.98 MB game. 542 RNC ProPack **method 2** streams; a resource archive that uses `LoadSeg`'s relocation table as its own pointer fixup; the game's own IFF data files written **little-endian**; a complete, unreachable **Pirates! Gold demo** with CD32 language detection; and the **fifth `D J Pocock` master**, leaving 232 sectors exactly as predicted |
| [Prey: An Alien Encounter, **CDTV**](https://github.com/vs-sr-dev/cd32-prey-doc/blob/main/docs/09-cdtv-1992.md) | **1992** | The same game a year earlier, published by KirkMoreno alone. **The first disc here not mastered with ISOCD**, the first CDTV disc, the oldest master by fourteen months, and the control that corrected two claims about the other three. 1,453 files, of which **1,201 are byte-identical to the CD32 release** |
| [Myth: History in the Making](https://github.com/vs-sr-dev/cd32-myth-doc) | **1992/1993** | System 3 Arcade Software, UK — developer and publisher in one, a label new to this set, and **the disc that is its own floppy release**. One track, **no audio track**, **five files and two directories**, 27,361 sectors of which **25,600 are a hole of exactly 50.000000 MiB** — 94.86 % of the declared volume — leaving a 2.72 MB game. Three of the five files are **901,120 bytes each: one 880 KiB Amiga floppy disk, exactly**, bootblocks and unused blocks included, so the floppy ancestor is not inferred but pressed. The 18,656-byte CD shim has **zero relocations**, four media back ends (DOS, floppy with MFM decode, hard disk with `RigidDiskBlock` parsing, CD through **Akiko**), a **hand-written `LoadSeg`**, and it hands the game a fixed key the floppy earned from its copy protection. Compression is **Bytekiller under the magic `DAVE`** — the programmer's first name — 23 streams, **depth 0**, every one validated three ways. **Expansion 1.369x, the lowest of ten.** The preparer field is a **fourth pattern: a company**, `ROB NORTHEN COMPUTING`, the author of RNC ProPack — on a master that does not use it. And the PVD's **1992-12-21 is falsified by the disc's own `.TM` block**, which is copyright 1993 |
| [James Pond 2: Codename RoboCod](https://github.com/vs-sr-dev/cd32-jamespond2-doc) | **1993** | Millennium Interactive, UK — a 1991 two-floppy platform game on a 195 MiB data track, and **three products on one master**: the game, a 2 m 43 s CDXL cartoon and a three-language electronic book, dispatched by a shell script that is a main loop. **65.55 % of the declared volume is a hole of exactly 128.000000 MiB** (65,536 sectors, 2^16, verified zero) and **93.90 % of the file bytes are CDXL video**, so two of the four hypotheses for a large data track are true at once for the first time. The **game is 1,033,508 bytes on disc / 1,258,076 resident — 18.1 % below Alfred Chicken's floor**, which had stood for one disc. Nothing packed, with a mechanism: all three hunks are `CHIP`, 1,185,496 of a 2 MB budget. **All seven Red Book tracks reachable** from byte 11 of an 86-record level table where bit 7 of the music id chooses Red Book or Paula, with the TOC never read. Five bitplanes with a **24-bit `LOCT` palette**, and an unreachable message in which the programmer apologises for the plane count and claims he left no debug symbols — **both verified**. A **three-language manual containing no characters at all**, 115 IFF ILBM pages measured in pixels. Preparer `Dean Ashton`, a **sixth name**, trailing run 32 — and the **first preparer identifiable from the disc in his own words**, in a signed 44-line comment whose three dates the filesystem confirms |
| [Alfred Chicken](https://github.com/vs-sr-dev/cd32-alfredchicken-doc) | **1993** | Twilight for Mindscape, UK — the **first disc here read from physical media rather than from an image file**, and the one that settled what a file cannot. Ten tracks: a **918-sector** data track and **nine Red Book tracks**, so **99.02 % of the pressed disc is audio** and the game is 1.26 MB — **43.9 % below Guardian's floor**, which had stood for seventeen discs. The MCN read from **subchannel Q** is `0000000000000` with MCVAL set, so the thirteen zeros four discs carry are the master and not the dumper; the volume declares **691** sectors and the disc physically holds **918** of valid MODE1 — every one verified on sync, header address and EDC — with the extra **227** stopping exactly where track 2's pregap begins, which is what the 32..232 overrun has always been. `MODE1/2048` **verified** by descrambling, ISRC **absent on all ten tracks**, and the nine audio tracks **perfectly contiguous** with one 150-sector pregap on the whole disc. 30 files, **RNC ProPack 1** validated 11 of 11 by CRC at depth 0, expansion **1.297x, the lowest of eleven**. The preparer is **`Abersoft`, the second company** in that field, with a 32-sector run — and since Mindscape's other disc, Liberation, is `D J Pocock` with 232, the field **follows the work, not the label**. Tiles derived three ways as **16x16x4**; **zero stored copper lists** but the screen mode hardcoded as `BPLCON0` immediates; **no text at all** — a fifth string model — with the game's own title existing only as a **320x184 picture**. And `intro`, built from source checked out **fourteen months before** `alfred`, ships a **working Amiga hardware debugger**: 47 custom-register description strings from Commodore's `hardware/custom.i` and `copdis`, a copper list disassembler |

---

## 1. Identify the disc, and do not trust the obvious fields

A CD32 game is an ordinary ISO 9660 disc with an AmigaDOS volume inside it.
There is **no boot descriptor, no signature file, and no header that says
CD32**. What you check instead:

| Where | What to expect |
|---|---|
| PVD system identifier (offset 8) | `CDTV` — *not* `CD32` **[3 of 3]** |
| `s/Startup-Sequence` | present, and it is the boot script |
| `c/` | AmigaDOS commands: `SetPatch` plus one or two custom tools — or a whole Workbench `C:` |
| The trademark block | **at the LBA the PVD points to**, which is *not* always 21 (section 2) |
| `/CD32.TM` | may be present as an ordinary file — the trademark block's own source (section 2) |
| Track 1 mode | `MODE1/2048` **[3 of 3]**; Mode 2 Form 1 also occurs |
| `libs/` | may be absent, or may carry the CD32 ROM libraries so the same binary runs on an A1200 |
| `<Game>.info` | if present, `DefaultTool = IconX` and a sibling script — the desktop entry point |

**The system identifier lies about the machine and it is supposed to.** **[3 of 3]**
All three discs are CD32 titles and all three PVDs read `CDTV`, because the CD32
reads CDTV media and a CD32 disc identifies its volume the way a 1991 CDTV
title does. Do not conclude you have a CDTV disc from that field alone.

**Read the application identifier as well as the publisher.** Dragonstone's
is the title, `DragonStone`. Marvin's is **`Platformer`** — the genre. Prey's
is **`Game`**. [Liberation]'s is **`Liberation CD32`** — the title *and* the
console. Four discs, four different kinds of answer to the same box: the
title, the genre, the medium's most generic possible noun, and the title with
the platform stapled on. The field carries no information about the disc and a
great deal about who typed it.

If `s/Startup-Sequence` is missing, the disc is not bootable on a stock
machine and something else is going on — check for a CDTV-only boot path or a
disc that was never meant to boot.

**String fields may be malformed and nothing cares.** **[3 of 3]** Every
string field in all three PVDs is NUL-padded rather than space-padded;
Dragonstone's volume identifier is mixed case (`DragonStone`), Marvin's is
`MMA_CD32` with an underscore, Prey's is `Prey`. ISO 9660 asks for
d-characters, upper case, space-padded. Do not use strictness as a signal of
anything.

**And read the volume identifier for what it is, because it may be a
placeholder that shipped.** [Microcosm] is a retail Psygnosis release whose
volume identifier is **`CDTV_TEST`**, with the volume set, publisher,
application identifier *and* preparer name all empty. Every free-text field on
that disc is either blank or a test string. It got past everybody because
**nothing on a CD32 needs the volume name**: the boot script names the
executable with no path, and the executable addresses every file through `cd0:`,
which is the device rather than the volume. A CD32 boots a disc called anything.

**CORRECTION — that is true of Microcosm and it is not true of the format.**
[Fire & Ice]'s volume identifier is **`Fire`**, and the disc uses it: the boot
script reads `fire:c/SetPatch QUIET` and `Fire:AskBoot`, the icon's default tool
is `Fire:c/IconX`, the Workbench script assigns `Fire:Libs`, and the game's own
three resource paths are `Fire:Cores/`, `Fire:Graphics/` and `Fire:Sets/`.
Rename that volume and the disc does not boot. So the field is sometimes
decorative and sometimes load-bearing, and which one it is takes one `grep` for
the volume name across the boot script, the `.info` files and the executable's
string table. **Do that grep before concluding the name is free text** — and if
it *is* used, a placeholder volume identifier would have been caught in
testing, which changes what an odd name means.
So do not read the volume identifier as an assertion about the title — read it
as evidence about the person who cut the master, exactly like the preparer
field, and check whether the disc uses it at all.

**And read the volume-set identifier, because somebody may have typed something
else into it entirely.** [HeroQuest II]'s is **`15 June 1994 17:30`** — a
hand-typed date and time, on a single-volume disc, in the field ISO 9660
reserves for naming a multi-disc set. The PVD's own creation stamp is
`1994-06-15 17:34:13`, four minutes later, so it is neither an inherited build
date nor a mistake: it is the mastering session's date, rounded down to the half
hour, typed into a box by the person filling in the form. Six discs put a title,
a genre, a medium, a `_1` suffix or nothing in these fields; this is the first to
put a *timestamp* in one. **Read every free-text field, and read it as evidence
about the operator rather than about the title.**

**And read it for a volume-set suffix, because it is the
cheapest hint that the title came from somewhere else.** [Liberation]'s is
**`Liberation_1`** on a single-volume disc, and the game executable turns out
to carry `CaptiveII_Disk1` through `CaptiveII_Disk4` and a save-disk volume
called `Lib-Saves`. A `_1` costs nothing to notice and it pointed at the whole
four-floppy ancestor before anything was disassembled.

**Read the cue sheet for a `CATALOG` line — and then read the number.**
Marvin's has one (`5012635300344`) and Prey's has one (`5024913000068`), both
UK EAN-13s; Dragonstone's has none. **Speris has `CATALOG 0000000000000`** —
thirteen zeros, syntactically valid and meaning nothing, and **[Liberation]
does the same in 1994**, as do [Microcosm] and **[Guardian]**, so that is four
discs across two years. The field has three states, not two, and the presence of the line is not evidence of a catalogue
number. It is the disc's retail barcode *when it is one*, and it identifies
the release when the label does not.

**A CD32 disc need not have an audio track.** [Prey] One `MODE1/2048` track
and nothing else, on a disc whose 75 MB of speech and music is stored as
ordinary files and streamed through Paula (section 8). Do not treat "no audio
track" as a sign that you are looking at a data-only disc or a bad rip.

### The mastering tool leaves fingerprints — collect them

The **data preparer** field usually names the tool outright, and a person
with it:

```
Dragonstone   Sajjad Majid - ISOCD 1.04 by Pantaray, Inc. USA -
Marvin        Stewart.. - ISOCD 1.04 by Pantaray, Inc. USA -
Prey          Almathera - ISOCD 1.04 by Pantaray, Inc. USA -
Speris                  - ISOCD 1.04 by Pantaray, Inc. USA -
Legends       Richard Teather (Programmer) - ISOCD 1.04 by Pantaray, Inc. USA -
Liberation    D J Pocock - ISOCD 1.04 by Pantaray, Inc. USA -
Microcosm                 - ISOCD 1.04 by Pantaray, Inc. USA -
Gloom                     - ISOCD 1.04 by Pantaray, Inc. USA -
HeroQuest II  Kevin Dudley - ISOCD 1.03 by Pantaray, Inc. USA -
Guardian                  - ISOCD 1.04 by Pantaray, Inc. USA -
Banshee       D J Pocock - ISOCD 1.04 by Pantaray, Inc. USA -
Fire & Ice    D J Pocock - ISOCD 1.04 by Pantaray, Inc. USA -
Universe      D J Pocock - ISOCD 1.04 by Pantaray, Inc. USA -
Superfrog     Kenny Grant - ISOCD 1.04 by Pantaray, Inc. USA -
Myth          ROB NORTHEN COMPUTING, UK. TEL: + 44 428 707771
              FAX: + 44 428 707772 - ISOCD 1.04 by Pantaray, Inc. USA -
```

**AND THE ELEVENTH ENTRY IS A REPEAT, ACROSS TWO UNRELATED STUDIOS.**
[Banshee]'s preparer field is character for character [Liberation]'s. Two
studios (Core Design, Byte Engineers), two publishers (Core, Mindscape), three
months apart in 1994, one operator. `Pocock` appears nowhere else on either
disc — not in a credits screen, not in a version string, not in a file name —
and Banshee's credits screen names five people, none of them him.

Two consequences, and the second is the useful one.

**The field carries no studio information at all.** Core Design's other disc
here says `Sajjad Majid`; its second says a name that belongs to a different
studio's disc. Whatever this box records, it is not the developer and it is not
the label.

**And it now correlates with a layout anomaly.** See the unclaimed-sector count
below: the only two discs in twelve that leave **232** zero sectors rather than
32 are the only two whose preparer field says `D J Pocock`. Two observations
are not a correlation, and the test on the next disc costs one field
comparison. **When a mastering anomaly turns up, read the preparer field before
looking for a technical cause.**

**CORRECTION — it is not always 1.04.** Nine discs said `ISOCD 1.04`; the tenth
says **`ISOCD 1.03`**, in June 1994, two months *after* Liberation's 1.04 and
months before Marvin's. So the two versions were in use at the same time and a
version number is not a date.

**And 1.03 is indistinguishable from 1.04 on every habit in this section.**
Checked one by one on [HeroQuest II]: duplicate PVD at 16 and 17 with the
terminator at 18, optional path-table pointers filled with the mandatory ones
(L 20/20, M 19/19), NUL padding on every string field, NUL modification/expiry/
effective dates, mixed-case file names, path tables before the files, an image
longer than the declared volume (by 227 sectors, all zero) and a 32-sector run
of zeros at the end. **Record the version and expect nothing from it**; the one
thing that disc does differently is in the sector map below, and whether that is
the tool or the operator is open.

**A refinement to habit 3, from checking a control.** ISOCD does *not* NUL-pad
the **system identifier**: that field is `CDTV` followed by 28 **spaces**, on
[HeroQuest II] (1.03), [Gloom] (1.04, 1995) and [Liberation] (1.04, 1994) alike,
while every other field on all three is NUL-padded. So the habit is "NUL-pads
every field it is given a value for, and writes the system identifier as a
space-padded constant". It matters because a parser that trims only NULs gets
`CDTV` plus spaces back and may report it as a malformed field.

**Four of eleven leave the box empty**, and they span two years:
[Microcosm] (1994), **[Guardian] (1994)**, [Gloom] (1995) and Speris (1996). So an empty preparer is
neither an early habit nor a late one and not one studio's; it is simply what
happens when nobody types anything. On [Microcosm] it is part of a pattern — see
the volume identifier below. On [Gloom] the volume identifier is the title
(`GLOOM`) and every *other* free-text field is empty, so the two discs are not
the same case: one person typed nothing at all, the other typed the one field a
person would think of. **[Guardian] is a third of the same kind** — volume
identifier `GUARDIAN`, every other free-text field blank — so "the volume name
and nothing else" is the commonest way a CD32 master gets filled in.

**And be ready for the name to lead nowhere.** [Liberation] `D J Pocock`
appears **nowhere else in 169 MB** — not in a credits screen, not in a version
string, not in a file name. Four of the six named preparers are findable in
the title's own data and two are not; the field names whoever ran the tool,
which is sometimes the programmer and sometimes not anybody the game mentions.

**And check the name against the game's own credits, because sometimes it is
there.** [Legends] `Richard Teather` is on the disc twice: in this field, and
in a 320 x 200 digitised **photograph** captioned `RICHARD TEATHER (AMIGA)`
under the heading `THE PROGRAMMERS`. The person who ran the mastering tool is
the person the credits screen calls the Amiga programmer, and the two halves
of the disc agree without either knowing about the other. **[HeroQuest II] makes
it three for three where a disc has both**: its preparer is `Kevin Dudley` and
its credit scroll reads `Programming / Kevin Dudley`. Six discs of eleven name a
person here; it is the cheapest attribution on the format and it is
worth cross-checking against whatever credit screen the game has. **[Banshee]
is the second disc whose named preparer is findable nowhere on the disc he
prepared — and it is the same name as the first.** **And where
the preparer field is empty, the credits screen may still name the tools** — on
[Gloom] it names four, and the disc independently confirms three of them (step
22 of the order of work).

(Marvin's `Stewart..` is Stewart Gilray, one of the game's two producers,
who is also sixth in the game's own hall of fame. Whoever typed the field
did not finish typing. Prey's names the publisher and no person at all.
**Speris leaves the box empty**, and the tool signs it anyway — so the
leading `" - "` belongs to the tool rather than being the tail of a
truncated name, which only becomes obvious once you have a disc with
nothing in front of it.)

**The application identifier is a fourth field of the same kind, and it is
not one to lean on.** Dragonstone puts the title there (`DragonStone`),
Legends likewise (`Legends`), Marvin's the genre (`Platformer`), Prey the
medium (`Game`), the CDTV master nothing, Speris nothing, [Microcosm] nothing
[Gloom] nothing and **[Guardian] nothing**. Ten discs, four conventions, and
**five of the ten leave it empty** — which is now the single commonest answer to
the box.

**[Banshee] adds a fifth convention and it is the most informative one yet:
`Banshee CD32`, the title *and* the console** — which [Liberation] and
[HeroQuest II] also do, so that is three of eleven. On Banshee all three of the
volume identifier, publisher and application identifier are filled in with
three *different* kinds of answer at once (`Banshee`, `Core`, `Banshee CD32`),
which is the most anyone typed into these boxes on any disc here.

Pantaray wrote more than the mastering tool. [Prey] `MORENO/XLPlay`, dated
1992-03-02 and run by nothing, is *"XLPlay ... by Pantaray, Inc. Ukiah CA"* —
a CDXL player the developers evaluated and did not ship with. If a disc
carries an unexplained tool, check whether the mastering house wrote it.

**ISOCD 1.04 has three visible habits, and all three ISOCD discs show all
three — and the one non-ISOCD disc shows none of them.** That is what turns
three sightings of one tool into an actual attribution.

| | ISOCD 1.04 (3 discs) | the CDTV Prey master |
|---|---|---|
| String padding | NUL | **space** |
| Data preparer | names the tool and a person | **empty** |
| Optional path tables | copies of the mandatory ones | **separate, at their own LBAs** |
| Modification date | NUL | **set** |
| File names | mixed case | **strict upper-case 8.3** |
| Path tables | before the files | **after them, at the end of the volume** |
| PVD written twice at 16 and 17 | yes | **yes** |

**A fourth habit, worth a line because the number repeats — though not
reliably.** ISOCD leaves the image longer than the volume it declares, and the
overrun is **152 sectors of zeros on three of the nine ISOCD discs** — Marvin (6,833 in the image, 6,681
declared), Speris (2,455 / 2,303) and Legends (2,404 / 2,252). Dragonstone
overruns by 106, [Liberation] by 103, [Microcosm] by 225, **[Gloom] by 180
(952 in the image, 772 declared)**, HeroQuest II by 227, **[Guardian] by 150
(1,343 in the image, 1,193 declared) — two short of the recurring number, which
is worth recording precisely because it is so nearly it** — **[Banshee] by 86
(1,773 in the image, 1,687 declared)** and Prey CD32 not at
all, so it is not invariant; but a
declared-versus-image difference of exactly 152 has now turned up three times
and is worth recording rather than rounding off. **Always build the sector map
against the declared size**, or the trailing zeros read as unclaimed space
that means something.

**Only the duplicated descriptor survives the change of tool.** Two
unrelated mastering systems both write the primary volume descriptor twice
with the terminator at 18, so that one is a property of the format or the
era, not of ISOCD. Everything else on the list is ISOCD's.

1. **It writes the primary volume descriptor twice**, at sectors 16 and 17,
   byte for byte identical, with the terminator at 18. Nothing is wrong; a
   reader takes the first primary descriptor it finds.
2. **It fills the optional path-table pointers with the mandatory ones**
   rather than leaving them zero — `L` and `L-optional` both point at the
   same LBA, likewise `M`.
3. **It NUL-pads every string field** where ISO 9660 asks for spaces.

Other tools do other things. Log which tool wrote which disc and what its
layout habits are. The empty preparer field on the CDTV master is itself the
fingerprint of *not* being ISOCD: the tool did not sign its work, and
identifying it is an open item.

**The declared volume size and the image size need not agree.** Dragonstone
declares 1,635 sectors in a 1,741-sector image; Marvin declares 6,681 in
6,833. **[2 of 3]** The tail is zero in both cases. Prey's declared size and
image size are **exactly equal** at 59,787, so the mismatch is a property of
how a dump was made, not of the format. Build your sector map against the
declared size either way.

**Count the unclaimed sectors inside the volume — but the count is not a
fingerprint.** [Marvin] 32, all zero, at the end. [Prey CD32] **32, all zero,
at the end.** [Speris] **32, all zero, at the end** — LBA 2271–2302 of a
2,303-sector volume. [Legends] 32 as well.

[Microcosm] **32, all zero, at the end** — LBA 255,520–255,551 of a
**255,552-sector** volume.

**CORRECTION — this document called that "exactly 32 every time" and a fifth
ISOCD disc broke it.** [Liberation] leaves **232** zero sectors at the end of
an 82,502-sector volume, cut with the same ISOCD 1.04 in 1994, between Marvin
and Speris in date. So the fingerprint is not the number; what survives is the
weaker and still useful "ISOCD leaves a run of zeros at the end of the volume
and something else does not". Four discs at 32 and one at 232 is worth
recording as it stands, because the next disc decides whether 32 is a common
case or a coincidence of small volumes — the four are 2,303 to 59,787 sectors
and the outlier is the largest volume on the format.

**AND THE NEXT DISC DECIDED IT: the number is not a function of volume size.**
[Microcosm]'s volume is **255,552 sectors**, three times Liberation's and a
hundred times Speris', and it leaves **32**. The "coincidence of small volumes"
reading is therefore dead: five discs from 2,303 to 255,552 sectors leave 32 and
Liberation alone leaves 232. Liberation is the outlier and what makes it one is
still unexplained. Keep counting the run; the useful form of the rule is
**"ISOCD leaves a short run of zeros at the end of the volume, almost always
32"**.

**AND THE DISC AFTER THAT TESTED IT FROM THE OTHER END.** [Gloom]'s declared
volume is **772 sectors** — a third of Speris', a 331st of Microcosm's, and the
smallest on the format — and it leaves **32, all zero, at LBA 740–771**. So the
run is now 32 on six discs spanning 772 to 255,552 sectors, a range of 331 to 1,
and 232 on Liberation alone. There is no size dependency left to appeal to and
no remaining reason to expect the number to move; **treat anything other than 32
as the finding, and go and look at what else that disc does differently.**

**AND THE EIGHTH LEAVES 32 TOO, ON THE SECOND-SMALLEST VOLUME IN THE SET.**
[Guardian]'s declared volume is **1,193 sectors** and the trailing run is **32,
all zero, at LBA 1161–1192**. Eight discs at 32, from 772 to 255,552 sectors;
Liberation alone at 232.

**AND THEN A SECOND DISC LEFT 232, AND IT IS NOT A SIZE EFFECT — IT MAY BE A
PERSON.** [Banshee]'s declared volume is **1,687 sectors** and the trailing run
is **232, all zero, at LBA 1455–1686**: one forty-ninth of Liberation's volume,
the same anomalous number, and 14 % of the whole volume given over to it.

```
disc         preparer      declared volume   trailing zero run
Liberation   D J Pocock            82,502    232
Banshee      D J Pocock             1,687    232
the other 8  various          772..255,552    32
```

Every size-based reading of the 232 is now dead — the two discs that have it
are the largest volume in the set and the fourth-smallest. What they do share
is the **one PVD field that names a person**, and no other disc in the set
carries that name. Two observations are not a correlation; what makes this
worth writing down is that it is falsifiable for the price of reading one
field. **On the next disc, read the preparer before you look for a technical
explanation of any layout anomaly** — and if a third `D J Pocock` disc appears,
check the trailing run first.

**AND THE THIRTEENTH DISC MADE IT THREE FOR THREE, AGAINST A PREDICTION
WRITTEN DOWN FIRST.** [Fire & Ice]'s preparer field is
`D J Pocock - ISOCD 1.04 by Pantaray, Inc. USA -`, character for character
Liberation's and Banshee's, and its trailing run is **232, all zero, at LBA
1,038–1,269** of a **1,270-sector** volume.

```
disc         preparer      declared volume   trailing zero run
Liberation   D J Pocock            82,502    232
Banshee      D J Pocock             1,687    232
Fire & Ice   D J Pocock             1,270    232
the other 9  various          772..255,552    32
```

Three discs, three studios, three publishers, one name, and a 65:1 range of
volume sizes **inside the `Pocock` group alone**. On Fire & Ice the run is
**18.3 % of the whole declared volume**. This is no longer "worth checking":
**promote it to a finding — the trailing run is a property of who cut the
master, not of what was on it.** Nothing else separates the three from the ten:
same tool string, same padding habits, same duplicate PVD, same trademark
block, image overruns of 87 and 86 against 150 and 227 on discs that leave 32.

There is still no mechanism, and 232 − 32 = 200 sectors = 409,600 bytes matches
nothing on any of the three. **Read the preparer field first on every disc**,
and if a fourth `Pocock` master turns up, the useful thing is not another 232 —
it is anything else about the three that differs from the ten.

**AND THE FOURTEENTH DISC IS A FOURTH `POCOCK` MASTER.** [Universe] (Core
Design, 1994) declares 2,429 sectors and leaves **232, all zero, at LBA
2,197–2,428** — 9.6 % of its volume — again against a prediction written before
the sector map was built.

```
disc         preparer      declared volume   trailing zero run
Liberation   D J Pocock            82,502    232
Banshee      D J Pocock             1,687    232
Fire & Ice   D J Pocock             1,270    232
Universe     D J Pocock             2,429    232
the other 10 various            772..255,552  32
```

Four discs, four studios, four publishers, one name. The correlation is not in
question; the mechanism still is, and Universe was measured specifically to
attack it. Newly ruled out on that disc: **image overrun 80 sectors** (the
group now reads 103/86/87/80 against 106/150/152/152/152/180/225/227/0 — and
Dragonstone's 106 sits *inside* the Pocock range, so the separation is not
clean and this is not it); **directory record order** (strict ISO 9660 ASCII,
three inversions against LBA order); **`;1` version suffixes** (present,
ordinary); **root directory extent** (4,096 bytes, two sectors); audio track
count (23, against 10/2/22 in the group and 0–28 outside it).

**And one new lead, which is a file rather than a field.** Universe's
`C/FreeAnim` and `C/noopenwb` are **byte-identical to Liberation's, timestamps
to the second included** — and Liberation is the other Pocock master that has
a `c/` directory at all. Banshee and Fire & Ice ship neither file and open
`freeanim.library` from CD32 ROM. So two of the four Pocock discs shipped the
same two utility binaries out of the same directory, across two unrelated
studios. That is not a property of the group and does not explain the 232, but
it is the first artefact found that links two Pocock masters and no other
disc. **On the fifth `Pocock` disc, hash the `c/` directory before anything
else.**

**AND THE SIXTEENTH DISC ADDS A THIRD SHAPE TO THE FIELD, WHICH TIGHTENS THE
RULE INSTEAD OF BREAKING IT.** [Superfrog]'s preparer is
`Kenny Grant - ISOCD 1.04 by Pantaray, Inc. USA -` — same wrapper, a **new named
operator**, trailing run **32**. The field now has three shapes:

```
preparer shape                       discs   trailing run
`D J Pocock`                             5   232, every time
empty name, tool signature only          5   32 (on the four cut with ISOCD)
seven other named operators              7   32
a COMPANY, with a phone and fax number   2   32   <- [Myth], [Alfred Chicken]
```

The prediction written before that field was read was **empty name**, because
the other Team 17 disc is one of the empty five. It was wrong, and being wrong
is what sharpened the rule: the correlation is not "empty means 32", it is the
narrower **`D J Pocock` leaves 232 and nobody else does** — 5 of 5 against 11 of
11, across eleven studios.

**A FOURTH SHAPE, AND IT IS NOT A PERSON.** [Myth]'s preparer field reads
`ROB NORTHEN COMPUTING, UK. TEL: + 44 428 707771 FAX: + 44 428 707772` before
the usual `- ISOCD 1.04 by Pantaray, Inc. USA -`. A **firm, with a telephone
number and a fax number**, advertising itself in a volume descriptor. Trailing
run **32**, so the correlation survives and *not-Pocock leaves 32* is now
**12 of 12**.

**AND THE NINETEENTH DISC ANSWERS THE QUESTION THE OTHER SIX COULD NOT.**
[James Pond 2] is `Dean Ashton - ISOCD 1.04 by Pantaray, Inc. USA -`, a
**seventh named operator**, trailing run **32**, so *not-Pocock leaves 32* is
**14 of 14**. That part is routine. What is not routine is that this is the
**first disc where the person in that field is identifiable from the disc, in
the first person, at length**. Its `s/Startup-Sequence` is 3,922 bytes of which
twenty-one are the launcher; the rest is a comment signed

```
; This funky startup sequence hurriedly put together at 1:30am 14.07.93
; by the master of the kludged code, Dean Ashton.
```

and he is not the mastering operator in any separable sense — the same name is
on the game's own credit screen as `AGA CONVERSION BY DEAN ASHTON`, on a hidden
string in the executable as `Dean Ashton, programmer, June 1993`, and in the
boot script's credit list as the author of the whole A1200/CD32 conversion.

So the field has now held: an anonymous tool signature, a bureau operator
appearing on five unrelated masters, two contractor firms, a menu author who
demonstrably did not write the game ([Superfrog]), and now **the studio's own
conversion programmer, who cut the master himself**. That is five distinct
owner-types on nineteen discs, and it is why "the operator" was always going to
be too narrow: the box records *whoever ran the tool*, and on a small 1993 team
that is whoever was awake.

**Two consequences worth carrying.** First, **when a named preparer turns up,
grep the boot script for the name before anything else** — it is free, and on
this disc it is where the answer was. Second, this disc is the counter-example
to [Superfrog]'s: there, the preparer wrote the menu and demonstrably not the
game; here, the preparer wrote the conversion, the boot script and the CDXL
conversion. **The field says nothing about role. It says who was at the
keyboard.**

Two things follow.

**The box does not always hold a person, so "the operator" is too narrow a
label for what it records.** It records *whoever ran the tool*, and this disc
shows that could be a **mastering bureau under contract** rather than anyone at
the studio. That is a fifth possible owner for an artefact — not the studio, not
the label, not the tool, not one named person, but a contractor — and it fits
the `D J Pocock` group better than anything proposed so far: one name on five
masters from five unrelated studios and five unrelated publishers, findable
nowhere on any of them, is the shape of a bureau operator, not of an employee.
That remains an inference; the test is another disc naming a firm, or a
`D J Pocock` disc that names a firm anywhere else.

**And the firm is the author of the set's commonest cruncher.** Rob Northen
Computing wrote **RNC ProPack**, which is on Dragonstone, Banshee, HeroQuest II,
Universe, Gunship 2000 and [Alfred Chicken], with Liberation's codec wearing its
magic — seven discs of eighteen. The firm that wrote it cut the master of an
eighth, **and that eighth does not use it**: [Myth] packs with Bytekiller, written by the game's
own programmer. One negative, one for one, and it is the cleanest separation of
the mastering step from the build step this set has: the same firm's name is on
the master and its packer is nowhere in the game. **On the next disc, read the
preparer field for a company name as well as a person's, and if you find one,
ask whether its own tools appear in the payload.**

**And it is the first disc whose named preparer is the author of a program on
it.** `s/T17Menu` carries `$VER: T17MENU 39.1 Kenny G (23.07.94)`. Four of the
six previously named preparers were findable on their discs as credit-screen
entries; this one is findable as a `$VER:` string. So the man who ran the
mastering tool also wrote the front-end menu — and, since none of the six game
programs on that disc has a `$VER:` or a bare build banner, he is demonstrably
**not** the person who wrote the game. **That is a mechanism, not a
correlation**, and it is what open item 14 needed: see the note under that item.

**AND THE SEVENTH DISC LEAVES 32 AS WELL, INCLUDING THE ONE CUT WITH A
DIFFERENT TOOL VERSION.** [HeroQuest II]'s volume is 25,436 sectors, cut with
**ISOCD 1.03** rather than 1.04, and the trailing run is **32, all zero, at LBA
25,404–25,435**. Seven discs at 32 across two tool versions and a 331:1 span of
volume sizes; Liberation alone at 232. The number does not move.

**A dump can be much larger than the disc.** [Prey CDTV] the image is 119,988
sectors and the declared volume is 48,637; the 71,351 sectors after it —
146 MB, **58 % of the file you were given** — hold no ISO structure, no
readable string, and a short repeating byte pattern. It is a dump artefact.
Always build the map against the declared size, and say what the remainder
is rather than assuming it is content.

**And a large zero gap can sit *inside* the volume, ahead of the files.**
[Microcosm]'s volume starts at 19 in the ordinary way — descriptors 16–18, path
tables 19–20, trademark block 21, root directory 22 — and then **LBA 23 to
15,022 is 15,000 sectors of zero**, 30.7 MB, 5.87 % of the declared volume,
before the first file at 15,023. That is a second shape of the same phenomenon
as Prey's, and it means "the volume starts where it should" does not imply "the
files start where they should". Build the sector map, look at the largest free
run, and say what is in it. 15,000 sectors is exactly 200 seconds of CD frames
and that disc's audio track is 203.0 seconds; whether the two are related is
open.

**AND IT CAN BE ALMOST THE WHOLE VOLUME.** [HeroQuest II] takes the same shape
to an extreme that changes how the check should be run. Descriptors 16–18, path
tables 19–20, trademark block 21, root directory 22 — all correct — and then
**LBA 23 to 24,294 is 24,272 sectors of zero, 49.7 MB, 95.42 % of the declared
volume**, before the first file at 24,295. All 97 files and all seven directory
extents fit in the 1,109 sectors from 24,295 to 25,403, and the ordinary
32-sector run follows them.

Three discs now have a large zero gap ahead of their files — Prey CD32 (6,000
sectors, 10.0 % of the image), Microcosm (15,000, 5.87 % of the volume) and this
one (24,272, **95.4 %**) — and none of the three is explained. What the third one
adds is a candidate mechanism worth testing on the next: the layout puts every
file the game reads within about 1,100 sectors of the audio tracks, and that
title plays Red Book *while loading*, on a console with one head. That is an
inference from the layout, not a measurement — nothing in the executable says so
— but it is testable. **When you find a front gap, check whether the disc
streams Red Book during play, and where the files sit relative to track 2.**

**AND THE FIRST TEST OF IT IS NEGATIVE.** [Guardian] plays Red Book *while the
game runs* — twelve tracks, played straight out of the disc's own table of
contents, on a console with one head — and it has **no front gap at all**:
descriptors 16–18, path tables 19–20, trademark block 21, root directory 22,
first file at **23**, with its whole 61-file volume in 1,138 sectors. If the gap
were a seek optimisation for Red-Book-during-play, this is the disc that most
needed one and it does not have one. The candidate mechanism is not dead — three
discs still have the gap and nothing explains it — but it is now one negative
down, and the next thing to try is the mastering tool's own input rather than the
title's behaviour.

**AND THE SECOND TEST IS NEGATIVE TOO.** [Banshee] plays Red Book while the
game runs — two tracks, five minutes of them, re-issued by a watchdog every
three seconds — and its volume runs descriptors 16–18, path tables 19–20,
trademark block 21, root 22, **first file at 24**, with no gap anywhere. Two
discs that stream Red Book during play, two discs with no front gap. The
mechanism is now two negatives down and nothing has moved the positive side.

**AND THE THIRD IS THE ONE THAT SHOULD HAVE SETTLED IT IN FAVOUR.**
[Fire & Ice] is **68 % Red Book by sector** — twenty-two tracks, 50 minutes 33
seconds, against a 1,270-sector data track — and it plays them while the game
runs. If any disc on this format had a reason to buy itself a seek advantage by
pushing its files away from the lead-in, it is this one. Its volume runs
descriptors 16–18, path tables 19–20, trademark block 21, root 22, **first file
at 24**, no gap anywhere. **Three negatives, and the three include the two
discs with the most audio in the set.** The seek-optimisation reading should now
be treated as refuted rather than merely unsupported; the three discs that have
the gap need an explanation from the *mastering* side.

**AND THE FOURTH NEGATIVE IS THE MOST AUDIO-HEAVY DISC IN THE SET.**
[Universe] carries **23 Red Book tracks and 40:37 of music against a
2,429-sector data track** — 98.65 % of the sectors it uses are audio, the
highest ratio here — and plays them while the game runs, out of a hand-written
Akiko driver. Descriptors 16–18, path tables 19/20, trademark block 21, root
22–23, **first file at 24**, one unclaimed run in the whole volume and it is
the trailing 232. No gap. Four negatives, and they are the four discs with the
most Red Book in the set.

Two practical consequences, both cheap. A sector map built against the *image*
rather than the declared volume merges the trailing run with the overrun and
reports 259 instead of 32. And a map that reports only the largest run, or only
the run at the end, misses one of the two entirely. **Report every unclaimed run,
with its LBA range and whether it is zero.**

**The volume need not start at LBA 19.** [Prey] The descriptor terminator is
at 18 and the M path table is at **6019**, with **6,000 sectors of zero in
between** — 12,288,000 bytes, 10.0 % of the image. Both other discs put the
path table at 20. 6,000 sectors is exactly 80 seconds of CD frames, which may
mean something and may be a coincidence; the space is zero so there is nothing
to read. **Never assume the file system starts where it usually does; read the
path-table LBAs out of the PVD.** This is also what makes the trademark
pointer in section 2 legible as a pointer.

---

## 2. The `.TM` block — follow the pointer, and read what it points at

**Do this on every CD32 and CDTV disc.** It costs a minute and it is the
highest-yield first move on the format so far.

**And it is not decoration — the disc does not boot without it.** The *Amiga
CD32 Developer Notes* (Commodore, 19 May 1993), chapter 3:

> In order to boot, your title must have the Commodore trademark file right
> after the PVD sectors.

Which names it (**the Commodore trademark *file***, confirming from
Commodore's side what `/CD32.TM` on the Prey master showed), says it is
**required**, and explains the position: right after the volume descriptors.
Sectors 16–18 are the descriptors, 19–20 the path tables, and the block lands
at **21** — the number this section used to be named after. It is a
consequence, not a rule, which is why it moves the moment a volume starts
anywhere but 19. Prey's volume starts at 6019 and its block is at 6021.

**It is not always at sector 21, it is not always 2,048 bytes, and it is not
always a trademark.** All three were true of the first two discs here, which
is why earlier versions of this section were called "Sector 21". [Prey CD32]
puts it at **LBA 6021**, and sector 21 on that disc is entirely zero.
[Prey CDTV] puts **22,152 bytes** at **LBA 48,621**, and what is there is a
device driver. **[Speris] puts 22,152 bytes at LBA 21** — the position this
section was originally named after and the length of the CDTV block, on the
same disc, which is as good an argument as exists for reading both fields
rather than either.

The block is **outside the file system**: no directory record covers it, and a
sector map built from the directory shows it as free space. The only pointer
to it anywhere is in the PVD's **application-use area** (offset 883 onward),
which is normally empty and on all three discs holds the same shape:

```
ISOCD 1.04 (three discs)
offset 883:  00
offset 884:  46 53 00 00        "FS"
offset 888:  54 4D 00 14        "TM", 0x0014 = 20      <- a CONSTANT
offset 892:  00 00 08 00        0x0800 = 2048          <- the block's LENGTH
offset 896:  00 00 00 15        the block's LBA        <- 21, 21, and 6021

Speris (ISOCD 1.04, and the shape is identical — only the numbers differ)
offset 884:  46 53 00 00        "FS"
offset 888:  54 4D 00 14        "TM", 0x0014 = 20      <- the same constant
offset 892:  00 00 56 88        0x5688 = 22,152        <- eleven sectors
offset 896:  00 00 00 15        21

the CDTV Prey master
offset 883:  00
offset 884:  54 4D 00 14        "TM", 0x0014 = 20      <- same constant
offset 888:  00 00 56 88        0x5688 = 22,152        <- eleven sectors
offset 892:  00 00 BD ED        0xBDED = 48,621, and repeated four times
```

**Find the `'TM'` tag; do not assume an offset.** The `'FS'` record before it
is ISOCD's, and the CDTV master omits it, so a parser that reads fixed offsets
gets the wrong longwords. Read the two-byte constant, then the length, then
the LBA.

**Correction 1.** This section used to read the `20` at the constant position
as the path-table LBA, because on Dragonstone and Marvin the L path table is
at 20 and the block at 21. Prey's L path table is at **6020** and the field
still reads **20**; so does the CDTV master's, whose path tables are at
48,633. It is a fixed value and that reading was wrong.

**Correction 2.** A later version of this section said the block is always
"the sector immediately after the L path table". That holds on the three
ISOCD discs (20→21, 20→21, 6020→6021) and **not** on the CDTV master, whose
path tables are at 48,633–48,636 and whose block is at 48,621. **There is no
positional rule. Follow the pointer.**

The first ~1,100 bytes of the sector are ASCII art: `Copyright (c) 1993 -
Commodore Electronics Ltd.`, the Commodore logo drawn in `C`, `/` and `\`, and
a trademark notice.

### Then check what comes after the banner

**[3 of 3]** On all three discs the banner is followed, at offset `0x44C`, by
**876 bytes of unlinked AmigaDOS object file**:

```
0x44C  HUNK_UNIT
0x454  HUNK_NAME       name = 'exec'
0x460  HUNK_CODE       268 bytes
0x574  (2 filler bytes — the blob slips two bytes here, resync on the hunk id)
0x576  HUNK_EXT
        REF32  _intena        at 0x2E, 0x74, 0x98, 0xB4, 0xD4
        REF16  _LVOWait, _LVOSignal, NewList, _LVOCause,
               FindNode, Permit, AddNode
        DEF    AddPort = 0x0    GetMsg  = 0xAC   PutMsg   = 0x22
               FindPort = 0x102 ReplyMsg = 0x10  WaitPort = 0xDA
0x696  HUNK_SYMBOL
        AddPort, pm_call, pm_exit, pm_signal, REMHEAD.033,
        wp_wait, wp_exit, GetMsg, PutMsg, FindPort,
        ENABLE.031, ENABLE.032, ENABLE.034, PutMsg1,
        ReplyMsg, WaitPort
0x7B2  HUNK_END
```

A compilation unit named **`exec`** defining Commodore's own message-port
functions, with its debug symbols intact. `REMHEAD.033` and `ENABLE.031/032/034`
are Commodore's Exec assembler macros expanded by line number. This is a
fragment of the Amiga operating system's own source, compiled, pressed onto a
game disc in 1994, in a sector nothing reads.

### On CD32-era discs: sixteen discs, the same bytes

**All three SHA-1s match, byte for byte, on seventeen of the eighteen CD32-era
discs** — Dragonstone, Marvin, Prey CD32, [Legends], [Liberation], [Microcosm],
[Gloom], [HeroQuest II], [Guardian], [Banshee], [Fire & Ice], [Universe],
[Gunship 2000], [Superfrog] and **[Myth]**:

```
SHA-1  c5ffcef2a5e33d2df606185823cd95d1c174d65f   the whole sector, 2048 bytes
SHA-1  8d84115154d70360b3469acc99cdad3db0ed2c92   banner only, bytes 0x000..0x44C
SHA-1  690aae24a96b69659066e691d0b07db301260572   object file, bytes 0x44C..0x7B8
```

Eleven studios, eleven publishers, eleven engines with nothing in common, and
**thirty-eight months** between Prey's CD32 master (1993-11-29) and Legends'.
Same 2,048 bytes, in a sector nothing on any of them reads.

**AND THE BLOCK DATES THE MASTER THAT CARRIES IT.** Its banner reads
`* Copyright (c) 1993 - Commodore Electronics Ltd. *`, and Prey's `/CD32.TM`
file puts the assembly of this version before 1993-06-10. So **a volume whose
PVD claims a date earlier than 1993 and which carries these bytes is lying about
its date**, and the check costs one `grep`. [Myth] is where that first paid: its
PVD says 1992-12-21 and it carries the 1993 banner, which is the first hard
falsification of that epoch anywhere in this set. The same argument applies
unchanged to [Banshee] and [Marvin], the two other discs stamped 1992-12-21,
because both carry the same block. **When a CD32-era PVD predates mid-1993, read
the trademark banner before believing the date.** [Microcosm],
[Gloom] and [HeroQuest II] carry it and ship **no `.TM` file in their root**,
like Speris and unlike both Prey masters. **[HeroQuest II] also shows that the
block survives the change of tool version**: it was written by ISOCD 1.03 and is
byte-identical to the seven written by 1.04.

**And one CD32-era disc has none of it.** See the correction below before
treating those three hashes as anything more than fifteen sightings of one
widely-copied file. The score is now **sixteen discs with the Commodore banner
and one with the CDTV driver** — which is worth keeping in that form, because
it is the ratio, not the identity, that this section is actually measuring.
(This line read "ten and one" for four discs after it stopped being true. The
count is now re-derived from the disc list at the top of the document rather
than incremented, and the same should be done to it next time.)

### CORRECTION — a CD32 disc carrying `CDTV.TM`

[Speris] is a CD32 disc, mastered with ISOCD 1.04 on **1996-01-10**, and its
`.TM` block is **22,152 bytes of `cdtv.device`**:

```
Nu..cdtv 35.2 (6.2.91)
CDTV Device Driver
Copyright (c) 1990, Commodore-Amiga, Inc.
Created by Carl Sassenrath, Ukiah CA
cdtv.device
dmac.semaphore
```

```
SHA-1  fd3e764e6393974dea05612909e25ddb2124eb8b   all 22,152 bytes
```

That is **byte-for-byte the `/CDTV.TM` of the 1992 CDTV master of Prey**.
Same hash, same length, **three years and five months apart**, on a different
console, from an unrelated studio, through a different mastering tool. There
is no Commodore trademark banner anywhere on the Speris disc.

So this section's previous conclusion —

> What is in that file depends on the console — and the `exec` fragment is
> therefore a **CD32-era** accident.

— **is wrong in its second half.** The `.TM` block is not console-determined.
It is:

> **whatever `.TM` file the person cutting the master handed to the mastering
> tool.** Commodore shipped developers a `.TM` file per console; ISOCD copies
> the bytes it is given into the reserved area and writes the length and LBA
> into the descriptor. It does not know or care which file it got. Binary
> Emotions, cutting a CD32 disc in 1996, gave it the CDTV one — and nothing
> noticed, because nothing on either console reads the block.

Which downgrades the matching CD32 hashes from evidence about the *format* to
evidence about **how widely one particular file circulated**. They are still
worth recording, and a mismatch is still the interesting result: **this is the
first and so far only mismatch, and it took four discs to find; four more have
since matched again.**

Two smaller notes from the same disc. **Speris ships no `.TM` file in its
root** — both Prey masters ship theirs as an ordinary file as well as
embedding it, and this one only embeds it. And the eleven-sector block sits
at LBA 21–31, **ending flush against the root directory at 32**, so on a
compact disc the block can be the largest single unclaimed run in the volume
and still be invisible to a reader that trusts the old 2,048-byte figure. A
tool that dumps one sector at 21 would have got the first 9 % of it and a
plausible-looking result.

### ANSWERED, and by a file: `/CD32.TM`

Prey's CD32 master has the trademark block **twice**: once in the reserved
sector at 6021, and once as an ordinary file in the root of the file system.

```
LBA 6062   2,048 bytes   1993-06-10 14:39:53   /CD32.TM
SHA-1      c5ffcef2a5e33d2df606185823cd95d1c174d65f      — the same sector
```

Nothing on the disc references it. It is not in the boot script, not in either
executable's strings, and no other file names it. It has a real date, five and
a half months before the master, in a directory whose other files are all
either project material or a copied Workbench.

That is a file sitting in the developer's build directory, swept into the ISO
tree because it was there, and also written to the reserved sector because
that is what ISOCD does with it. Which answers the question the hashes could
only narrow:

> **Commodore distributed the trademark block to CD32 developers as a
> 2,048-byte file named `CD32.TM`, and that file already contained the 876
> bytes of `exec` object code with its debug symbols.**

The stale-buffer accident happened **once, at Commodore**, when whoever built
the distribution file concatenated the banner with a buffer that still held a
fragment of the operating system's own build output. Every disc since has
copied that file. Prey is the disc that shipped the file itself.

### ANSWERED: the CDTV block is a different thing entirely

The CDTV release of Prey has the same pointer, the same `'TM'` tag and the
same constant, and there is **no Commodore trademark banner anywhere on the
disc** — zero hits for `Commodore Electronics`, zero for `registered
trademark`, zero for the ASCII-art logo, in a 245 MB image. What the pointer
points at is `/CDTV.TM`, 22,152 bytes, beginning:

```
4E 75 00 00  "cdtv 35.2 (6.2.91)" 0D 0A 00
             "CDTV Device Driver" 00
             "Copyright (c) 1990, Commodore-Amiga, Inc." 00
             "Created by Carl Sassenrath, Ukiah CA" 00
             "cdtv.device" 00 "dmac.semaphore" 00
```

**The CDTV device driver**, by the designer of AmigaOS's Exec kernel, in the
block the format reserves. Note there is **no `$VER:` prefix** on that version
string, so a `$VER:` sweep of the disc never finds it — it was found by
dumping what the pointer pointed at.

Note also that here the PVD points **at the file itself**: same LBA, same
length, no separate reserved copy. ISOCD makes a duplicate; this tool did not
need to.

So the rule generalises and the payload does not:

> **Every CDTV and CD32 disc carries a `.TM` file in its root and a pointer to
> it in the volume descriptor's application-use area. What is in that file
> depends on the console.** On CDTV it is a working device driver. On CD32 it
> is a 2,048-byte trademark banner with 876 bytes of stale `exec` object code
> stuck to the end of it.

Which also dates the `exec` fragment. It is **not** something Commodore has
been pressing onto discs since 1991: it arrived when the shorter **CD32-era**
`.TM` file was assembled, some time before 10 June 1993, replacing a file that
had a real job to do. Whoever built it concatenated the banner with a buffer
that still held part of the operating system's own build output.

**What to do on the next disc**

1. Read the application-use area, **find the `'TM'` tag, and follow the
   pointer**. Do not assume 21, do not assume 2,048 bytes, do not assume an
   `'FS'` record precedes it.
2. **Look for the `.TM` file in the root** and read its date.
3. **Keep recording the three CD32 hashes.** Ten discs across thirty-eight
   months and two ISOCD versions agree, and one carries the CDTV driver instead;
   a mismatch is the interesting result.
4. On a CDTV disc, **record the driver version**. One CDTV disc cannot say
   whether `CDTV.TM` is always `cdtv 35.2 (6.2.91)` or tracks the master date.

`tools/tmsector.py` in
[cd32-prey-doc](https://github.com/vs-sr-dev/cd32-prey-doc) finds the `'TM'`
tag, reads the declared length and LBA, and dumps whatever is there, on both
layouts; the copies in the Dragonstone and Marvin repositories assume sector
21 and 2,048 bytes.

---

## 3. Timestamps — five epochs, and the outliers are the finding

**Sort the directory by timestamp before you read a single file.** It is free
and it has paid on every disc.

ISO 9660 directory records store the year as an offset from 1900. There are
**five epochs to recognise**, not one — this section was called "four" for
longer than the table below had four rows in it:

| Reads | Means |
|---|---|
| 1978-01-01 + mm:ss, or 1978-01-*nn* | AmigaDOS `DateStamp` day zero — an Amiga whose clock was never set. The day number is days of uptime |
| 1980-01-01 or a few weeks after | **MS-DOS `FAT` day zero** — the file came through a PC filesystem, and the day number reads as **uptime** exactly as the AmigaDOS epoch does. [Guardian]'s single outlier is `1980-01-09 23:17:58` — nine days of uptime on a machine keeping PC time with an unset clock |
| a plausible date **one to two years before the master** | **check before you call this a dead clock battery.** It is at least as often an earlier build of the same material, carried forward with its dates intact — see the correction below |
| a plausible real date | a machine whose clock was set; note *which* machine |
| a **specific, self-consistent, impossible** date | [Legends] a clock that was set, and set wrong. Every one of its 118 records reads **1992-03-06**, on a CD32 disc — a console announced in July 1993 — published in 1996. This is neither day zero nor an inherited build: the times inside it are a coherent afternoon in four sittings. **A wrong date is not the same as an unset one, and the times can still be the finding** |

**Then check the PVD's own date against the files it indexes.** [Legends] the
descriptor is stamped `1992-03-06 18:12:02` and **nine files it indexes are
stamped 20:31–20:32 the same day**. ISOCD writes the descriptor from the clock
at mastering time and the file dates from the source file system, and an image
cannot be cut before its contents exist — so on that disc the two fields did
not come from the same clock reading. It costs one comparison and it tells you
whether the two halves of the timestamp evidence can be trusted together.

### The strongest test for a wrong-looking date: ask the file

[Liberation] is the disc that settles how to handle a date that is years too
early, and it settles it **without leaving the disc**. Twelve of its 197
records read **1992-02-05**, two years and two months before the master, on a
title for a console announced in July 1993. One of the twelve is
`/captiveII`, the game executable — and the first string inside that
executable is

```
$VER: Liberation : Ratt V2.02 : Wyvern V2.00c :
(c) 1993 ( The Byte Engineers. ... : Friday 08-Apr-94 09:35:08 )
```

The build system stamps the link time into the version string. The same 245,628
bytes cannot have been linked in April 1994 and written in February 1992, there
is no earlier release for the datestamp to have been inherited from, and a
second file in the same group (`c/playasp`) says `Version 1.7 ( 07-Jul-93 )`.
So the twelve dates are a **wrong clock**, on the machine that copied the last
twelve files into the tree, and the proof cost one `grep` for `$VER:`.

**So the order is: sort by timestamp, notice the outliers, and then read the
outliers' own version strings before doing anything else.** Prey needed a
second release of the same game to settle the same question; Liberation needed
one string. Check the file before you go looking for a control disc.

**AND THE STRING NEED NOT BE A `$VER:` — LOOK FOR A BARE BUILD BANNER.**
[Banshee] has **41 of its 45 records stamped 1992-12-21** on a disc mastered
1994-07-08, and no `$VER:` anywhere in the volume. What settles it is 23 bytes
at file offset 0x50 of the game executable, between an `rts` and the next
routine, with a length byte after it:

```
4E 75  "8/7-94 12:59 CD32 slutp"  14 4E 75
```

**8 July 1994, 12:59** — seventeen minutes before the master, in a file whose
own directory record claims December 1992. Written day/month-year with a dash,
which is the Scandinavian convention, with the Danish word *slut* ("end") in
it; the game's fourth language is Danish and its programmer's name is Danish,
so the banner corroborates three other things on the disc at once. **Grep for a
four-digit year, for `-9x`, and for the program's own nickname, not only for
`$VER:`.**

### And a wrong clock is still a stopwatch

The same disc adds a method that costs one subtraction. Its two clocks are
nineteen months apart, and the *correct* one brackets the wrong one:

```
12:59:00   game executable linked      from the banner inside it
    +0     first file copied           wrong clock reads 1992-12-21 15:11:46
   ...     41 files
 +15:48    last file copied            wrong clock reads          15:27:34
13:13:22   ISOCD writes the first directory record   correct clock
13:16:10   PVD written
```

The real window is **17 min 10 s** and the wrong clock's span is **15 min
48 s**, so the copy fits inside the window with 82 seconds to spare. That check
is worth running whenever a wrong-clock block sits between two trustworthy
stamps: if the span fits, **the wrong clock's *relative* times are a real write
log** and can be read as one — file by file, with the gaps tracking size at
150–200 KB/s and the one gap that does not (Banshee's is 7 min 28 s before the
last file) standing out as a finding. If the span does *not* fit, the block was
not written in that session and you have learned something more interesting.

### The same wrong date, on two unrelated discs, in the same quarter hour

Unresolved, and recorded because the next disc can settle it:

```
Banshee   41 file records            1992-12-21 15:11:46 .. 15:27:34
Marvin    PVD                        1992-12-21 15:15:40
Marvin    all nine directory records 1992-12-21 15:24:31 .. 15:26:43
Myth      the bulk write group       1992-12-21 15:12:38 .. 15:15:31
```

**A THIRD DISC, AND THE FIRST ONE THAT CAN BE PROVEN WRONG FROM INSIDE ITS OWN
IMAGE.** [Myth]'s bulk group falls inside Banshee's window and brackets Marvin's
PVD: three discs, three unrelated publishers, three unrelated studios, one
afternoon.

[Myth] is the hard case, because it is a **1992 game** — its bootblock and its
credit screen both say `1992` — so a 1992 master date looked like it might
simply be correct. It is not, and the disc says so: the `.TM` block it carries
reads `Copyright (c) 1993 - Commodore Electronics Ltd.`, and its loader needs a
68020 and Akiko, neither of which existed in a shipping Commodore console in
December 1992. **A date that happens to match the game's real year is the
hardest one to doubt, and the trademark banner settles it for one `grep`.** All
three of these discs carry that block, so the same argument falsifies all three.

**And the window is where the session STARTS, not where it lives.** [Myth]'s
records run from 15:12:38 to 17:10:58 — nearly two hours — and only the first
three minutes fall inside the shared quarter hour. That is a genuine test of the
stored-base-date hypothesis rather than a restatement of it: a machine that
restores a fixed date at boot and runs forward predicts that the *first* bulk
write clusters and that everything after it does not. Three discs now show a
clustered start. **On the fourth, look for the first bulk write near 15:1x and
let the rest of the session run where it likes.**

Two discs, unrelated studios, unrelated publishers, the same wrong date, and
time-of-day ranges that overlap inside one sixteen-minute window — from the
*source* file system on one disc and from the *mastering* machine on the other.
A dead battery on an Amiga gives 1978, not this.

The shape that would explain it is a machine with **no battery-backed clock at
all**, where AmigaDOS restores the date from the boot volume at every boot and
the time then runs forward: every session starts at the same stored date and
the time of day is a function of uptime alone, exactly as the 1978 and 1980
epochs behave. That would make 1992-12-21 a **sixth epoch — a non-zero stored
base** — and it predicts that other discs prepared on such machines carry other
fixed dates with plausible times of day.

Neither repository can test it. **When a wrong date turns up, record the time
of day as well, and check it against this pair.** (Section 3.)

It also gives the build-versus-master gap directly: linked 1994-04-08
09:35:08, mastered 1994-04-15 09:39:39, **seven days apart** — and the
community dump is named `(1994-04-08)`, after the build rather than the master,
which is worth knowing before you trust a dump's filename as a date.

**CORRECTION — "a machine stuck in 1992" was wrong on one of the two discs it
was claimed for.** This document used to say that Marvin and Prey both had a
build machine with a dead clock battery reporting 1992. Then the **CDTV
release of Prey** turned up, and it was mastered on **1992-09-02**, with its
1,453 files stamped 15:00:53–15:05:26 that afternoon.

The CD32 disc's 1,213-file block is stamped 1992-09-03, 15:01:00–15:05:25 —
the same four-and-a-half-minute bulk copy, the same time of day, one day
later — and **1,201 of those files are byte-identical to the CDTV ones**. The
dates are real. They are the CDTV build session, carried into the CD32 master
fourteen months afterwards with the datestamps intact.

Marvin's 1992-12-21 directories may still be a dead battery; nothing tests
that. **The method is the finding: when a date is one or two years early,
look for an earlier release of the same title before concluding the clock was
wrong. A byte-level diff against that release settles it in one pass.**

Amiga build machines frequently had no set clock, and **1 January 1978 is day
zero of the AmigaDOS `DateStamp`**. A record reading:

```
4E 01 01 00 mm ss 00   =  1978-01-01 00:mm:ss +00:00
```

is not corrupt. It is the time since the build machine was switched on.

**Sort the files by it.** [Dragonstone] Doing so turns the directory into a log
of the mastering session:

```
00:01:09   L1_GSBlk.cru        first level file
00:15:08   Lc_XMemI.cru        all eleven levels written
00:19:43   Lx_ChipI.cru        shared data begins
00:22:36   c/SetPatch          boot commands
00:26:35   s/Startup-Sequence  last file written
```

Twenty-six minutes, the twelve levels taking fourteen of them, and the level
data written *before* the loader and the boot sequence. The hour field is
always 0, the seconds never exceed 59 and the minutes climb monotonically — so
it is a clock, not a counter, and the gaps between files are real pauses in the
build.

**The outliers isolate a subsystem. This has now paid on every disc.**
**[3 of 3]**

* [Dragonstone] Three of 91 files carry genuine 1992 timestamps, from a
  machine whose clock was set, two years and four months before the master —
  and they are exactly the three files that contain the disc's hand-written CD
  driver.
* [Marvin] Two of 212 files carry **1980-03-22**, a date a few weeks past the
  MS-DOS epoch, where the other 210 carry plausible 1994 dates. They are two
  of the three files carrying the older of the disc's **two builds of its
  music player** — a split independently visible by diffing the music files
  against each other, and by the fact that those three are the only ones whose
  extension is capitalised. Three signals, one subsystem, none of them
  requiring a disassembler.
* [Prey] **113 of the 1,225 sound files carry the AmigaDOS 1978 epoch** and
  1,093 of the rest carry one bulk-copy stamp. All 113 are in **one directory
  out of nine** — scenes 68 to 89 — and within it the write order is *not* the
  name order (`S0077C03` between `S0074C01` and `S0074C02`; `S0068C12` alone,
  two days after its neighbours). One block of the soundtrack re-recorded
  chunk by chunk on a machine with no clock.

  **And this one has been checked against an independent source.** Diffing the
  CD32 disc against the CDTV release of the same game: the scene files that
  *differ* inside that directory number **113**, and they are **the same 113
  files**. Two unrelated signals — a timestamp epoch and a byte comparison
  against a disc made a year earlier — pointing at exactly the same set. That
  is as close to confirmation as this method gets, and it is worth doing when
  a second release exists.

  Two honest footnotes from the same comparison: eight further chunks differ
  and are *not* at the 1978 epoch, so content can change without the datestamp
  moving; and one file *is* at the 1978 epoch and is byte-identical to the
  older disc, so a 1978 stamp does not always mean the content changed.

**When the outliers are at the 1978 epoch, sort them and read them as a log.**
The day number is uptime, so several separate sittings show up as several
different "days" of January 1978. [Prey] five sittings across days 10, 20, 24,
26 and 31, each internally monotonic. That is a per-file work log for the one
subsystem that was reworked.

In both cases the split was visible before anything was disassembled. Whether
the outlying *files* were carried forward or merely their datestamps is
unresolved on both discs; it does not matter for the purpose.

**AND THE TWO CLOCKS CAN BE THE OTHER WAY ROUND.** Every disc above has the
*descriptor* readable and some subset of the *files* wrong. [Microcosm] inverts
it exactly: all 34 files carry real, self-consistent 1994 dates, and the
**PVD's own creation date is `1978-01-26 09:30:04`** — day 26 of the AmigaDOS
epoch, twenty-five days of uptime on a machine whose clock had never been set —
with the root directory record at `1978-01-01 00:00:00`, hour, minute and second
all zero.

The consequence is worth stating as a rule, because it is the opposite of the
advice above: **on that disc the file dates are the trustworthy half and the
descriptor is the impossible one.** A master cannot be dated from its PVD there
at all; the only bound is the newest file. Check both fields against each other
in both directions before deciding which one to believe, and note that an
epoch-zero PVD is *self-identifying* in a way a merely wrong one is not — you
do not need a control disc to know 1978 is not real.

Sorted, [Microcosm]'s 34 records give the whole master in three sittings: the
five-byte boot script on 1994-01-23, the **483 MB video file alone** on
1994-02-04 at 14:22:59 with nothing else within seventy-four minutes of it, and
then **the entire game — one executable and 32 overlays, 9.5 MB — copied in 66
seconds** between 02:44:58 and 02:46:04 on 1994-02-09. The per-file gaps track
the file sizes at roughly 150–200 KB/s, which identifies the source as a hard
disk. And the sequence has **no pause where the missing `eolb4` would sit**,
which is how you tell "cut before the master" from "never built": the file that
the loader still names was not built and dropped, it never existed.

**Where the real dates live is itself informative.** Marvin is the inverse of
Dragonstone, and Prey has both patterns at once — 1,213 files on a wrong
clock, 78 system files at one identical second (`1993-09-22 12:19:26`, a
Workbench directory copied wholesale), 131 at the 1978 epoch, and only 43
genuine dates, which are the whole development log. Marvin: its **files** carry genuine dates spread over seven months of
development (2 May to 23 November 1994) and its **directories** — the records
ISOCD creates itself — all carry 1992-12-21, the mastering machine's own
wrong clock. So

* file dates → the development log,
* directory dates and the PVD creation date → the mastering session.

Sorted, Marvin's file dates give the whole schedule: first surviving asset in
May, the publisher's logo animation in August, the easter egg at three in the
morning on 17 November, all 61 levels batch-exported in 26 seconds on
21 November, `work` rebuilt on the 23rd, and one single level rebuilt four
minutes after it — the last write on the disc.

One anomaly worth watching for: on Marvin all nine directories are stamped
within three minutes of each other **except** `/mlevs`, four hours later, and
`/mlevs` is also the only directory whose extent needs two logical blocks.
Unexplained.

Note also that the **on-disc order is not the write order**. Files are laid out
alphabetically within each directory, so the shared files written last sit at
the lowest LBAs.

**AND A DISC MAY SIMPLY HAVE NOTHING TO SAY.** [Gloom] is the first disc here
where every record — all 138 of them and the PVD — carries one real, ordinary
date: **1995-06-28, between 17:03:41 and 18:06:57**, GMT offset 0. No 1978
epoch, no 1980 epoch, no clock years out, no impossible date. The sort is still
worth doing, because it is free and because *this* disc's answer is itself
informative: the file dates are a copy operation, not a development log, so the
disc offers no schedule and no subsystem split, and the only thing it dates is
the mastering session. Sorted, that session is 128 files copied in **seventeen
seconds** at 17:17:46–17:18:03, the boot script five minutes later, the game
executable alone at 18:06:22, and the master **35 seconds after it**. Record
"nothing to see" as a result rather than as a failed check, and note the two
files that *are* outliers even on such a disc — on Gloom, `freeanim` and the
boot script's icon, copied fourteen minutes before everything else, are the two
files on the disc that have nothing to do with the game.

**AND A THIRD KIND: ONE FILE FROM A DIFFERENT MACHINE, AND IT IS THE PROGRAM.**
[Guardian] stamps **60 of its 61 files and all six directory records inside one
seven-second window** (1994-08-03 11:36:39–46) — a single bulk copy, in directory
order, on a correctly-set clock. The 61st is `/game`, the executable itself, at
**`1980-01-09 23:17:58`**: the MS-DOS epoch, day 9. Every asset came off one
machine in seven seconds and the program came from somewhere else.

That is the outlier rule at its cleanest — one record out of 67, and it isolates
the one thing on the disc that is actually the product — and it is worth doing
even on a disc whose dates are obviously a single copy operation, because seven
seconds of uniformity is exactly what makes the one exception visible. It also
gives the tightest master gap in the set: root directory record `1994-08-04
14:25:19`, PVD `14:26:37`, **one minute and eighteen seconds**, against eleven
minutes on Prey and eleven and a half on HeroQuest II. A short gap says the
master was cut on top of a tree that had already been assembled and checked; a
long one says the build was still moving.

**AND A SECOND DISC WITH NOTHING TO SAY, WHICH IS WHAT MAKES IT A CATEGORY.**
[HeroQuest II] is the second: all 105 records and the PVD carry real,
self-consistent 1994 dates, GMT offset 0, no epoch and no impossible value. Two
of ten discs now answer "nothing", which is worth recording as a rate rather
than as a curiosity. And on this one the sort still pays, because the file dates
are a *copy* log rather than a development log and the copy log has a shape:
92 of the 97 files and five of the seven directory records in one **six-minute**
session on 1994-06-02, ordered by directory; then `/loaderblackpal` alone twelve
minutes later; then `/C/setpatch` five minutes after that; then three files on
three later days. **The three `C:` commands were fetched one at a time as the
boot script grew** — `Stack` in the middle of the root files, `Assign` at the
end of the session, `setpatch` seventeen minutes after everything else — which
is the same story Legends' four-second `c/` gap tells and is visible on any disc
for the price of the sort.

**Compare the PVD creation date with the newest file.** [Prey] the last file
written was the title screen at 21:03:54 on 1993-11-29 and the PVD says
21:15:11 — **eleven minutes and seventeen seconds** between the last asset and
the master. The two executables were linked the previous evening, twelve
minutes apart. That single subtraction dates the end of the project to the
minute, and on this disc it also explains a leftover: the executable still
names a CDXL animation for the publisher's logo, and what shipped in its place
is a still image finished eleven minutes before the master (section 4).

**And the same subtraction on a second disc gives almost the same number.**
[HeroQuest II]'s game executable is stamped `1994-06-15 17:22:39`, six seconds
after the root directory record, and its PVD `1994-06-15 17:34:13` — **eleven
minutes and thirty-four seconds**. Two discs, two studios, a year apart, and on
both the last thing written before the master is the program. Worth doing on
every disc: it is one subtraction and it says whether the master was cut on top
of a finished build or on top of a still-moving one.

---

## 4. The boot chain

Kickstart mounts the volume and runs `s/Startup-Sequence` as a shell script.
It runs from **one line to twenty-two** across the discs here, and the length
says nothing about the game: the two-line extremes are a 483 MB streaming FMV
title and a floppy port.

A typical CD32 game's is three or four lines:

```
c:setpatch quiet          ROM patches, data cache, cd.device fixes
c:noopenwb >nil:          suppress the Workbench screen
c:<something> >nil:       game- or publisher-specific
<Game>.exe                the actual first stage
```

Marvin's is four lines and does the same work differently:

```
c/setpatch quiet
c/cdgsxl 21st.cdxl blit nopointer multipal xlspeed=150 fireabort x=80 y=60 patchopenwb NOXLEEC
work
c/ColdReboot
```

**[Microcosm]'s is one line and five bytes, and it is the floor for the
format:**

```
cosm
```

No `SetPatch`, no `NoOpenWB`, no redirection, no publisher stub, and no `c/`,
`libs/` or `devs/` directory anywhere on the disc — one directory holding one
file. That is possible because the executable does everything itself, and the
mechanism is worth taking away from this disc (see "`fl_Key` is the file's LBA"
below). **If a boot script does nothing, the interesting code is all in the
first stage; do not read a short script as a simple disc.**

**A fifth shape, and it is the one that pays: a `c/` that exists and three
`Assign`s of floppy volume names.** [HeroQuest II]'s is 208 bytes and seven
non-blank lines:

```
C:setpatch >nil:

LOADERBLACKPAL

C:STACK 8192

C:ASSIGN >NIL: "Legacy of Sorasil DISK 1:" "cd0:"
C:ASSIGN >NIL: "Legacy of Sorasil DISK 2:" "cd0:"
C:ASSIGN >NIL: "Legacy of Sorasil DISK 3:" "cd0:"

QuestII 2
```

Three things to take from it. **The `Assign` lines name the floppy release
outright** and the loader then addresses all 91 of its data files through those
volume names (step 15) — Speris' `speris-1:` … `speris-4:` idiom, a second
sighting, and on this disc it reconstructs a complete three-floppy layout in one
string search. **`C:STACK 8192`** is the only sighting of that command on the
format and it is why `Stack` is in `c/` at all. And **the game is launched with
an argument** (`QuestII 2`) that nothing in the executable visibly parses —
worth grepping for `ReadArgs` before assuming a bare command line is bare.

The second line runs a command in the **root** rather than in `c/`, which is
Gloom's shape on a disc that has a `c/` as well: **list the root even when `c/`
exists.**

**A sixth shape is the fourth one again, and the repeat is what makes the `.bak`
rule.** [Guardian]'s is 35 bytes and three lines, with both commands in the
**root** and no `c/`, `libs/` or `devs/` anywhere:

```
setpatch >nil:
freeanim
game m1 f
```

and beside it, pressed, `s/startup-sequence.bak`, 33 bytes:

```
setpatch >nil:
freeanim
sw m1 f
```

**The previous boot script, kept, and it names a different program.** `sw` is not
on the disc — and it *is* the name of the executable on that title's own A1200
floppy release. Two discs now ship a `.bak` beside the boot script ([Gloom] and
this one) and **both times it named the ancestor**, so the check has gone from a
curiosity to a rule: **look for a `.bak` beside the boot script, and read the
line that changed.**

Two smaller things from the same script. The game is launched with **two
arguments** (`m1 f`) and, unlike HeroQuest II's `QuestII 2`, this executable
really does parse them — a hand-written scanner in the first 72 bytes of the code
hunk that folds case with `andi.w #$5f` and dispatches on `F`, `Q`, `P` and
`M<digit>`, of which the shipped script uses two and nothing on the disc ever
passes the other two. **Grep for `ReadArgs`, and if there is none, look at the
program's entry point anyway**: a bare `cmp.b #'X',d0` chain is what an assembler
programmer writes instead.

**A SEVENTH SHAPE, AND IT IS THE ONE THAT SHOULD HAVE BEEN TAKEN OUT.**
[Banshee]'s is 230 bytes and twelve lines, and lines 2 to 6 are a **live
developer branch**:

```
c:Setpatch quiet
c:assign >NIL: DebugDisk: exists
if not warn
   c:assign t: ram:
   c:execute DebugDisk:debugscript
endif
;
C:assign banshee1: CD0:
C:assign banshee2: CD0:
C:assign banshee3: CD0:
C:assign banshee4: CD0:
bans.exe
```

`assign >NIL: DebugDisk: exists` is the AmigaDOS idiom for "does this assign
exist"; `if not warn` is true when it does. So on a machine with a volume or
partition assigned `DebugDisk:`, the **retail** boot script gives itself a
writable `T:` and **executes a script off that volume** before the game starts.
On a console the branch never fires and nobody noticed.

The strings `DebugDisk` and `debugscript` occur once each in the whole volume,
in this file, and the game executable contains neither. That is why it
survived: **it is not in the program**, so nothing about building, crunching or
linking the program would have removed it. **Read the boot script as a
program, not as a launcher** — three discs here now have something in it that
is not about launching the game (Liberation's RAM disk, Prey's `assign env:`,
this).

The `assign bansheeN: CD0:` lines are the third sighting of the floppy-volume
idiom (Speris, HeroQuest II, this), and the loader's own file table carries a
**disk number byte** beside every path, so the four-floppy layout comes out
whole — including the detail that makes it real: **level 3's two halves are on
different disks**, which is what happens when a level does not fit on one
880 KB floppy and is not something anyone would invent for a CD.

**And there is a fourth shape: no `c/` directory, but the commands in the root.**
[Gloom]'s is three lines —

```
freeanim >nil:
setpatch >nil:
gloom >nil:
```

— and `freeanim` and `setpatch` are ordinary files in the volume root, which
Kickstart's `C:` assign finds on a booted CD32 volume. **Do not conclude from
"there is no `c/`" that no AmigaDOS commands ship; list the root.** The same
disc also ships `s/startup-sequence.bak`, 31 bytes, which is the *previous*
release's boot script (`setpatch quiet` / `run >nil: gloom`) kept as a backup
file and pressed — the cheapest single piece of evidence on that disc that the
CD32 build is the floppy build. **Look for a `.bak` beside the boot script.**

Prey's is three lines and shorter than either:

```
prey:c/setpatch >nil:
prey:c/assign env: ram:
prey:moreno/Prey
```

— no `noopenwb` and no reboot, because the game never takes the machine; it
runs inside Intuition with AmigaDOS alive underneath it. It addresses the
volume by name (`prey:`) rather than through the `C:` assign, and
**`assign env: ram:`** is a line written by somebody who watched the game fail
on a read-only volume: `ENV:` has to be writable and a CD is not.

Back to Marvin's: no `noopenwb`, because the CDXL player's own `patchopenwb`
option suppresses the Workbench screen, and **a fourth line that reboots the
machine**. A game that has taken the hardware apart cannot hand it back, so
the boot script resets it. `c/ColdReboot` is twenty bytes of code and one
relocation:

```
21fc 0000000a 0080   move.l  #reboot,$80.w     ; the TRAP #0 vector
4e40                 trap    #0                ; -> supervisor mode
reboot:
41f8 0002            lea     $0002.w,a0
4e70                 reset
4ed0                 jmp     (a0)
```

**Look for a second entry point.** If the root holds `<Game>.info` with
`DefaultTool = IconX` and a sibling script with the same name, the disc is
also meant to be double-clicked on an A1200 or A4000 desktop, and the script
is the boot sequence minus SetPatch and the reboot. [Marvin] `IconX` version
38.8 (13.2.92) is in `c/` for exactly that. [Liberation] `/The Game.info` has
`DefaultTool = SYS:c/iconx` — the *system* copy — and the disc ships no
`IconX`, so the icon only works on a machine that already has one. **Read the
`DefaultTool` path, not just the presence of the icon**: `SYS:` means the
entry point is for a hard-disk user and cannot work on the console.

**A boot script can mount a device, and one of them does.** [Liberation]'s is
twenty-two non-blank lines and the middle of it is

```
CaptiveII:c/mount >NIL: RRD: from CaptiveII:DEVS/Mountlist
IF NOT EXISTS "RRD:s"
C:makedir >NIL: rrd:s
C:copy >NIL: captiveII:s/startup-sequence2 rrd:s/startup-sequence
C:copy >NIL: captiveII:c/WARNING RRD:
ENDIF
C:relabel >NIL: rrd: Ram_Reset
```

with `Devs/Mountlist` describing `ramdrive.device` — the **recoverable** RAM
disk, twelve cylinders of 264 blocks, 132 KB — and `s/Startup-sequence2`
containing one line, `rrd:WARNING`. The disc builds itself a bootable RAM disk
that survives a warm reset and outranks the CD at boot, so a reset boots a
warning program instead of the game. **If you see a `Devs/` directory on a
CD32 disc, read the mountlist**: it is the only place a title can put state
that survives a reset without `nonvolatile.library`.

**Diff the `c/` directory against the boot script.** [Marvin] `c/SpeedyCD`
switches the CD32 drive to double speed and prints
`Read commands are at maximum speed` — and nothing on the disc runs it. It
is a development tool that shipped.

**Read the `c/` directory as a dating tool.** [Prey CDTV] `ASK`, `NEWCLI`,
`ENDCLI`, `FF`, `LAB`, `RESIDENT`, `SETENV`, plus `L/DISK-VALIDATOR`,
`L/NEWCON-HANDLER`, `L/SPEAK-HANDLER` and `LIBS/INFO.LIBRARY` — that is a
**Workbench 1.3** system, which is what a CDTV runs. [Prey CD32] the same
project's next release ships Workbench 3.1. The `c/` directory tells you which
Kickstart the disc was built against before you look at a single executable.

**And be prepared for the whole of Workbench.** [Prey] `c/` holds **59
commands** — `Ed`, `Edit`, `Install`, `Mount`, `MagTape`, `RemRAD`,
`UpdateWBFiles`, `ExtractKickstart` — of which the boot script runs **two**.
78 files across `c/`, `l/`, `libs/` and `devs/` carry the identical timestamp
`1993-09-22 12:19:26`, so a Workbench system directory was copied wholesale
and nobody looked at what was in it. One of the things in it is
**`c/Prod_Prep`**, `$VER: prod_prep 39.1 (22.12.92)`, Commodore's factory
tool for partitioning, RDB-writing and low-level formatting a SCSI hard
drive — on a retail game disc, in the directory Kickstart assigns to `C:`.
`c/joymouse` is *"JoyMouse ... Copyright 1990 by Jonathan Potter"*, a
joystick-to-pointer handler, also unused.

[Prey CDTV] does the same thing a generation earlier and worse: **`c/WACK`**,
35,336 bytes, is *"Wack Version 1.0"* — Commodore's low-level debugger, with
breakpoints, single-stepping, disassembly, `tasks`, `symbols` and a serial
console. And **`c/BOOKIT`** says of itself:

```
Written by Leo L. Schwab.  Designed by Sassenrath/Reichart/Ware.
Copyright 1991, Silent Software, Inc.
Part of the CDTV Survival Kit.
*** This program may NOT be freely distributed ***
```

— on a pressed retail disc, and it *is* used, from the boot script. So the
same studio shipped a piece of Commodore's internal tooling on both of its
masters, a different one each time. **Read the usage text of every command in
`c/` that is not a Workbench one you recognise.**

**Read the `$VER:` string in every `c/` command.** They date the tools and say
whether the command is Commodore's or the studio's:

```
$VER: setpatch 40.14 (7.10.93)     Commodore, the Kickstart 3.1 release   [Dragonstone]
$VER: setpatch 40.12 (16.9.93)     Commodore, another 3.1 SetPatch        [Prey]
$VER: setpatch 39.6  (8.9.92)      Commodore, the Kickstart 3.0 release   [Marvin]
$VER: noopenwb 37.1  (3.11.93)     not Commodore's                        [Dragonstone]
$VER: iconx    38.8  (13.2.92)     Commodore, Workbench 2.x               [Marvin]
$VER: prod_prep 39.1 (22.12.92)  Commodore's factory HD formatter         [Prey]
$VER: cdgsxl   1.48  (24.9.93)   Wayne D. Lutz    third-party CDXL player [Prey]
$VER: cdgsxl   1.51  (16.12.93)  Wayne D. Lutz    third-party CDXL player [Marvin]
$VER: setpatch 39.6  (8.9.92)      Commodore 3.0 — the identical binary    [Legends]
$VER: assign   37.4  (25.4.91)     Commodore, Workbench 2.04               [Legends]
$VER: setpatch 40.3  (10.5.93)     Commodore, a fifth version              [Gloom]
$VER: setpatch 40.3  (10.5.93)     the identical binary                    [Guardian]
```

The SetPatch version is not the machine's: Marvin ships a 3.0-era SetPatch
and runs it on a CD32's 3.1 ROM. Six discs, five versions (39.6, 40.3, 40.12,
40.14, 40.16), no agreement.

**And hash the binary, not only the version string.** [Legends] `c/SetPatch`
is **byte for byte Marvin's** — SHA-1
`4d4aae988310b07726329e436b2250c0f769ddff`, 7,364 bytes — across two studios,
two publishers and two years. **[Gloom]'s `/freeanim` is byte for byte
[Liberation]'s `/c/FreeAnim`** — SHA-1
`449c610071ace58d8c7877aafd114588b8aa7074`, 3,492 bytes, another two studios and
another two publishers. Like the `.TM` block, Commodore-era developer files
circulated as single copies and studios passed them around; a matching hash
tells you which copy a studio had, and a *mismatching* one at the same version
would be the interesting result. **Hash everything in `c/` — and everything in
the root, on a disc that has no `c/`.**

**Read `c/` for age, not just for content.** [Legends] ships `assign` 37.4
from **April 1991** next to a `setpatch` from September 1992 on a disc
mastered in 1996, and its `c/` timestamps say the two were copied off a
Workbench disk four seconds apart. Whoever assembled `c/` used whatever was to
hand, and the spread between the oldest and newest command in it is a rough
lower bound on how long the studio had been reusing the same build machine.

**When the same third-party tool turns up twice, diff the versions.**
`cdgsxl` is on two of three discs and the difference between 1.48 and 1.51 is
exactly two entries in its `ReadArgs` template: 1.51 adds `PATCHOPENWB/S` and
`NOLOWPASS/S`. That is a free changelog for a piece of CD32 software with no
other documentation, and it explains why the older disc has to deal with the
Workbench screen differently.

`SetPatch`'s string table also names every patch it can install, and a CD32
title ships it partly for the `cd.device` ones — `Drive Firmware Patch`,
`CDPatch Interrupt`, `cd CD_SEEK`.

**AND THE HASHES PAY AGAIN, TWICE, ON ONE DISC.** [HeroQuest II] ships three
commands and two of them are copies already in this series:

```
SHA-1  5fa6e23089c82e7292073fecebaab8b6ed03ad49  12,968 B  c/setpatch 40.12 (16.9.93)
       == [Liberation]  (Byte Engineers / Mindscape, April 1994)
       == [Prey CD32]   (KirkMoreno / Almathera, November 1993)
       == [HeroQuest II] (Gremlin, June 1994)              -- THREE discs

SHA-1  b5b7edb67f578019d46af425a16458ec0cdb1c2e   3,220 B  c/Assign 37.4 (25.4.91)
       == [Prey CD32], [Speris], [Legends], [Liberation], [HeroQuest II]
                                                           -- FIVE discs
```

So the list of Commodore-era files shown to circulate as single copies is now
four, and two of them travel much more widely than the `.TM` block's eight
sightings suggested was normal:

| File | Discs | Span |
|---|---:|---|
| the `.TM` block | **11** | 1993–1996 |
| `c/Assign` 37.4 | **6** | 1993–1996, six studios, six publishers — Prey CD32, Speris, Legends, Liberation, HeroQuest II, **Banshee** |
| `c/setpatch` 40.12 | **3** | 1993–1994, three studios, three publishers |
| **`setpatch` 40.3** | **2 discs + 1 floppy** | [Guardian] (CD32, Aug 1994), [Guardian] (A1200 floppy) and [Gloom] (June 1995) — SHA-1 `8b6cf0011d6a55754c8b762eec1e808576e6c246`, 10,964 B |
| `c/SetPatch` 39.6 | 2 | Marvin, Legends |
| **`c/SetPatch` 40.14** | **5** | [Dragonstone], [Banshee], [Fire & Ice], **[Universe] and [Gunship 2000]** — 13,200 B, SHA-1 `00d74a35300f7009ed02bc47db88427e9e0fc0a5`. **CORRECTION: this row used to read "the only same-label pair in the table"**, because the first two are both Core Design. Fire & Ice is Graftgold, published by Renegade, and carries the same 13,200 bytes — so the pair was a coincidence of sample size and the row now spans two studios and two labels, like the others. **SECOND CORRECTION, from [Gunship 2000]:** the row is now **five** discs — four studios, five labels, two countries — and it includes both `D J Pocock` and non-Pocock masters. A 13,200-byte `SetPatch` means "somebody installed Workbench 3.1" and nothing narrower. Note also that Gunship's other ten `c/` commands are all **37.x** (Workbench 2.0): a 3.1 `SetPatch` dropped into an otherwise 2.0 `C:` directory, which is worth recording separately from the `SetPatch` hash |
| `freeanim` (3,492 B) | 2 | Liberation, Gloom |
| **`s/startup-sequence.info`** | **2** | [Guardian] and [Gloom] — SHA-1 `6bb943b7dac227070ce10d44f82a9ed85f51a74e`, 396 B, and it is **not** a Commodore file (below) |

A command dated April 1991 shipping unchanged on six CD32 discs across three
years is not a surprise on its own; **six byte-identical copies is a
measurement of how the format's tooling was actually distributed, and it costs
one `sha1sum` per file.** Hash everything in `c/` and everything in the root,
and keep the table.

**CORRECTION — A MATCHING `SetPatch` IS NOT EVIDENCE OF A SHARED SHELF, AND
THE CONTROL FOR THAT IS ALREADY IN THIS TABLE.** [Banshee] and [Dragonstone]
are the same publisher and their `SetPatch` is byte-identical, which looked
like the strongest studio-level evidence this document could hope for. Laid out
in full it is not evidence of anything:

| SHA-1 | Bytes | `$VER:` | Discs |
|---|---:|---|---|
| `00d74a35…` | 13,200 | `setpatch 40.14 (7.10.93)` | Dragonstone, Banshee — **same label** |
| `5fa6e230…` | 12,968 | `setpatch 40.12 (16.9.93)` | Prey CD32, Liberation, HeroQuest II |
| `8b6cf001…` | 10,964 | `setpatch 40.3 (10.5.93)` | Guardian, Gloom |
| `4d4aae98…` | 7,364 | `setpatch 39.6 (8.9.92)` | Marvin, Legends |
| `568db17c…` | 13,484 | `setpatch 40.16 (14.2.94)` | Speris |
| `7b42c0b6…` | 5,088 | `SetPatch 1.34 (12-May-89)` | Prey CDTV |

Eleven discs, six binaries, and **a matching hash always means a matching
`$VER:` and never means anything else**. Four of the six binaries are shared by
two or more discs and **only one of those four groups is same-label** — the
other three pair unrelated studios and unrelated publishers. So the prior
probability that a `SetPatch` match indicates a shared build kit is about one
in four, which is to say the match is real and carries no information. What it
identifies is **which Kickstart release was on the build machine**, and in
1993–94 there were five in circulation.

**Record the version, not the hash — and if the hash ever differs at the same
version, that is the finding.**

**AND HASH THE `.info` FILES TOO, BECAUSE THE SHARED FILE NEED NOT BE
COMMODORE'S.** [Guardian] and [Gloom] ship the identical 396-byte
`s/startup-sequence.info` — a Workbench **project** icon on the boot script whose
`DefaultTool` is **`blitz2:blitz2`**. Two studios ten months and two publishers
apart, and the file is not a Commodore developer file at all: it is the icon a
**Blitz Basic 2** installation attaches to a project. Gloom's credits screen says
`UTILITIES CODED IN BLITZ BASIC 2` and confirms it from the other side; Guardian
has no credits screen, so on that disc the icon is the *only* evidence Blitz was
in the build chain.

So the unit of shared practice is wider than "Commodore-era developer files": it
is **anything a common tool drops into a build directory**, and an `.info` is
exactly that. Four bytes of `sha1sum` per icon, and it identified a development
tool on a disc that names none.

**And a command with no `$VER:` is still identifiable.** [HeroQuest II]'s
`c/Stack` is 872 bytes with no version string and no match in any other
repository here; its four error messages (`bad argument for STACK`,
`current stack size is %n bytes`, `Suggested stack size too small` / `too
large`) are Commodore's wording, so it is a Commodore `Stack` from a release
early enough not to carry one. **Read the error messages when the `$VER:` is
missing.**

### The five CD32 modules, named by Commodore

Everything the console adds to a stock Amiga is five things, and the *Amiga
CD32 Developer Notes* (19 May 1993) list them:

> Five special system modules were created for the AmigaCD32 console:
> `lowlevel.library`, `nonvolatile.library`, `freeanim.library`, `cd.device`,
> CD-ROM file system

with the distribution rule that explains what you find on a disc:

> The `lowlevel.library`, `nonvolatile.library` and the CD-ROM file system
> will be part of Workbench 3.1 […] The `freeanim.library` will **not** be
> included with the normal Workbench distribution.

So:

| Module | Expect to find it |
|---|---|
| `lowlevel.library` | **in `libs/` on the disc** — pre-3.1 machines have no copy |
| `nonvolatile.library` | **in `libs/` on the disc**, same reason |
| `freeanim.library` | **never on a disc** — ROM only, and no Workbench copy exists |
| `cd.device` | never on a disc — ROM |
| CD-ROM file system | never on a disc |

[Speris] ships exactly two libraries and they are exactly the first two. That
is not a choice about this game; it is the documented shape of a CD32 title,
and **a `libs/` holding anything else is worth a second look** — [Marvin]'s
ships eight and opens five.

**Which also means the CD32-specific surface of any title is small and
enumerable.** Grep for those five names, and whatever else the disc opens is
a stock Amiga library. It is the fastest way to separate "this is a CD32
game" from "this is an Amiga game on a CD32", and on [Speris] it takes one
grep: `lowlevel`, `nonvolatile` and `freeanim` present, `cd.device` used once
by a 384-byte boot command, Akiko untouched.

**`freeanim.library` — ANSWERED by Commodore's own documentation, and every
observation below turns out to be the documented idiom.** **[4 of 4]** It is
on no disc, because it is resident in the CD32 ROM.

The *Amiga CD32 Developer Notes* (Commodore, 19 May 1993, confidential at the
time), chapter 3, "Startup Environment":

> While the system is loading a title into memory, there is a small animation
> playing on the screen. […] Your application can control this animation with
> a special AmigaCD32 library, the `freeanim.library`.
>
> `FreeAnimBase = OpenLibrary("freeanim.library", 0);`
>
> This will tell the startup animation to begin shutting down, which involves
> removing itself from the display and freeing the resources it uses. This may
> take a while, up to about a second. While the startup animation is shutting
> down, your application can prepare data to display and generally initialize
> itself.
>
> `CloseLibrary(FreeAnimBase);`
>
> This will wait for the animation to complete its shutdown.

So the reading this document arrived at from six sightings is right, and
sharper than it guessed: **the open starts the shutdown and the close waits
for it**, and the gap between them is deliberate parallelism. That is why the
call never appears — there is no call. Opening and closing *is* the whole
interface.

Two more things the notes explain outright:

**Why nobody error-checks it.** The notes tell developers not to:

> users may try to run your code on a regular Amiga computer equipped with
> CD-ROM […] there will not be a `freeanim.library` around, so your code
> should not fail when `freeanim.library` cannot be opened. This is easy to
> do, just don't put any error checking in […] `CloseLibrary()` accepts a
> NULL pointer and ignores it.

and they print the one-liner `CloseLibrary(OpenLibrary("freeanim.library",
0));` for programs with nothing to do in between. **[Speris]** `c/FreeAnim` is
92 bytes and is exactly that, with a `tst.l d0` the notes say you can omit.

**Why it is always opened first.** The notes require the title not to take
over the display until the animation has gone, and warn that the animation
may start using `audio.device` in a future ROM. Opening it first, before
`dos.library`, is the documented order of operations — which is what
[Marvin] and [Prey] do.

The empirical sightings, kept because they are what the disc shows:

* [Dragonstone] `c/FreeAnim`, a SAS/C 6 program that opens `dos.library`,
  `intuition.library` and `freeanim.library`, run after Workbench is
  suppressed and immediately before the game takes the machine.
* [Marvin] the game executable itself opens it, and **opens it first, before
  `dos.library`**. In 176 KB of code the only other reference to its base is
  `CloseLibrary` at shutdown. **It is opened and never called.** The
  third-party `c/cdgsxl` opens it too.
* [Prey] the **first stage opens it, and names it first**, before
  `dos.library`. `c/freeanim` is on the disc as well and the boot script does
  **not** run it. `MORENO/cdgsxl` 1.48 opens it too.

* [Speris] `c/FreeAnim`, 92 bytes, run by the boot script immediately before
  the game. `libs/` holds only `lowlevel.library` and `nonvolatile.library`.

* **[HeroQuest II] wraps the pair in a 228-byte program that also blanks the
  palette — and ships it with its symbol table intact.** `/loaderblackpal`, in
  the volume root, is one chip CODE hunk, 11 relocations and **13
  `HUNK_SYMBOL` entries**, which is the only symbol table on that disc:

  ```
  START:  movea.l 4.w,a6
          lea     FREEANIMNAME,a1        ; 'freeanim.library'
          moveq   #0,d0
          jsr     -552(a6)               ; OpenLibrary -- NOT OldOpenLibrary
          move.l  d0,FABASE
          bsr     OPENLIBRARIES          ; dos, graphics, lowlevel
          movea.l 4.w,a6
          movea.l FABASE,a1
          jsr     -414(a6)               ; CloseLibrary
          movea.l MYGFXBASE,a6
          suba.l  a1,a1
          jsr     -222(a6)               ; LoadView(NULL)
          bsr     BLACKCOLOURS           ; 32 colour registers to zero
          moveq   #0,d0
          rts
  ```

  Opened **first**, closed after three further `OpenLibrary` calls, with no test
  of the result — the documented idiom, with a gap that is small but not empty.
  Two of its thirteen symbols, **`BLUEBITS` and `GREENBITS`, both have the value
  of `START`**, in a program with no blue or green code in it: labels left behind
  by a per-channel fade that was deleted. And `BLACKCOLOURS` writing exactly
  **32** registers is that disc's own statement of its colour depth, which is
  worth more than any palette file (section 7).

* **[Gloom] ships the same 3,492 bytes as Liberation, and they are byte for
  byte identical.** `/freeanim` on the 1995 Black Magic / Guildhall disc has
  SHA-1 `449c610071ace58d8c7877aafd114588b8aa7074`, which is `/c/FreeAnim` on
  the 1994 Byte Engineers / Mindscape disc. Two studios, two publishers,
  fourteen months, the same file. **This is the third Commodore-era developer
  file shown to circulate as a single copy**, after the `.TM` block (seven
  discs) and `SetPatch` 39.6 (two) — so hash `freeanim` as well, and the
  `/auto/close/wait` template is now a **fourth** sighting rather than a third.

* **[Liberation] ships two of them and runs the bigger one.** `c/FreeAnim`,
  3,492 bytes, is a SAS/C 6 program (`HEADDBGV01`, `main.c`, `_main`) whose
  `ReadArgs` template is **`/auto/close/wait`** — the *third* sighting of that
  exact string, after Prey's `c/freeanim` and `cdgsxl` 1.48, so it is one
  wrapper circulating between studios rather than three people writing the
  same thing. Beside it, **run by nothing and named by nothing**, sits
  `c/CloseAnim`, 120 bytes, 48 of them code, no relocations, with its two
  symbols intact:

  ```
          lea     name(pc),a0        HUNK_SYMBOL:  AL = 0x1C
          moveq   #0,d0                            Panic = 0x1A
          movea.l 4.w,a6
          jsr     -552(a6)        ; OpenLibrary
          tst.l   d0
          beq.s   Panic
          movea.l d0,a1
          jsr     -414(a6)        ; CloseLibrary
  Panic:  moveq   #0,d0
          rts
  name:   dc.b 'freeanim.library',0
  ```

  That is Commodore's documented one-liner, hand-written, **with the `tst.l d0`
  the notes say you can omit** and with the error path named `Panic` even
  though it only returns zero. Two implementations on one disc, the smaller
  unused.

* **[Legends] `c/ShutDown`, 100 bytes, and it does not close the library — it
  *removes* it.** One code hunk of 44 bytes and one relocation:

  ```
      lea     name(pc),a1
      movea.l 4.w,a6
      jsr     -552(a6)        ; OldOpenLibrary
      movea.l d0,a1
      movea.l 4.w,a6
      jsr     -414(a6)        ; RemLibrary        <-- not CloseLibrary (-414, not -378)
      rts
  name: dc.b 'freeanim.library',0
  ```

  `RemLibrary` unlinks the library from Exec's list and expunges it, where
  `CloseLibrary` only drops a reference. It is the **first** program in this
  series to do more than open-and-close, it is the **first line** of the boot
  script, and it runs before `SetPatch`. Whether it is a stronger reading of
  the same documented requirement or a misuse that happens to work is not
  something the disc settles — but if you find a 100-byte program in `c/` with
  one relocation, check which LVO it calls before assuming it is the
  documented one-liner.

Eleven sightings across seven discs, **no function call to the library in any of
them**, always at the moment the program claims the machine — and now we know
that is the API, not an oddity. Seven of the eight open and close; one removes
it outright.

**New, and the first independent support the reading has had: the CDTV
generation has a command whose name says it.** [Prey CDTV] the boot script is

```
CD0:c/bookit bjv
CD0:c/rmtm
Prey:Moreno/Prey
CD0:c/endcli >NIL:
```

`c/RMTM` — *remove TM* — is 2,820 bytes, opens `dos.library`,
`intuition.library` and **`playerprefs.library`**, and runs once, immediately
before the game. Same position in the sequence as the CD32 `freeanim` open,
same shape of job: make the console's boot-time branding go away and give the
memory back. On CDTV it is a named command in `c/`; on CD32 it is a library
whose *open* is the operation. Not proof — `rmtm` has not been disassembled —
but it is the first thing outside the CD32 discs that points the same way.
**On a CDTV disc, look for `c/rmtm` in the boot script.**

**New: the argument template.** [Prey] `c/freeanim`'s `ReadArgs` template is

```
/auto/close/wait
```

and the same three-word string sits in `cdgsxl` 1.48's own data hunk. Against
the documented semantics those three words now read straight: **WAIT** is the
`CloseLibrary` half done separately, **CLOSE** the open-and-close pair, and
**AUTO** presumably the one-liner. `c/freeanim` is somebody's command-line
wrapper around a two-line C idiom.

* **[Microcosm] does the pair inline in the game, and the gap is empty.** Four
  instructions at hunk offset `0x07d8` — `OpenLibrary`, `movea.l d0,a1`,
  `CloseLibrary` — with the result never stored and never tested, exactly as the
  notes prescribe. But it is **not opened first**: the program has already
  allocated its globals, hooked three exception vectors, installed a copper list
  and opened `graphics`, `nonvolatile` and `dos` before it gets there. The
  *position* is still right — the next instruction is `LoadView(NULL)` — so the
  documented "before you take the display" rule is obeyed and the documented
  "give yourself the animation's fade-out to initialise in" benefit is thrown
  away. Seven sightings now, and this is the first with a zero-length gap.

**So the useful measurement is the gap, not the open.** The notes describe an
interval a title is *meant* to fill; measure how many instructions are actually
in it. Six discs put their whole start-up there and one puts nothing.

Still worth a grep on every disc — `grep -c freeanim` over `c/` and the first
stage — because *where* a title opens it says how the title is structured.

### `fl_Key` is the file's LBA — the trick that lets a boot script be five bytes

**[Microcosm]** uses AmigaDOS exactly once, at start-up, and then never again:

```
Lock(name, ACCESS_READ)        dos -84
  lock << 2 -> struct FileLock
  fl_Key                       = the file's first block on the CD
  byte offset = fl_Key << 11   = LBA * 2048
Examine(lock, fib)             dos -102
  fib_Size at FileInfoBlock +124
UnLock(lock)                   dos -90
```

Run over a table of eighteen `cd0:` names, that yields `{offset, length}` for
every file the game will ever load, after which the whole filesystem is
redundant and everything goes through `cd.device` at absolute byte offsets.
That is why the disc needs no `c/`, no assigns and a one-word boot script, and
it is also why the volume can be called `CDTV_TEST` without anything noticing:
`cd0:` is the device.

**Look for `<< 11` (or `lsl.l #8` followed by `lsl.l #3`) on the result of a
`Lock`.** It is a two-instruction idiom, it is the signature of a title that
has decided the filesystem is too slow, and it turns the loader's name table
into a complete map of the disc for free. Dragonstone parses ISO 9660 by hand
to get the same answer the expensive way; this is the cheap way, and both
titles end up reading raw sectors.

**Grep the whole disc for library names anyway, then check which are
actually opened.** [Marvin] `libs/` ships eight libraries and the game opens
five of them; `mathieeesingtrans.library` is opened by nothing and itself
depends on `mathieeesingbas.library`, which is not present. Dead libraries in
`libs/` cost nothing on a disc and survive to be found.

### How the first stage reaches the CD — two greps and a histogram

The first stage is usually a single-hunk AmigaDOS executable that does
`move #$2700,sr` and then never asks the OS for anything again. Two searches
tell you how it gets its data:

* **`4E AE xx xx`** (`jsr d(a6)`) — count them. **Zero means the OS is not
  being used at all**, and the program parses ISO 9660 itself. [Dragonstone]
  53 KB of code, three RELOC32 entries, not one library call, and not one
  library or device name string in the file.
* **the 32-bit constant `00 B8 00 00`** — **Akiko**, the CD32's custom chip,
  whose register block carries the CD-ROM interface. `lea $B80000,a5` is a
  program driving the drive directly.

Also worth grepping: `00 BF E0 01` (CIA-A port A — bit 0 is the power LED and
Paula's low-pass filter, bit 7 the fire-button test).

**Do not grep for the custom-chip base `00 DF F0 00`. Grep for the three-byte
prefix `00 DF F0` and histogram the fourth byte.** [Prey] `MORENO/DoPrey`
contains **zero** occurrences of the base address and **448 references to
individual registers written absolutely** as `move.w #imm,$00DFF0xx` — all
four Paula channels, the Blitter, `DMACON`, `INTENA`. A test that counts
`lea $DFF000,aN` scores this program as never touching the hardware while it
is in fact driving all of Paula. The histogram is also more informative than
the count: it tells you *which* subsystems, immediately.

`tools/scan.py --regs` in
[cd32-prey-doc](https://github.com/vs-sr-dev/cd32-prey-doc) does this and
names the registers.

**The two extremes both exist, and neither is normal.** [Marvin] The same two
greps on this disc give **169 library calls, 39 distinct LVOs, ten libraries,
three devices, and zero references to `$B80000`**. AmigaDOS stays alive for
the whole game; the custom chips are reached through nineteen
`lea $DFF000,a5` inside a display Intuition set up. Do not assume either
model — count the `4E AE` first, it takes ten seconds and it decides how you
read everything else.

**A fourth position: the game runs other programs.** [Liberation]'s executable
names `:CityGen`, `:PlotGen` and `:BuildingGen` and runs them as separate
AmigaDOS executables to lay out the city, lay out a building and generate the
plot and every conversation in it. **And it names a second copy of each**:
`:backup/CityGen`, `:backup/PlotGen`, `:backup/BuildingGen`, with
`c/Liberation` doing the same for the game itself
(`CaptiveII:CaptiveII` then `CaptiveII:BackUp/CaptiveII`). All four backup
copies are byte-identical to their originals and the timestamps show each was
made four to six seconds after its original was built. **A `backup/` directory
on a CD32 disc is not automatically a developer's stray folder — grep the
loader for its name before assuming.**

**A fifth position, and it is the commonest thing a floppy port does.**
[HeroQuest II] keeps `dos.library` alive for the whole game and loads every one
of its 91 files with `Open`/`Read`/`Close`, while driving the hardware itself:
**78 `jsr d16(a6)` call sites across 33 LVOs**, of which 57 are exec, 9 dos, 6
lowlevel, 2 nonvolatile — and **zero graphics**, on a disc that opens
`graphics.library` and never calls it. It also **loads `$DFF000` into an address
register 83 times** and addresses every register as `d16(An)`, so the absolute
scan this section recommends finds 13 registers where a base-tracking scan finds
**57**. That is Prey's lesson inverted: on Prey the base never appears and every
register is absolute; here the base appears 83 times and almost no register is.
**Run both scans.**

**AND THE THIRD ARRANGEMENT IS "NEITHER `lea` NOR ABSOLUTE".** [Guardian] loads
the base with **`movea.l #$dff000,a6`** — `2c7c`, not `41f9` — twenty-one times,
and a scan that looks only for `lea $dff000,aN` scores it as **zero base loads**
on a program that drives the Blitter from `d16(a6)` throughout. Its absolute scan
finds 79 references in 14 registers and its base-tracking scan finds the entire
Blitter, which the absolute scan does not see at all. **Match both opcodes
(`4?f9` and `2?7c`) followed by `00 df f0 00`, and run the absolute histogram
beside it.**

**And there is a third position between them.** [Prey] the first stage makes
64 library calls and touches **no** custom-chip register at all; the game
makes 120 across 44 LVOs, keeps AmigaDOS alive, opens six libraries and
`cd.device` — and simultaneously programs Paula and the Blitter by absolute
address, 448 times. OS-hosted and hardware-driving at once. A **two-process
split** is worth watching for on its own: Prey's first stage and its game
executable are separate files that talk over message ports (`kennport`,
`gameport`) with four-character longword commands (`'kenn'`, `'shut'`,
`'done'`, `'jazz'`).

**REPORT AKIKO AS TWO COLUMNS, NOT ONE.** This document used to keep a single
"Akiko" row, and that hid the only positive result in it. The chip does two
unrelated jobs — it carries the CD-ROM interface *and* it does chunky-to-planar
conversion — and a title can use either without the other:

| | Discs using it | Which |
|---|---:|---|
| `$00B80000` as a **pointer load** — driving the drive | **3 of 17** | [Dragonstone], [Universe], **[Myth]** |
| `$00B80030` — the **I²C port to the CD32's serial EEPROM** | **1 of 17** | **[Universe]** |
| `$00B80038` / `$00B8003C` — the **C2P port** | **0 of 17** | none |
| `$C0DE0000` — the identification constant | **0 of 17** | none |

*(These denominators were stale at "14" for three discs. They are recounted
here against the nineteen discs in the list at the top of this document, and
the lesson is the general one: **re-read the counts you quote, not only the ones
you add**.)*

**THE THIRD DRIVE-DRIVER, AND THE BASE RATE WAS THE WRONG PRIOR.** [Myth]
predicted `$00B80000` absent on the base rate — 2 of 16 — and was wrong. The
mechanism was available and would have got it right: **a disc that kills the
Exec in its first two hundred instructions and opens no device has no other way
to reach the CD.** [Myth] makes exactly three library calls in its whole loader
(`OpenLibrary`, `CloseLibrary`, `Disable`), zero `OpenDevice` anywhere on the
disc, and then drives eleven Akiko registers by hand: `$04` and `$08` for the CD
interrupt request and enable, `$10`/`$14` for the command buffer addresses,
`$18`–`$1F` for the transmit and receive ring indices, `$20`, and `$24` for the
CD DMA register. **Condition the Akiko prediction on whether the loader opens a
device, not on how many previous discs drove the chip.**

**A THIRD COLUMN, FROM THE FOURTEENTH DISC.** Akiko's register block does not
carry two jobs, it carries three. [Universe] loads `$00B80030` into `a2` and
`$00BFE001` into `a1` and then **bit-bangs I²C** — address counter, read/write
bit, clocked-out bytes, an acknowledge test that branches on the sign bit — to
reach the CD32's 1 KB serial EEPROM. That is the save system, written by hand,
because the loader called `SuperState()` and cleared `INTENA`/`DMACON` before
the game started and there is no Exec left to call `nonvolatile.library` with.
**Eight discs here save through that library and this one cannot**, so when a
disc kills the OS, look for the EEPROM at `$B80030` before concluding it has no
save system.

[Banshee] is what forced the split, because it was the best remaining candidate
for the first column and came back zero. Same label as Dragonstone, three
months earlier, the same cruncher and a byte-identical `SetPatch` — and **zero
pointer loads, zero C2P references, zero `$C0DE0000`**, over both code hunks
and both data hunks of the game and over its second executable. It loads its
files through `dos.library` instead. So the one disc that drives the drive
through Akiko is not reproduced by its own label's other title, and the C2P
column is still empty after twelve discs — **thirteen, with [Fire & Ice]**,
which came back zero on all three columns in both of its executables and in all
21 of its unpacked resources.

**And Fire & Ice is a clean demonstration of the false positive**, which is
worth having written down once with the bytes beside it. It shows two raw
`00 B8 00 38` hits. Both are at **odd file offsets** — so neither can be a
longword operand of any instruction — and both are inside the **chip data
hunk**, not the code hunk. Read at the correct even alignment the neighbourhood
is `f820 fc00 f800 fc00 ... bd00 3100 ba00 3a00 b800 3800 e000 e000`: runs of
`0xF8`, `0xFC`, `0xE0` and `0xF0`, i.e. left-aligned bitmask data for planar
sprites. The bare three-byte `00 B8 00` pattern occurs 61 times per executable
and 110 times across the resources and means nothing at all. **Check alignment
and hunk before you check the byte pattern.**

Keep both scans and report both numbers. A disc that scores zero on the second
and non-zero on the first is doing something completely different from what
"uses Akiko" usually means.

**CORRECTION — SCAN ALL EIGHT ADDRESS REGISTERS. THE SCAN THIS DOCUMENT WAS
CARRYING RETURNS A FALSE NEGATIVE.** `tools/akiko.py`, written for Guardian and
reused on five discs since, matches exactly two encodings: `41f9`
(`lea $B80000,a0`) and `2c7c` (`movea.l #$B80000,a6`). [Universe] loads the
Akiko base into **`a5`** (`4bf9`) in three places and into **`a2`** (`45f9`) in
two more, and every one of the five was invisible to it. The prediction written
before the scan — negative on all three columns, following thirteen discs of
precedent — was **wrong**, and it was wrong because of the tool rather than
because of the reasoning.

There are eight forms of each instruction and a scan has to cover all sixteen:

```
lea $xxxxxxxx.l, An     41f9 43f9 45f9 47f9 49f9 4bf9 4df9 4ff9   a0..a7
movea.l #$xxxxxxxx, An  207c 227c 247c 267c 287c 2a7c 2c7c 2e7c   a0..a7
```

`tools/akiko2.py` in
[cd32-universe-doc](https://github.com/vs-sr-dev/cd32-universe-doc) does this.
**Re-run it on any disc whose Akiko result was recorded as zero from the
two-encoding scan** — the C2P and `$C0DE0000` columns are byte-pattern counts
and are unaffected, but the pointer-load column is not.

**And Universe supplies a new false positive for the C2P port, from a genre
this document had not seen.** It shows seven raw `00 B8 00 38` hits and four
`00 B8 00 3C`, none of them in code: all are inside resource files, and every
one is a **hotspot rectangle in a point-and-click's clickable-region table**
whose x coordinate is 184 (`$00B8`) and whose y coordinate is `$38` or `$3C`.
One complete table from that disc:

```
00b8 0038 0028 0028 8013 8014 ffff      x=184 y=56 w=40 h=40, two message ids
00b8 0004 0024 0024 8013 8014 ffff
00f8 002c 0048 0048 8015 8016 ffff
```

So the collection of things that look like `$00B80038` and are not now reads:
**ProTracker's period table** (Gloom, HeroQuest II), **planar sprite mask data
at odd offsets** (Fire & Ice), and **screen coordinates in an object table**
(Universe). Check alignment, check the hunk, and check whether the file
contains any code at all.

**Akiko is untouched on eleven of the twelve CD32 discs, and the twelfth uses
it as a drive controller, not for chunky-to-planar.** The console's headline feature is
used in the *game* by nothing here except the easter-egg demo a programmer left
on Marvin's disc, which is not the game. [Liberation] is the strongest negative
result so far and is worth the paragraph, because it was the best remaining
candidate: a 1994 first-person polygon engine, two experienced Amiga
programmers, 169 MB to play with. Zero `lea $B80000,aN`, zero
`movea.l #$B80000,aN`, zero references to `$B80038` or `$B8003C`, zero
`$C0DE0000`, over the code and data hunks of all twenty-five hunk files on the
disc; the seven `00 B8 00 xx` byte hits are all identifiable (four in a
parameter table, two in `move.w $B8(a6),$CA(a6)`, one in SetPatch).

**And that disc explains itself, which is the transferable part.** Two things
in the same executable say why:

* **the two CD32-only libraries are both opened behind one runtime flag.**
  `nonvolatile.library` and `lowlevel.library` — and nothing else — are opened
  only when a byte at `$3299(a5)` is clear, and neither open is fatal if it
  fails, where the other seven library opens branch to the give-up path. A
  program with a switch that turns off exactly the CD32 modules is a program
  that expects to run on an A1200, and Akiko does not exist there;
* **the renderer has no chunky buffer to convert.** Its 3D library programs
  the Blitter and nothing else (45 of 47 register references), and its wall
  surfaces are pre-rendered planar sprites, not texture-mapped spans.

**So the useful test on the next disc is not only "does it touch `$B80000`"
but "is there anything for a C2P pass to convert".** A blitter renderer and a
planar asset set answer the question before you grep.

**CORRECTED AGAIN, AND THE QUESTION IS THE OTHER WAY ROUND.** [Gloom] is a
real-time texture-mapped renderer whose textures, sprites and HUD are *all*
8-bit chunky — so "is there anything for a C2P pass to convert" answers *yes*
and Akiko is still zero. What is missing on that disc is the other end: **there
is no planar destination.** Its 3D view is displayed by a copper list carrying
one `MOVE` per pixel over a fixed colour-index ramp in the bitplanes (section 7),
so the renderer's output is a 12-bit `$0RGB` value, not a pixel index, and a
chunky-to-planar converter has nothing to do with it. **Ask "where does the
frame end up?" before "what shape is the frame?"**

**AND THE FOURTH MECHANISM IS THE PLAINEST ONE, ON THE BEST CANDIDATE YET.**
[Guardian] is CD32-first, has no floppy ancestor to inherit a loader from, and
runs a genuine real-time triangle rasteriser — the first in this set. Akiko is
still zero, and the reason is that **the Blitter writes planar, so the renderer
writes planar**: there is no intermediate representation of the frame at any
point. See "the polygon filler is a Blitter cookie-cut" in section 7 for the
register-by-register account. The transferable test is short:

* **Is there a `BLTCON1` write anywhere?** If not, the title is not doing an
  area fill, whatever else it is doing.
* **What is `BLTSIZE`'s height, and what are the three modulos?** A height equal
  to the plane count with modulos of `bytes_per_row − width` is one Blitter
  operation painting **one scanline across all planes of an interleaved bitmap**,
  and it is the whole answer.
* **Is `BLTCON0`'s minterm `$CA`, with `USEA` clear and `BLTADAT` written once
  outside the loop?** That is a cookie-cut whose only per-pixel input is
  `BLTAFWM`/`BLTALWM` — a span fill with sub-word-accurate ends and no shifting.

None of the three costs more than a grep, and together they distinguish "fills
planar directly" from "rasterises chunky and converts" without disassembling the
inner loop.

Two more things to check while you are in the executable:

* **Which `OpenLibrary`?** [Marvin] all eleven opens go through
  **`OldOpenLibrary` (LVO −408)**, not `OpenLibrary` (−552), so no version is
  requested and none is checked. [Prey] the same — ten opens across two
  executables, all −408, zero −552. **[Liberation] is the other way round**:
  nine libraries, all through **`OpenLibrary` (−552)**, with `moveq #0,d0` so
  it asks for version zero anyway — and only *two* call sites, because seven of
  the nine go through one shared subroutine in a loop. **Count the call sites,
  not the opens**, or a disc that opens nine libraries looks like a disc that
  opens two.
* **Then find where the bases are stored, and the LVO histogram stops being
  ambiguous.** [Liberation] keeps all nine in one A5-relative block
  (`$150(a5)` dos, `$154` exec, `$158` intuition, `$15C` graphics, `$160`
  vector, `$164` tridee, `$168` nonvolatile, `$3350` lowlevel, `$34A0` math),
  so walking the code and tracking the last `movea.l d16(a5),a6` attributes
  every `jsr d(a6)` to a library by name. That turned 181 ambiguous calls into
  nine exact lists in one pass, and it is the difference between "−30 is one of
  six things" and "`ReadNVData`, once".
* **Which memory do the hunks ask for?** [Marvin] all six hunks of a 926 KB
  executable are `MEMF_CHIP`, including 176 KB of code — 1.57 MB of a CD32's
  2 MB of chip RAM claimed before the program allocates anything. A hunk
  table is four bytes per hunk and reading it is free.

**Interrupt-level subsystems tend to be signed and dated even when the
program is not.** [Marvin] `work` carries no `$VER:` string at all, but its
four hand-written handlers each carry a banner: `EXEC's Revenge...
20/Aug/1994`, `Marvy's Input Slaughter...`, `MARVY_INT/COPPER 1994 V8.2 -
20/Aug/94`, `MARVY_INT/MUSIC! 1994 V8.2 - 24/Aug/94`. Grep for the program's
own nickname, not only for `$VER:`.

**Look for the module-end label.** [Dragonstone] The three files containing the
CD driver each hold the string `CDIOEND`, sitting at the end of a run of zero
bytes exactly where an assembler leaves a section-end symbol. A marker like
that tells you which modules share a hand-written subsystem before you
disassemble any of them — and here it correlated perfectly with the anomalous
timestamps in section 3.

---

## 5. Compression — check that there is any

**Check whether there is any.** [Marvin] Not one `RNC` header anywhere on
the disc, and no other compression either: 212 files, 13.6 MB, all raw.
[Microcosm] the same, and it is the cleanest case yet: nothing on the disc
reaches entropy 7.2, no first longword equals the file size or the file size
minus four, and one pass for every magic in this section over 523 MB returns
nothing. The **34 files are raw, and the 483 MB of video inside one of them is
compressed by a codec that has no magic number and is not a file format at
all** — it is a chunk stream the game's own decoder reads
(section 5's "no magic number" case, taken further).
[Prey] the same, on a much larger disc: 1,439 files, 122 MB, **zero** hits for
`RNC`, `PP20`, `IMP!` or `XPKF` over the whole image. A CD32 disc has 650 MB
and a 2× drive; a studio that decided the read time was cheaper than the
decompression time was making a reasonable call, and **two discs out of five
made it**. The three that packed were all floppy games moved onto CD with
their floppy-era loaders intact — which is the pattern, now **[3 of 3]**:
**compression on this format tracks the floppy origin, not the disc.**
[Microcosm] is the strongest confirmation available: it is the first
CD32-exclusive title here, it has no floppy ancestor at all, and it compresses
nothing. **[4 of 4]** on the negative side too — every uncompressed disc so far
either has no floppy SKU or kept none of its loader. **[Gloom] makes it
[5 of 5] on the positive side**: it ships the floppy release's own hard-disk
installer in its root, two floppy-disk prompts compiled into the CD32
executable, and 115 of 131 files packed. **[HeroQuest II] makes it [6 of 6]**:
three floppy volume names assigned in its boot script, all 91 data paths
addressed through them, a floppy-disk prompt in all three language files
(`Please insert Legacy of Sorasil Patch`) and a complete disk-swap wait loop in
the binary — and 92 of its 97 files packed at 49.1 %.
**[Fire & Ice] makes it [8 of 8]**, and it is the strongest positive so far
*because the disc had every excuse not to pack*: the whole game is 2.8 MB on a
650 MB medium, it uses 0.41 % of the CD, and it leaves 232 sectors of its own
volume empty. It packs 21 of 29 files anyway, with **PowerPacker 2.0**, because
the code that loads them was written for floppies — and the same executable
still contains the floppy disk-swap prompt and a manual copy-protection prompt
to prove where it came from.

**[Myth] makes it [12 of 12], and it is the end of the line for this rule's
positive side** — there is no stronger form available. The disc does not
*refer* to a floppy ancestor and does not *inherit* a floppy loader: it **is**
the floppy release. Three of its five files are 901,120 bytes each — one
880 KiB Amiga disk, exactly — carrying their own bootblocks with valid
checksums, their own chunk directories in block 2, and their own unused blocks
complete with a stray copy of Commodore's `ConClip`. The CD-specific part of the
product is an 18 KB shim that emulates a floppy drive out of CD sectors, and it
compresses nothing that the floppy release did not already compress.

**Which is also a warning about the census.** A file whose length is an exact
multiple of a known medium's capacity is a medium, not a file: 901,120 for an
Amiga DD floppy, 1,802,240 for an HD one, 368,640 or 737,280 for PC 5.25-inch
formats. Check the length before running any magic scan, because the streams are
one level down and the offsets that name them are in the image's own directory
block, not in the ISO. On [Myth] a disc-wide magic scan over the five files
would have found **zero**, because 22 of the 23 streams carry a magic the scan
does not know and the twenty-third carries none at all.

**[Banshee] makes it [7 of 7]**: 37 of 45 files RNC ProPack 1, four
`assign bansheeN: CD0:` lines in the boot script, a disk number byte beside
every one of the loader's 37 paths, and level 3 split across two of those
disks. Note what it does *not* have — **no disk-swap prompt anywhere**, no
`Insert`, no `Disk`, no `Please`. The prompt was taken out and the volume names
were not, so **the assigns are the evidence and their absence would not have
been**.

### THE RULE IS NOW A CONTROLLED EXPERIMENT, NOT A CORRELATION

Every entry above compares *different* titles. [Guardian] compares **one title on
two media**, and it is the strongest form of the result this document can get.

It is the first title here whose floppy SKU exists but does **not** predate the
CD: it is CD32-first, and its CD32 master carries **nothing compressed at all** —
0 of 61 files above entropy 7.0, no magic anywhere in 2.75 MB, zlib re-compressing
its own files to 0.038–0.62. That confirms what the rule predicts.

Then diff it against the A1200 release's data floppy. **Twenty-four of the CD32
disc's data files sit inside that floppy byte for byte**, in eleven 24,832-byte
groups laid out `split` at +0, `dither` at +0x4000, `map` at +0x4100 — and the
1.35 MB of sprite banks that will not fit on an 880 KB disk are **packed into the
floppy's second half at entropy 7.89–7.98**. Same data set, same build, one
medium each, packed on one and raw on the other.

So the rule can be stated in its strong form: **compression on this format is a
decision about the medium, and where a title ships on both, the same bytes are
packed on the floppy and raw on the CD.** The diff is cheap — search the ADF for
each CD file's first 64 bytes, then extend the match — so **do it on any title
with another SKU, even a cracked dump**: the crack lives on disk 1 and the data
disk is usually untouched. On this title the two cracked variants differ by 256
bytes on the data disk and by 20.7 % on disk 1, which tells you which one to use.

### AND A SECOND DISC HIDES A DIFFERENT CODEC INSIDE A DIFFERENT EXECUTABLE

[Banshee]'s file census is correct and reports `picture.exe`, 274,764 bytes, as
"AmigaDOS hunk executable, not compressed". **Three of its four hunks are RNC
ProPack *method 2* streams**, 329,184 bytes of them, behind a 484-byte hunk-0
stub — and method 2 appears nowhere else on that disc, whose 37 data files are
all method 1. A magic scan over files finds nothing because the magic is 44
bytes in, behind a hunk header.

The cheap thing that catches it is the column the census prints anyway:

```
bans.exe      149,524 B   entropy 6.172     a normal 68k executable
picture.exe   274,764 B   entropy 7.840     not a normal 68k executable
C/SetPatch     13,200 B   entropy 6.175
```

**A hunk file above entropy 7.5 is packed, whatever its first four bytes say.**
Two discs now, two different codecs, one lesson.

### CORRECTION — ENTROPY IS SUFFICIENT, NOT NECESSARY, AND THE THIRD DISC PROVES IT

[Fire & Ice] hides **29 packed streams inside already-unpacked files** — one in
each of its two executables, and two to five inside each of its seven world
files, which are themselves PowerPacker streams. **PowerPacker inside
PowerPacker.** And the entropy column finds **none of them**:

```
                          whole file   8 KB windows > 7.5   highest window
FirePAL       410,184 B      6.151         0 of 101              7.222
FireNTSC      409,820 B      6.151         0 of 101              7.269
Core1.bin u.  115,900 B      6.396         0 of  15              7.059
core3.bin u.  117,616 B      6.694         0 of  15              7.401
core7.bin u.  299,288 B      6.385         0 of  37              7.017
```

Zero windows over the threshold on any file at either scale, with 29 genuine
streams present. The reason is **size**: the largest embedded stream is 3,896
bytes and the smallest 496, against files of 105 KB to 410 KB. A 496-byte blob
is 0.12 % of a 410 KB file and 6 % of an 8 KB window, and cannot move either
average. Guardian's and Banshee's embedded data was **hundreds of kilobytes**
and could.

So keep printing entropy — when it fires it is free and decisive — but **do not
treat a clean entropy column as an answer.** The check that found all 29 is the
other one: **scan for every container magic at every offset, and validate each
hit by actually running the decompressor.** That cannot produce a false
positive, because a byte sequence that decodes cleanly to its own declared
length is a packed stream by construction. Both checks belong in the method and
only the second is reliable at small sizes.

### AND THE NESTING GOES DEEPER THAN TWO LEVELS

[Universe] takes the same idea one level further, in a different codec, with a
CRC at every step. Its census reports **47 packed files**; a magic scan
validated at every byte offset by running the decompressor reports **342
streams**:

```
depth 0    62 streams    4,324,396 packed ->  5,664,640 unpacked   1.31x
depth 1   236 streams    2,899,539 packed ->  6,078,872 unpacked   2.10x
depth 2    44 streams      309,870 packed ->    609,936 unpacked   1.97x
          259 raw gaps between streams, 1,092,381 bytes
```

Depth 2 is **RNC ProPack 1 inside RNC ProPack 1 inside RNC ProPack 1**, and
every CRC-16 in all 342 headers matches. Three container shapes occur on the
one disc and only the third is what a census sees:

* a file that **is** one stream (`title.np`, `code.prg`);
* a file that is a **concatenation of streams with raw gaps between them**
  (`scene37.dat`: three streams, 92.5 % of the file covered, and a census that
  reads only the first reports a 35 KB file that unpacks to 732 bytes when it
  actually holds 87,552);
* a file that is **one stream whose output is a concatenation** (`part9.dat`:
  one outer stream, 22 inner, five inner-inner).

**After you unpack, re-scan — and then re-scan again.** Two passes were enough
on Fire & Ice; here it takes three. And the gaps are not padding: on this disc
they carry the resource offset tables, the hotspot tables and the script
bytecode.

### A SEVENTH CRUNCHER: PowerPacker 2.0

[Fire & Ice] packs 21 of its 29 files with **`PP20`**, which had not appeared on
the previous twelve discs. The layout:

```
0x00  'PP20'
0x04  four offset-length bytes (the "efficiency" table)
0x08  packed bit stream
-4    24-bit unpacked length, then one byte of bits to skip at the start
```

The bit stream is read **backwards** in big-endian longwords from the end of
the packed data, bits consumed from the low end of the longword, each field
assembled MSB first; output is written backwards from the end of the
destination buffer. Every file on that disc carries the same efficiency table,
`[9, 10, 12, 13]` — PowerPacker's standard setting, unchanged across 21 runs,
which is one operator with one set of options.

**PowerPacker carries no checksum of any kind**, unlike every RNC stream in
this set. The only validation available is structural: the write pointer must
reach exactly zero and the byte count must equal the declared length. Write the
decruncher to raise rather than to return short. Reference implementation:
`tools/pp20.py` in cd32-fireandice-doc; `tools/ppscan.py` in the same repository
is the every-offset scanner with the windowed-entropy column beside it.

The running list of crunchers on this format is now **seven**: RNC ProPack 1,
Imploder, Bytekiller (no magic at all), CrunchMania, RNC ProPack 1 under a
rotating XOR key, RNC ProPack method 2, and PowerPacker 2.0.

### AND A CENSUS OVER FILES CAN BE RIGHT AND STILL MISS THE COMPRESSION

The same disc. Nothing on the volume is packed, and the census says so
correctly — but **nine images inside the executable are ByteRun1** (the IFF
`cmpByteRun1` code), behind a twelve-byte header:

```
UWORD width, height, planes, x, y, size      size == width/8 * height * planes
```

with `size` the *unpacked* length, packed to 24.8 %–79.8 %. Two things to carry.
The length relation identifies the container across the whole family before a bit
is decoded, which is the usual free check. And **"the file census found nothing"
answers a question about files, not about the program** — on a disc whose game is
one executable plus a pile of raw data, look inside the executable anyway.

One caution from the same disc: four of the nine images are stored **raw**, and a
ByteRun1 decode of them also terminates at exactly the declared length — and
produces noise. **"The decode ended on the declared size" is necessary and not
sufficient; render it.**

**And do not stop at `RNC`, and do not stop at the file count either.**
[Liberation] has exactly **five files** above entropy 7.0 out of 187 and they
are the only packed ones — two `.ASP` scripts and three `.sty` archives, 1.0 MB
of a 2.9 MB game. Three quarters of what is not speech or wall graphics is raw.
[Speris] returns nothing for `RNC` and 35 files
for `IMP!`, which is 6.8 MB of the disc's 8.5 MB. Running the first grep,
finding no hits and concluding "nothing is compressed" would have left the
whole game shut.

### CORRECTION — a magic scan that finds nothing proves nothing

This section used to end "one pass for the four magics over the whole image
answers it." **It does not.** [Legends] scans clean for `RNC`, `RNC`,
`IMP!`, `ATN!`, `PP20`, `PP11`, `XPKF`, `CrM!`, `LZX` and `SQSH` — every magic
this document knew — and **79 of its 111 files are packed**, 4.17 MB down from
11.84 MB. There is no magic number anywhere on the disc because the container
does not have one:

```
ULONG  offset to the trailer   (always filesize - 4, so it points at the last longword)
BYTE[] packed data
ULONG  checksum                (present in all 79 files; read by nothing)
ULONG  unpacked size
```

A four-byte length-looking field and then entropy. Nothing to grep for.

**So the scan is the second step, not the first. The first is the census.**
Sizes, entropy, and the last non-zero byte, over every file (section 9's
census, moved up):

- **entropy 7.0–7.8 across a whole file set** is packed data or encrypted
  data, whatever the first four bytes say. Raw planar artwork does not score
  that; on Legends the `.Pal` files score 2.4–5.8 and every `.Pak` scores
  above 6.7.
- **a first longword equal to `filesize` or `filesize - 4`** is a container
  header. On Legends it is `filesize - 4` on all 79, which is what made the
  family obvious before any of it was decoded.
- then **find the decruncher in the loader**, exactly as before. It was 201
  bytes at hunk offset `0x703E`, it is reachable from the one routine in the
  program that calls `Read`, and transcribing it took one pass.

**A fifth cruncher, and the disc names its author on screen.** [Gloom] scans
clean for every magic above and returns **`CrM2` on 115 of its 131 files** —
**CrunchMania**, by Thomas Schwarz. The container is fourteen bytes:

```
offset 0   'CrM2'  (or 'CrM!', the earlier non-Huffman method)
offset 4   UWORD  leeway -- extra bytes to decrunch in place; read and discarded
offset 6   ULONG  unpacked length
offset 10  ULONG  packed length
offset 14  the stream, read BACKWARDS from its last byte
```

`14 + packed == filesize` on all 115, and the game's own loader confirms the
header length before any of it is decoded: it opens the file, seeks to the end
and back for the size, then `Read`s exactly **14** bytes and compares the first
longword with `'CrM2'` and `'CrM!'`.

The stream is Huffman plus LZ, decoded backwards, with **both alphabets stored
in the stream** — a 9-bit literal/length alphabet (bit 8 set marks a literal)
and a 4-bit offset-width alphabet, each as a count of code lengths, then one
count per length, then the symbol values, turned into canonical `limit[16]` /
`base[16]` tables by a routine in the loader. A one-bit flag after each block
says whether another follows. The output pointer must land exactly on zero,
which is the same in-place self-check the Imploder gives.

Two transferable things. **The credits screen names the cruncher's author**
(`DECRUNCHING CODE BY THOMAS SCHWARZ`) — the first time on this format that a
disc has attributed its own packer, and worth a `grep` of the credits before
reaching for a format description. And **the loader ships a decoder for a
method no file uses**: both `CrM!` and `CrM2` are linked in, 712 bytes between
them, and the packer was set to method 2.

### A SIXTH CRUNCHER, AND IT IS STOCK RNC WITH AN OBFUSCATION LAYER

**[HeroQuest II] is the first disc here where the container is a format you
recognise and the *stream* is not.** Every one of its 106 blocks is RNC ProPack
method 1: an 18-byte header, both CRC-16s present and both correct, and
`18 + packed == filesize` on all 88 whole-file blocks — a relation across a
whole family, and it identified the container before a bit was decoded.

Run a stock ProPack decoder on it and you get output of **exactly the right
length** that **fails the CRC every time**. That is the informative failure: the
Huffman tables, the token loop and the bit reader are all right, and the bytes
are wrong. `English.Bin` should start with a table of 32-bit offsets and starts
`d0 d0 d5 78 d0 d0 d5 78 …` — that table with `0xD0` XORed through it.

The two extra instructions are in the game's own decruncher:

```
  move.b  (a3)+,(a5)+        ; copy one literal byte
  eor.b   d5,-1(a5)          ; XOR it with the low byte of a 16-bit key
  dbra    d0,...
  ror.w   #1,d5              ; rotate the key, once per non-empty literal run
```

**Literals only.** Match copies take their bytes from output that has already
been de-XORed, which is exactly why the structure decodes and the content does
not. The `bmi` that skips an empty literal run jumps *past* the `ror`, so a
zero-length run does not advance the key — get that wrong and it desynchronises
at the first one.

**Three variants ship on one disc and the CRC tells them apart**, so nothing has
to be guessed:

| Variant | Key | Blocks |
|---|---|---:|
| plain | 0x0000 — no obfuscation | 15 |
| fixed | **0x5ED0**, an immediate in the decruncher | 88 |
| stream | 16 bits read after the two RNC flag bits — 0xBE1A | 3 (the executable's own hunks) |

and the containers **mix variants internally**, which dates the blocks relative
to each other: `OverG.Rnc` is plain for its four screens and keyed for its
music, `CreditsG.Bin` the other way round. The blocks were packed separately and
concatenated later.

**Solve the key, do not search for it.** CRC-16/ARC with a zero initial value and
no final inversion is **linear over GF(2)**: `crc(A xor B) == crc(A) xor crc(B)`
for equal-length messages. So decode once with key 0 while recording, for every
output byte, which literal run it descends from (a match copy inherits its
source byte's run); the mask the real key would have XORed in is then a XOR of
at most **128 basis masks** — one per (run class 0..15, bit 0..7) — and 65,536
candidate keys become 128 precomputed CRCs and a table lookup.

**And do not trust a brute force.** A naive search that decodes and CRCs 65,536
times produces roughly one false positive by construction, and it duly did: on
one file it returned `0x41FC`, which passes the CRC-16 and yields obvious
garbage. **Check a recovered key's output against a second file before believing
it.** `tools/xorkey.py` in
[cd32-heroquest2-doc](https://github.com/vs-sr-dev/cd32-heroquest2-doc) does the
linear solve.

**What to take to the next disc.** A magic you recognise is not a format you
recognise — Liberation already taught that with a twelve-byte `RNC` header — and
this adds the other half: **a container you recognise, whose length arithmetic
checks out and whose CRC does not, is an obfuscated stream, not a corrupt file.**
Decode it anyway, look at the output, and read the XOR out of the game's own
decruncher rather than guessing at it.

### A container idiom worth recognising on sight

The same disc uses one wrapper at four different levels — text, graphics, sound
and the executable's hunks:

```
ULONG offset[0]     == 4 * n, i.e. the length of the table itself
ULONG offset[1]
...
ULONG offset[n-1]
   the blocks, in order
```

Reading `n = file[0..4] / 4` gives the entry count for free, and the blocks
chain (`offset + 18 + packed` lands on the next offset, modulo one byte of
padding). **An offset table whose first entry is its own length is a very cheap
thing to test for**, and on that disc it identified the three language files, a
39-entry sound bank, five sprite banks and three graphics containers in one
pass. An offset of **0** is an empty slot and repeated offsets are shared
blocks — both are content findings (section 9's placeholders, and step 21).

**Four crunchers before that, and the fourth is a trap.** [Liberation] scans clean
for everything except **`RNC`**, 46 hits, and the container is *not* RNC
ProPack:

```
offset 0   'RNC' 0x02
offset 4   ULONG unpacked length
offset 8   ULONG packed length
offset 12  the stream                    <- twelve bytes, not eighteen
```

RNC ProPack's header is eighteen bytes with two CRCs, a leeway byte and a
chunk count at offsets 12–17; here offset 12 is already data, and
`12 + packed == filesize` holds on all 44 real occurrences. The stream is a
**backwards** byte-wise bit reader — source read down from its last byte,
output written down from the end of the buffer — with the routine's two widest
field widths **patched at run time from the nibbles of the stream's own last
byte**, so every file carries two of its own table entries. **A magic that you
recognise is not a format that you recognise: read the header length before
reaching for a decoder.**

That disc also shows the census catching something a magic scan would have
mis-filed: `c/warning` is a hunk executable whose DATA hunk **declares 7,232
bytes and stores 2,460**, and the stored body is an `RNC` block. The
"declared allocation much larger than the stored body" tell from Legends works
on a DATA hunk as well as a CODE hunk, and it is what makes a 548-byte program
that decrunches its own data legible.

**A cautionary note about transcription.** The Liberation routine was
transcribed instruction by instruction into Python and **it does not
round-trip**: it decodes the first token verifiably right (a literal run that
reproduces the packed stream's own tail, which is the shape a backwards
decoder's first token must have) and desynchronises on the second match. A
search over both branch senses, all six offset-tier permutations, the
literal-count loop's start values and ±1 on every count did not find it. Where
Speris' 350-byte Imploder decoded 35 files on the first run, this one did not,
and the honest record of *where* it fails is more useful than a guess. Budget
for the possibility.

**And three before that.** RNC ProPack on Dragonstone, the Imploder on
Speris, and on Legends the **Bytekiller** token set — a backwards longword
bitstream with a sentinel bit, literal runs of 1–8 and 9–264 bytes, and
matches of 2, 3, 4 and 1–256 bytes at 8-, 9-, 10- and 12-bit offsets, output
written backwards in place. It is the cruncher *Another World* used in 1991,
shipping in a 1996 CD32 title, **with the checksum verification removed**: the
routine steps over the checksum longword with a bare `subq.w #4,a0`.

Which is the other lesson. Two of the three crunchers on this format put a
**self-check in every file that the shipped loader does not run** — the
Imploder's pair of pointers on Speris, Bytekiller's checksum on Legends.
Where the check is one you can reproduce, run it: a file that fails is a file
that was already broken when it was pressed. Where it is not — Legends' is a
32-bit value that no code on the disc verifies, so there is nothing to
recover the algorithm from — **record the values and move on**, because the
next disc from the same studio may be what identifies the cruncher.

### The Imploder — `IMP!` and `ATN!`

[Speris] 35 of 47 files, 41.2 % of their unpacked size. The Amiga cruncher by
Albert-Jan Brouwer; `IMP!` marks crunched data and `ATN!` crunched
executables, and a decruncher that handles one usually accepts both.

```
offset 0    'IMP!'  or  'ATN!'
offset 4    ULONG  unpacked length
offset 8    ULONG  packed length
offset 12   packed data
            38-byte tail:
              ULONG  initial literal-run length
              UWORD  initial bit buffer; high byte is a flag
              UWORD x 8    offset bases
              UBYTE x 12   offset bit widths, three tiers of four
              ULONG  checksum
```

**The overhead is a constant 50 bytes**, which lets you confirm the layout
across a whole disc before decoding a bit: `filesize - packed_length == 50` on
all 35 files.

**The decode tables live in the file, not in the decruncher.** All 35 files
here carry the Imploder's defaults —

```
bases  64 128 256 512 | 192 640 1280 4608
bits    6   7   8   9 |   7   9   10   12 |  9  11  13  15
```

— and note that each tier's base is the sum of the powers of two of the tiers
below it (`192 = 64+128`, `640 = 128+512`, `1280 = 256+1024`,
`4608 = 512+4096`). A stream *could* carry its own tables; none seen yet does,
so a decruncher that reads them from the tail costs nothing and cannot be
caught out.

The stream decrunches **in place and backwards**: the write pointer walks down
from the end of the output, the read pointer walks down through the packed
data, and **both must land on zero together**. That is the self-check — like
RNC's CRC, it makes a wrong implementation obvious instead of subtly broken.

**Get the decruncher out of the game rather than out of a format description.**
Speris carries its own at hunk offset `0x1E87C` of the main executable, 350
bytes, and it opens by testing both magics:

```
cmpi.l  #$41544E21,(a0)      ; 'ATN!'
beq.s   go
cmpi.l  #$494D5021,(a0)      ; 'IMP!'
```

Transcribed register-for-register into Python — same in-place buffer, same
16-bit truncations — it decrunched all 35 files exactly on the first run.
**Grep the executable for the magic as an immediate** (`0C 90` + the constant,
or `0C 93` and friends for other address registers); on a disc that packs, the
loader has to contain the decoder, and the routine is the specification.

**Where there is RNC, it is the default assumption.** Magic
is ASCII `RNC` at offset 0 followed by a method byte of 1 or 2. Extensions
vary by studio — `.cru` on Dragonstone, often no extension at all — so scan
by magic, not by name.

Header, 18 bytes, big endian:

| Offset | Size | Field |
|---:|---:|---|
| 0 | 3 | `RNC` |
| 3 | 1 | method (1 or 2) |
| 4 | 4 | unpacked length |
| 8 | 4 | packed length |
| 12 | 2 | CRC-16 of the unpacked data |
| 14 | 2 | CRC-16 of the packed data |
| 16 | 1 | leeway — extra bytes needed to unpack in place |
| 17 | 1 | chunk count |

The CRC is the reflected CRC-16, polynomial `0xA001`, zero initial value.

**Method 1's bit reader is easy to get subtly wrong, and the header CRC makes
the implementation self-checking — always verify it.** Bits are read LSB-first
out of little-endian 16-bit units, but the byte pointer runs **two bytes ahead**
of the bits being handed out, and the stream is interleaved with runs of literal
bytes taken from wherever the byte pointer is. After a literal run the buffer is
refilled above the residual bit count **without resetting that count**, so the
leftover bits of the unit before the run survive it. Get that wrong and a file
still decodes for a few hundred bytes before falling apart.

The token loop, for reference:

```
skip 2 bits (flags; bit 1 marks an encrypted stream)
while output is short of the target:
    read three Huffman tables:  raw, len, pos
    subchunks = 16 bits
    while subchunks--:
        n = value(raw)                  number of literal bytes
        if n: copy n literals, then resynchronise the bit reader
        if subchunks:                   the last subchunk has no match
            offset = value(len) + 1     note: the SECOND table gives offset
            count  = value(pos) + 2     and the THIRD gives length
            copy count bytes from output[-offset]
```

A table is 5 bits of leaf count, then 4 bits of code length per leaf, canonical
in increasing length order, stored bit-reversed. A decoded leaf index `i` gives
the value `i` for `i < 2` and `(1 << (i-1)) | read_bits(i-1)` otherwise.

`tools/rnc.py` in
[cd32-dragonstone-doc](https://github.com/vs-sr-dev/cd32-dragonstone-doc) is a
working method-1 decoder; it verified 84 of 84 files on that disc.

### A NINTH CONTAINER, PROVEN STRUCTURALLY AND NOT YET DECODED

[Superfrog] carries nine files beginning `PaCK`, which is none of the eight
crunchers above. The header was deduced from the files:

```
+0   char[4]  'PaCK'
+4   UWORD    0            (zero on all nine)
+6   ULONG    unpacked size
+10  ULONG    packed size
+14  ...      packed bytes, exactly `packed` of them
```

`14 + packed == filesize` on **9 of 9**, and the disc supplies its own control:
four of the nine have a same-named sibling in a `RAW/` directory, and the
declared unpacked size equals that sibling's byte count **exactly** in all four
cases.

**And it is still only a container, not a cruncher, because nobody has run the
decompressor.** That distinction is worth keeping sharp. The eight above are
crunchers because their streams were decoded and checked; this one has a proven
header and an unread stream. Write it as "a ninth container format" until
someone reads the stream, and do not add it to the cruncher count.

The same disc shows the best validation setup this format has offered: because
the packed and unpacked forms of four assets **ship side by side**, a candidate
decoder can be verified without the format being understood at all. If a disc
ever gives you both forms of the same asset, that is worth more than a checksum.

### AND THE INHERITED-TOOL TRAP CAUGHT A FOURTH DISC

Three previous cases: `akiko.py` on Universe, `containers.py` and
`audiotracks.py` on Gunship. The fourth is [Superfrog], and it is the most
explicit yet, because the assumption is a literal line of source:

```python
if magic == b'CrM!':
    raise NotImplementedError("CrM! stream: no file on the disc uses it")
```

That is `crm.py`, written on the Gloom disc, where the statement is true. Run
it on Superfrog's two `CrM!` files and it reports `0 decrunched, 2 failed` — a
clean negative on a disc whose CrunchMania headers parse **exactly**, both of
them, `14 + packed == filesize` to the byte.

Note also what did *not* get written up as a negative: the Universe-era
`containers.py` and `unpackall.py` decode **RNC method 1 only**, and Superfrog
has no RNC at all and 158 Imploder streams. Those two report zero. They were not
used, because the rule was followed.

**The rule, restated because it has now paid four times: if an inherited tool
returns zero, read the tool before you write the zero.** The cost of checking is
one minute; the cost of not checking is a false negative published under a
number that looks measured.

### zlib as a diagnostic

If a file resists, re-compress the *unpacked* result with zlib and read the
ratio. [Dragonstone] Ordinary game data lands at 0.09–0.64; the one file
carrying a second compression layer inside it lands at 0.825. That one line
distinguishes "I have the wrong geometry" from "there is another codec here"
before you spend an afternoon on the wrong one.

### Expect fixed sizes, packed or not — and check what is in the padding

**[3 of 3]** Files of a given type are the same length whatever the level,
because the length is the buffer the loader allocates, not the size of the
data. The loader never reads a length.

* [Dragonstone] Every file of a given type unpacks to exactly the same length
  (319,488 for the tile bank, 81,920 for a text file, 160,256 for the object
  map, 32,768 for the object directory), while the last non-zero byte moves
  around — 73.9 % to 95.2 % of the buffer used.
* [Marvin] Nothing is packed, and the effect is visible directly: all 64
  level files are **exactly 15,092 bytes** whether the level is 19 cells wide
  or 380.

* [Prey] Every animation family is a fixed buffer in round *decimal* numbers
  somebody typed — 529,200, 512,000, 358,400, 258,000, 200,000, 51,200 — none
  of which is a multiple of the 10,240-byte frame. `AIR001` is 258,000 bytes:
  25 frame slots and 2,000 bytes over, of which **20 slots are real frames**.
  And the 1,225 sound files are all exactly 61,440 bytes because that is the
  number written to `AUD3LEN` (section 8).

**Then look at the padding, because it may not be padding.** [Marvin] The
unused part of every level file contains between 1,563 and 6,952 non-zero
bytes and **no two files are alike**: the editor wrote its buffer out without
clearing it, so each file carries the tail of the previously edited level —
its map data *and*, because the file has a fixed-offset trailer, fragments of
its title and author strings. One file contains `' OF THE FOREST'`, the tail
of the previous level's title. Sixty-four files, sixty-four different ghosts.

[Prey] the same, without the text: the trailing slots of every animation file
hold stale bitplane data, and **all 34 `AIR` files carry the identical tail**,
as do all five `END` files — one buffer, never cleared, one converter run. The
`BDL` family splits **three** ways by tail hash (eleven files, then `BDL001`
alone, then `BDL005` alone), which is a build split visible from a hash and
nothing else.

A fixed-size file whose declared content is short is an invitation: diff the
tails, hash them, count the non-zero bytes, and read the strings. **Hashing
the tails across a family is the cheapest build-split detector on the
format** — it costs one line and it has now found a split on two discs.

**A cheap real/stale test for headerless bitmap slots**: score each slot by
the fraction of adjacent bytes that are equal. [Prey] real bitplane data
scores 0.25–0.95, stale buffer 0.02–0.20, and the boundary is unambiguous.

---

### AND A DISC CAN HAVE A REASON NOT TO PACK, WHICH IS BETTER THAN A CORRELATION

Five discs of nineteen have nothing packed at all — both Prey masters, Marvin,
[Guardian] and [James Pond 2]. On the first four the finding is a negative and
stops there. On the fifth there is a **mechanism in the hunk table**, and it is
worth a step of its own because it costs one command.

```
python3 tools/hunkinfo.py extract/RoboCod
  hunk 0: 81158 longwords (324632 bytes) mem=CHIP
  hunk 1: 153403 longwords (613612 bytes) mem=CHIP
  hunk 2: 61813 longwords (247252 bytes) mem=CHIP
```

**All three hunks are `MEMF_CHIP`** — 1,185,496 bytes of the CD32's 2 MB of
chip RAM, for one program, before the game allocates a single buffer. A
whole-file decruncher needs a destination as large as the output *and* the
packed input live at the same time; there is no room. The 324,632-byte *code*
hunk does not need to be in chip RAM at all, so about 317 KB of the scarcest
memory on the machine is being spent on a link-time convenience, and the
compression decision follows from it.

**So: read the memory flags in the hunk table before concluding anything about
why a disc is or is not packed.** A game that has taken more than half of chip
RAM for itself cannot pack, whatever the medium looks like. This is the
complement of the [Legends] correction — there, a clean magic scan hid 65 %
packing; here, a clean magic scan is confirmed by an independent constraint.

And note what the same disc does compress: its 115-page manual is IFF ILBM with
**`ByteRun1`**, 7.36 MB of raster down to 2.98 MB, a ratio of 0.404. **A format's
own RLE is not a cruncher and should not be counted as one** — but it should be
measured, because on that disc it is the only compression there is and leaving
it out of the census would have said "nothing on this disc is compressed",
which is false in the way that matters to a reader.

## 6. Executables and overlays

AmigaDOS hunk format, magic `00 00 03 F3`. `tools/hunk.py` in the Dragonstone
repository reads the subset that matters: HEADER, CODE, DATA, BSS, RELOC32,
SYMBOL, DEBUG.

Useful tells:

* **Relocation count.** A 50 KB code hunk with three RELOC32 entries is
  position-independent hand-written assembler. Hundreds of them usually means
  a C program — but check for `HUNK_DATA`/`HUNK_BSS` before concluding it.
  [Prey] `DoPrey` is a **single** 98 KB code hunk with **5,323** relocations
  and no data or bss hunk at all, which is hand-written assembler addressing
  its own variables absolutely (`move.l $00xxxxxx.l,d0`); every one of those
  needs a relocation. A C program of the period would have emitted separate
  data and bss hunks, and SAS/C would have left `HEADDBGV01`.
* **`HUNK_DEBUG` before the first code hunk, tagged `HEADDBGV01`**, is SAS/C 6.
  `main.c`, `ver6.00` and `_main` in the code hunk confirm it.
* **Measure how much of a code hunk is zero.** A hand-written assembler program
  that declares its working storage with `ds.b` inside the last section, rather
  than as a separate `HUNK_BSS`, ships those zeros on the disc. [Gloom]'s single
  174,128-byte hunk is **29.9 % zero**: 8,256 bytes of trailing zeros after the
  last non-zero byte, and a 1,248-byte run in the middle that turns out to be
  the decruncher's Huffman tables (`lea $25046(pc),a6`, indexed `$1e(a6)`
  through `$4de(a6)`). Finding the zero runs first tells you where the scratch
  areas are before you disassemble anything that uses them.
* **A game executable with real DATA and BSS hunks is a compiled program**, and
  that is not the norm on this format. [Liberation] `/captiveII` is four hunks
  — 225 KB CODE, 32 KB BSS, 14 KB DATA and a **40-byte chip BSS** — with 1,356
  relocations, against Prey's single 98 KB code hunk with 5,323. Forty bytes is
  also the whole of its static chip claim, where Marvin takes 1.57 MB of a
  CD32's 2 MB before it allocates anything: **read the hunk memory flags first,
  they cost four bytes each and they tell you how much machine the program
  takes before it starts.**
* **`HUNK_SYMBOL` survives surprisingly often** — but not always. [Prey]
  **one** file on a 1,439-file disc kept a symbol table, and it is
  `c/freeanim`'s two-entry stub (`_OpenLibrary`, `_CloseLibrary`); neither
  game executable kept anything, and there is no `HUNK_DEBUG` anywhere.
  **Check every file, not only the obvious executables.** [Marvin] `work`'s table was stripped, but
  `libs/color_fx.library` kept its entire export list (a 40-function
  hand-written assembler palette engine, `CreatePaletteCopperlist`,
  `ColorFX2RawAGA`, `ShadePalette`, …) **and so did all four files in
  `languages/`** — which named the whole text format, section by section,
  before a byte was disassembled. See below.
* **Assembler-generated local labels are a toolchain fingerprint in their own
  right.** Commodore's `REMHEAD.033` / `ENABLE.031` style (section 2) and
  Marvin's `.err$16` / `.loop$21` / `.ok2$23` style are different assemblers
  leaving different marks. Collect them.
* **A library that ships in `libs/` may not be Commodore's.** [Marvin]
  `color_fx.library 40.1 (03/Sep/1994)` is in-house, and says so in its own
  expunge message: *"You may assemble a new library and replace the old one in
  LIBS:."* Read the `$VER:` of everything in `libs/`, not just `c/`.

### Data wrapped in a hunk file is a real pattern

[Marvin] The four language files are one-hunk AmigaDOS executables — magic
`00 00 03 F3`, no resident list, one `HUNK_CODE` — whose "code" is a data
blob. Wrapping data that way lets a program that already has `dos.library`
open read it with a single `LoadSeg()`.

Two consequences: a file with the hunk magic is **not necessarily code**, and
its `HUNK_SYMBOL` table, if present, is documentation of the data format.
Marvin's read

```
Language = 4     TEXT = 0x14     PW = 0x1F48
PictureTexte = 0x1F6C            Manual = 0x3279
```

and that is the whole format: an identifier, a table of four offsets relative
to `Language`, and four sections of NUL-separated strings.

**And a hunk file may be a crunched hunk file, which the OS cannot load.**
[Legends] Each of the five level overlays is a well-formed hunk file — header,
one `HUNK_CODE`, `HUNK_RELOC32`, `HUNK_END` — whose CODE *body* is a packed
stream, and whose declared hunk size is the **unpacked** size. The tells are
free:

* the header's allocation is far larger than the body in the file (572,984
  bytes of "code" declared as a 1,531,604-byte chip hunk), and it matches the
  unpacked size **to the byte**;
* the relocation offsets run past the end of the body — up to 940,974 in a
  572,984-byte hunk;
* the body's first longword is the packer's container header, not an
  instruction.

Which means `LoadSeg` cannot load it: AmigaDOS relocates immediately after
reading, and the bytes to relocate do not exist yet. So look for the game's
**own** hunk loader. On that disc it is 400 bytes at hunk `0x6E02` of the
front end, dispatching on `hunk_id - 0x3E7` through a 15-entry table, with the
decruncher called from inside the `CODE` handler between "read the body" and
"apply the relocations". **A program that loads hunk files and never calls
`LoadSeg` (`jsr -150(a6)`) has written its own, and it wrote its own for a
reason** — grep the LVO histogram for `-150` before you assume AmigaDOS is
doing the loading.

### A hunk file can decrunch AND relocate itself, and then it has no relocations at all

**[HeroQuest II]** takes Legends' crunched-hunk pattern one step further and the
tell is different, so it is worth its own entry. `/QuestII` is six hunks and, as
it sits on the disc, has **no `HUNK_RELOC32`, no `HUNK_SYMBOL` and no
`HUNK_DEBUG`** — which is impossible for a six-hunk program that must reference
its own data, and is the first thing to notice.

Three of the six hunks store

```
ULONG  offset of the HUNK_RELOC32 block inside the *unpacked* hunk
ULONG  that value / 4, with the hunk's memory flags in the top bits
       an RNC ProPack block, unpacked length == the declared allocation - 4
```

so each hunk decrunches to **its real content followed by a complete
`HUNK_RELOC32` block** — 4,505 relocations in the code hunk, 1,019 in the data
hunk — where `LoadSeg` cannot see them. Hunk 0 is 584 bytes of uncrunched code
that walks the AmigaDOS segment list with `pea (-4,pc)`, tests byte 8 of each
hunk for the `RNC` magic, decrunches in place, applies the relocations itself,
and finishes by **overwriting the return address it pushed as its first
instruction** so that its own `rts` enters hunk 1.

Two things to carry:

* **the embedded relocation tables number hunks from the first *crunched*
  segment**, one less than the file's hunk index, because the stub excludes
  itself from the walk. Settle it from the data rather than from the loop:
  three of that disc's five target ranges do not fit the hunk their number names
  and do fit the next one;
* **the stub clears each longword of the table as it consumes it**, so 22 KB of
  relocation table becomes 22 KB of zeros at the tail of the code hunk. A large
  zero run inside a code hunk is not always `ds.b` scratch space (Gloom); it can
  be a table that has already been eaten.

**AND A SECOND, INDEPENDENT IMPLEMENTATION OF THE SAME IDEA — SO IT IS A
PATTERN, NOT A STUDIO'S TRICK.** [Banshee]'s `picture.exe` is four hunks with
**zero relocations**, and hunk 0 is **484 bytes** doing exactly the two jobs
HeroQuest II's 584 bytes do, with different code and a different codec (RNC
ProPack **method 2**). Its prefix is two longwords rather than HeroQuest II's,
and the second is a copy of the hunk-table entry rather than a derived value:

```
+0   the original hunk's length in bytes         <- used by the stub to find
+4   the hunk table entry (longwords + memflags)    where the reloc tables start
+8   'RNC' 02, then the ordinary 18-byte header
```

Two things to carry from it, one of which repeats HeroQuest II's warning in the
opposite direction:

* **the embedded relocation tables' hunk numbers are again off by one, and
  again in the direction the stub's own loop dictates** — here `dbra d0` follows
  **d0 + 1** links from the head, so a table naming "hunk N" relocates against
  **segment N + 1**, because the packer inserted itself as hunk 0 and left the
  original numbering alone. Read literally, one of Banshee's constants points
  636 bytes into a 916-byte hunk and is nonsense; read correctly it lands
  exactly at the start of the picture. **Settle the off-by-one from the data —
  find one target you can identify and check which hunk it lands in;**
* the stub also **clears the tables as it consumes them** (`clr.l (a4)+`),
  the same as HeroQuest II's, so the same "large zero run at the tail of a hunk
  may be an eaten table" caveat applies.

Both stubs are under 600 bytes, both leave a hunk file with no relocations, and
neither carries a magic number of its own. **A hunk executable with zero
`HUNK_RELOC32` entries and more than one hunk is the tell, and it costs one
parse.**

**Game overlays are usually not hunk files.** Look for a short custom header
instead. [Dragonstone] uses a sixteen-byte one:

```
offset 0   'DNLD'
offset 4   load address        ($00020000)
offset 8   end of the initialised code/data area
offset 12  entry point         (always load + 0x10)
```

which is what a loader that has already killed AmigaDOS needs and no more.

### The loader's file table is worth finding early, and it carries more than names

**[Banshee] shows the richest form of it so far**, and it is worth the shape
because it packs three separate things into one run of bytes. 37 variable-length
records in the game executable's data area:

```
+0  buffer size, 4 bytes big-endian
+4  floppy disk number, 1 byte
+5  flag byte, 0x01 on all 37
+6  the path, NUL-terminated, padded to an even offset
```

The path is `bansheeN:<name>` and the disk byte is the same `N`, so the table
is simultaneously the file list, the **four-floppy layout of the A1200
release**, and the memory map. And the size field is visibly **hand-maintained
in decimal**: the seven intro-sequence entries are their packed sizes rounded
up to the next hundred bytes (4,342 → 4,400; 8,254 → 8,300; 11,429 → 11,500),
ten cut-scene frames share one buffer big enough for the largest, and one file
is given 25,362 bytes more than it needs because it shares a buffer with a
bigger sibling. **Check the table's sizes against both the packed and the
unpacked file sizes** — which of the two a given entry matches tells you
whether the file is staged and decrunched elsewhere or decrunched into a buffer
of its own.

And it ends with a leftover: a thirty-eighth NUL-terminated name with **no
record header at all**, under a volume-name convention nothing on the disc
assigns, naming a file that is not there.

**[3 of 3]** [Legends] the same shape again: 57 NUL-terminated names in one
run at hunk `0x19CC` of the front end — six floppy volume names, then every
file it can open, in index order. All 51 filenames exist on the disc and three
are spelled with capitals the disc does not use. And the *level* executables
carry the complementary trick: a filename **template** with a literal `x` in
it (`LEVEL4/SPRITESx.PAK`) and a separate compiled string naming the contents
of each bank. **Grep for `/` and for the disc's own directory names**, and
grep for uppercase forms of them too.

[HeroQuest II] the same shape a third time, and it is the whole floppy release:
**91 NUL-terminated paths** in one run in the data hunk, every one of the form
`Legacy of Sorasil DISK n:...`, immediately followed by the string
`input.device`. 90 exist on the disc; the 91st, `Legacy of Sorasil
DISK 2:Level.Map`, does not, and it sits at the end of the run right after the
nine dungeon maps that do. Case is inconsistent between the three disks
(`Hq2title.Rnc` on disk 1, `CHAPS/BARBRIAN.RAW` on disk 3) where the disc itself
is mixed case throughout — harmless on an Amiga, fatal on a case-sensitive host,
and a hint that the three tables were written at different times.

[Dragonstone] The resident loader carries a run of fixed-width NUL-terminated
filenames followed by a table of 16-bit indices into them, dimensioned by
level. Finding it gave up, in one read: the complete list of data files, the
load order, **21 filenames spelled with the wrong case** relative to the disc
(harmless on an Amiga, fatal on a case-sensitive host), and a **row of seven
`0xFFFF` entries where a cut level used to be**. Look for a dense run of
same-length names before you disassemble the loader.

---

## 7. Graphics

**Assume planar until proved otherwise** — **[5 of 5]**, and on all five
discs reading the same bytes as chunky gives noise. That holds even when the
size makes chunky look plausible: [Legends] every screen is **64,000 bytes**,
which is 320 x 200 at eight planes *and* 320 x 200 at one byte per pixel, so
the size decides nothing and the render decides everything.

**But test interleaved *and* separated.** Dragonstone, Marvin and Speris are
interleaved; [Prey] every animation file on the disc and every frame of its
CDXL stream is **plane-separated** — all of plane 0, then all of plane 1 —
and so is [Legends], down to the individual 16 x 16 font glyph. The tell is
free: render the file as a single-bit-deep strip at the candidate width and
look. A separated image shows up as *N* stacked copies of the same
picture at *N* levels of detail; an interleaved one shows up as one picture
with horizontal banding. The CD32's Akiko
chunky-to-planar hardware is not a reason to expect chunky data: [Marvin]
never touches Akiko in the game at all, though the demo its programmer left
in an easter-egg directory on the same disc drives it happily. Planar first.

Get the proof from the copper list rather than from the pixels where you can:
if `BPLxMOD = (planes - 1) * bytes_per_row` and consecutive `BPLnPT` values
are one row apart, the bitmap is interleaved. [Dragonstone] Two copper lists
on the same disc, one 320 pixels wide at 3 planes (`BPLxMOD = $50 = 2 * 40`)
and one 128 wide at 4 (`BPLxMOD = $30 = 3 * 16`), both agree.

**But you may not get a copper list at all.** [Marvin] builds every copper
list at runtime through an in-house library — `color_fx.library`'s
`CreatePaletteCopperlist` — so there is not one static copper list on the
disc. When that happens, autocorrelation plus rendering is the whole method,
and the display depth has to come from an emulator trace instead.

**A CDXL stream can be either, too, and two releases of one game disagreed.**
[Prey CD32] 619 frames, 240 x 96, 7 planes, **plane-separated**.
[Prey CDTV] 100 frames, 160 x 128, 6 planes, **line-interleaved**. Render four
frames both ways and look; it costs nothing and the wrong one is obvious.

**A CDXL whose palette is too small for its plane count is HAM.** [Prey CDTV]
6 planes with a 32-byte palette — 16 entries where 64 are needed — is HAM6:
sixteen base colours and 4,096 displayable, which is how you got photographic
colour out of an ECS Amiga. Decoded as plain planar it is noise; decoded as
HAM6 it is a flight over forested mountains. **The palette-to-plane mismatch
is the tell**, and it is in the header, so you never have to guess.

**And separated is what a game with no scrolling background chooses.** The
split so far is not random: the two discs that store screens plane-separated
(Prey, Legends) both point the bitplane registers at a whole loaded screen,
and the three that interleave (Dragonstone, Marvin, Speris) all blit a window
out of a larger bitmap. Interleaving costs nothing when the blitter walks the
bitmap and saves nothing when the display hardware does. **Guess from what the
game does with the screen, then confirm by rendering.**

**Interleaved and separated can coexist in one file family.** [Marvin] Eight
of nine `blockNN.fbb64` files are 320 x 400 six-plane *interleaved* tile
banks; the ninth, same extension and same directory, is 448 x 256 six-plane
*separated* — and is the title screen rather than a tile bank. Test both
layouts on any file whose size does not match its siblings'.

**Disassemble the copper lists first.** They give you the plane count
(`BPLCON0` bits 14–12, plus bit 4 for AGA's eighth plane), the width
(`DDFSTOP - DDFSTRT`), the height (`DIWSTRT`/`DIWSTOP`) and the palette, all
before you have guessed anything. `tools/copper.py` in the Dragonstone
repository does this with AGA register names.

**Check `FMODE` ($DFF1FC).** A CD32 game that writes `FMODE = 0` is an ECS
game wearing AGA hardware — almost always a port of an A500 or A1200 floppy
release, and a strong hint that there are floppy-era leftovers elsewhere in the
code. [Dragonstone] writes it in the first-stage loader and never touches
`BPLCON3`, `BPLCON4` or the AGA colour banks anywhere on the disc.

**Where `FMODE` is not reachable, read the palettes instead — but ask two
separate questions, because they have different answers.**

*Precision.* An Amiga `$0RGB` word is 12-bit; AGA's colour registers take 24.
An IFF `CMAP`, however, **always stores eight bits per gun whatever the target
hardware**, so the question is whether the bytes in it are reducible to four
bits.

**CORRECTION — the test this section used to give was unsound.** It looked
only for nibble-*doubling* (`v * 17`: `0xF` written as `0xFF`). A 4-bit value
is just as often written as `v << 4` (`0xF` as `0xF0`), and the CDTV Prey
master uses that form **exclusively**: its six ILBM screens are 5-plane,
32-colour, unambiguously ECS, and the doubling-only test scores every one of
them as 24-bit colour. Use both conventions:

```python
def needs_more_than_4_bits(b):
    return (b & 0x0F) != 0 and (b >> 4) != (b & 0x0F)
```

Re-run on the five discs: the CDTV master scores **0 bytes on all six files**,
as ECS requires. [Prey CD32] **6 of 14 screens** carry a substantial count
(282 of 384 bytes on one, 222 of 768 on another), three more carry eight
stray bytes each that are probably conversion rounding, and five are pure
12-bit. [Marvin] and [Dragonstone] have no value above `0x0FFF` at all in
their raw palette files. [Speris] **1,648 of 3,072 bytes, 53.6 %**, and — the
part that matters — **every one of its sixteen levels scores between 82 and
116 of its 192 palette bytes**. Not a few deepened screens: the whole game.

[Legends] **all twenty of its 768-byte palettes fail the 4-bit test heavily**
— 464 to 585 bytes of 768 carry a non-zero low nibble, and only 5–16 % have
matching nibbles on the screens with photographic content, which is roughly
what chance gives. 256 entries of three bytes, eight planes per screen: this
is the deepest disc on the format so far.

So AGA colour depth is used on **five** discs of nine — Prey CD32, Speris,
Legends, [Microcosm] and [Gloom] — and three of the five use it everywhere. But **the plane count is still the claim that needs no
interpretation**, and it should carry the weight.

**And ask the question separately for the front end and for the game.**
[Legends] the front end is eight planes with 256-entry 24-bit palettes; the
*levels* are four and five planes with sixteen 32-entry `$0RGB` tables, which
is an ECS-class game. **One disc, two answers.** The tell was free and it did
not come from a palette file at all: every sprite in the level banks is stored
as an image plus a one-plane mask, and **the ratio of their lengths is the
plane count** — 5 on 552 pairs, 4 on 48, out of 607. If a format pairs each
object with a mask, divide.

**A palette table may also be *named*.** [Legends] each level executable
carries fifteen or sixteen `0xFF`-terminated ASCII names (`MAIN PAL`,
`MINECART PAL`, `DUNGEON PAL`, `EMPTY PAL`) immediately in front of the colour
data. Grep for `PAL` and for other short all-caps words before you go looking
for the table by offset — and count the `EMPTY` entries, because they are cut
content in the cheapest possible form.

**The cheapest AGA test of all is which palette call the program makes.**
[Liberation] calls **`LoadRGB4` (graphics −192) four times and `LoadRGB32`
(−858) never**, opens an Intuition screen rather than programming the display,
and writes **no bitplane pointer, no colour register, no copper instruction,
no `BPLCON0` and no `FMODE` anywhere on the disc**. `LoadRGB4` takes 12-bit
words and cannot express anything else, so one histogram of the LVOs settles
the colour question with no palette file involved — and on that disc the one
palette that *is* stored as data (32 `$0RGB` entries in the 64-byte tail of
`gamemenu.spr`) agrees, every value ≤ `0x0FFF`. **Histogram −192 against −858
before you go looking for palettes.**

**A FOURTH OUTCOME: the library is opened and never called at all.**
[HeroQuest II] opens `graphics.library` and there is **not one
`movea.l <gfxbase>,a6`** in 113,112 bytes of code — the base is stored at start-up
and never loaded again. So `LoadRGB4` is zero, `LoadRGB32` is zero, and unlike
[Microcosm] (which calls `LoadView` and `WaitTOF`) and [Gloom] (four calls) the
count is zero on every graphics vector. The single graphics call on that whole
disc is a `LoadView(NULL)` in a 228-byte root command that opens its own copy of
the library (section 4).

**On such a disc the colour count can still be measured directly, and the
cheapest measurement is a blanking loop.** That root command ends with

```
lea     $DFF180.l,a0
move.w  #$1f,d7
move.w  #$0,(a0)+
dbra    d7
```

— **exactly 32 colour registers**. A program with 64 or 256 colours to blank
would have written 64 or 256, so on a disc with no palette call, no palette file
and no `BPLCON3`, one `dbra` count settles the depth. **Look for the start-up
blank before looking for the palette.**

**CORRECTION — the histogram has a third outcome, and it is not "no palettes".**
[Microcosm] calls **neither**. A histogram of every `jsr d16(a6)` in its 106 KB
code hunk finds exactly two `graphics.library` entries — `LoadView` (−222) and
`WaitTOF` (−270), both used once, to take the display away from Intuition — and
after that the library is never called again. There is no palette call to count
because there is no palette *call*: the game writes 256 colour registers from a
**copper list**.

So the test is cheap and worth running first, but read a zero-zero result as
"this program programs the display itself", not as "this program has no colours".
**[Guardian] is the third**, and on it the whole of `graphics.library` is seven
calls — `LoadView` twice and `WaitTOF` five times, all of them in the eight
instructions that take the display away from Intuition. Three discs of eleven now
program the display themselves. **[Gloom] is the second disc to score zero-zero** — `LoadRGB4` never, `LoadRGB32`
never, and only four `graphics.library` calls in the whole file (`LoadView`,
`WaitTOF` twice, `OwnBlitter`/`DisownBlitter`) — so on this format a zero-zero
result is not exotic. On such a disc the answer is in the copper list, and it is
just as unambiguous:

```
COPPER/COLOURCOPPERLIST.S, 2,292 bytes in the chip DATA hunk

  BPLCON3 <- 0000   bank 0, LOCT=0     COLOR00..COLOR31
  BPLCON3 <- 2000   bank 1
  ...                                  (banks 2..7)
  BPLCON3 <- e000   bank 7
  BPLCON3 <- 0200   bank 0, LOCT=1     COLOR00..COLOR31 again
  ...
  BPLCON3 <- e200   bank 7
```

Eight banks of 32 registers written twice, once with `LOCT` clear and once with
it set: 256 entries at eight bits per gun, 512 copper `MOVE`s, and AGA by
construction. **The same LOCT test section 7 already gives for code applies to
copper lists — scan for `$106` moves whose value differs only in bit 9.**

**And the list may be built at run time rather than stored, which is the same
finding through a different door.** [Gloom] allocates `$430` = **1,072 bytes**
and fills it with four `BPLCON3` banks x 32 `COLOR` registers x two `LOCT`
passes — 8 x (1 + 32) + 4 = 268 longwords, which closes on the allocation
exactly. The palette source is read **four bytes per entry**, and the loop's
`lea -$7e(a1),a1` between the two passes is what gives it away: after 32 entries
the pointer has advanced 128 bytes, and stepping back 126 leaves it on the *low*
word of the first pair. So on that disc the stored `.pal` files are **128
entries of two big-endian words — the `LOCT` pair** — and read as 256 single
12-bit words they render as noise. **When a palette file's length is 4 x the
colour count rather than 2 x, try it as `LOCT` pairs before concluding the
geometry is wrong.**

**AND A SECOND DISC DOES IT AT FIFTY TIMES THE SCALE, FOR A SKY.** [Guardian]'s
twelve `data/splits/splitNN` files are **exactly 16,384 bytes each**: 4,096
entries of two big-endian words, the `LOCT` pair. Read as 8,192 twelve-bit `$0RGB`
words they are noise; read as pairs they are gradients that change **one low
nibble at a time**, which is the entire point — a twelve-bit sky banded over 200
scanlines and a 24-bit one does not. The copper list pours them out at two
colours per raster line from a template of ~205 identical 28-byte units the game
patches every frame (two `WAIT`s, three `MOVE`s whose register numbers are
patched, and two `BPLCON3` writes toggling `LOCT`).

**A file that is exactly 16,384 bytes with no header, on a disc that writes
`BPLCON3` with `LOCT`, is 4,096 colours and not 8,192.**

Two corroborating AGA registers on the same disc, also copper-only:
`BPLCON0 = 0x0210`, which is `BPU3` set with `BPU2..0` clear — **eight
bitplanes**, a value that does not exist on OCS or ECS — and `FMODE` at
`0x400F`, the widest AGA fetch mode. And it writes `BPL7PT` and `BPL8PT`, which
earlier chip sets do not have.

**And corroborate it in the code, or in the copper list, which is cheap and
unambiguous.** [Speris]
writes its palettes like this:

```
move.w  #$0000,$DFF106      ; BPLCON3, LOCT = 0  -> high nibbles
move.w  #$0000,$DFF180      ; COLOR00
move.w  #$0200,$DFF106      ; BPLCON3, LOCT = 1  -> low nibbles
move.w  #$0000,$DFF180      ; COLOR00
```

Two passes over the same colour register with `BPLCON3`'s LOCT bit toggled is
the AGA 8-bit-per-gun write and nothing else. **Histogram `$DFF106` against
`$DFF180`**: 47 against 46 on this disc. Paired counts of those two registers
settle the question without touching a palette file at all.

**And six bitplanes with no `BPLCON3` is Extra-Half-Brite, which is an ECS
answer.** [HeroQuest II] writes `BPLCON0 = $5000` (BPU = 5) for the top of its
320 x 200 screen and, after a copper `WAIT` at raster line 204, `$6000`
(BPU = 6) for the bottom 60 lines — with **`BPLCON2 = $0024`, leaving `KILLEHB`
(bit 9) clear** and `BPLCON3` never written anywhere on the disc, so colour
registers 32–63 can never be loaded. Six planes, KILLEHB clear, registers 32–63
untouched: the deep strip is genuine EHB and behaves identically on OCS, ECS and
AGA. **When you find `BPU = 6` and no `BPLCON3`, check `BPLCON2` bit 9 before
concluding the disc needs AGA — and if it is clear, it does not.**

**AND THE SECOND SIGHTING IS A WHOLE GAME, NOT A STRIP.** [Universe] runs its
*entire* display in EHB: `BPLCON0 = $6200` (BPU = 6, and `BPU3` at bit 4 is
zero, so the naive read of bits 14–12 happens to be right here),
`BPLCON2 = $001B` with bit 9 clear, exactly 32 colour registers written and
every value ≤ `$0FFF`, no `BPLCON3`, no `BPLCON4`, no `DIWHIGH`. **The only AGA
register the disc touches anywhere is `FMODE`, written once, with zero** —
which is the write that makes AGA silicon fetch like ECS. A 1994 CD32 release
whose relationship with the CD32's graphics hardware is one instruction telling
it to get out of the way.

That disc also makes the practical consequence concrete. Its pictures are
`6 x 8,000` separated planes plus a 64-byte 32-entry `$0RGB` palette, and
**a renderer with 32 entries and no EHB draws every value 32–63 wrong** — which
looks exactly like a bad stride and is not one. If a planar render comes out as
structured noise, check the plane count against the palette size before you go
looking for the geometry. Rendering the planes one at a time as monochrome
settles it in seconds: six coherent images and two solid stencils is a
different answer from six streams of noise.

*Count.* This is the one that decides whether the disc **needs** AGA, and it
is a two-line test. OCS and ECS reach 64 colours only through
**Extra-Half-Brite**, in which entries 32–63 are entries 0–31 at half
brightness:

```python
def half(w): return ((w>>8&15)//2)<<8 | ((w>>4&15)//2)<<4 | (w&15)//2
ehb = sum(1 for i in range(32) if pal[32+i] == half(pal[i]))   # 32 => EHB
```

[Marvin] scores **0 of 32** on eight of its nine tile palettes (2 of 32 on
the ninth, by coincidence), with 107 distinct colours in one 128-entry file.
Arbitrary 64- and 128-colour palettes cannot exist on ECS, so this disc
genuinely requires AGA.

**AND A DISC CAN CARRY TWO DIFFERENT AGA SCREENS AND SWITCH BETWEEN THEM,
SO READ EVERY `BPLCON0` IN THE FILE, NOT THE FIRST ONE.** [Banshee]'s chip data
hunk holds two copper-list templates that differ in five registers:

```
game     BPLCON0 $0211   BPU = 8, lores, ECSENA        BPL1MOD = 112
picture  BPLCON0 $8211   BPU = 8, HIRES, ECSENA        BPL1MOD = 552
```

with the same `DIWSTRT $2c81` / `DIWSTOP $2cc1` (320 colour clocks, i.e. 320
lores or **640 hires** pixels), the same `DDF`, the same `FMODE $0007` — 64-bit
bitplane fetch, which eight planes in hires needs — and the same palette
apparatus: **sixteen blocks of `BPLCON3` + 32 `COLORxx` moves**, banks 0–7 once
plain and once with `LOCT`, i.e. **256 colours at 8 bits per gun**. `BPLCON2` is
`$0224`, so `KILLEHB` is set and the EHB ambiguity above does not arise.

Note the trap in `BPLCON0` itself, which is the reason to compute the plane
count rather than read bits 14–12: `$0211` has **zero** in the classic `BPU`
field and **bit 4 (`BPU3`) set**, so a scan that reads three bits reports zero
bitplanes on an eight-plane screen.

**Second instance, on an unrelated disc:** [Fire & Ice]'s game screen is
`BPLCON0 = $0611` — again zero in bits 14–12, again `BPU3` set, again eight
bitplanes, this time with `DBLPF` so they are two four-plane playfields. Two of
thirteen discs now have an eight-plane screen that a three-bit scan calls
empty, and both are the *main* display rather than a curiosity. **Always
compute `BPU = ((v >> 12) & 7) | (((v >> 4) & 1) << 3)`.**

**And the picture files are the display, byte for byte**: 164,864 bytes each,
being 1,024 bytes of 256-colour palette in exactly the `BANK`/`LOCT` word-pair
form the copper wants, followed by 163,840 bytes of 640 × 256 interleaved
eight-plane bitmap. When a disc's pictures are the same size as its screen plus
a round number, **the round number is the palette and it is in hardware
format**.

**AND HAM8 EXISTS ON THIS FORMAT, ON A DISC WHOSE GAME NEVER USES IT.** The
same disc's unreferenced second executable displays a **640 × 512 interlaced
HAM8** image: `BPLCON0 = $8A14` — `HIRES` (15), `HOMOD` (11), `BPU3` (4) and
`LACE` (2) — eight bitplanes, a **64-entry** 24-bit palette, and hand-rolled
interlace (two subroutines that rewrite the eight bitplane pointers, one adding
one interleaved row, alternating on `VHPOSR`). Two things to carry: **a
64-entry palette with eight bitplanes is the signature of HAM8**, because HAM8
indexes 64 base colours with six data bits; and **the plane order need not be
the display order** — this one is rotated by two so that the six *data* planes
come first in memory and the two *control* planes last, which is sensible for a
converter to do and fatal for a renderer to guess.

**Where the graphics are IFF, the plane count is free, and it is the strong
evidence.** [Prey CD32] ten of its fourteen ILBM screens have
`BMHD.nPlanes == 8` — 256 colours, which no ECS Amiga can display — and their
`CAMG` is `0x00021000`, plain PAL lo-res, with `0x00029004`
(PAL + HIRES + LACE) on the one 640 x 512 title screen. Read `BMHD` and `CAMG`
before doing anything else with an IFF file.

**The control makes this airtight.** The same six screens on the CDTV release
of the same game, by the same people, are **5 planes and 32 colours**. And
`EVALUATE`'s first 32 `CMAP` entries on the CD32 disc are byte-identical to
the CDTV file's entire palette, with 224 entries added underneath: the
artwork was deepened for AGA, not redrawn. **If two releases of a title exist,
diff the palettes — it tells you what the hardware upgrade actually bought.**

**So do not collapse the two findings.** Dragonstone writes `FMODE = 0` and
runs an ECS display on AGA silicon — a floppy port wearing new hardware.
Marvin needs AGA for its bitplane count and then uses nothing else AGA
offers: no 32-bit fetch, no 24-bit colour, no Akiko. **Prey needs AGA for its
bitplane count *and* uses its colour depth**, and still never touches Akiko.
**Speris does the same, in every level of the game**, and never touches Akiko
either. So the pattern is not "CD32 games ignore AGA": three of four use it
for depth, two of four for colour, and **one of four touches Akiko** —
Dragonstone, which drives it directly. **AGA used as a deeper ECS** remains
the common case and is worth testing on every disc; a disc that uses the
chunky-to-planar hardware in the *game* is still the thing nobody here has
found.

**And there is a fifth kind of AGA use, which is neither depth nor colour.**
[Gloom] writes `FMODE = $000F`, `BPLCON0` with `BPU = 7`, `BPLCON3` with `LOCT`,
`BPLCON4` and `DIWHIGH` — so it needs AGA on all the usual grounds — but the
register that carries its display is **`BPLCON4`'s `BPLAM`**, which XORs the
bitplane index before the colour lookup. It toggles `BPLAM` between `$80` and
`$00` on alternate rows, and ORs the same flag into the `BPLCON3` bank field, so
each row of the 3D view reads out of one half of AGA's 256 colour registers
while the copper reloads the other half for the row below it. **Grep for
`BPLCON4` ($DFF10C) writes, and if you find them, find out what `BPLAM` is being
used for** — on this disc it is what makes a chunky display possible with no
conversion at all. See "a framebuffer that is a copper list", below.

**AND A SECOND DISC USES `BPLAM` FOR SOMETHING ELSE ENTIRELY: RELOCATING A SHALLOW
DISPLAY INTO A HIGH COLOUR BANK.** [Guardian] writes `BPLCON4 = $80AA` **once**,
statically, at the top of its copper list. `BPLAM = $80` XORs the bitplane index
before the colour lookup, so a **six-plane** display whose indices run 0–63 reads
colour registers **128–191** — which is exactly the two `BPLCON3` banks (4 and 5)
that the same copper list loads, each twice with `LOCT` toggled. The accounting
closes with nothing left over and registers 0–127 are never touched.

Two very different uses of one register, then: Gloom toggles `BPLAM` per row to
double-buffer inside the colour registers; Guardian sets it once to move a
64-colour display out of the way. **If you find a `BPLCON4` write, work out which
range of colour registers the display actually reads before you go looking for a
palette** — because on both discs the answer is "not the ones you would expect".

**One display can be two displays with different plane counts, stacked.**
[Guardian]'s copper list opens with `BPLCON0 = $6201` (six planes) and
`BPL1MOD = BPL2MOD = $C8 = 200`, and its `DIWSTRT`/`DIWSTOP` give a 239-line
window from raster line 48. Two bitplane-pointer loops in the code say what those
239 lines are:

```
lea   copperlist+BPL1PTH,a0 / move.l panelbuffer,d0
moveq #5,d1     ; SIX planes      moveq #$28,d2  ; 40-byte plane stride
...
movea.l copperslot,a0      / move.l drawbuffer,d0
moveq #3,d3     ; FOUR planes     moveq #$28,d1  ; 40-byte plane stride
                                  moveq #$10,d2  ; 16-byte copper slot stride
```

— a **320 x 38 six-plane HUD panel on lines 48–86** and a **320 x 200 four-plane
3D view on lines 87–286**, and 39 + 200 = 239 exactly. The modulo test in this
section gives the six-plane figure and would have been wrong about the game's own
viewport. **Count the `dbra` in the bitplane-pointer loop, not only the `BPLxMOD`,
and expect a title to change plane count part-way down the screen.**

The same loop is also the cheapest confirmation of interleaving there is: a plane
stride of 40 with a 320-pixel screen means the six (or four) pointers are 40 bytes
apart, which is interleaved by construction.

**Beware the byte pattern `00 B8 00` as evidence of Akiko.** [Speris] has 32
of them and uses Akiko not at all: every one is inside a palette or an offset
table. [Gloom] has 45 in its executable and eight of them are **consecutive
entries of one descending 16-bit table** (`… 00c3 00b8 00ae 00a4 …`), which is
the false positive in its purest form.

**AND THAT TABLE IS NOW IDENTIFIED, ON A SECOND DISC.** [HeroQuest II] has six
bare hits in its code hunk and two of them are inside the *same four words* —
`00c3 00b8 00ae 00a4` — that Gloom shows. It is **ProTracker's chromatic period
table**: 36 entries from 826 down to 109, successive ratios 0.944 = 2^(−1/12),
three octaves, with `$00B8` = 184 as entry 33. Any Amiga program that ships a
tracker replay ships this table, which is most of them. **The `00 B8 00` false
positive is not a coincidence of one disc; it is a property of the platform's
music code, and finding it should reassure you rather than delay you.** The test that means something is a
**pointer load** — `movea.l #$B80000,An`, `lea $B80000,An` — or a reference to
`$B80038`, the C2P port, or the `$C0DE0000` identification constant. All four are
zero on both.

### A framebuffer that is a copper list

**[Gloom]** is the disc that shows a CD32 title can rasterise in chunky and still
have nothing for Akiko to do, and the mechanism is worth carrying because it is
cheap to recognise.

The tell is an allocation whose size is **four bytes per pixel**:

```
move.w  $c(a2),d0           ; width
move.w  d0,d1
subq.w  #1,d0
lsr.w   #5,d0               ; (width-1) / 32
addq.w  #3,d0
add.w   d1,d0               ; width + (width-1)/32 + 3
lsl.w   #2,d1 ... move.w d1,$30(a2)   ; bytes per row
mulu.w  $e(a2),d0           ; x height
addq.w  #4,d0
lsl.l   #2,d0               ; x4
moveq   #2,d1               ; MEMF_CHIP
... lsl.l #1,d0 ...          ; x2, double buffered
```

Four bytes per pixel is not a pixel format, it is a **copper instruction**, and
the accounting closes with **no slack at all**: for width 90 the 95 longwords are
90 `COLOR` moves + 3 `BPLCON3` bank switches + 1 `WAIT` + 1 `BPLCON4`, and for
width 66 the 71 are 66 + 3 + 1 + 1. The emitter writes, per rendered row, a
`WAIT` at that raster line (`VP, $E1, $FFFE`), then one
`MOVE COLORnn, <value>` per pixel with the register index counting **down** from
127, then `BPLCON4`.

**And the skeleton is built once per screen, not once per frame** — which is the
first thing to check before costing the technique. On [Gloom] the builder has
**no direct callers**: it is reached only by the fall-through from the screen
constructor, which runs at screen open, and the per-row `WAIT` emitter is called
from two sites, both inside the builder. So the register numbers, the bank
switches, the `WAIT`s and the `BPLCON4` writes are static, and a frame changes
**two bytes out of every four** — 16,200 B for a 90 x 90 view, 7,920 B for
66 x 60. **Trace the builder's callers before assuming a per-frame cost.**

Underneath it, the bitplanes hold a **fixed descending ramp of colour indices**
— 127, 126, 125 … each repeated `xscale` times — written once at screen creation
by the only chunky-to-planar loop in the program: seven `bset`/`bclr` per pixel
at a 40-byte stride, over one row, over a constant. **A per-pixel `bset`/`bclr`
planar plotter is not necessarily a renderer; check what it is writing and how
often it runs before calling it the C2P.**

Three consequences worth carrying to the next disc:

* **The frame's pixel value is a colour, not an index.** Gloom picks a 12-bit
  `$0RGB` word out of one of sixteen pre-shaded copies of the level palette, so
  what the renderer writes is already a copper `MOVE`'s data word. If you find a
  table of N progressively darkened copies of a palette, the renderer is
  probably not writing indices at all.
* **The technique has a hard ceiling of one row per colour bank.** Seven
  bitplanes give 128 distinct indices, so a row cannot be wider than 128 pixels.
  Gloom's 3D views are 90 x 90 and 66 x 60 (doubled to 180 x 180 and 132 x 120);
  its 320-wide screen descriptor is the one the menus and title pictures use,
  which is an ordinary planar bitmap with a 128-colour palette copper.
* **It is not an extra pass, it is the only pass.** There is no chunky buffer,
  so the rasteriser's store *is* the copper-list write. For the same 8,100
  pixels a chunky-buffer-plus-C2P route moves 8,100 B written + 8,100 B read
  back + 7,087 B of planar output = **23,287 B** plus the conversion; the copper
  route moves **16,200 B**, once, with no read-back and no ALU work. The price
  is two bytes per pixel where a planar bitmap costs seven-eighths of one, which
  is why the view is a window.
* **The binding constraint is copper DMA, and it sets the geometry.** A copper
  `MOVE` takes two DMA slots and a `WAIT` three; a PAL line offers on the order
  of 113 slots. A 90-pixel row block is 94 `MOVE`s and a `WAIT` = **191 slots
  against ~226** in the two scanlines it covers — **85 %**. Which is why
  `yscale = 2` exists at all (at 1:1 there would be ~113 slots for 191 slots of
  work), and why the width ceiling is **~108 pixels** — 217 free slots after the
  fixed six, before bitplane DMA takes anything — rather than the 128 the
  seven-bitplane palette would allow. The widest view shipped is 90. **Do this
  arithmetic before believing a width you have only read out of a table.**
* **A display like this makes the widest AGA fetch mode look like a bandwidth
  decision.** Gloom writes `FMODE = $000F` for a 320-pixel lores screen, which
  needs nothing like it for width; what it does need is bitplane DMA out of the
  copper's way. That is an inference, not a measurement, and it wants an
  emulator trace to confirm — but on any disc that drives the display from the
  copper, read `FMODE` as a bandwidth setting first.

Two structural reasons a CD32 title will refuse Akiko even when its authors
can drive it, both visible on Marvin's disc without any disassembly:

* **The same binary has to run on an A1200.** Marvin ships `<Game>.info`
  with `DefaultTool = IconX`, and ships `lowlevel.library` and
  `nonvolatile.library` in `libs/` because an A1200 running Workbench 3.0
  does not have them. Akiko exists only on the CD32, so a C2P renderer would
  have meant maintaining two display paths.
* **There is a floppy SKU.** The plain-text DISKMAP compiled into the CD32
  executable assigns every asset to one of three floppies. The CD build is
  the floppy build plus Red Book audio and an intro animation.

Marvin's programmer knew all of this: the C2P demo he left on the disc
carries a note saying *"'ROTATE' really work's only on systems, supporting
the c2p hardware..."*, and its own header is dated **© 1993/4** while the
game's is **© 1992/3/4**. The engine predates the console.

**A sprite container can compress without a codec, and it changes what the
census means.** [Liberation]'s `ImgA` containers store six plane pointers per
image and **a pointer of zero means that plane is all zeros and is not
stored**; two pointers may also hold the same offset and share one buffer. The
declared size counts only the distinct stored planes, so `MainSp.img` holds
158 images in 51,460 bytes where six full planes each would be 77,052 — 1.5:1,
free, with no decompression and no buffer. **A container whose per-image size
field is smaller than width × height × planes / 8 is not necessarily
compressed; check for a sparse plane table first.**

**And a "3D" game may not texture-map at all.** [Liberation]'s 71
`Wall*.VGM` files are 11.9 MB and every one is **exactly 167,766 bytes** with
the identical bank structure — four `AmSp` banks of 42, 45, 24 and 41 sprites,
same width, height, plane count and mask flag in all 71, walk landing on the
file size to the byte. Rendered, they are **pre-computed perspective
projections of one wall face** at dozens of angles, four planes plus a
one-bit mask, blitted by view. 10,792 sprites doing the job of a texture
mapper. **When a first-person game's largest asset family is a set of
identically-sized sprite banks, render one before assuming it is a texture
set.**

Palette files are usually raw and headerless: a run of big-endian `$0RGB`
words, sized 2 x the colour count (256 bytes = 128 entries, 64 bytes = 32).
The entry count often exceeds the plane count of the bitmap beside it, which
tells you the display is deeper than the layer and that the layers occupy
colour banks.

**A chip-RAM image is a thing you will meet.** [Dragonstone] One file unpacks
to a straight snapshot of chip memory — copper lists at the front, the rest
mostly zeroes, with two islands of bitmap. 87 % of the file is empty because
the buffers are part of the snapshot. Do not read it as a container; read it as
memory, and follow the copper's `BPLnPT` values into it.

### The polygon filler is a Blitter cookie-cut, one per scanline

**[Guardian]** is the disc that shows what a *classic* Amiga answer to real-time
polygons looks like, and it is worth having beside Gloom's copper framebuffer
because the two are opposite solutions to the same problem.

The frame buffer is an ordinary **interleaved four-plane 320 x 200 bitmap**,
32,000 bytes, double-buffered out of one 160,000-byte `MEMF_CHIP|MEMF_CLEAR`
allocation split four ways. The rasteriser sets the Blitter up **once per
polygon**:

```
BLTCON0 = $07CA      USEB|USEC|USED, USEA clear; minterm D = (A AND B) OR (NOT A AND C)
BLTADAT = $FFFF      A is a constant -- only BLTAFWM/BLTALWM modulate it
```

and then, **once per scanline**:

```
BLTAFWM:BLTALWM      one longword out of a 43,520-byte lookup table, indexed by the span ends
BLTBMOD = BLTCMOD = BLTDMOD = 40 - width
BLTBPT  = the dither pattern for this face's shade
BLTCPT  = BLTDPT = the screen row
BLTSIZE = (4 << 6) | words        <- height 4 = the four interleaved planes
```

Height four with a modulo of `40 − width` walks plane 0 to plane 3 of the *same*
screen row, so **one Blitter operation paints one polygon scanline across every
bitplane**. There is no chunky buffer, no `bset`/`bclr` plotter, and **no
`BLTCON1` write anywhere in the program** — no area fill, which is the technique
an Amiga polygon engine traditionally uses and this one does not.

Four things to take to the next disc.

* **The lookup table is the trick.** 43,520 bytes indexed by pixel column giving,
  per column, the containing word's byte offset and the first/last word masks. The
  inner loop turns an X coordinate into a complete Blitter set-up with four table
  reads and **no shifts at all**. A large table with no obvious content, read with
  `d16(An,Dn.w*8)`, is worth identifying before you read the loop around it.
* **The routine steals `a7`.** It saves the stack pointer to a variable, uses `a7`
  as the table base for the whole polygon, and restores it on exit — so nothing
  inside is a subroutine call. **A `move.l a7,<abs>` early in a rendering routine
  is not a bug; it is a seventh address register.**
* **Two colours per face, and the winding test picks one.** The 2D cross product
  is computed with `muls.w`/`sub.l` and then **stored** with `sge.b` rather than
  branched on; the sign selects the high or low byte of a 16-bit colour word, and
  a byte of zero means "do not draw this side". Back-face culling and per-side
  shading are the same three instructions.
* **The dither pointer advances by the row stride, not by the polygon.** It steps
  ±160 bytes per scanline — exactly one interleaved row — so the pattern is
  **screen-aligned**, and two adjacent faces of the same shade tile without a
  seam. **If you find a shading table indexed by a colour byte, check what the
  pointer into it does between scanlines**; screen-aligned and polygon-aligned
  look identical in one frame and completely different across two.

The edge walker uses `divs.l` and `muls.l` with 32-bit operands, so the renderer
is **68020-only** — it cannot run on a 68000 at all, which is a constraint worth
noting on a format where most titles are careful to stay portable.

### Finding block geometry with no header

Measure the row pitch by byte autocorrelation: for each candidate stride, count
`d[i] == d[i+stride]` over a sample of the data. A real bitmap gives a **sharp**
peak at its pitch. [Dragonstone] one file scores 0.695 at stride 16 against
0.491 at 14 and 0.495 at 18 — 32 pixels x 4 interleaved planes, unambiguous.

Be honest about when it fails. On the same disc the tile banks give a smooth
decay with no peak above the pixel level, and every plausible sheet geometry
renders as noise, while zlib and entropy both say the data is raw pixel art.
When that happens the missing piece is an *index*, not a stride: look for a
directory file whose records hold two file pointers each and follow those
instead of guessing.

**Scan wide, not narrow, and read the harmonics.** [Marvin] a scan to stride
160 gives one file a weak peak at 40 and nothing convincing; scanning to
1,300 gives a clean 240/480/720/960 family, and 240 = 6 x 40 is the answer —
six planes, 320 pixels. The series is the signal. Then *render it* at the
candidate plane counts and look: five, six, seven and eight planes side by
side settle in one glance what the numbers leave ambiguous.

**A size that is not a whole number of rows means a header, a trailer or a
buffer** — work through those three in that order. [Marvin]'s parallax layers
are 216 x 209 + 40 at a pitch that renders undistorted, with content stopping
at 70 % of the file; still unresolved there.

**Collision and attribute tables are usually a flat array indexed by the map
cell, and the sizes say so.** [Marvin] map cells range 0-811, and each world
has an 8,200-byte `setNN.characteristics`: eight bytes of header and **1,024
records of 8**, one per possible cell, mostly zero. Matching the maximum cell
value in the level data against a table's record count is a thirty-second
check that identifies the file.

---

## 8. Audio

**First: check whether there is a Red Book track at all — and then check
whether anything plays it.** [Microcosm] has one 203.0-second track of genuine
44.1 kHz stereo, continuous music to 195 s and then a clean fade to digital
silence, and **no code on the disc ever plays it**. Scanning every `io_Command`
immediate in the executable and all seventeen overlays finds `CMD_READ`,
`TD_MOTOR`, `TD_ADDCHANGEINT`, `CD_INFO`, `CD_CONFIG`, `CD_READXL` and
`CD_READ`, and no `CD_PLAYTRACK` (38), `CD_PLAYMSF` (39), `CD_PLAYLSN` (40),
`CD_PAUSE` (41) or `CD_ATTENUATE` (45).

That is a cheap and worthwhile check on any disc with an audio track, because a
CD32 has **one mechanism**: a title that streams data off the drive continuously
cannot play Red Book at the same time, and on this one 92 % of the data track is
a video stream. **Histogram the `io_Command` immediates — `move.w #n,$1c(An)`,
which assembles as `3?7c 00nn 001c` — before assuming the audio track is used.**

**AND ATTRIBUTE EVERY `io_Command` TO THE `IORequest` IT IS WRITTEN INTO,
BECAUSE THE SAME NUMBER MEANS DIFFERENT THINGS.** [HeroQuest II] opens
**`cd.device` twice and `input.device` once**, and its five `io_Command`
immediates are 9, 10, 33, 37 and 41. Read as `cd.device` commands, 9 and 10 are
`TD_MOTOR` and `TD_SEEK` — a game spinning up a drive and seeking. They are
nothing of the kind: both are written into the `IORequest` that
`OpenDevice("input.device")` filled in, with an `Interrupt` structure in
`io_Data`, and for `input.device` 9 is **`IND_ADDHANDLER`** and 10 is
**`IND_REMHANDLER`**. The game is installing an input handler.

A `OpenDevice` count of zero makes every `io_Command` hit a false positive
(Gloom); a count of three **to two different devices** makes half of them mean
something else. **Find each `OpenDevice`, note which base each `IORequest` came
from, and read the commands per device.**

**AND THE IMMEDIATE MAY NOT EXIST AT ALL.** [Guardian] opens `cd.device`, plays
twelve Red Book tracks, and the `3?7c 00nn 001c` histogram returns **zero**,
because the whole request is filled in from registers by two generic wrappers:

```
move.w  d0,$1c(a1)      ; io_Command
move.l  d1,$24(a1)      ; io_Length
move.l  a0,$28(a1)      ; io_Data
move.l  d2,$2c(a1)      ; io_Offset
jsr     -456(a6)        ; DoIO      -- and an identical SendIO twin
```

So the commands are `moveq` constants at the **call sites of the wrapper**, not
immediates at the request. Find the wrappers first (a `move.w Dn,$1c(An)` is the
tell), then enumerate their callers — **and include `jmp` as well as `jsr` and
`bsr`**, because on that disc two of the four call sites are tail calls and a
`jsr`-only search finds half of them.

**Then read what the disc does with the table of contents, because it decides
how many tracks are reachable.** Guardian issues `CD_CONFIG` (33), `CD_TOCMSF`
(34) with `io_Length` 100 into a 600-byte buffer, `CD_INFO` (32) as a status
poll, and `CD_PLAYTRACK` (37) through `SendIO` — and between the TOC read and the
play it runs this:

```
move.b  (a0),d2         ; the CONTROL nibble of a TOC entry
andi.w  #$d0,d2
cmp.w   #$40,d2         ; bit 6 set = a DATA track
beq.s   skip            ; ... so skip it
move.b  $1(a0),(a1)+    ; otherwise keep the track number
addq.w  #1,d1
addq.w  #6,a0
dbra    d0,loop
```

**A title that filters the TOC by its CONTROL bits has no track table to find and
every audio track is reachable** — the opposite of HeroQuest II, whose track
numbers are `moveq` constants and which can reach two of five. Three states,
then, and they are worth distinguishing: plays by constant (some tracks
reachable), plays out of the TOC (all of them), plays nothing at all
(Microcosm).

**And run one cheaper check first: count `OpenDevice` (exec −444).** [Gloom] has
**zero** — no device of any kind is opened anywhere in its executable, and
`cd.device` is not a string on the disc. That settles the question in one grep
and it also makes the `io_Command` histogram interpretable: the single `3?7c
0002 001c` hit in that file cannot be a command because there is nothing to
command, so it is a coincidence in data. **A zero `OpenDevice` count turns every
`io_Command` hit into a false positive; do the histogram anyway, but read it in
that light.**
The presence of a finished, mastered, faded piece of music that nothing triggers
is itself a finding about when the design changed.

**And it can be a subset rather than all of it, which is harder to notice.**
[HeroQuest II] has **five** audio tracks, 31 min 42 s, and plays two. There is
exactly one `CD_PLAYTRACK` (37) call site, reached with `moveq #2,d0` or
`moveq #3,d0`, and the "the track finished" handler is a strict toggle
(`if 2 -> 3, if 3 -> 2`). **Tracks 4, 5 and 6 — 7 min 15 s, 9.8 % of the whole
disc — are named by no constant anywhere.** A disc that plays *some* Red Book
passes the "does anything play it" check and can still be leaving a third of its
soundtrack unreachable, so **find the call site and read the constants that
reach `io_Offset`, not just the command number.** Note also that this title
never calls `CD_TOCLSN` (35): it plays by track number, so there is no
table-of-contents read to find and the numbers are all in the code.

**And the negative case scales badly, which is the point of recording it.**
[Fire & Ice] has **twenty-two** audio tracks and reads no TOC at all: no
`CD_TOCMSF`, no `CD_TOCLSN`, no `CD_INFO`, no `CD_GETNUMTRACKS` in any
`io_Command` write. It writes exactly four commands — `CMD_START` (10),
`CMD_STOP` (9), `CD_PLAYTRACK` (37) and `CD_PAUSE` (40) — and the play routine
is

```
move.l  (pc+..),d0        ; track index, negative means play nothing
add.l   (pc+..),d0        ; + 2, a longword constant in the code hunk
move.w  #$25,$1c(a1)      ; CD_PLAYTRACK
move.l  d0,$2c(a1)        ; io_Offset = track number
move.l  #1,$24(a1)        ; io_Length = 1 track
```

so the mapping between game music and physical track is `index + 2`, baked in.
Guardian reads its own TOC and filters by the CONTROL bits, which is what makes
all twelve of its tracks reachable; Banshee and Fire & Ice name tracks as
constants. **Twenty-two tracks addressed by a hard-coded base is the widest
version of this so far**, and a disc pressed with its tracks in another order
would play the wrong music silently.

**A caution about how to look, from the same disc.** A scan for `moveq #34,dN`
and the other command numbers returns *sixty* hits in that 92 KB program and
every one checked is an absolute address or a data byte that happens to encode
as `moveq` — `move.l $7022.l,d0` matches `moveq #34,d0` byte for byte if the
scan does not respect instruction boundaries. Six further sites write a
register into offset `0x1c` of a structure, and all six turn out to be **game
objects, not IORequests**. Only five immediate writes survive checking, and
what makes them survivable is that each one loads the request pointer from the
same variable two instructions earlier. **Anchor the io_Command scan on the
IORequest pointer, not on the offset `0x1c`.**

**A THIRD ANSWER TO THE TOC QUESTION, AND IT MAKES THE WHOLE `io_Command`
METHOD INAPPLICABLE.** [Universe] plays **23 Red Book tracks, 40:37**, and
calls `OpenDevice` **zero** times. Its loader goes `SuperState()`, masks the
interrupts and clears `DMACON` before the game starts, so there is no
`cd.device`, no `IOStdReq`, no `io_Command` and no `io_Offset` to scan for at
all. The game reaches the drive by driving **Akiko** directly — the CD-ROM
interface at `$B80004`, `$B80008`, `$B80010`, `$B80014`, `$B80018`–`$B8001F`,
`$B80020` and `$B80024`, with a hand-written service routine that tests bits
26–31 of `$B80008 AND $B80004` and then reads CIA-B's `$BFED01`.

So the column now reads: **reads the TOC and filters by CONTROL** (Guardian),
**names tracks as constants in `io_Offset`** (Banshee, Fire & Ice), and
**bypasses the OS entirely and builds the command in Akiko's register block**
(Universe). Count `OpenDevice` first, as this section says — but read a zero as
"look at `$B80000`", not as "no CD audio". How many of Universe's 23 tracks the
game can reach is open, because no literal track number survives in either
executable.

Also: [Prey] there is
not — one `MODE1/2048` track and nothing else, on a disc that carries
**63 minutes 40 seconds of speech and atmosphere as ordinary files**. A CD32
game with no audio track is not a data disc and not a bad rip; it may be a
game that streams everything through Paula because it needs the drive for
data at the same time. Four places to look, and a CD32 game may use all
four:

* **Red Book tracks** — read the cue sheet. Check whether the audio is real
  stereo or mono in a stereo container, where it fades, and how much digital
  silence is padded on. [Dragonstone] one track, 118.08 s, genuine stereo,
  -0.8 dBFS peak, 2.4 s of silence at the tail.
* **Or interleaved into the video stream** — [Microcosm] puts ten runs of raw
  8-bit PCM, 864,252 bytes in total, *between* frames inside its 483 MB video
  container, all of them in one stretch of eleven consecutive movies. They
  arrive in the same `CD_READXL` transfer as the picture and cost no extra seek.
  A chunk walker that stops at the first unparseable byte will report the file
  as truncated; resynchronise on the frame magic instead and measure what the
  gaps contain.
* **Raw 8-bit signed PCM** for Paula samples, usually stored **uncompressed**
  because there is nothing to gain on a few kilobytes — so these are often the
  only files on the disc that are not packed, which makes them easy to spot in
  a census.
* **Streamed raw PCM as ordinary files** — [Prey] 1,225 files of exactly
  61,440 bytes, 75.3 MB, 68.6 % of everything on the disc. See below.
* **Or one file per *bank* with an index beside it** — [Liberation] stores
  **195 minutes of speech in ten files**, each a bare run of `FORM 8SVX` with
  nothing between the samples, and a `.LOG` beside it that is nothing but
  `'  LG'` and a list of 32-bit file offsets ending with the file size as a
  sentinel. That is the same amount of speech as Prey in 1/125th of the
  directory records. **If a disc has huge files with no header and a small
  file of the same name beside them, read the small one as an offset table
  first.**

  Two things fall out of that index. **An entry of `0xFFFFFFFF` means the line
  was never recorded**, and there are 63 of them, so the index is also the
  production status of the voice sessions. And the sample rate is in each
  clip's own `VHDR`, chosen **per line** — `shop1/Voice1` uses fifteen distinct
  rates across 568 clips, from 7,365 to 15,980 Hz — so there is no single
  "the disc's speech rate" to quote.

  The disc also holds the **same script recorded twice**, `Voice1` and `Voice2`,
  with the same number of index entries and different durations, which is two
  actors rather than two encodings. Check the `.LOG` lengths against each other
  before assuming a second file is a copy.
* **OctaMED modules** — magic `MMD0`/`MMD1`/`MMD2`/`MMD3` at offset 0, with a
  32-bit module length at offset 4 that should equal the file size. [Gloom]'s
  two tunes are `MMD1` and the length field matches the decrunched size to the
  byte on both, which is a free check that a decruncher transcription is right.
  A ProTracker sweep misses them entirely: that disc returns **zero** for
  `M.K.`, `M!K!`, `FLT4`, the `NCHN` family, `FORM` and `8SVX` over the whole
  image and both extracted trees. **Scan for the `MMDn` family as well**, and
  read the instrument names — Gloom's are the composer's working names
  (`STRING1MAJ`, `CRESCENDO1`, `TINABEAT1`, `FLUTEBULLY`, `flutebullyhigh`,
  `string+harpsichord`), and the two modules share five of them, so the tunes
  share a sample kit.
* **ProTracker modules** — scan for `M.K.`, `M!K!`, `FLT4`, `4CHN`, `6CHN`,
  `8CHN` at offset 1080 of a candidate. The 20-byte title and the 22-byte
  sample names frequently carry the musician's own filenames verbatim;
  [Dragonstone]'s ending module has a sample slot reading
  `mod.heim(2)xtratune1`. **Ignore the extension.** [Legends] `Title.Mod` is
  a plain 31-sample `M.K.` module, and it is the only file on that disc the
  extension would have got right.
* **IFF `8SVX` linked into an executable** — scan every file, unpacked, for
  `FORM` followed by `8SVX`. [Legends] eight complete `FORM ... 8SVX` samples
  are sitting inside three of the five level executables **with their wrappers
  intact**, so each one still carries the filename it had on the artist's
  machine (`bullet.ss`, `RAYgun.ss`, `COPTER.SS`) in its `NAME` chunk and the
  name of the tool that saved it in its `ANNO` chunk (`Protracker 3.10`). The
  assembler included the file exactly as the tracker wrote it. **This is the
  cheapest tool fingerprint on the format** — one `find` for four bytes — and
  a disc that has it in some executables and not others is telling you about
  its own build process: on that disc the two largest levels have no `FORM` at
  all.

If a scan for all of those turns up nothing and the game clearly has music,
it is an in-house player with no magic word — look in the resident loader
first, and then at the data files themselves.

**And when there *is* a Red Book soundtrack, read how the game addresses it.**
[Legends] 28 tracks, 65 minutes 36 seconds, **88.6 % of the disc**, driven by
about 120 bytes of code: `OpenDevice("cd.device", 0)`, one `DoIO` with
`IO_COMMAND = 35` to read the table of contents into a 100-byte buffer, and
then `IO_COMMAND = 39` with `IO_OFFSET`/`IO_LENGTH` taken from a TOC entry,
issued with **`SendIO`** so the game never blocks on the drive. Stopping is
`AbortIO` + `WaitIO`.

The consequence for reading the disc: **a game that plays out of the TOC has
no track table to find**. There is no list of track numbers in the executable
because the numbers come off the disc at runtime. Histogram the `4E AE`
offsets for `-444` (`OpenDevice`), `-462` (`SendIO`) and `-480` (`AbortIO`)
and read the `IO_COMMAND` immediates instead; the two that matter are 35
(`CD_TOCLSN`) and 39.

### AND A DISC CAN USE TWO OF THE FIVE PLACES AT ONCE

[Myth] has no audio track and uses **place 1 and place 2 together**: two OctaMED
`MMD0` modules that each occupy a whole asset chunk, and two IFF `8SVX` samples
**inside a hunk executable**, invisible to any census of files. The modules are
validated by their own declared length matching the chunk to the byte, and the
8SVX carry `ANNO` chunks naming the tool — `Audio Master` on one and
`Audio Master II` on the other, two versions of one sampler on one disc.

Two counts worth taking on any module: **how many instrument slots are empty**
(2 of 18 here) and **how many are named** (**0 of 18** — both modules were saved
with a two-byte `iinfo` entry, so there is no room for a name and the composer
has to come from the credit screen). And check the play sequence against the
block count: one of Myth's two modules never plays block 2 of its four.

### A FIFTH PLACE FOR THE MUSIC, AND A `M.K.` SCAN CANNOT SEE IT

The four places this document has listed — ProTracker-family modules, IFF
`8SVX`, raw PCM, an in-house player — missed a whole category, and
[Superfrog] is where it showed up.

A scan of that disc for `M.K.`, `M!K!`, `M&K!`, `FLT4`, `FLT8`, `4CHN`, `6CHN`,
`8CHN`, `OCTA`, `CD81`, `MMD0`, `MMD1`, `MMD2` and `MMD3`, at **every byte
offset** and with the ProTracker header validated (song length 1..128, order
bytes <= 127, sample volumes <= 64), returns **zero**. The disc has no Red Book
track, so the music has to be somewhere, and it is:

```
SFData/L1MU  ->  50 34 31 41 ...      'P41A'   The Player 4.1A
SND/P40.INGAME1  ->  50 34 30 42 ...  'P40B'   The Player 4.0B
```

**The Player** is a replayer that stores a converted module in its own layout.
Its four-byte magic **is the version string**, so it matches neither a tracker
scan nor any cruncher magic, and a census over file heads calls it "unknown
data". Superfrog carries **37 validated modules**, 26 `P41A` and 11 `P40B` —
two versions on one disc, matching its two development houses.

Header, read from the files rather than from a format description:

```
+0   char[4]  magic, the version string
+4   UBYTE    number of patterns
+5   UBYTE    a sample-related count -- 32, 33 and 36 all occur, so it is NOT
              "samples used, of 31"; do not bound it at 31 or you will reject
              three of the nine modules
+6   UBYTE    song length in positions
+7   UBYTE    0
+8   ULONG    offset of the sample-descriptor table
+12  ULONG    offset of the pattern-offset table
```

Validate structurally: byte +7 zero, song length and pattern count in range,
and both table offsets non-zero and inside the file.

**What to do on the next disc.** Add `P41A`, `P40A`, `P40B`, `P50A`, `P60A` and
`P61A` to the magic list, and treat "no tracker module and no Red Book" as a
**prompt to look for a replayer format**, not as evidence that the music is
elsewhere. The general lesson is wider than one packer: **a replayer whose magic
is its own version string is invisible to both of the scans this document
tells you to run**, and the only thing that finds it is looking at the first
four bytes of a file whose *name* says music.

Superfrog also supplies the confirmation for free — a file **named**
`P40.INGAME1` whose first four bytes are `P40B`. When a filename and a magic
agree, that is the cheapest identification available; look for it.

Two more things from that disc, both already stated elsewhere but worth
repeating here because they are section 8's business:

* **Count `OpenDevice` first even on a silent disc, and then cross-check.**
  Superfrog has no audio track and a non-zero `OpenDevice` — four calls. Cross
  checking against the device-name strings resolved it immediately and
  harmlessly: `trackdisk.device` in the Arcade Pool demo and `input.device` in
  the Super Stardust demos. **No audio device anywhere.** A count on its own
  would have looked like a lead.
* **Samples live inside binaries.** 27 IFF `8SVX` on that disc and **all 27
  inside one executable**, in the 1.44 MB of a "code" hunk that carries no
  relocations. A census over files sees zero. This is the second disc where
  that is true, after Gunship's fifteen.

### Telling raw PCM from everything else, and finding its rate

**Three cheap measurements identify raw 8-bit signed PCM with no header.**
[Prey] on 61,440-byte files with no magic of any kind:

| | script chunk | a known 8SVX `BODY` | a bitmap file |
|---|---:|---:|---:|
| mean absolute delta between adjacent bytes | 0.8 - 3.5 | 2.4 - 5.9 | 24.9 |
| sign changes | 2 - 11 % | 7 - 12 % | 13 % |
| spectral energy median | 0.04 of Nyquist | 0.04 | — |

Then **plot the envelope**. Speech is unmistakable: syllable-shaped bursts
with silence between them. A bitmap never looks like that.

**Or the file may carry its own period, in four bytes.** [Gloom]'s 24 effects
begin `UWORD Paula period, UWORD length in words`, and `4 + 2 * length ==
filesize` on **all 24** — which identifies the header without disassembling the
player and gives a per-effect rate. Eight of the 24 use period 321 (11,050 Hz),
the studio default; the rest were pitched by ear, down to 870 (4,077 Hz) for a
door. **Test `4 + 2 * n == filesize` on the first longword of any headerless
sample family before assuming there is no header.**

**Otherwise the sample rate is in the executable, as a Paula period.** There is
nowhere else for it to be in a genuinely headerless file. Search for immediates written to
`AUD0PER`/`AUD1PER`/`AUD2PER`/`AUD3PER` (`$DFF0A6/B6/C6/D6`) — both
`move.w #imm,$00DFF0x6` and `move.l #imm,d0` / `move.w d0,$00DFF0x6` — and
convert: **PAL rate = 3,546,895 / period**. [Prey] fourteen distinct periods
from 128 to 1500; the one used on the two channels that stream the scenes is
**180 = 19,705 Hz**.

**Cross-check it against the file sizes, both ways.** `AUDxLEN` is a *word*
count, so double it:

* [Prey] `move.w #$7800,AUD3LEN` = 30,720 words = **61,440 bytes = exactly one
  scene chunk**, and `#$F000,AUD2LEN` = two. The file format *is* the DMA
  buffer.
* `move.w #$415D,AUD0LEN` = 16,733 words = 33,466 bytes, which is the exact
  size of two of the sample files. Three more immediates match three more
  files exactly.
* Any `AUDxLEN` immediate that is *shorter* than half a file is a sub-sample
  inside a **sample bank**: several effects concatenated with the offsets and
  lengths compiled into the code, so there is no index on the disc to find.

Two of Prey's periods (200 -> 17,734 Hz, 340 -> 10,432 Hz) land within 1 % of
a rate an IFF `VHDR` on the same disc *declares*, which is a free check that
the whole reading is right.

**Effects are set up on channel pairs.** [Prey] the same length and period go
to AUD0 and AUD1, or to AUD2 and AUD3, and then `DMACON` enables both
(`#$8003`, `#$800C`) — the standard way to centre a mono sample on the
Amiga's hard-panned outputs. The register-reference histogram shows it
without any disassembly: the streaming pair is touched three to six times as
often as the effects pair.

**A directory may be named after a format most of its contents are not in.**
[Prey] `PREY8SVX/` holds twelve files of which **two** are IFF 8SVX; the other
ten are raw. The split is chronological — the two with real 1993 dates kept
their headers, the ten in the older bulk copy had theirs stripped — and the
loader does not care either way.

**In-house modules often carry the player inside every song, and diffing the
songs against each other finds it for free.** [Marvin] Twelve files in
`music/`, none a hunk file, none a tracker module, every one beginning with a
seven-entry `jmp d16(pc)` table:

```
4efa 002a   4efa 06fc   4efa 077c   4efa 0814
4efa 0846   4efa 18dc   4efa 08ee
```

The **longest common prefix between any two of them is the player** — 6,535
bytes here. Better, the prefix lengths *cluster*, and the clusters are
builds: nine files share 6,535 bytes and three diverge at byte 23, one byte
inside the jump table. That split then matched the timestamp outliers of
section 3 and the files' own capitalisation. **Diff the music files against
each other before doing anything else with them.**

The same player was linked into the game executable twice over as well,
identifiable by its strings (`musicirq`, `music_soft_irq`, `ciab.resource`).

**Read the sample slots as text.** 22-byte NUL-padded names, tracker fashion,
and composers use the empty ones. [Marvin]'s carry a systematic
three-letter-source naming scheme (`d10-` for a Roland D-10, and so on), a
group signature `(c)noogman/complex`, an end-of-data sentinel spelled
`deadbeef` in ASCII rather than assembled as a longword, and — in two
modules — **private postal addresses**, put there in 1994 as contact details.
Read them; think before you republish them.

**A CD32 title may use Red Book and an in-house player at once, for different
things.** [Marvin] has eleven audio tracks (43 minutes, ten of them
normalised to exactly 0.00 dBFS) *and* twelve `.pc` modules, credited to
different people in its own manual. Do not stop looking when you find one.

---

### A THIRD DISC PLAYS RED BOOK WITHOUT EVER READING THE TOC — AND IT IS THE ONE WITH THE MOST TO GET WRONG

[Fire & Ice] plays 22 tracks from constants; [Gloom] drives the drive through
Akiko with no `OpenDevice` at all. **[James Pond 2] is the third, and the
cleanest case yet**, because the mapping is *data* rather than code and can be
read out whole.

```
python3 tools/iocmd.py extract/RoboCod
     9 (0x09) x1   input.device IND_ADDHANDLER
    10 (0x0a) x1   input.device IND_REMHANDLER
    37 (0x25) x1   CD_PLAYTRACK   io_Length=#$1  io_Data=0  io_Offset=$6b8.l
    40 (0x28) x2   CD_PAUSE       io_Length=#$1 / #$0  (pause, then resume)
```

**Three CD commands on the whole disc.** No `CD_INFO`, no `CD_CONFIG`, no
`CD_TOCMSF`, no `CD_TOCLSN`, no `CD_GETNUMTRACKS`. Stopping is `CheckIO` /
`AbortIO` / `WaitIO` on the outstanding request, with no command at all.

And `io_Offset` comes from a table:

```
015b66  lea.l   $2cf3a.l, a0      ; the level table
015b6c  move.w  $3c59a.l, d0      ; the level number
015b72  mulu.w  #$c, d0           ; 12 bytes per record
015c8e  move.b  $b(a0), d0        ; byte 11 = the music id
00bd70  btst.b  #$7, d0           ; bit 7 -> Red Book, else the internal replayer
00bd78  bclr.b  #$7, d0           ; ...and the low seven bits are the TRACK NUMBER
```

**Bit 7 of a music identifier selects Red Book or Paula, per tune.** [Fire &
Ice] offers the same choice as a menu option; this disc bakes it into a data
table, and all **86** of its records choose Red Book — so the internal replayer
is present, reachable and never asked for. Tracks 3–8 are used 15/14/19/9/24/5
times and track 2 comes from a constant in the front end, which makes **all
seven audio tracks reachable** and the disc the third "every track reachable"
case after [Guardian] and [Marvin].

**Two things to carry.**

**When `io_Offset` is a variable rather than a constant, find the table before
giving up.** One `lea` and one `mulu` in the level-start routine gave the
address, the stride and the column; walking 86 records then gave the whole
soundtrack map for the cost of one script. A disc that plays "some tracks" and
a disc that plays "all of them from a table" look identical at the `io_Command`
histogram and are completely different findings.

**And a hardcoded table means the music is welded to the pressing.** There is
no TOC read anywhere, so the same executable on a disc with a different track
layout plays the wrong music silently. That is worth knowing before anyone
re-masters one of these.

**A watchdog with no query.** `CD_PLAYTRACK` plays one track and stops, so
continuous music needs the end noticed. [Fire & Ice] re-issues after a
`CD_INFO` poll every 150 frames. This disc has **no query at all**: it sets a
counter to 250 after each play, decrements it in the game loop and re-issues
when it expires. **If a disc plays Red Book and never queries the drive, look
for a bare countdown** — it is the cheapest version of the idea and it leaves
only a `move.l #$fa` and a `subi.l #$1` behind.

## 9. Text

**HOW MUCH TEXT IS THERE? MEASURE IT, AND SAY WHICH DENOMINATOR.** This section
was the thinnest in the document for thirteen discs because on thirteen discs
the text was a garnish. [Universe] is the first title here whose *content* is
text — a point-and-click — and it supplies the number the section was missing:

```
                bytes of prose   of the resident image   of the bytes on disc
Universe             602,344            6.53 %                 13.70 %
```

6,644 strings, 6,426 of them unique, in **four complete languages** — English
21.7 %, French 25.2 %, German 24.7 %, Italian 22.4 %, 6.0 % too short to
classify. Those shares are what four real translations of one script look
like, and a disc where they are lopsided has a localisation that stopped.

**State which of the three figures you divided by.** On disc, 602 KB against
4.19 MB is 13.7 %; against the fully unpacked 8.79 MB it is 6.5 %. Both are
true and they differ by a factor of two. The rest of the set for comparison:
Guardian "one language and about forty lines of it", Prey thirteen performance
ratings and three death messages, Microcosm nothing outside the video.

**And on a text-heavy disc, expect the prose at the bottom of the packing.**
On Universe the string tables are at RNC nesting depth 1 and 2 (section 5);
47 of the 49 tables are below the top level, so a pipeline that unpacks one
level and greps finds the menus and none of the script.

**A string table need not declare its own length, and the three things that
break a naive parser are all on one disc.** [Universe]'s tables are a run of
32-bit big-endian offsets at the head of a blob:

* **there is no count.** The run ends at the first entry that does not point at
  a plausible record, and it can never be longer than `min(offsets) / 4`
  because the first record follows it;
* **entries repeat and point *backwards*.** A line used twice is stored once.
  So a record's extent comes from its NUL terminator and **never** from the
  next offset — `offs[i+1] − offs[i]` produces garbage on a fifth of the tables
  and makes the rest look non-monotonic;
* **there are two record shapes and only the first byte distinguishes them.** A
  speech record carries a four-byte header (`ff ff 14 08`, `0c 09 14 08`); a
  plain name or description has none and the text starts at the offset. The
  first byte of a header is never printable and the first byte of text always
  is, which is the whole test.

**A FOURTH MODEL, AND IT IS NOT A FLAT TABLE AT ALL.** The set has now seen
four ways of storing display text: an offset table into flat strings
([Universe]), everything inline in the code ([Gunship 2000]), separate text
files parsed at run time ([Superfrog]), and — on [Myth] — **a relocated
longword page index over chains of position-prefixed records**. A record there
is

```
[flag] [column] [row] TEXT
```

with `$FF` starting a new page, `$00` continuing one, and **the next record's
flag byte serving as this record's terminator**; there is no NUL. Two things
follow that are worth carrying:

* the page-index entries are covered by `HUNK_RELOC32`, so `relocs.py --list 0`
  **proves they are pointers** instead of leaving it to plausibility — and each
  one lands one byte *past* its page's flag, on the `column` byte;
* a raw strings dump reports the `row` byte as a leading character on every
  line, so the credits come out as `:MARK CALE`, `2THE FINAL` and
  `HALAN HUNNISETT`. **When every string in a dump has one junk character in
  front of it, that character is the layout, and the record header is three
  bytes wide.**

Myth's two tables hold 12 and 10 entries, one ending at an explicit
`$FFFFFFFF` and one running straight into the data it points at, with **zero
empty slots** and no repeated or backward entry — so of the three traps below,
only the second applies, and it applies with `$00`/`$FF` in the terminator's
place. **Establish which model a disc uses before writing the parser; the traps
are model-specific and two of the four models have none of them.**

A parser that assumed a length field, forward-only offsets and one record
shape found 26 tables and 61 KB on that disc. Fixing all three found **49
tables and 180 KB**, and the raw prose scan over the leaves found 602 KB.
**When a text scan on a text-heavy disc returns an implausibly small number,
suspect the table model before suspecting the disc.**

**And an entry of zero is a slot, not a parse failure.** Universe has 23 empty
slots across 2,109 — some a null pointer, some a record header with no text
behind it. Two of them are in the inventory-description table, which means two
objects the player can be told nothing about.

**Where a disc keeps its languages in one blob, look for a fixed-length
separator.** Universe puts all four in the same blob, in the order EN/FR/DE/IT,
separated by a run of **exactly 160 zero bytes**, with the offset table
indexing only the English blocks and the translations reached by adding a
per-language base. Nothing declares any of that; the constant 160 is what makes
it recognisable as a marker rather than padding.

**Do not assume anything about the encoding — determine it, because it says
where the text was written.** The first two discs go opposite ways and both
are informative; the third has almost no text at all.

* [Dragonstone] IBM **CP437**: `é` is `0x82`, `ß` is `0xE1`. The text was
  authored on a PC and carried across as bytes.
* [Marvin] **ISO 8859-1** throughout, in all four language files and in the
  `©` of the boot script and the `´` in the executable's own error messages:
  `è` `0xE8`, `ß` `0xDF`, `Ü` `0xDC`. Authored on an Amiga.
* [Universe] **7-bit ASCII plus CP437, and it is the cleanest case in the
  set**: 23 distinct high bytes, every one of them a character English, French,
  German or Italian needs (`0x82` é ×1,968, `0x81` ü ×723, `0xE1` ß ×487,
  `0x8A` è ×934 …) and nothing else. Nothing outside CP437's accented block
  and nothing inside it these four languages do not use. Where Banshee needed
  CP437 *plus* a private substitution for Danish, this disc simply uses the
  code page. The programme also carries an **accent-folding table** mapping the
  high range onto base letters, right beside its keyboard map.
* [Prey] **plain 7-bit ASCII, one language, no accented character anywhere**,
  because the only text the player reads outside a bitmap is thirteen
  performance ratings and three death messages. A disc can have almost no text
  at all; do not go looking for a localisation model that is not there.

* [Legends] **7-bit ASCII in all three languages, with the accents *dropped*
  rather than encoded**: `AuBerirdische` for *Außerirdische*, `Sudpol` for
  *Südpol*, `Agypten` for *Ägypten*, `zerstoren` for *zerstören*, `apres JC`
  for *après JC*. Not CP437, not Latin-1, not a transliteration convention —
  every mark simply removed, `ß` becoming `B` by shape. **A localised disc
  with no high bytes anywhere is a third answer**, and the reason is usually
  in the font: that one has 77 glyphs and none is accented.

* [HeroQuest II] **a fifth answer: the accents are remapped onto ASCII
  punctuation.** Zero bytes above 0x7F in any of three languages, and yet the
  German is fully accented: `)` is **Ä** (`ST)RKETRANK`), `*` is **Ö**
  (`AUSGEL*ST`), `+` is **Ü** (`ZUR+CK`), and in French `(` is **Ç**
  (`FOR(ANT`). `<` and `>` are the opening and closing single quotes and `>`
  doubles as the apostrophe (`Aranwyth>s`, `D>ACTIVER`), which is
  typographically correct and is why French uses it 400 times against English's
  76. `ß` is spelled `SS` and every French acute, grave and circumflex is simply
  dropped, so the font was extended by exactly four glyphs and the two
  translations were fitted to it. **A file with no high bytes is not necessarily
  unaccented — check whether the punctuation counts differ between languages.**
  On that disc `)`, `*` and `+` appear 135, 78 and 254 times in German and zero
  times in English or French, which is the whole discovery in one histogram.

  The code confirms it from the other side: a **70-character alphabet string**
  (`A–Z a–z 0–9 ( ) * + - : ; ` and space) sits in the executable, and its four
  odd trailing glyphs are exactly the four accents.

* [Guardian] **a sixth answer, and it is the null one: there is no localisation
  model to look for.** 7-bit ASCII, upper case, one language, and the whole
  readable text of the game is about forty lines. The font has no character map
  and no width table; the index is a **32-character alphabet string** in the
  executable —

  ```
  ABCDEFGHIJKLMNOPQRSTUVWXYZ.! #&*
  ```

  — twenty-six letters and six punctuation marks, in order, and nothing else. The
  game prints digits (`SFX VOLUME : 075%`, `ZONE 01.1 CLEARED!`) so there is a
  second glyph set the string does not index. **Count the string and count the
  glyphs**: where they match you have the mapping for free (Legends' 77-glyph
  font), and where they do not, the difference is the set you have not found yet.

* [Banshee] **a seventh answer, and it is two of the above in the same string
  table with no marker between them.** German and French are ordinary **CP437**
  (`0x81` ü, `0x82` é, `0x84` ä, `0x85` à, `0x8A` è, `0x8B` ï, `0x94` ö,
  `0xE1` ß) — and the fourth language, **Danish, is not**, although CP437 has
  the letters it needs. Its three extra letters are on ASCII punctuation:

  ```
  0x22 "  ->  AE      0x2B +  ->  ae
  0x24 $  ->  AA      0x3D =  ->  aa
  0x9C    ->  OE      0x7E ~  ->  oe
  ```

  so `S~ren` is *Søren*, `p= sk+rmen` is *på skærmen* and `$h, Svend` is *Åh,
  Svend*, while `Zur81ck` decodes correctly as CP437 two strings away. **A
  straight CP437 decode of that disc produces clean German and French and
  nonsense Danish**, and the give-away is one language full of `~`, `=` and `+`
  where letters should be.

  What settles the mapping rather than guessing it is the **hall-of-fame
  name-entry alphabet**, a `0xFF`-separated list in the executable whose three
  characters after `Z` are `"`, `0x9C` and `$` — and **Æ Ø Å is where the Danish
  alphabet goes after Z**. Five of the six went on free punctuation slots and
  the sixth did not, which is why one of them is a high byte. **Find the
  alphabet string and read its order; it converts a substitution table from a
  guess into a fact.**

  The structure is worth a line too: four variants per string, `0xFF` between
  them and `0xFE` between groups, fixed order English/German/French/Danish, no
  index table and no length prefix — and where a language was not translated
  the English is repeated verbatim, so the table is complete and the French menu
  is partly English.

Check three or four accented characters against both tables; it takes a
minute and it places the authoring machine. **And check whether there are any
bytes above 0x7F at all before reaching for a table** — if there are none in a
German file, the question is not "which code page" but "what did the font
have".

**Watch for all-upper-case text and ask why.** [Marvin] every string in all
four languages is capitals, accents included (`É`, `Ü`, `Ö`, `À`), because the
game's font — legible in the title-screen bitmap — has no lower case.

**Check every language file separately, not one per language.** On the same
disc, nine of eleven German files put `ü`, `ä`, `ö` at the CP437 values
`0x81`, `0x84`, `0x94`, and two put them at `0x8F`, `0xA5`, `0x8C` while `ß`
stays at `0xE1` — a third encoding, in the two biggest German files, mixed with
a handful of correctly-encoded characters inside the same file.

**Find the control-code vocabulary early.** It makes an entire dialogue system
legible in one go. [Dragonstone]'s is four bytes:

```
0xFF  end of string
0xFE  line break
0xFC  wait for the player, then continue on a fresh page
0xFD  substitute the name the player entered
```

**Diff the language files against each other and count the strings that are
identical, because that is the untranslated set.** [HeroQuest II] has 362
strings per language and **43 are byte-identical in all three** — nine of them
placeholders and numbers, and **nineteen of them English prose**. Eighteen are
consecutive (entries 304–321) and are the **entire closing narration of the
game**: a German or French player who finishes it is shown the ending in
English. `LOAD`, `SAVE`, `RESET` and `EXIT` are untranslated too, while the
save-slot labels beside them are. One further entry in the set is a floppy
prompt naming a volume nothing on the disc assigns. **The count of
byte-identical strings across a localisation is a one-line measurement and it
tells you where the translation stopped.**

**Compare the three language files byte for byte.** [Dragonstone] They are
identical from byte 0 to within a few hundred bytes of the text block, and the
text block starts at the *same offset* with the *same string count* in all
three. What differs is the run of 16-bit string pointers inside the shared
script. That tells you the localisation model — build once, emit three pointer
tables — and it tells you where the string table is without finding it.

**Two alphabets in one executable means one of them is not text.** [Legends]
the level code carries `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:.` and, right
after it, `abcdefgh/ijklmnopqrstuvw`. The second is a **box-drawing set**
mapped onto lower-case letters, which is why the shipped dialogue contains
records reading `ioj` / `p/m` / `knl` — the three rows of a frame. Text that
looks like nonsense in a dump may be the UI drawing itself with the text
renderer, and the alphabet string tells you which is which.

**And the alphabet string may be the font's only index.** [Legends] the
77-glyph font has no character map, no header and no width table; the
77-character string in the executable *is* the index, in order. Count the
glyphs, count the string, and if they match you have the mapping for free.

**A 64-character alphabet is a password alphabet.** `A-Za-z0-9+-` is six bits
per symbol; where you find it, the save system is a bit field printed six bits
at a time and there is no save file to look for.

**Fixed-width centred strings tell you the field width.** [Prey] thirteen
performance ratings are each padded with spaces to exactly 20 characters in
the source string, so the box they are drawn into is 20 characters wide and
you know it without looking at a pixel. `Saved xxx out of 150` beside them is
a template whose `xxx` is overwritten at run time — the same shape as a
placeholder, but this one is meant to be overwritten and is.

**A fixed-width table of phrases is the other kind of password system.**
[Marvin] thirteen sixteen-byte records in the code hunk — fourteen characters,
a NUL, and the level number to jump to — terminated by `0xFF`. Finding it
gives the complete password list and the checkpoint map in one read. The
width is not arbitrary: it is the width of the box on the title screen.

**And a template that is *meant* to be overwritten looks the same and is not a
finding.** [Guardian] ships `INSTALLATIONS PRESERVED : 100%` and
`SFX VOLUME : 075%`, whose digits the game writes over at run time — Prey's
`Saved xxx out of 150` again. The tell that separates the two cases is whether
the shipped content is *plausible*: `76543210` and `XXXXXXXX` are not values,
`075` and `100` are. **A placeholder is a string of the right length with
impossible content; a template is one with a plausible default.**

**When the same table ships more than once, diff the copies and read the slots
that are empty in all of them.** [Universe] carries the ship's star-map
gazetteer in two different `part` files. The two copies are identical entry for
entry **except slots 8, 9 and 10** — the three destinations that chapter lets
you plot a course to — and **slots 12, 13, 15 and 40 are empty in both**, with
slot 14 a header and no text. The table otherwise describes thirty places in
two or three sentences each, so those four are places the console has a slot
for and nobody wrote. Their positions are the tell: 12/13/15 sit between the
course-plotting message and the first gazetteer entry, and 40 between the last
entry and the out-of-fuel refusal — **the ends of two runs, which is where an
unfinished list stops rather than where a deliberate gap would be.**

Two copies is a weak N and the finding is still worth the two minutes: it is
the same shape as [Fire & Ice]'s nine resource slots zero in all seven worlds
and [HeroQuest II]'s map cell byte 7 zero in all nine dungeons. **Build the
occupancy table across every parallel copy and print the indices that are empty
in N-1 or N of N.**

**Placeholders survive.** [Marvin] the language files' password section holds
a fourteen-character string and a line of instruction; the instruction is
translated into all four languages and the string is not, because it is the
template the real password is copied over at runtime. It shipped, four times.
A string that is the right *length* for a field and the wrong *content* is a
placeholder, not data. [HeroQuest II] ships **nine** of them in each of three
languages — `00000000`, `0000`, `00`, `..`, `0`, `  ` and, the one that gives
the game away, **`76543210`**: not zeros but a descending run, which is what
somebody types to see which digit lands in which column. Seven of the nine are
stored twice, once for each of a pair of fields, and seven further entries are
the empty string with live pointers into them.

**Look for the manual.** [Marvin] one of the four sections of every language
file is the **entire instruction manual** as plain text — aim of the game,
both control schemes, hints, the collectables table, the full credits and the
publisher's postal address. It is the best single source on the disc for who
made the thing, and it is the kind of section a `HUNK_SYMBOL` table will name
for you (`Manual`, `TEXT`, `PW`, `PictureTexte`).

**Text is where a disc's localisation jokes live.** [Marvin] the four
language files are named `englisch` (the German spelling of "English"),
`germany` (the country, not the language), `frensch`, and `berlucsoni` —
Silvio Berlusconi, misspelled, used as the file name for the Italian text six
months after he became Prime Minister of Italy. The menu the player sees is
correct in all four. **Read the file names, not only the file contents.**

**Check the `locale.library` table if there is one.** [Marvin] four eight-byte
records — seven characters, a NUL, an index — which fits `deutsch`, `english`
and `italian` and truncates `français` to `françai`. Fixed-width language
tables have a natural off-by-one and it is worth noticing which language got
cut.

---

**A disc may store a text *generator* rather than text, and may ship its
source.** [Liberation] has nine text files: three are **source with the
author's comments intact** and six are compiled. The compiled record is

```
0xD7  UWORD id  UWORD length  '[' ... ']'
```

with `0xD7 0xFFFF 0x0000` closing a nested block, the ASCII caret introducing
control codes (`^On[a|b|c]` picks one of n at random, `^Nx-y` a random number,
`^P` a personal name, `^J` a profession, `^;` a comment), and **`0xB1` + UWORD
playing the speech clip of that index**. Counting distinct `0xB1` markers
against lines in the `.LOG` beside the same directory gives 566 against 566,
71 against 71 and 5 against 5 — **two formats confirming each other with
neither decoded from the other**, which is the cheapest cross-check on that
disc.

**And read the source files' prose, not just their data.** `PGE.txt` opens with
384 words of **notes addressed to translators**, explaining the control codes
one at a time, signed by the author and ending with his direct phone number.
Nothing on the disc was translated. On a format where studios shipped
whatever was in the build directory, a file whose first bytes are English
sentences rather than markup is worth reading to the end.

### A SIXTH STRING MODEL: A COMPLETE LOCALISATION WITH NO CHARACTERS IN IT

[Alfred Chicken] was the fifth model — **no text at all**, with the game's own
title existing only as a 320 x 184 picture. [James Pond 2] is the sixth and it
is the mirror image: a **complete three-language manual**, eleven chapters,
115 pages, 7.36 MB of raster — and a prose census over the whole 195 MiB volume
of **10,875 bytes, 0.0155 % of the file bytes**, whose largest single
contributor is the **boot script**.

The manual is 115 IFF ILBM pages, 320 x 200 x 8 planes, `ByteRun1`, in `uk`,
`fr` and `gr` sets of 37, 38 and 40 pages. There is not one character in any of
them. So every measurement this section prescribes — string count, encoding,
byte-identical strings across a localisation, accents remapped onto punctuation
— returns **zero**, and zero is not the same as nothing to measure.

**What to measure when the text is pixels.** Three things, none of which needs
a character, and all three paid on that disc:

1. **Count the distinct palettes.** All 115 pages share **one** byte-identical
   768-byte `CMAP`; the same disc's CDXL streams carry a fresh palette in every
   one of 2,530 chunks. One artist against one palette versus a frame-by-frame
   quantiser, separated without opening a pixel.
2. **Diff the same page number across languages, pixel by pixel.** Unpack the
   `ByteRun1`, convert the planes to one index per pixel, and count differences.
   On that disc exactly **one page of 115 is byte-identical across all three
   languages**, and it is the largest and the inkiest — the one full-page
   illustration with no text on it. Every other page differs by 3.7 % to 25.9 %
   of its pixels, mean 12.94 %. **That is the pixel-domain form of "count the
   byte-identical strings to find where the translation stopped"**, and here it
   proves the translation stopped nowhere.
3. **Read the chunk list, not only the image.** 17 of the 115 pages carry a
   Deluxe Paint **`DPPS`** page-setup chunk — **ten English, seven French, zero
   German**. A chunk nobody reads, present on a subset, is a build split for
   the cost of one parse; and it names the paint package, which is otherwise
   unrecorded anywhere on the disc.

**And the page counts alone are a finding, available from `ls`.** 40 German
pages against 38 French and 37 English is German running 8.1 % long, and the
chapter indices confirm it independently: identical files for English and
French, every German chapter one page later from chapter 2 onward.

**One thing measurement cannot reach, and it is worth admitting rather than
guessing.** Which language `gr` is, and what the book is called, are not
recoverable from any byte in it. Both were settled by **rendering one page and
looking** — `gr` is German, and the book's title page reads `FI5H FILE`, which
also explains the otherwise inexplicable `if $RoboSelection EQ "FI5H"` in the
boot script. **When the content is pixels, the measurements tell you about the
production and only a render tells you about the content.** Budget for one
render per disc of this shape; it is step 24 applied to a manual.

**A localisation split the set had not produced.** That disc translates its
**manual** into three languages and its **game** into none: no
`GetLanguageSelection`, no second language string anywhere in the executable.
[Universe] translates prose and interface together; [Legends] translates
neither. **Count the two separately**, because a disc can do one and not the
other.

## 10. Baselines

Nineteen discs, and they bracket the format rather than agreeing on it. Prey CD32
and Prey CDTV are the same game on the two consoles, so that pair is a control
rather than two independent samples. Legends and Gloom are two discs with
the same *publisher* — Guildhall, a year apart — and they agree on nothing at
all (see below); **Dragonstone and Banshee are the second such pair**, Core
Design three months apart in 1994–95, and they agree on three things, all three
of which turn out to be attributable to something wider than the label (open
item 14). Speris and Legends are both 1996 releases and they sit at
opposite ends of the disc-occupancy column: 0.74 % and 89.4 %. Their *games* are
the same size.

**And the games themselves cluster far more tightly than the discs do.**
Strip the Red Book audio, the streamed speech **and the streamed video** and
every title here is between 2.7 MB and 13.3 MB: Dragonstone 2.7, Liberation
**2.9**, **Gloom 3.9**, **HeroQuest II 4.1**, Legends 4.4, Speris 4.5,
**Microcosm 9.1**, Marvin 13.3, Prey CD32 34 (of which the intro animation is
12). A CD32 disc's *size* tells you almost
nothing about the game on it; the occupancy column measures what got poured on
top, and there are three kinds of it — Red Book audio on four discs, digitised
speech stored as files on two, and **streamed video on one**.

**Ten discs, ten games, and the band has not moved.** [HeroQuest II] is 2.16 MB
on the disc — *below* the band — and **4,285,931 bytes = 4.09 MB** unpacked,
between Gloom (3.86) and Legends (4.4). That is the second disc in a row where
the compressed figure would have broken the band from underneath and the
decompressed one lands inside it. **Measure the decompressed size**, every time.

**AND THE ELEVENTH BREAKS IT, WITH NO CORRECTION AVAILABLE.** [Guardian] is
**2,249,822 bytes — 2.25 MB — and nothing on it is packed**, so there is no
decompressed figure to rescue it. Two earlier discs went below the floor
compressed and came back inside it unpacked; this one is 2.25 MB either way, and
it sits below Dragonstone's 2.7.

**AND THE FIFTEENTH DISC WAS THE BEST CHANCE TO BREAK THE CEILING, AND DID NOT.**
[Gunship 2000] has the **second-largest data track in the set** — 157.84 MB,
within 2 % of Liberation's — and it is the disc this document expected to break
13.3 MB from above. The game is **6,939,994 bytes on disc and 8,363,560 resident
(7.98 MiB)**, comfortably inside. Where the 157.84 MB goes is the whole answer:
**63.4 % of the volume is a zero hole of exactly 100 MiB**, 86.9 % of the *file*
bytes are three CDXL streams, 1.3 % is a bundled second game that never runs, and
**the game is 4.2 % of its own disc**. Fifteen discs, eleven studios, five years,
and the ceiling has still not moved.

The band's *floor* therefore moves to **2.25 MB** and what the band measures is
unchanged: 2 MB of chip RAM and a 68EC020 still bound how much resident code and
data a title can have, and this one simply uses less of it — a whole 3D game, its
eleven zones and its artwork in 2.25 MB, with 41.3 % of the disc given to music
on top. **The useful form of the finding is the ceiling, not the floor**: nothing
in this set exceeds 13.3 MB, across five years, ten studios and every genre the
format shipped.

**CORRECTION, AND IT IS THE SIXTEENTH DISC THAT MAKES IT: the ceiling is broken,
on one of the two readings, and holds on the other.** [Superfrog] is
**4,102,748 bytes on disc and 13,336,690 resident** once all 158 Imploder
streams are expanded at both depths — **84,993 bytes and 0.64 % above Marvin's
13,251,697**, which had been the maximum. Read on disc it is 4.10 MB and sits
comfortably inside. So for the first time the two readings return **different
verdicts about the same disc**: on-disc says "inside the band", resident says
"new maximum", and both are correctly computed.

Keep them separate and quote the denominator. Do not average them, and do not
pick the one that makes the better sentence. The rule above — that the band is
coherent only as an on-disc measurement — was written when obeying it merely
tidied the numbers; this is the disc where obeying it **changes the answer**.

Three further things that disc settles about how to reach the figure at all:

* **Strip what is not the game first, and say how much you stripped.** Superfrog
  shares its master with two playable demos. The whole disc is 17,404,587 bytes
  resident; the game is 13,336,690 of it. Quoting the disc total would have put
  it 31 % over the ceiling and meant nothing. This is the third mechanism after
  Red Book audio and streamed video, and the first where the other content is
  **other games**.
* **The expansion factor is not predictable from the genre.** Superfrog expands
  **3.25x**, second only to Dragonstone's 3.78x, on a 2D platformer where the
  prediction written in advance was "bottom of the scale". The eight known
  factors now run **1.369x**, 1.43x, 1.89x, 1.99x, 2.00x, 2.10x, 2.72x, 2.93x,
  **3.25x**, 3.78x — ten of them — and nothing about the genre picks the bin.
  **[Myth] is the new bottom at 1.369x**, on a 2D platformer, which is the same
  genre that holds second place. Two of the ten extremes are the same genre, so
  the genre carries no information at all.
* **And the denominator can be somebody else's data.** [Myth]'s three floppy
  images contain **172,010 bytes — 6.36 % of its on-disc total — that no chunk
  table claims**, including a copy of Commodore's `ConClip` and 156 KB of
  high-entropy residue left on the physical media before the game was written to
  it. Measured on both sides against only the bytes the game reaches, the factor
  is 1.394x. **When a disc ships whole media rather than files, say which
  denominator the expansion figure uses.**
* **Say what "resident" does not mean.** It is bytes after every container is
  expanded, which is a property of the corpus. `SFIntro` alone contributes
  3,290,454 resident bytes and the game plainly does not hold them all at once.
  The figure is comparable across discs because it is defined identically for
  all of them; it is not a memory-footprint claim, and it should not be quoted
  as one.

One inconsistency in the numbers above used to be flagged here rather than
tidied away: the 2.7 quoted for Dragonstone is its **on-disc** size, while the
figures for Gloom and HeroQuest II are **unpacked**.

**RESOLVED, by the one disc that could resolve it.** [Banshee] is the same
publisher as Dragonstone with the same cruncher and the same fixed-size-buffer
habit, so the two can be measured by one tool over the same kind of tree. All
three figures, for both:

| | Files | On disc | Resident after unpacking | Actually used |
|---|---:|---:|---:|---:|
| **Banshee** | 45 (37 packed) | **2,879,663** (2.88 MB) | **5,768,936** (5.77 MB) | **5,542,774** (96.1 %) |
| **Dragonstone** | 89 (84 packed) | **2,709,626** (2.71 MB) | **10,354,949** (10.35 MB) | **9,410,064** (90.9 %) |

Read **on disc**, the two are 6 % apart and both sit at the bottom of the band.
Read **unpacked**, they are 80 % apart and land in different parts of it. So
**the band as written is only coherent as an on-disc measurement**, and the
entries quoted from unpacked figures should be restated. The unpacked number is
a more interesting quantity — it is the size of the game rather than of the
file set — but it is not the number the band was built from, and mixing the two
makes two discs from one publisher look like different classes of title when
the only thing that differs is which column somebody quoted.

**Quote all three numbers for every disc**, and say which one any claim is
being tested against. The third — bytes actually used, i.e. the last non-zero
byte of each unpacked buffer — is worth keeping on its own account: the gap
between resident and used is the buffer slack a studio was willing to carry,
and it is 226 KB (3.9 %) on Banshee against 945 KB (9.1 %) on Dragonstone.

**A third data point, and it widens the slack range by an order of magnitude.**
[Fire & Ice]: **2,035,183 on disc / 2,906,735 resident / 2,898,523 used**, so
the slack is **8,212 bytes — 0.3 %**, against Banshee's 3.9 % and Dragonstone's
9.1 %. Three discs, three studios, and a 30:1 spread in how much buffer a studio
was willing to carry. The number is cheap and it is starting to look like it
says something about the studio; keep collecting it.

**A fourth point, and it lands at the tight end.** [Universe]:
**4,397,639 on disc / 9,217,125 resident / 9,172,928 used**, slack
**44,197 bytes — 0.5 %**.

```
Gunship 2000  0.004 %   Fire & Ice  0.3 %   Universe  0.5 %   Banshee  3.9 %   Dragonstone  9.1 %
```

**THE FIFTH POINT FALSIFIES THE HYPOTHESIS BELOW. Read the paragraph after this
one, then read this.** [Gunship 2000] is **6,939,994 on disc / 8,363,560 resident
/ 8,363,199 used**, slack **361 bytes — 0.004 %**, the tightest in the set by two
orders of magnitude over Dragonstone. And it **keeps AmigaDOS alive throughout**:
it boots from a startup-sequence, opens eight libraries and three devices, calls
`LoadView` rather than seizing the display, and *returns to the shell* so the
script can kill its own backdrop task by name. By the hypothesis it should be at
the loose end. It is at the tight end, alone.

So slack tracks neither studio (Universe killed that) nor OS survival (Gunship
kills this). The plainest remaining candidate is that it tracks whether the asset
build tool padded to a block size, which is a fact about a tool and not about a
game. **Keep collecting the number, stop theorising about it until a sixth point
suggests something.**

The per-file check still earns its place: on Gunship the largest single slack on
the disc is **245 bytes in `roster.dat`** — a 1,680-byte scratch save whose
squadron is named `ERASE ME` — and everything else is one or two bytes of IFF
even-length padding.

Two of the four are now under 1 %, which **weakens the "studio habit" reading**:
Universe and Dragonstone are the same label and sit at opposite ends of the
range, 18:1 apart. What the two tight discs share is not a studio but a shape —
both take the machine over completely and allocate nothing, so there is no
allocator rounding anything up. The two loose ones keep AmigaDOS alive. That is
one hypothesis and one more disc tests it.

Universe also makes the *third* figure worth stating separately for another
reason: read at one unpack level it is 5.66 MB and read at all three it is
8.79 MB. **A "resident" figure taken from a single unpack pass understated that
disc by 38 %.** Say how deep you unpacked.

And the per-file breakdown is more legible than the total: on Universe the
slack is concentrated in exactly two files — `copper.prg` at **48.3 %** (two
reserved copper-list regions) and `hand.spr` at **49.3 %** — and every other
file on the disc is under 5 %. A single aggregate slack figure can be one
deliberate buffer wearing a disguise.

**And the on-disc reading of the band now has a second exception, from the same
direction as the first.** Read on disc, Fire & Ice is **1.94 MB** — below the
2.25 MB floor, and the smallest game in the set. Read unpacked it is **2.77 MB**
and sits inside the band near the bottom. That is exactly the [HeroQuest II]
pattern (2.16 MB compressed, 4.09 MB unpacked), so two of thirteen discs fall
out of the band's floor when measured on disc and none fall out when measured
unpacked. Banshee's finding stands — the band is only *coherent* as an on-disc
measurement, because the unpacked figures scatter two discs from one publisher
by 80 % — but **the floor of 2.25 MB belongs to the unpacked reading, not the
on-disc one.** Quote all three and say which you are testing against; that
instruction is doing real work now.

**The band survived the disc that should have broken it, twice, from both
ends.** [Microcosm] spends 92.3 % of its data track on a single 483 MB file and
is still a 9.1 MB game. [Gloom] goes the other way — a **1.3 MB** data track,
0.23 % of a CD, the smallest volume on the format — and its 30 % packing ratio
puts the game at **3.86 MB**, still inside. Nine discs, four years, eight
studios, and the number that does not move is the one bounded by 2 MB of chip
RAM and a 68EC020 rather than by the medium. **Measure the decompressed size,
not the compressed one**: on Gloom the compressed figure would have broken the
band and been wrong.

| | Dragonstone (1995) | Marvin's Marvellous Adventure (1995) | **Prey CD32 (1993)** | **Prey CDTV (1992)** | **The Speris Legacy (1996)** | **Legends (1996)** | **Liberation: Captive II (1994)** | **Microcosm (1994)** | **Gloom (1995)** | **HeroQuest II (1994)** | **Guardian (1994)** | **Banshee (1994)** | **Fire & Ice (1994)** | **Universe (1994)** | **Gunship 2000 (1994)** | **Superfrog (1994)** | **Myth — History in the Making (1992/1993)** | **Alfred Chicken (1993)** | **James Pond 2: RoboCod (1993)** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--- | --- |---|---|---|
| Publisher / studio | Core Design, UK | 21st Century / Infernal Byte, UK+DE | Almathera / KirkMoreno, UK+DK | **KirkMoreno alone** | Binary Emotions / Team 17, UK | **Krisalis Software / Guildhall, UK** | **Mindscape / Byte Engineers, UK** | **Psygnosis, UK — CD32-exclusive** | **Black Magic Software / Guildhall, UK** | **Gremlin Graphics, UK** | **Acid Software — CD32-first, and the first real polygon engine here** | **Core Design, UK — the same label as Dragonstone, and the first same-label control here; written by a two-person Danish team** | **Graftgold / Renegade, UK** — the studio is named nowhere in ISO 9660; it is inside the executable under XOR `0x1b`, together with the engine's own name, `68000 Game System`, and the copyright range `1990,94` | **Core Design, UK — the third disc from this label, and the first of the three whose credit panel names its whole team: Gary Antcliffe (code), Rolf Mohr / Stuart Atkinson / Jim Bottomley-Mason (art), Martin Iveson (music)** | **MicroProse — the first non-British publisher here, and the first flight simulator** | **Team 17, UK** — and the only **compilation** here: Superfrog 50.5 % of the bytes, a *Super Stardust* demo 39.6 %, an *Arcade Pool* demo 7.4 % | **System 3 Arcade Software, UK — developer and publisher in one**, and a label new to this set. Verified from the PVD field, the `MYTH.A` bootblock and the credit screen, plus a 320×256 logo picture | **Twilight (developer) for Mindscape (label)** — and the **first disc in the set where the two are separable from the artwork**: the copyright and the trademark are Twilight's, Mindscape is the label only. PVD publisher field says `Mindscape`; the build is Twilight's by its RCS keywords | **`Millennium Interactive Ltd`** in the PVD publisher field — a label new to this set — and **no developer is named anywhere on the disc**: not in any descriptor field, not in a `$VER:`, not in either credit list. Only *people*: `Chris Sorrell` (original design, programming, graphics), `Dean Ashton` (the A1200/CD32 and AGA conversion, and the preparer field), `Richard Joseph` (music), `Steve Bak` (maps), `Steve Loughran` (the book reader) and `Wayne D. Lutz` (the CDXL player, by `$VER:`). The studio has to be recovered from a **comment in the boot script**, which is a first |
| Master cut | 1994/1995 | 1994/1995 | **1993-11-29 21:15:11** | **1992-09-02 15:05:26** | **1996-01-10 20:47:52** | **stamped 1992-03-06 18:12:02 — impossible** | **1994-04-15 09:39:39** — and the game was **linked 1994-04-08 09:35:08**, seven days earlier, per its own `$VER:` | **PVD stamped `1978-01-26 09:30:04` — the AmigaDOS epoch**; newest file 1994-02-09 02:46:04 | **1995-06-28 18:06:57** — every record on the disc is the same afternoon | **1994-06-15 17:34:13** — and the game executable was written **11m34s** earlier; the volume-set field reads `15 June 1994 17:30`, typed by hand | **1994-08-04 14:26:37** — and the root directory record **1m18s** earlier, the tightest gap in the set; the community dump is labelled *1995* | **1994-07-08 13:16:10** — and the executable's own banner says it was linked at **12:59** the same day, **17m10s** earlier | **1994-03-16 18:24:51** — six days after the last file it indexes, so the two halves of the timestamp evidence are consistent | **1994-09-13 11:48:04**, 2 h 17 m after the last file was written | **1994-04-19 13:46:56** — and four files are stamped 14:06, **19m12s after the PVD**: the only disc here where the descriptor predates what it indexes | **1994-08-24 12:17:15** | **PVD says 1992-12-21 17:10:58 — and the disc falsifies it.** The `.TM` block it carries reads `Copyright © 1993 - Commodore Electronics Ltd.`, and the loader needs a 68020 and Akiko. Third disc with the 1992-12-21 epoch, and the first one proven wrong from inside the image | **PVD 1993-12-06 17:54:10, and step 39 *confirms* it** — the first clean pass in the set. `.TM` says © 1993, and the shipped `c/setpatch 40.14 (7.10.93)` puts a hard floor at **1993-10-07**, sixty days earlier. `/alfred` was written **alone, 21 h 26 m after every other file**, and the image was cut 3 m 29 s later | **PVD 1993-08-17 10:12:55**, 5 h 14 m 49 s after the newest file it indexes — an ordinary, healthy gap. Root directory record 1993-08-15 16:47:26, *earlier* than two files, because AmigaDOS directory times follow their own contents and the two late files live in `/C` and `/S`, whose records carry their exact times. `.TM` says © 1993 and nothing contradicts it. **And the boot script's own prose dates check out**: "Sunday 15th August 1993, at 10:05am" (it was a Sunday; three directories rebuilt 36–45 min later), "Friday 13th" (it was; `Intro.cdxl` stamped that evening), "1:30am 14.07.93" (four files stamped 00:03–01:18 that morning) |
| Tracks | 1 data (`MODE1/2048`) + 1 audio | 1 data (`MODE1/2048`) + **11** audio | 1 data (`MODE1/2048`), **no audio track** | 1 data, **no audio track** | 1 data (`MODE1/2048`), **no audio track** | 1 data (`MODE1/2048`) + **28** audio | 1 data (`MODE1/2048`) + **10** audio | 1 data (`MODE1/2048`) + 1 audio | 1 data (`MODE1/2048`); **no cue sheet or audio track in the dump supplied** | 1 data (`MODE1/2048`) + **5** audio | 1 data (`MODE1/2048`) + **12** audio | 1 data (`MODE1/2048`) + **2** audio | 1 data (`MODE1/2048`) + **22** audio — the second-highest track count here | **24** — 1 data + **23 audio** | 1 data (`MODE1/2048`) + **5** audio — tracks 4, 5 and 6 declare a **one-frame pregap that matches nothing in the samples** | 1 data (`MODE1/2048`), **no audio track** | 1 data (`MODE1/2048`), **no audio track** — the fourth such disc | **10 — 1 data (`MODE1/2048`, *verified* by descrambling raw sectors and reading the header mode byte on all 902, not sampled) and 9 audio** | **8 — 1 data (`MODE1/2048`) + 7 audio**, with `PREGAP 00:02:00` on track 02 and no other pregap declared |
| Data track sectors | 1,741 (1,635 declared) | 6,833 (6,681 declared) | **59,787 (59,787 declared — equal)** | 48,637 declared **in a 119,988-sector dump** | 2,455 in the image, **2,303 declared** | 2,404 in the image, **2,252 declared** | **82,605 in the image, 82,502 declared — the largest on the format** | **255,777 in the image, 255,552 declared — the largest on the format by 3.1x** | **952 in the image, 772 declared — the smallest volume on the format** | 25,663 in the image, **25,436 declared**, overrun 227 | **1,343 in the image, 1,193 declared**, overrun 150 — the second-smallest volume on the format | 1,773 in the image, **1,687 declared**, overrun 86; the volume's files end at 1,454 | **1,357 in the image, 1,270 declared**, overrun 87; the volume's files end at 1,038 | **2,429 declared, 2,509 in the image** (overrun 80, all zero) | 80,813 in the image, **80,735 declared**, overrun 78 — **the second-largest on the format**, and **63.4 % of it is a zero hole** | **4,194 (4,164 declared)** — and the image is an **exact multiple of 2048**, unlike all fifteen before it | **27,361 exactly** (26,987 declared) — second consecutive image that is an exact multiple of 2,048, and a **374-sector overrun**, the largest in the set | **918 carrying data** (LBA 0–917) + **150 of silent pregap**; volume declares **691**, so a **227-sector overrun** — and the physical disc shows *why*: the data run is padded up to where track 2's pregap begins | **100,125 in the image — 205,056,000 bytes, an exact multiple of the sector size**, only the second such image in the set after Superfrog. Declared volume **99,975**, so a **150-sector overrun**, all zero — and 150 is *numerically identical* to the declared track-2 pregap, which an image cannot disambiguate (open question) |
| Audio | 118.08 s, 8,856 sectors | **2,600.9 s**, 195,068 sectors | 0 s Red Book; **3,820 s of PCM in files** | 0 s Red Book; **3,922 s of PCM in files** | 0 s Red Book; **12 ProTracker modules** | **3,936.1 s**, 295,209 sectors | **2,064.9 s**, 154,864 sectors | **203.0 s**, 15,225 sectors — **and nothing on the disc plays it** | 0 s Red Book; **2 OctaMED `MMD1` modules + 24 raw PCM effects**, and **no `OpenDevice` anywhere** | **1,902.1 s**, 142,659 sectors — **and only tracks 2 and 3 are ever played**; 6 ProTracker modules + 39 raw PCM effects | **1,835.6 s**, 137,672 sectors, **all twelve tracks reachable** — the game filters the disc's own TOC by its CONTROL bits; no module and no PCM file anywhere | **305.7 s**, 22,928 sectors, **both tracks played while the game runs** with `CD_PLAYTRACK` and re-issued by a `CD_INFO` watchdog every 150 frames; + 2 **Player 6.0A** modules by Jarno Paananen, who is named on the credits screen | **3,033.4 s**, 227,506 sectors, **all 22 distinct by SHA-1** — three share a byte length and differ in content. Played with `CD_PLAYTRACK` while the game runs, and the player can switch to the internal replayer instead | **2,437.5 s, 182,814 sectors, all 23 distinct by SHA-1** — 98.65 % of the sectors the disc uses | **935.1 s**, 70,136 sectors, 5 tracks, all distinct — reached through `cd.device`; how many the game plays is open | **0 s. No Red Book at all**, and no PCM bank standing in for it | 0 s Red Book; **2 OctaMED `MMD0` modules** (156,006 and 48,782 B, 88.8 % of them samples) and **2 IFF 8SVX inside an executable** (`wing1` 2,796 Hz, `FLASH2` 8,860 Hz, `ANNO` `Audio Master` and `Audio Master II`) | **9 Red Book tracks, 92,445 sectors, 20 m 32 s** — peaks 11,458–22,442, **zero lead-in silence on all nine and zero pregap between them**, so the soundtrack was cut as one run and split. Reached via **`cd.device`** (2 `OpenDevice`). **No ISRC on any track** (TCVAL=0), no pre-emphasis, two-channel. Also raw 8-bit PCM inside both executables, no header, no name | **966.000 s exactly, 72,450 sectors, 16:06**, 7 tracks. Every track a whole number of *sectors*; **4 of 7 a whole number of seconds** (180, 230, 90, 71) and the two longest are the two roundest — so the round ones were **cut to a length** and the ragged ones taken as they came, the opposite of the prediction. Lead-in 0.16–0.51 s on all seven, trailing 1.56–1.84 s on six and **exactly zero on track 8**. Peaks 21,236–32,767, two at full scale. **All seven reachable** |
| Share of a 333,000-sector CD | ~3.2 % | **60.7 %** | 18.0 % | 14.6 % | **0.74 %** | **89.4 %** — game 0.72 %, music 88.6 % | **71.3 %** — data 24.8 %, audio 46.5 % | **81.3 %** — data 76.7 %, audio 4.6 %; inside the data track, **video 70.8 %**, game 1.4 %, 15,000 empty sectors 4.5 % | **0.232 %** — a third of the previous smallest | **50.5 %** — data 7.6 %, audio 42.8 %; inside the data track, **95.4 % is zero** | **41.8 %** — game **0.40 %**, audio 41.3 % | **7.4 %** — game **0.44 %**, audio 6.9 % | **68.7 %** — game **0.41 %**, audio **68.3 %**; the music outweighs the data track **168 : 1** by sector | **55.7 %** — 0.73 % data, 54.9 % Red Book | **45.3 %** — data 53.5 % / audio 46.5 %, **the first disc here where data is the larger half** | **1.26 %** — with zero audio, the occupancy figure *is* the content | 8.22 % pressed — but **0.41 % of content**: 94.86 % of the declared volume is a hole | **28.08 % pressed** (93,513 sectors to lead-out) — but the data track is **0.28 %**: **99.02 % of the physical disc is audio** | **51.87 %** — 172,725 sectors (100,125 data + 150 pregap + 72,450 audio). Data 30.07 %, audio 21.76 %. Half the disc unused **and** 65.55 % of the used data track empty |
| Files / directories | 91 / 2 | 212 / 9 | **1,439 / 24** | **1,453 / 20** | **47 / 10** | 111 / 7 | 187 / 10 | **34 / 2** | **131 / 7** | **97 / 7** | **61 / 6** | **45 / 4** — and **two of the files are zero bytes long**, one directory is empty | **29 / 8** — and **two of the directories are empty** (`/Initial`, `/Misc`), created seven seconds apart as the last act of that session | **52 files / 3 directories** (`/`, `/C`, `/s`); no empty directory, **no `.info` file anywhere** | 140 / 9 (one of them empty) | **221 / 22** | **5 / 2** — the smallest tree in the set. Three of the five files are **901,120 B each: one 880 KiB Amiga floppy image, exactly** | **30 / 4**, zero empty directories. **11 levels from 6 tile sets**, read from two parallel fixed-stride tables in `alfred`, plus a 12th entry (`cloud`) that exists only in the tile-bank table | **135 / 6** (`/C`, `/CDXL`, `/Devs`, `/Libs`, `/Pages`, `/S`), of which **115 are electronic-book pages** and **3 are CDXL streams**. The game is **three files** |
| Bytes on disc / unpacked | 2,721,914 / 10,284,352 | 13,251,697 / — | 109,786,031 / — | 99,327,202 / — | 4,514,540 / **8,543,154** | 4,351,859 / **11,836,224** | 168,272,839 / — (**91.2 % of it speech**, 7.1 % wall sprites, 1.7 % game) | 492,497,755 / — (**98.1 % of it one video file**) | 1,315,110 / **3,855,390** | 2,156,143 / **4,285,931** | 2,249,822 / **2,249,822 — nothing is packed** | 2,879,663 / **5,768,936**; **bytes actually used 5,542,774 (96.1 %)** | **2,035,183 / 2,906,735**; **bytes actually used 2,898,523 (99.7 %)** — buffer slack **0.3 %**, the tightest in the set | **4,397,639 / 9,217,125** (used 9,172,928, slack **0.5 %**) | 59,789,206 / 61,610,596 whole tree; **6,939,994 / 8,363,560 game only** | 8,126,565 / **17,404,587** whole disc; **4,102,748 / 13,336,690 Superfrog alone** — the resident figure is **0.64 % past Marvin's 13,251,697** | 2,722,021 / **3,726,007** — expansion **1.369×, the lowest of ten measured**; used 3,723,675, slack **0.063 %**. On disc it sits **21.0 % above Guardian's floor**, so the floor survives a second disc predicted to break it | **1,261,776 / 1,636,635** — expansion **1.297×, the lowest of eleven**; used 1,610,416, slack **1.602 %**. **Breaks Guardian's floor by 43.9 %**, the first disc to do so in eighteen — because the content is in Red Book, not in the data track | whole tree **70,262,959** — but **93.90 % of it is CDXL video** and 4.38 % is the manual, so the disc total is meaningless for the band. The **game is 1,033,508 on disc / 1,258,076 resident** (1,211,470 on disc if the whole boot chain counts), and `RoboCod` alone is **959,956 / 1,185,496**. **Breaks Alfred Chicken's floor by 18.1 % on disc and 23.1 % resident**, the second time in two discs. Expansion **1.217×, the lowest measured** — and structurally so, because it is a `BSS` declaration and not a decompression |
| Compression | RNC ProPack 1, 84 of 91 files, 25.7 % | **none at all** | **none at all** | **none at all** | **Imploder `IMP!`, 35 of 47 files, 52.8 %** | **Bytekiller, no magic number**, 79 of 111 files, 35.2 % | **`RNC` with a 12-byte header — not RNC ProPack**, 44 blocks in 5 files, 1.0 MB of the 2.9 MB that is not speech or walls | **none at all** — nothing above entropy 7.2, no magic anywhere in 523 MB | **CrunchMania `CrM2`, 115 of 131 files, 30.0 %** — the fifth cruncher on the format, and the credits name its author | **RNC ProPack 1 with a rotating XOR key over the literals**, 106 blocks in 92 files, 49.1 % — three variants (fixed `0x5ED0` x88, plain x15, stream `0xBE1A` x3) | **none at all**, on any file — but **nine images inside the executable are ByteRun1**, and the same title's A1200 floppy packs the sprite banks it cannot fit | **RNC ProPack 1, 37 of 45 files, 45.7 %** — and Dragonstone's decoder unpacked all 37 first run. Plus **RNC ProPack *method 2* inside `picture.exe`**, 329,184 B in three hunks, which the file census scores as uncompressed | **PowerPacker 2.0 (`PP20`) — the seventh cruncher**, 21 of 29 files, 69.2 %, every one with the same `[9,10,12,13]` table and every one decoding to its declared length. **The format has no checksum at all**, so the length is the only validation there is. Plus **29 further PP20 streams nested inside already-unpacked files**, which a file census misses and for which **no 8 KB entropy window anywhere on the disc exceeds 7.5 b/B** | **RNC ProPack 1, 47 of 52 files — and nested three levels deep: 342 validated streams, every CRC good** | RNC ProPack **method 2**, 542 streams in **3 of 140 files**, depth 0 only, 96.1 % of `cd32rez` | **Imploder `ATN!`, 96 of 221 files**; 158 validated streams, **depth 2**; 3.25x on the game alone. Plus 2 `CrM!` and a **ninth container, `PaCK`** | **Bytekiller — the eighth cruncher, under a magic nobody had seen: `DAVE`**, the programmer's first name. 23 streams (22 with the container header, 1 bare), 2,526,172 → 3,530,158, 71.6 %. **Nesting depth 0**, and the checksum Legends' copy had removed is still here, so every stream validates three ways | **RNC ProPack method 1, real** — 11 streams, decoded by the unmodified Dragonstone decoder with the header CRC validating **11 of 11**. Seven are whole files, **four are embedded inside `alfred`**. **Nesting depth 0**, reached by decoding. 104,373 → 479,232 = 4.59× on the streams alone | **none.** Thirteen container magics over all **205,056,000** raw bytes return **0**; no file's first longword equals its size or size−4; **1 of 135** above 6.7 entropy and it is an 11-hunk executable with a 256-colour title screen in it. The 115 manual pages use IFF **`ByteRun1`** (ratio 0.404, 7.36 MB → 2.98 MB), which is a format feature and not a packer. **And there is a mechanism**: all three of the game's hunks are `CHIP`, 1,185,496 bytes of a 2 MB budget, so there is no room for a decrunch buffer even if there were a reason |
| PVD system id | `CDTV` | `CDTV` | `CDTV` | `CDTV` (correctly, this time) | `CDTV` | `CDTV` | `CDTV` | `CDTV` | `CDTV` | `CDTV` | `CDTV` | `CDTV` | `CDTV` | `CDTV` + 28 spaces | `CDTV` | `CDTV` | `CDTV` + 28 spaces — and this is a **CD32** disc: Akiko, `freeanim.library` and `movec cacr` all say so | `CDTV` + 28 spaces — wrong again: `lowlevel.library`, `freeanim.library` and `setpatch 40.14` all say CD32 | `CDTV` |
| PVD application id | `DragonStone` (the title) | `Platformer` (the genre) | `Game` (the medium) | **empty** | **empty** | `Legends` (the title) | `Liberation CD32` (title **and** console) | **empty** | **empty** | `Legacy of Sorasil CD32` (title **and** console) | **empty** | `Banshee CD32` (title **and** console) | **`Fire&Ice CD32`** (title **and** console) — the second disc to answer that box this way | **`Iniverse CD32`** — the title with one adjacent key wrong, on a retail pressing | `Gunship 2000 CD32` | **`s/startup-sequence` — a path, not a title**; the first time this field is neither name nor genre nor medium | **empty** | **empty** | **`RoboCod_CD32`** — the title *and the console*, a shape no other disc here uses; volume identifier `RoboCod_CD`, so the master spells the game two different ways in two adjacent fields |
| Cue `CATALOG` | absent | `5012635300344` | `5024913000068` | — (no cue) | **`0000000000000`** — thirteen zeros | `5012323060062` | **`0000000000000`** — thirteen zeros again | **`0000000000000`** — thirteen zeros, the third disc | — (no cue supplied) | absent | **`0000000000000`** — thirteen zeros, the fourth disc | **`5020717200444`** — a real UK EAN-13, Core's own `502071` prefix | **`5018247373455`** — a real UK EAN-13, the second real catalogue number here | `5020717200529`, a real UK EAN-13 | `5015352330281` | **`5022358170384`** — a real EAN-13 | `5020573000264` — a real EAN-13 | **`0000000000000` — and for the first time in the set this was read from the disc**, not from someone's cue: subchannel Q MODE-2, **MCVAL=1**. The thirteen zeros are what the master carries, so the four discs showing them are not a dumper artefact | **`0000000000000`** — the **fifth** disc in the set with the thirteen zeros. Not confirmable from an image, which carries no subchannel; transfers by provenance from [Alfred Chicken]'s physical read |
| Mastering tool | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | **not ISOCD — unidentified** | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | **ISOCD 1.03** (Pantaray) — the first non-1.04 master here | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 by Pantaray | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) |
| Preparer field | `Sajjad Majid - ...` | `Stewart.. - ...` | `Almathera - ...` | **empty** | **empty name**, tool signature only | `Richard Teather (Programmer) - ...` — **and he is in the credits screen** | `D J Pocock - ...` — **and he is nowhere else on the disc** | **empty name**, tool signature only — the second such disc | **empty name**, tool signature only — the third such disc | `Kevin Dudley - ...` — **and he is `Programming` on the credits screen** | **empty name**, tool signature only — the fourth such disc | **`D J Pocock - ...` — character for character Liberation's**, a different studio and publisher; nowhere else on either disc | **`D J Pocock - ...` — the third disc with this name**, character for character; a third studio and a third publisher | **`D J Pocock`** — the **fourth** disc with this name, and the fourth to leave 232 | **`D J Pocock - ...` — the fifth** | **`Kenny Grant - ...` — a THIRD pattern**, neither `Pocock` nor empty; and `s/T17Menu`'s `$VER:` names `Kenny G` as **the menu's author**, so the man who cut the master wrote the front end and not the game | **`ROB NORTHEN COMPUTING, UK. TEL: + 44 428 707771 FAX: + 44 428 707772 - ...` — a FOURTH pattern: a company with contact details**, not a person and not empty. The firm is the author of **RNC ProPack**, the set's commonest cruncher — and this master does not use it | **`Abersoft - ISOCD 1.04 by Pantaray, Inc. USA -` — the SECOND company** in the field after Rob Northen Computing. Not Pocock, and the final run is **32**, so `D J Pocock`→232 survives at **5 of 5 against 13 of 13** — and survives its first same-label test, since Mindscape's other disc (Liberation) *is* Pocock. `Abersoft` appears nowhere else on the disc | **`Dean Ashton - ISOCD 1.04 by Pantaray, Inc. USA -`** — a **sixth named individual**, and *not Pocock leaves 32* is now **14 of 14**. It is also the **first disc where the man in that field identifies himself on the disc, in the first person**: the boot script's 44-line comment is signed `by the master of the kludged code, Dean Ashton`. And he is the **conversion programmer**, credited by both credit screens — so the field can record a studio's own programmer, a **sixth owner-type** after operator, bureau, company, contractor and menu author |
| Duplicate PVD | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | **yes** — the one habit that crosses tools | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, 16 and 17, terminator at 18 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17, terminator at 18 | yes, sectors 16 and 17 **byte-identical whole-sector**, terminator at 18 | yes, sectors 16 and 17, **byte-identical in all 2,048 bytes**; terminator at 18 |
| Volume starts at LBA | 20 | 20 | **6019 — 6,000 zero sectors first** | 19; **path tables at 48,633, after the files** | 19 | 19 | 19; M path table at 19, L at 20 | 19 — **but the first file is at 15,023, after 15,000 zero sectors** | 19; M path table at 19, L at 20 | 19; M path table at 19, L at 20 — **but the first file is at 24,295, after 24,272 zero sectors** | 19; M path table at 19, L at 20; **first file at 23 — no front gap** | 19; M path table at 19, L at 20; **first file at 24 — no front gap**, on a disc that streams Red Book during play | 19; M path table at 19, L at 20; **first file at 24 — no front gap**, on a disc that is 68 % Red Book and plays it during the game | **19**, first file at **24**, no front gap | 22 (root) — but **the files start at 51,225**, after **exactly 100 MiB** of zeros | 20 | 19 — **but the first file is at 25,624, behind a hole of exactly 50 MiB** | 22 (root); **first file at 23**, no hole anywhere | 19 (path tables 19 and 20, `.TM` 21, root directory 22) — **but the first file is at 65,559**, because LBA 23–65,558 is a hole |
| `.TM` block at | sector 21, 2,048 B | sector 21, 2,048 B | **6021**, 2,048 B, and again as `/CD32.TM` | **48,621, 22,152 B**, and it *is* `/CDTV.TM` | **21, 22,152 B** — eleven sectors | 21, 2,048 B | 21, 2,048 B | 21, 2,048 B | 21, 2,048 B | 21, 2,048 B | 21, 2,048 B | 21, 2,048 B | 21, 2,048 B | **21**, 2,048 bytes | sector 21, 2,048 B | sector 21, 2,048 B | sector 21, 2,048 B, reached through the `'TM'` tag at PVD byte 888. **No `.TM` file in the root** | sector 21, 2,048 B, reached through the `'TM'` tag at PVD byte 888, constant `0x0014`. No `.TM` file in the root | sector 21, 2,048 bytes, from the pointer rather than the constant: `TM` tag at app-use offset 5 (absolute 888), constant `0x0014`, length `0x00000800`, LBA `0x00000015` |
| `.TM` contents | trademark banner + 876 B `exec` object | identical | identical | **`cdtv.device` 35.2, Carl Sassenrath — no banner anywhere** | **`cdtv.device` 35.2 — the CDTV driver, on a CD32 disc** | trademark banner + 876 B `exec` object — **the fourth identical copy** | trademark banner + 876 B `exec` object — **the fifth identical copy** | trademark banner + 876 B `exec` object — **the sixth identical copy**; no `.TM` file in the root | trademark banner + 876 B `exec` object — **the seventh identical copy**; no `.TM` file in the root | trademark banner + 876 B `exec` object — **the eighth identical copy**, and the first written by ISOCD 1.03; no `.TM` file in the root | trademark banner + 876 B `exec` object — **the ninth identical copy**; no `.TM` file in the root | trademark banner + 876 B `exec` object — **the tenth identical copy**; no `.TM` file in the root | trademark banner + 876 B `exec` object — **the eleventh identical copy**; no `.TM` file in the root | the common Commodore banner + `exec` object — **all three SHA-1s match, twelfth disc** | the common 2,048 B; all three SHA-1s identical | **identical** — the standard three SHA-1s, and **not** Speris's, on the other Team 17 disc: the block follows the **tool**, predicted in writing | identical — all three SHA-1s match, making it **fifteen of the sixteen CD32-era discs** | identical — all three SHA-1s match, making it **sixteen of the seventeen CD32-era discs** (Speris still the odd one) | **identical** — all three SHA-1s match (`c5ffcef2…` / `8d841151…` / `690aae24…`). **Seventeen CD32-era discs with the Commodore banner and one with the CDTV driver.** No `.TM` file in the root |
| Unclaimed sectors in the volume | — | 32, all zero | **32, all zero** | none | **32, all zero** | **32, all zero** | **232, all zero** — the number that broke the "always 32" fingerprint | **32, all zero** — on a 255,552-sector volume, which kills the 'small volumes' reading | **32, all zero** — on a 772-sector volume, which kills the last size reading | **32, all zero, at the end** — *and* **24,272, all zero, at the front** | **32, all zero, at the end** | **232, all zero** — the second disc to do this, and the second `D J Pocock` disc | **232, all zero** — the third disc to do this and **the third `D J Pocock` disc**; on a 1,270-sector volume, so **18.3 % of the whole volume**, the largest share the anomaly has taken | **232**, all zero, LBA 2,197–2,428 — **9.6 % of the volume**, predicted in writing before the map was built | **232**, all zero — plus the 51,200 in front of the files | **32, all zero, LBA 4132-4163** — and separately a **30**-sector overrun past the declared volume, a new value for that column | **32, all zero, at the end** — *and* **25,600 in front of the files, exactly 50.000000 MiB, 94.86 % of the declared volume**; plus a **374**-sector overrun past the volume, the largest so far | **32, all zero, at the end** (LBA 659–690) — the ordinary final run; plus **227 sectors past the declared volume**, all zero but **genuine MODE1 with valid sync, matching header address and passing EDC**. First disc that could prove the overrun is the mastering and not the dumper | **32, all zero, at LBA 99,943–99,974** — the non-`Pocock` value, on a new name. **Plus a 65,536-sector hole at LBA 23–65,558** — **134,217,728 bytes = 128.000000 MiB, 2^16 sectors, every byte verified zero** — which is **65.55 %** of the declared volume and the **third *round* hole** in the set after 50.000000 MiB and 100 MiB. With the CDXL padding, the trailing run and the overrun, **69.75 % of the data track is zero** |
| Timestamps | AmigaDOS 1978 epoch, except 3 files | real 1994 dates; dirs 1992; **2 files at the MS-DOS 1980 epoch** | four epochs: 131 at 1978, **1,213 inherited from the CDTV build**, 84 Commodore stamps, 43 real | one 4½-minute session, all real | **all real**; four sittings, Dec 1995 and Jan 1996 | **all 118 read 1992-03-06**; four sittings, and the PVD is stamped before nine of its files | 184 real (1993-05-19 to 1994-01-23); **12 at 1992-02-05, disproved by the executable's own build stamp**; the root record at the 1978 epoch | **inverted**: all 34 files real and self-consistent; **the PVD itself at the 1978 epoch**. Three sittings; the whole game copied in **66 seconds** | **all real and all one hour**: 128 files copied in 17 s, the executable 48 min later, the master 35 s after that | **all real**; 92 files in a six-minute copy on 1994-06-02, three files on three later days, the executable 11m34s before the master | **60 of 61 files and all 6 directories in one seven-second copy** (1994-08-03 11:36:39–46); `/game` alone at **1980-01-09 23:17:58 — the MS-DOS epoch, day 9** | **41 of 45 at 1992-12-21 15:11:46–15:27:34, a wrong clock**, disproved by the executable's own build banner; 3 `C:` commands 1993; boot script 1994-06-22; directories and PVD 1994-07-08. The two zero-length files carry an all-zero stamp | **two clocks and no AmigaDOS epoch anywhere.** 19 files with real 1994 dates that read as a work log — six `Graphic` files in one second, seven `Set` files one a minute, `SetPatch` and `core4.bin` **18 s apart**, the two executables **2m08s apart** — and **10 files at the MS-DOS 1980 epoch**, the largest such group in the set. Inheritance from the 1992 floppy release was a priori plausible here and is **disproved by the disc**: 1980 predates the Amiga, and `AskBoot`, a CD32-only tool, is in the 1980 group. **No `1992-12-21` anywhere** | **all real, no wrong clock, no 1978 or 1980 group**: three inherited 1993 utilities, 44 files in one 9 m 36 s pass on 1994-08-26, four rebuilt in 26 s on 09-02, the two programs 5 s apart on the morning of the master | real, 1993-12-20 to 1994-04-19, 24 calendar days — **no 1980 and no 1978 epoch at all**, from the most DOS-first publisher here | **two calendar days, 19 distinct stamps**; no 1978, no 1980; PVD **25m22s newer** than the newest file; but the **root directory record is 1994-08-17, seven days older than every file it indexes**, stored identically in all three places | **all eight records 1992-12-21**, in two clusters: the three floppy images and the boot script in 2 m 53 s at 15:12–15:15, then **1 h 44 m 34 s of nothing**, then `/myth` alone at 16:59:25. PVD **+11 m 33 s**; **root directory record −1 s** from the newest file, which is step 37's second and first *normal* reading | **all 33 records in 1993**, five calendar days. Fifteen files copied in a **9-second block** on 11-30; `/alfred` alone on 12-06 after **21 h 26 m** of nothing. PVD **+3 m 29 s** from the newest file, the tightest in the set; **root directory record −33 s**, normal, stored identically in three places. **Zero 1980 and zero 1978 timestamps** — the fourth such negative. And a dating instrument the set has not had: **expanded RCS `$Header:` keywords**, `Hard0:alfred/rcs/amiga.c 93/11/19 JJS` and `.../intro/rcs/amiga.c 92/09/29 JJS` — **fourteen months apart** | **two epochs, and the disc is otherwise clean.** One file in the 1978 AmigaDOS epoch (`C/SetPatch`, 1978-02-01 15:00:02, falsified by its own `$VER: setpatch 40.2 (17.2.93)`); everything else real, 1993-06-07 to 1993-08-17, a legible ten-week build log. **No 1980 MS-DOS epoch** — on a disc whose largest asset was demonstrably converted from PC-side 16-bit TARGA captures, which is a real negative for that candidate epoch. The directory records are a **second** build log agreeing with the first |
| SetPatch | 40.14 (7.10.93) | 39.6 (8.9.92) | 40.12 (16.9.93) | none — `bookit` + `rmtm` instead | **40.16 (14.2.94) — ships, never run** | **39.6 (8.9.92) — byte-identical to Marvin’s** | 40.12 (16.9.93) | **none — no `c/` directory at all** | **40.3 (10.5.93)** — a fifth version | **40.12 (16.9.93) — byte-identical to Liberation’s and Prey CD32’s**; `c/Assign` 37.4 byte-identical to four other discs | **40.3 (10.5.93) — byte-identical to Gloom's and to this title's own A1200 floppy**; no `c/` at all, it sits in the root | **40.14 (7.10.93) — byte-identical to Dragonstone's**, and the only same-label pair among six binaries | **40.14 (7.10.93) — byte-identical to Dragonstone's *and* Banshee's.** Third disc, second studio, second label: **the 'only same-label pair' reading of this hash is retired.** No `c/Assign` on the disc | **40.14 (7.10.93)**, 13,200 B, SHA-1 `00d74a35…` — predicted before opening the disc | 40.14 (7.10.93) — dropped into an otherwise **37.x** `C:` directory | **40.16 (14.2.94), 13,484 B — a sixth version and a size not seen before**, in an otherwise 37.x/38.x `C:` | **none — no `c/` directory at all**, and no `libs/`, `devs/` or `fonts/` | **`c/setpatch 40.14 (7.10.93)`**, beside `c/assign 37.4 (25.4.91)` and `c/execute 37.11 (14.5.91)` — three Commodore commands from two OS releases two and a half years apart, and the newest is what dates the master | **40.2 (17.2.93)**, `b308c42d7193ba8ec99b8813910d8099e121e17d`, stamped 1978-02-01. Neither the version nor the bytes match [Alfred Chicken]'s 40.14 (7.10.93) |
| First stage | 1 hunk, 3 relocations, **0 library calls**, Akiko direct | 6 hunks all chip, 4,278 relocations, **169 library calls**, no Akiko | 1 hunk any-mem, 245 relocations, 64 library calls, **0 hardware registers** | **324 bytes**: open dos, load the game | none — a **7-line** script, 4 of them `assign` | none — a **9-line** script; `ShutDown`, `SetPatch`, 6 `assign` | none — a **22-line** script that mounts a **recoverable RAM disk** and makes it bootable | none — a **five-byte** boot script: `cosm` | none — a **three-line** script; `freeanim`, `setpatch`, `gloom`, all in the **root** (no `c/`) | none — a **seven-line** script; `setpatch`, `/loaderblackpal` (in the root), `Stack 8192`, **three `Assign`s of floppy volume names**, `QuestII 2` | none — a **three-line** script; `setpatch`, `freeanim`, `game m1 f`, both commands in the **root**; and `s/startup-sequence.bak` beside it runs **`sw`** | none — a **twelve-line** script with a **live `DebugDisk:` developer branch** and four `assign bansheeN: CD0:` | none — a **nine-line** script: `SetPatch QUIET`, `AskBoot`, then `FireNTSC` or `FirePAL` on `If WARN`. No assign, no RAM disk, no debug branch. **`AskBoot`** is a 3,144-byte SAS/C program whose payload is **14 instructions** reading `GfxBase->DisplayFlags` bit 0 | **`loader`, 40,820 bytes of which 757 are code**; opens `dos.library`, reads `cd0:intro.prg`, `SuperState()`, `INTENA`/`DMACON` cleared, decrunches to `$70000` and jumps. The other 40,003 bytes are a read buffer left in `HUNK_CODE` | `gunship 2000`, 3 hunks, 119 relocations — assigns four **floppy** volumes and chains | **there is none.** `s:T17Menu` is a program that **writes `ram:T17.bat`**, and the startup-sequence executes what it wrote — dispatch by generated shell script | `/myth`, 18,656 B, 1 hunk, **0 relocations** — fully self-relocating. **3 library calls** (`OpenLibrary`, `CloseLibrary`, `Disable`), **0 `OpenDevice`**, **Akiko direct**. Contains **four media back ends** (DOS, floppy with MFM decode, hard disk with `RigidDiskBlock` parsing, CD) and a **hand-written `LoadSeg`** | `/alf`, 13,736 B, 2 hunks, 8 relocations (1.49/KB) — **a SAS/C 6.00 C program that is 46.9 % debug information**: `HEADDBGV01`, the full symbol table, `alf.c` and a line-number table, all pressed. What it does is run `intro` and then `alfred` | the **boot script itself**, which is a shell-level main loop — `Lab select` / `RoboSelect` / three `if` blocks on an `ENV:` variable / `Skip select BACK`, forever — and then `RoboLoader`: 1 hunk, 93 relocations, 45 library calls, whose whole job is to blank the screen and start the game. The game's own prologue is the requirements list: `ExecBase->AttnFlags` tested for 68040/030/020 into three flag bytes read back with **one `tst.l`** (exit code 100 otherwise), five `OpenLibrary` at **V39**, and `GfxBase->ChipRevBits0 & $0C == $0C` — **both AGA chips or refuse to run**, in four instructions |
| Game executable | (same file) | (same file) | 1 hunk, **5,323 relocations**, 120 library calls, **448 register writes** | 71,316 B, and a **324-byte** first stage | 1 hunk, **1,647,128 B in chip**, 3,404 relocations, 72 library calls | 1 hunk, 37,848 B **in chip**, 1,020 relocations, 60 library calls | 4 hunks, 225 KB code + 14 KB data + 32 KB bss + **40 bytes chip**, 1,356 relocations, 181 library calls | 2 hunks, 106 KB code + 117 KB **chip** data, **22 relocations**, ~50 library calls, **68020-only addressing**, and **78 `HUNK_DEBUG` blocks naming 77 source files** | 1 hunk, 174,128 B `MEMF_ANY`, 1,277 relocations, **no symbols and no debug hunks**, 56 library calls, **29.9 % of the hunk is zero** | 6 hunks, 1,153,536 B allocated (**762,988 chip**), **0 relocations, 0 symbols, 0 debug in the file** — it decrunches and relocates itself in 584 bytes, with 5,524 relocations compressed inside the hunks; 78 library calls, 33 LVOs | **3 hunks** — 152,164 CODE (any) + 232,188 DATA (any) + **245,656 DATA (chip)**; 5,113 relocations, 4,893 of them hunk 0 into itself; no symbols, no debug, **no `$VER:` anywhere**; 62 library calls, 32 LVOs | **6 hunks** — 97,500 CODE + 26,932 DATA + 342,356 BSS + 288 CODE (chip) + 16,752 DATA (chip) + **1,285,052 BSS (chip)**; 1,948 relocations; 71 library calls, 33 LVOs; **1.30 MB of chip RAM claimed before it allocates anything**. A second executable, `picture.exe`, is **named by nothing on the disc** | **two whole executables, one per video standard.** `FirePAL`: 2 hunks — 92,236 CODE (any) + **309,252 DATA (chip)**; 2,155 relocations, 2,106 of them hunk 0 into itself; no symbols, no debug, **no `$VER:` anywhere** — the version is a bare banner, `AGA 1.04`, inside XOR-`0x1b` text. `FireNTSC` is the same program 364 bytes shorter, built **2m08s** later; the two differ in 23 scanlines of copper list and one string | **`code.prg`, a private relocatable format**: `u32` offset to a trailer of `u32 0 + u16 900 + 900 x u16` **word** offsets, byte position = `entry x 2 + 4`; base 0; head is a **123-entry `jmp abs.l` export table**. Second `LoadSeg` re-implementation in the set | **two**: `gs` (front end, 0 blitter writes) and `gs2.run` (engine, 177) | `SuperFrogCD`, 1 CODE hunk, **8,996 relocations (43.6 per KB)**, 21 `jsr d16(a6)` sites. `TUNNELDEMO` is the opposite: **0.63 per KB**, all 904 in the first 2.51 % — step 36's second instance | `MYTH.A+s3c00`, 126,700 B, 5 hunks, **2,950 relocations** (35.5/KB); a second program `MYTH.C+s79548`, 75,336 B, 177 relocations (29.6/KB), draws the ending | `/alfred`, 816,616 B, 8 hunks, **7,231 relocations**. The whole-file 16.46/KB is meaningless — **the 6,102 relocations of its 441,780-byte CODE hunk all sit in the first 24.2 %**, so it is ~107 KB of code at ~57/KB followed by ~335 KB of data in a CODE hunk. Also `/intro`, 255,376 B, **42.46/KB**, built from source checked out **fourteen months earlier** | `RoboCod`, **3 hunks, every one `CHIP`**: 324,632 `CODE` + 613,612 `DATA` + 247,252 `BSS` = **1,185,496 resident**. 5,399 relocations (**16.63/KB of code**), of which 133 in the 600 KB data hunk and **all of them in its first 528 bytes**. 69 library calls. **No `HUNK_SYMBOL`, no `HUNK_DEBUG`** — and a string in the file says `I'm not stupid enough to leave debug symbols in`, which is true. **Everything is in this one file**: 86 levels, all art, all sound, a 12-byte-per-level table of 86 records, 16 small jump tables (73 branches) |
| Libraries opened | none | 10, via `OldOpenLibrary` | 6, via `OldOpenLibrary` | `cdtv.device`, `bookmark.device` | 5: graphics, dos, intuition, lowlevel, nonvolatile | 3: dos, intuition, graphics (+ `cd.device`, `ciaa`/`ciab.resource`) | **9**, all via `OpenLibrary` (−552): dos, intuition, graphics, lowlevel, nonvolatile, **and three in-house — `vector`, `tridee`, `math`** | 5: graphics, nonvolatile, dos, lowlevel, **freeanim** (+ `cd.device`, opened twice) | 3, via `OldOpenLibrary`: dos, graphics, nonvolatile (+ `ciaa`/`ciab.resource`). **`lowlevel.library` never opened** | 4, all via `OpenLibrary` (−552): dos, graphics, nonvolatile, lowlevel (+ `cd.device` twice, `input.device` once). **`graphics.library` is never called** | **3**, all via `OldOpenLibrary` (−408): nonvolatile, dos, graphics — in that order (+ `cd.device` once). **`lowlevel.library` never opened and not on the disc**; `freeanim` opened by a 72-byte root command | **5**, all via `OpenLibrary` (−552): lowlevel, freeanim, graphics, dos, intuition (+ `cd.device`, `input.device`, `audio.device`). Files are loaded with `dos.library` `Open`/`Read`/`Seek`/`Close` | **5**, all via `OpenLibrary` (−552): **freeanim**, lowlevel, nonvolatile, dos, graphics — in that order (+ `cd.device` **twice**, `input.device` once). Files are loaded with `dos.library` `Open`/`Read`/`Close`. An `audio.device` name string ships and is reached by nothing | **`dos.library` only, in the loader. Zero library and device calls in either game program** | 8 named + 3 devices; **AmigaDOS alive throughout**, and the script regains control after the game exits | `dos`, `graphics` (game); `intuition`, `iffparse`, `diskfont`, `lowlevel` (`T17Man` only) | **1, and its result is discarded**: `freeanim.library` is opened and closed without being tested | **8 `OpenLibrary` in each of `alfred` and `intro`, 3 in `alf`**; 2 `OpenDevice` each against exactly two named devices (`cd.device`, `input.device`) | **five by the game at V39** — `dos`, `intuition`, `graphics`, `lowlevel`, `nonvolatile` (the last allowed to fail) — plus `cd.device` **twice** and `input.device`. Across the five programs: **ten libraries and five devices**, including `gadtools`, `asl`, `iffparse`, `utility`, `console.device`, `audio.device` and `cdtv.device`. **AmigaDOS is alive from the first instruction to the last in every one of them** — the credit line `A1200/CD32 OS-Friendly conversion` is measurable, and the mechanism is two named interrupt servers, `ROBO_VERTB_Server` and `ROBO_COPER_Server`, hung off Exec's own chains |
| `freeanim.library` | opened by `c/FreeAnim` | opened **first** by the game, never called | opened by the first stage; `c/freeanim` ships unused | **not present — `c/rmtm` instead, and it is run** | opened by `c/FreeAnim`; **not on the disc** — it is in CD32 ROM | **opened by `c/ShutDown` in order to `RemLibrary` it** | opened by `c/FreeAnim` (SAS/C, template `/auto/close/wait`); **`c/CloseAnim` ships too and is run by nothing** | opened and closed **four instructions apart, with nothing in between** — the documented pair, with a zero-length gap | opened by `/freeanim` in the root — **byte-identical to Liberation’s `c/FreeAnim`** | opened **first** by `/loaderblackpal` in the root, closed after three further opens; that file keeps its **13 symbols** | opened by **`/freeanim`, 72 bytes, 18 of them code** — the smallest wrapper on the format, and the gap is zero | opened by the game; **not on the disc and no wrapper command** — CD32 ROM only, so this executable cannot run from this disc on an A1200 | opened **first** by the game; **not on the disc and no wrapper command** — CD32 ROM only. And the Workbench script tries `Assign Libs: Fire:Libs Add` when **`/Libs` does not exist**, so the A1200 path is broken twice over | opened by `C/FreeAnim` — **byte-identical to Liberation's, timestamp included** | **named by `gs` and `CDGSXL` and not present on the disc** | **opened by three binaries; no `FreeAnim` file on the disc** — library and file are different things | **opened and immediately closed, result never read** — a CD32 probe whose answer nothing uses | **named by both game executables but not shipped** — taken from CD32 ROM. (Liberation, the other Mindscape disc, ships its own copy in `c/`) | opened by **`C/FreeAnimation`, a purpose-built 120-byte wrapper** whose entire program is `OpenLibrary("freeanim.library", 0)` followed immediately by `CloseLibrary` — opening it *is* the effect — carrying its own `$VER: FreeAnimation 1.0 (7.6.93)`. **Third disc** to reach it, and not byte-identical to the `C/FreeAnim` that Liberation and Universe share |
| Akiko | driven directly | untouched | untouched | n/a (CDTV) | untouched | untouched | untouched — 0 pointer loads, 0 C2P-port references, 0 `$C0DE0000` | untouched — **0 references to `$00B80038` in 9.5 MB of code**, and the decoder writes planar directly, so there is no chunky data to convert | untouched — **0 `$00B80038` in the image, in all 131 files and in all 115 decrunched files**, and the 3D view has **no planar destination** to convert to | untouched — 0 `$00B80038`, 0 pointer loads, 0 `$C0DE0000` in the image, in all 97 files and in all 111 decrunched blocks; the 6 bare `00 B8 00` hits include **ProTracker’s period table**, the same one Gloom shows | untouched — 0 `$00B80038`, 0 pointer loads, 0 `$C0DE0000` in the image and in all 61 files. **Eleven of eleven**, and on the best candidate yet: the rasteriser writes planar with the Blitter, so there is nothing to convert | untouched — **0 pointer loads, 0 `$00B80038`, 0 `$C0DE0000`** in both executables and all 37 unpacked files. **Twelve of twelve on the C2P port**, and the best remaining candidate for the drive-controller use came back zero | untouched — **0 pointer loads, 0 `$00B80038`, 0 `$C0DE0000`** in both executables and all 21 unpacked files. **Thirteen of thirteen on the C2P port.** The two raw `00 B8 00 38` hits are at **odd offsets inside the chip data hunk**, inside a run of `F8`/`FC`/`E0` bytes — planar sprite mask, not an address | **DRIVEN — 3 x `lea $B80000,a5` (CD-ROM) and 2 x `lea $B80030,a2` (I²C EEPROM).** C2P port **0 of 14**, `$C0DE0000` **0 of 14**. The inherited scan missed all five: it matched 2 of 8 address registers | untouched — **0 / 0 / 0 / 0**; the one `$C0DE0000` hit straddles two entries of a stride-16 table | **untouched — 0 / 0 / 0 / 0** across `$B80000`, `$B80030`, `$B80038`/`$3C` and `$C0DE0000` | **driven directly** — 1 pointer load of `$00B80000` (third disc in seventeen, first outside Core Design), displacements `$04 $08 $10 $14 $18 $19 $1A $1D $1F $20 $24`. **0** `$B80030`, **0** C2P port, **0** `$C0DE0000` | **untouched — all four figures zero**: 0 loads of `$00B80000`, 0 of `$B80030`, 0 C2P port, 0 `$C0DE0000`. Predicted absent from the *mechanism* — the disc boots AmigaDOS, leaves Exec alive and reaches the CD through `cd.device` | **untouched — 0 / 0 / 0**: zero `$00B80000` pointer loads across **all eight** address registers, zero `$B80030`, zero C2P port `$B80038`/`$B8003C`, in all five programs. C2P merge constants **122 as data, 0 as immediates**. The drive is reached through `cd.device` and the save EEPROM through `nonvolatile.library`, so even the two non-graphics uses go through Commodore's layers |
| Colour | `FMODE = 0`, ECS path on AGA silicon | **all palettes 12-bit** | **6 of 14 screens exceed 12-bit** | all 12-bit, as ECS requires | **24-bit palettes in all 16 levels**, 6 planes | **front end 8 planes / 256 colours / 24-bit; levels 4-5 planes / 32 colours / 12-bit** | **`LoadRGB4` only, `LoadRGB32` never**; the one stored palette is 32 entries, all ≤ `0x0FFF` | **genuine 24-bit AGA, loaded entirely from the copper**: 8 `BPLCON3` banks x 32 registers x 2 (`LOCT`), 8 bitplanes, `FMODE 0x400F`. **`LoadRGB4` and `LoadRGB32` both never called** | **128 colours at 24 bits**, built into a 1,072-byte copper list at run time (4 banks x 32 registers x 2 `LOCT`). `LoadRGB4` and `LoadRGB32` both never called | **32 colours, 5 bitplanes**, 6 in EHB below raster line 204 (`KILLEHB` clear). **No `BPLCON3`, `BPLCON4`, `FMODE` or `DIWHIGH` anywhere on the disc**; `LoadRGB4` and `LoadRGB32` both never called; the start-up blank writes exactly 32 registers | **64 entries at 8 bits per gun** in AGA registers **128–191**, reached through `BPLCON4`'s `BPLAM = $80`; `BPLCON3` banks 4 and 5, each twice with `LOCT`. `FMODE $000F`. `LoadRGB4` and `LoadRGB32` **both never called** — the third zero-zero disc | **256 colours at 8 bits per gun**, from **16 `BPLCON3` blocks** (banks 0–7, plain and `LOCT`) × 32 registers in the copper; `FMODE $0007`; `KILLEHB` set. And the unreferenced `picture.exe` runs **HAM8** with a 64-entry 24-bit palette. `LoadRGB4` and `LoadRGB32` both never called | **32 colours at 8 bits per gun**, from `BPLCON3` banks **0 and 1**, each written plain and with `LOCT`, entirely in the copper; `PF2OF = 5` puts playfield 2 at colour 32. **`LoadRGB4` and `LoadRGB32` both never called** — the fourth zero-zero disc. Bank 1 is reloaded **193 times down the screen**, once per scanline of the play area; bank 0 gets its low nibbles exactly once. The only palette baked into the file is the status panel's, and it is **12-bit — high nibbles only** | **32 colours, 12-bit, six bitplanes in Extra-Half-Brite** (`BPLCON0 $6200`, `BPLCON2 $001B`, `KILLEHB` clear). **No `BPLCON3`, `BPLCON4` or `DIWHIGH`; `FMODE` written once with zero.** `LoadRGB4`/`LoadRGB32` both never called — the fifth zero-zero disc, and the first where the reason is that the OS is gone | 256 colours (8 planes) in the front end via `LoadRGB32`; 16 (4 planes) in the flight engine — **the first disc here that calls both `LoadRGB4` and `LoadRGB32`** | **5 bitplanes, 32 colours**, `BPLCON3` written only to safe defaults, **`FMODE` never written in any validated list**; the one 6-plane list has `KILLEHB` **clear**, so **Extra-Half-Brite** — on a volume named `SuperFrog_AGA`. The real AGA is *Arcade Pool*'s `BPLCON0 $0210`, **BPU=8**, the third `BPU3` trap in the set | `FMODE = 0` (written five times) and `BPLCON3 = 0`, both by the loader and by nothing else; ECS-style output on AGA silicon. **`LoadRGB4` and `LoadRGB32` both called zero times** — every colour comes from a copper `MOVE` or an IFF `CMAP` | **`intro` calls `LoadRGB4` *and* `LoadRGB32`, once each — the third disc in the set to call both**, and unlike Superfrog these are in a shipped game executable. `alfred` calls neither (4 × `LoadView`) and takes its colours from copper `MOVE`s built in code. **No palette is stored anywhere** | **24-bit, on a 32-colour screen.** The one stored copper list writes `COLOR00`..`COLOR31` **twice**, with `BPLCON3` `$0000` then `$0200` between the passes — AGA `LOCT` pairs — so 32 simultaneous colours chosen from 16.7 million. **Neither `LoadRGB4` nor `LoadRGB32` is called**: the palette reaches the hardware only from the copper. Elsewhere on the disc: the CDXL streams carry a **fresh 32-colour palette in every one of 2,530 chunks** (a frame-by-frame quantiser) while the 115 manual pages share **one** byte-identical 256-colour `CMAP` (an artist), and `ident.cdxl` is **HAM6** — 6 planes with a 16-colour palette, identified from the header arithmetic rather than by rendering |
| Graphics | interleaved planar, 3 and 4 planes | interleaved planar, 6 planes (one file separated) | **separated planar**, 4 planes; ILBM at **8 planes** | same frames, 4 planes; ILBM at **5 planes** | interleaved planar, 6 planes; 16×16 tiles + **3 property planes** each | **separated planar**, 8 planes; 16x16 font glyphs also separated | **separated planar**, 4–6 planes; `ImgA` skips all-zero planes; **10,792 pre-rendered wall sprites instead of a texture mapper** | planar, **5 / 6 / 7 / 8 planes** selected per frame; video 320 x 144, decoded plane by plane with unrolled `move.l` | **7 bitplanes**, interleaved, 320 px, double-buffered; screens are ByteRun1 inside CrunchMania; **everything else is 8-bit chunky** and the 3D view is a **copper list, one `MOVE` per pixel** | **separated planar**, 320 x 200 at 4 and 5 planes; sprites 32 px x 6 planes (5 + mask), **24 bytes per row on all 36 sheets**; dungeons are 64 x 64 grids of 8-byte cells | **two stacked screens**: a 320 x 38 **six**-plane HUD panel over a 320 x 200 **four**-plane 3D view, both interleaved, `BPL1MOD = 200`; per-scanline 24-bit sky from a 7,144-byte copper list fed by 16,384-byte `LOCT` tables | **two eight-plane screens** — 320 × 256 lores for the game and **640 × 256 hires** for the pictures; picture files are 1,024 B of hardware-format palette + 163,840 B of interleaved bitmap. Objects are masked bob blits (minterm `$CA` with **`USEA` set**, six planes, 24,576 B plane stride); the only `BLTCON1` write carries a B-shift and **no fill bits**. `picture.exe` displays **640 × 512 interlaced HAM8** | **one eight-plane dual-playfield screen.** `BPLCON0 $0611`, whose plane count is **`BPU3` at bit 4** — a scan of bits 14-12 reads it as zero. 320 px foreground over a **960-px-wide** parallax layer, four interleaved planes each, derived from `BPL1MOD 120` and `BPL2MOD 440`; a four-plane status panel takes over 193 lines down. **One stored copper list on the whole disc**, a 5,496-byte template in the *code* hunk with every colour and every bitplane pointer zero-filled. Tiles are **16 x 16, four interleaved planes, 128 bytes**, 576-660 per world. Blitter: minterm `$CA` x7 with **`USEA` set** (ordinary masked bob), `$F0` x4, `$C0` x2; `BLTCON1` written twice, `$0000` both times — **no fill, no descending blit, no line mode** | **separated planar**, 320 x 200 x 6 in a 352-px-wide buffer (44 B/row, `BPL1MOD 2`, `DDF $30/$D0`); pictures are `6 x 8,000 + 64` and `8 x 8,000 + 64`, the extra two planes being **1-bit walk-behind stencils**. `copper.prg` is a stored list that is **96.5 % reserved space** — two regions of exactly 3,200 empty slots, 16 per scanline for 200 lines, double buffered. Blitter: no `FILL`, no `LINE`, one immediate `BLTSIZE`, `$CA` with `USEA` set | IFF ILBM throughout, 70 of 73 at 320x200x8; the engine's screen is **4 contiguous planes blitted as one `BLTSIZE $C814`**, h=800 = 200 rows x 4 | planar in planar, the ninth. C2P constants **42,017 as data, 37 as immediates — and four of the six are zero**. Tiles derived, not guessed: **840 x 16x16, 5 planes interleaved per tile, 160 B each**; blitter modulos give a **384-px** buffer over a 320-px screen | interleaved planar, **5 planes / 320×100 window** and **4 planes / 320×200**, from the modulos `$A0` and `$78`. **16 of 32 colour registers are `$0000`** in the five-plane list. **3 copper lists** accepted from 16 loose and 4,448 rejected runs. Blitter: no FILL bit in any readable `BLTCON1`, no `$CA` minterm, 13 of 16 `BLTCON0`s register-loaded | planar, **no C2P: 163 constants as data, 0 as immediates** — the 11th planar-in-planar disc; `$AAAAAAAA` and `$55555555` absent in both roles, so not even Myth's MFM merge. **Zero stored copper lists** (4,052 candidate runs rejected) — built at run time. Screen mode *is* hardcoded: `BPLCON0 = $4200` (**BPU 4**) in `alfred`, `$5200` (**BPU 5**) in `intro`, `BPLCON3 = $1400` so AGA is really used. **Tiles 16×16×4, 128 B, row-interleaved; maps 32×32 byte indices** — derived from three independent measurements: every graphics piece an exact multiple of 128, max map index exactly (len/128)−1 on **7 of 7**, and BPU=4 from the register. Blitter: **no FILL bit, no `$CA` minterm**, every BLTSIZE computed | interleaved planar, **5 bitplanes** (`BPLCON0 $5201`, `BPU3` clear) with a **4-plane region** (`$4201`); `DDF $30/$C8` = 320 px, `DIW` rows 44–252. `BPL1PT`..`BPL5PT` re-pointed **five times** down the screen, 8 sprites, and **14 copper `WAIT`s making two seven-line `COLOR01`/`COLOR02` ramps** at rows 109–115 and 228–234. **One** stored copper list (820 B) out of 6,122 candidate runs rejected. Blitter: **`BLTCON1 = $0000` on every readable write** — no fill, no line, no descending — minterms `$F0` and `$FC` only and **no `$CA` anywhere**, so not even an ordinary masked bob. Video: 320 × 100 × 5 scan-doubled, and 250 × 200 × 6 HAM6 |
| Text encoding | CP437, with two files in a third encoding | ISO 8859-1, all four languages | 7-bit ASCII, and there is almost none | 7-bit ASCII, and even less of it | 7-bit ASCII, 30-char fixed lines, **no apostrophe in the font** | 7-bit ASCII; **accents and eszett dropped**, not transliterated | 7-bit ASCII; a caret-introduced generator language, `0xD7` records, `0xB1` speech markers | 7-bit ASCII, upper case, five typos in the shipped mission text | 7-bit ASCII, lower case, and the mission script ships as **editable plain text** | 7-bit ASCII; **accents remapped onto punctuation** — `)` = Ä, `*` = Ö, `+` = Ü, `(` = Ç, `<`/`>` = quotes and apostrophe | 7-bit ASCII, upper case, **one language and about forty lines of it**; a 32-character alphabet string is the font's only index | **CP437 for German and French *and* a private substitution for Danish in the same table** — `"` Æ, `$` Å, `+` æ, `=` å, `~` ø, `0x9C` Ø, confirmed by the ordering of the hall-of-fame alphabet | 7-bit ASCII **XORed with the constant `0x1b`** — every user-visible string on the disc, including the strings inside the PowerPacker streams. The key is recoverable by scoring all 256 candidates; the giveaway is `;` where a space belongs | **7-bit ASCII + CP437**, 23 distinct high bytes and every one a character these four languages need — the cleanest encoding case in the set. Plus an accent-folding table beside a **UK Amiga keyboard map** | 7-bit ASCII — **no byte above 0x7F in any prose run on the disc** | **ISO 8859-1, correct in all three accented languages**; English has **zero** bytes above `0x7F`. Prose **1.054 % on disc / 0.496 % resident** | **7-bit ASCII, measured: 0 bytes above `0x7F` in 3,893 bytes of display text**. Prose **0.068 % on disc, 0.054 % resident**. A **fourth string model**: a relocated longword page index over `[flag][col][row]TEXT` record chains, 71 records, 28 pages, **0 empty slots** | **7-bit ASCII, measured: 0 bytes above `0x7F` in any prose run**. Prose **0.607 % on disc, 0.468 % resident** — but **0 % of it is in any asset file**, 19.6 % belongs to Commodore's commands and 78.8 % to a debugger and the SAS/C runtime. **A FIFTH string model: there is no table, because there is no text** — the game's own title exists on the disc only as a 320×184 four-plane *picture* | **none — a sixth string model, and the mirror of [Alfred Chicken]'s.** **10,875 bytes** of ASCII prose on a 195 MiB volume (0.0155 % of the file bytes), and the **largest single contributor is the boot script** at 1,878 bytes because 44 of its lines are a comment. The disc's 2.93 MB manual contains **no characters at all**: it is 115 IFF ILBM pictures of typeset text, so string count, encoding and accent handling all return zero and the localisation has to be measured **in pixels** |
| Languages | 3 (EN/FR/DE) | 4 (EN/DE/FR/IT) | 1 (EN), with Danish filenames | 1 (EN), same Danish filenames | 1 (EN) | 3 (EN/DE/FR) | 1 (EN) — **and a 384-word note to translators, plus 23 accented glyphs nothing prints** | 1 (EN) | 1 (EN) | 3 (EN/DE/FR) — **and 19 strings were never translated, 18 of them the whole ending** | 1 (EN) | **4 (EN/DE/FR/DA)** — and the Danish is not a translation: it renames the hero `Svend` and adds a joke the other three do not have | 1 (EN) | **4 (EN/FR/DE/IT), complete** — 602,344 bytes of prose, 6.53 % of the resident image, and **zero strings byte-identical across all four** on the 87 records that align | **1** (EN). The German build is of the **bundled Pirates! Gold demo**, not of the game | **4 (EN/FR/DE/IT)**, complete — and the manual is a **script in an in-house markup language**, shipped in source with its comment banners | 1 (EN), and no localisation of any kind | 1 (EN), and no localisation — nor anything to localise | **3 for the manual, 1 for the game** — the first disc here where those differ. `uk` 37 pages, `fr` 38, `gr` 40 (German runs 8.1 % long); **one page of 115 byte-identical across all three**, and it is the largest and inkiest, i.e. the only illustration with no text; mean **12.94 % of pixels differ** between the English and French copies of the same page. Chapter indices byte-identical for EN and FR, shifted by one page for DE. A Deluxe Paint **`DPPS`** chunk on 17 pages — 10 EN, 7 FR, **0 DE** — names the paint package and splits the artwork production. The **game** has no language selection at all |
| Music | 1 CD track + 1 ProTracker module | 11 CD tracks + 12 in-house `.pc` modules | **1,225 raw PCM files at 19,705 Hz** | **1,258 of the same files**, 178 scenes | **12 ProTracker modules** — 8 files, 4 embedded | **28 CD tracks** + 1 ProTracker module + 8 IFF 8SVX in the level code | **10 CD tracks** + 46 IFF 8SVX effects; **no ProTracker module, and the executable still names `mod.ingame`** | **13 ProTracker modules**, one per overlay, + 4 whole IFF 8SVX effects with their `ANNO` chunks; 1 Red Book track **never played**; 864 KB of raw PCM **interleaved between video frames** | **2 OctaMED `MMD1` modules**; 24 effects each carrying its own Paula period; no CD audio and no `cd.device` | **5 CD tracks, 2 of them reachable** + 6 ProTracker modules + 39 raw PCM effects; the replay is `Imagitec ProTracker Replay Routine (C) 1991 Imagitec Design Ltd` | **12 CD tracks, every one reachable** — played out of the disc's own TOC with `CD_PLAYTRACK`/`SendIO`; **no module, no 8SVX, no PCM file**; effects compiled into the chip data hunk and driven on channel pairs | **2 CD tracks, both played** + **2 Player 6.0A modules**; effects in two sample banks with a 16-byte record header each; Paula programmed both absolutely and through `d16(a6)` | **22 CD tracks** + an **in-house Paula replayer** written straight to `AUDnLCH/LEN/PER/VOL` with the channel index shifted in at run time; **no module and no PCM file anywhere**. The options panel offers `Off` / `On Chip` / `On CD`, so the player chooses which. **The disc never reads its own TOC** — `CD_PLAYTRACK` with `io_Offset = index + 2`, a constant in the executable. Second negative case, and the one with the most tracks to get wrong | **23 CD tracks, 40:37, and nothing else at all** — no module, no 8SVX, no PCM file, and Paula reached only by two `AUD1DAT` writes. `OpenDevice` is **zero**; the drive is driven through Akiko. A **third answer** to the TOC question, and the reachable track count is open | 5 CD tracks; **no module of any kind**; 2 raw PCM blobs, plus **15 IFF 8SVX inside an executable nothing runs** | **37 modules in The Player's own format** (26 `P41A`, 11 `P40B`) — **a fifth home for the music**, invisible to a tracker scan and to a cruncher scan. **0 ProTracker, 0 OctaMED.** 27 IFF `8SVX`, **all inside a binary** | **2 OctaMED `MMD0` modules** — 20 blocks/21-entry sequence and 4 blocks/3-entry sequence; **2 of 18 instrument slots empty**, **0 of 18 named** (the `iinfo` entry size is 2 bytes). 0 ProTracker, 0 The Player | **Red Book only**: 9 tracks, 20 m 32 s. **0 tracker modules, 0 IFF 8SVX, 0 The Player, 0 IFF FORMs of any kind on the whole disc.** Sound effects are **raw 8-bit PCM inside the executables**, headerless and nameless, found only because a device-path scan false-positived on `TUKLD:` inside a waveform | **7 Red Book tracks and every one of them reachable**, from **byte 11 of an 86-record, 12-byte-per-level table**, where **bit 7 of the music id chooses Red Book or Paula** — and all 86 choose Red Book. Tracks 3–8 used 15/14/19/9/24/5 times, track 2 from a constant in the front end. **The TOC is never read**: exactly three CD commands on the disc — `CD_PLAYTRACK` (37) and `CD_PAUSE` (40) twice, pause and resume — and no `CD_INFO`, `CD_TOCMSF`, `CD_TOCLSN` or `CD_GETNUMTRACKS`, with a bare **250-frame countdown** re-issuing the play. **No ProTracker, OctaMED or The Player module, no IFF `8SVX`, no PCM file**: effects are raw inside the chip data hunk. Separately, the CDXL player runs **1,122 B/frame of 8-bit mono on two Paula channels** with the period corrected from buffer drift every interrupt |
| Save system | password, 64-char alphabet, bit field | password table + CD32 `nonvolatile.library` | **none** | **none** | CD32 `nonvolatile.library` **and** floppy save-disk code | password, 8 characters; **no `nonvolatile.library`** | CD32 `nonvolatile.library` (4 vectors, one call each) **and** `RAM:Game.DAT` **and** a reset-surviving `RAD:` disk | CD32 `nonvolatile.library` alone, unguarded — app `MCOSM`, item `core`, ten bytes, **first word incremented every launch** | CD32 `nonvolatile.library` alone — app `Gloom`, item `Games`, **stores 2 bytes and reads 20 back** | CD32 `nonvolatile.library` alone — app `Hero Quest II `, item ` Save`; **stores 24 bytes and reads 238 back** (`divu.w #10` on the length) | CD32 `nonvolatile.library` alone — app `Guardian`, item `Heroes`; **stores 8 bytes and reads 80 back**; base null-checked at every call site | **none at all** — no `nonvolatile.library` anywhere, no password, no save file. The hall of fame lives in RAM and its default table is the development team | CD32 `nonvolatile.library` alone — app **`FireAndIce`**, item **`HiScores`**; the record is the 20-row high-score table. Both directions go through **generic wrappers taking the length in `d0`**, so there is no literal size at the library call and the store/read mismatch four other discs show cannot be checked here | **the CD32 EEPROM, over hand-written I²C at `$B80030`** — the first disc here that does not use `nonvolatile.library`, because there is no Exec left to call it. **And a complete second, unreachable save system**: `Please insert a save game disk.`, a format prompt and a filename entry prompt, on a console with no floppy drive | **`nonvolatile.library`** — the CD32 EEPROM through the OS, not through `$B80030` | **none.** `nonvolatile.library` ships and **nothing on the disc opens it**; no binary loads `$B80030` either | **none** — no `$B80030`, no `nonvolatile.library` shipped or opened. The only persistent-looking structure is a five-name default high-score table in RAM | **none**, confirmed two ways: 0 loads of `$B80030`, and `nonvolatile.library` is **neither shipped nor named by any game binary**. A third route to the same answer — Superfrog shipped it and opened it from nowhere, Myth had no `libs/` at all | **CD32 serial EEPROM through `nonvolatile.library`** — project `RoboCod Data`, item `High Score`, at hunk `$7fc` and `$809`. No password system anywhere. Where [Universe] bit-bangs the same hardware through Akiko's I²C port because it has no Exec left, this disc calls Commodore's library: the two ends of the same abstraction stack |
| Cut content | level 4, `0xFFFF` row in the loader table | 3 unlisted working levels, 1 unused music file | 7 sprite banks, 1 door animation, 2 files the code still names, **scene 0 dropped** | the same 7 sprite banks and door are already missing here | template level name in all 16; a **corrupt `BGFX` tag that shipped**; a crunched level in a stale buffer | `Legends_Disk4:` named by nothing, 18 `SIGN MESSAGE n` placeholders, 15 `XXXX` records, `EMPTY PAL` slots | `MainSP16.Img`, `Wall.Log` and `mod.ingame` named and absent; three test objects (`FatAnt.x3d`) and three pre-split geometry files present and unnamed; `[Sorry, this is only a 1 disk demo.]` in the retail binary | **`briefing` and `eolb4` named in the loader table with a presence flag of 0** and their `LEVELS/*4.S` modules still linked in; `filelist.i`/`filelist.s` generator stubs; the whole debug console and 195 copies of `internal hardware error` | the floppy release’s **hard-disk installer**, its boot script, its save file and two disk prompts; a demo build’s refusal; **ten debug colour flashes**, one of them the whole out-of-memory handler; 224 `FFFF` palette slots per texture bank; and **no zone 2 anywhere** | `Level.Map` named by the loader and absent; **a title screen that still reads `MASTERS`**; the publisher logo shipped twice, the unreferenced copy **with the copyright line removed**; `Please insert Legacy of Sorasil Patch` naming a fourth floppy volume; a complete disk-swap wait loop with **no callers**; three Red Book tracks nothing plays; nine placeholders x 3 languages; an empty container slot and four more pointing at end-of-file; map cell byte 7 zero in all nine dungeons; `BLUEBITS`/`GREENBITS` symbols with no code | a **twelfth zone's assets nothing can load** (`split12`, `spr12` — the largest sprite bank on the disc — `sprhead12`, `map12`), plus `map00`, `map99`, `dither00`, `dither98` and `dither99.iff`: **179,796 bytes, 8.0 % of the disc**, against an eleven-record zone table; `dither99.iff` is the **artist's Deluxe Paint working file** with its `GRAB` and six `CRNG` chunks intact; `PIRATES FUCK OFF` beside the copyright string at the top of the code hunk; **`hElP` written at the end of seven buffers and checked at run time**; `WAS ` and `GON `, four bytes each, in front of the two strings the save code does address | **`picture.exe`, 9.5 % of the data track, named by nothing** and holding a 640 × 512 HAM8 picture; the installer chain as **two zero-byte files** (`/scrpt2`, `/C/Installer`); an **empty `/icons`** on a disc with no `.info` anywhere; a thirty-eighth loader filename **with no record header**, `bans1:flev`, naming a volume nothing assigns; a **flashing-border halt loop with an `ILLEGAL` behind it**; a **live `DebugDisk:` branch** in the pressed boot script; and eight English-only lines, outside the four-language table, asking how anyone could seriously want to kill animals and civilians | a **floppy disk-swap prompt** (`Please put volume <n> in any drive and press FIRE or SPACE.`) and a **manual-lookup copy-protection prompt** (`Please match the key at location: F*7`) in a 1994 CD32 executable; `Assign Libs: Fire:Libs` naming a directory that is not there; a **developer diagnostic panel** reporting free chip RAM, free fast RAM and **disk cache size**, which is also the only place the build version is written down; **two empty directories**; `AskBoot` shipping its **`HUNK_SYMBOL` table** (`_OpenLibrary`, `_CloseLibrary`) and the whole SAS/C runtime error path it never reaches; **nine resource slots zero in all seven worlds**; an `audio.device` string nothing uses; and a default top high score of **68000 points to `AEB`** — the CPU part number and the programmer's initials | **18 files the shipped executable names and the disc does not have** — `block1_1.np` … `block5_4.np` and `capt.np`, 32 % of a 56-name loader table, with `block5` listed before `block4`; the whole floppy save-disk system and the **UK keyboard map** that serves it; `1meg.pak` and `fmem.pak` named for memory configurations a CD32 does not have; the intro script naming a **PC version of the game**; **40,003 zero bytes** in the loader's code hunk; `Iniverse CD32`; **four gazetteer slots empty in both copies of the same table** (12, 13, 15 and 40, at the ends of two runs, in a table that otherwise describes thirty places in full) and two null pointers in the inventory table; and a backtick for an apostrophe in one of 39 inventory descriptions| a **complete, unreachable Pirates! Gold demo** disabled by one commented-out line; `roster.dat` = `ERASE ME` / `THE ERASABLES`; a font descriptor pointing at a directory that does not exist; an empty `/GS2000/` | **`SDIFF:`**, a build-machine assign, left in **26 shipped level files** naming 8 IFF sources that never shipped, spelled three ways across 52 occurrences. Plus an **unclosed `@SCREEN`** from a doubled paste in the English manual only, and `PARTF` carrying a **second build of the engine** | **`THE SERIAL NO IS` / `GGGGGGGG I THINK`**, a live page of the credit table; `SNUFFLECAKE`; a pad combination that writes `COL!` into `$C0` and is never read back; **Commodore's `ConClip 37.7` pressed onto the disc** in unused floppy blocks (the disc's only `$VER:`); `SYS3` ×896 as a fill pattern; a `SPAM` memory probe with one branch patched out; `\myth\source\screens\ScreenA.lbm`; bootblocks dated **29/8/2004**; and the sequel `DAWN OF STEEL` named in the ending | **`intro` ships a working Amiga hardware debugger** — 47 register description strings lifted verbatim from Commodore's `hardware/custom.i`, plus **`copdis`, a copper list disassembler** with a null guard and an `UNKNOWN_OPCODE` path; `alfred`, built 14 months later, has none of it. **`alfred.info`'s DefaultTool is the string `JUNK`** with zero ToolTypes. **`End Of All Vars!`** between the globals and the code. The shipped boot script tests for a developer's own volume **`JJSDISK:`** (the disc's only unresolvable reference, and deliberately guarded), `alfred` carries **`alf2:%s`**, and RCS stamped **`JJS`** and **`Hard0:`** into both executables. **57 tiles drawn, packed, pressed and never placed by any map** (72 of 563 across seven banks, 12.8 %). `frontend.pak` is **shipped twice** — byte-identical inside `alfred` | **none identified**, and all three menu branches are reachable — the `FI5H` token that looked unreachable from the boot script alone is in `RoboSelect`, and page 1 of the book shows `FI5H FILE` is its **title**. Two things are shipped and not reached: an in-game level selector (`ROBOCOD MAP SELECT!`, `CURR. SECTION`, `SECTION NUMBER?`) whose reachability is open, and an **`ExtDebug.port`** message port in the book reader — the second shipped debugger hook in the set after [Banshee]'s `DebugDisk:`, and the first inside a binary rather than in a script |

---

**AND THE FLOOR MOVED AGAIN, ON THE VERY NEXT DISC, FOR THE SAME REASON.**
[James Pond 2] is **1,033,508 bytes on disc and 1,258,076 resident** —
**18.1 %** and **23.1 %** below [Alfred Chicken], which had itself broken a
floor that stood for seventeen discs. Two discs in a row, and both are platform
games whose content lives somewhere other than the data track: Alfred Chicken
puts 99.02 % of its pressed disc into Red Book, this one puts 41.95 % into Red
Book and 32.22 % of its volume into CDXL video.

That is enough to state what the floor was ever measuring. **It was measuring
"titles that keep their content in the file system", not "how small an Amiga
game can be".** A 1993 CD conversion can put the content in Red Book, in a
video stream, or in a picture-book manual and ship an executable that would
have fitted on two floppies — 959,956 bytes, 1.07 double-density disks. The
**ceiling has never moved** across nineteen discs, five years and every genre
the format had, and it is bounded by 2 MB of chip RAM and a 68EC020. **Quote
the ceiling; treat the floor as a property of the question.**

**And this disc forces the definition to be stated rather than assumed.** Its
file set is 70,262,959 bytes, of which 93.90 % is a cartoon and 4.38 % is a
manual. Quoting the disc total would overstate the game by a factor of **68**.
[Superfrog] made the same point at a factor of 2; this one makes it
unignorable. **Before quoting a band figure, say which files you counted**, and
if the disc has a non-game payload, give both numbers.

**A note on the expansion column.** That disc's is **1.217x**, below [Myth]'s
1.369x and [Alfred Chicken]'s 1.297x — and it is **not the same kind of
number**. Theirs are decompression ratios; this one is a `BSS` declaration on a
disc where nothing is packed, so it is bounded below by whatever the
uninitialised data happens to be. **The column mixes two quantities and should
be split** the next time it is touched.

## 11. The order of work that worked

1. **Read the cue sheet.** Track count, modes, `CATALOG`, pregaps. Eleven
   audio tracks and one data track is as much a CD32 disc as one and one.
2. **Dump the volume descriptors** — including the application-use area, the
   application identifier, the path-table LBAs, and whether the PVD is
   duplicated. **Do not assume the volume starts at 19**; Prey's starts at
   6019.
3. **Walk the directory and build a sector map.** List what is *not* claimed
   by any file. On this format that is where the trademark block turns up.
   Build it against the *declared* volume size, not the image size.

   **And the overrun past the declared volume is the mastering, not the
   dumper — [Alfred Chicken] settled this from the plastic.** Fifteen of the
   first seventeen images run 32..232 sectors past their declared volume and
   from a file it is undecidable. On this disc the declared volume is 691
   sectors, the disc physically carries **918** sectors of MODE1 data — every
   one with a valid sync pattern, a header address matching the sector asked
   for and a passing EDC — the extra 227 are all zero, and **they stop exactly
   where the next track's pregap begins**. So the data run is padded up to the
   following track, which explains the whole 32..232 range without invoking a
   dumper artefact anywhere.
4. **Find the `'TM'` tag in the application-use area, read the length and the
   LBA after it, and dump exactly that many bytes.** Not sector 21, not 2,048
   bytes: the CDTV Prey master declares 22,152 bytes at LBA 48,621 and what is
   there is a device driver. On a CD32-era disc, hash the result in three
   pieces against section 2. **Then look for the `.TM` file in the root** —
   both Prey masters ship it as a file, dated, and on CD32 that file is where
   the `exec` fragment came from.
5. **Sort the directory by timestamp** before reading a single file. Free, and
   it has given up a subsystem on all three discs. Recognise four epochs
   (1978, 1980, a wrong-by-years clock, real), and separate file dates from
   directory dates. **Then, before doing anything else with an outlier, grep
   that file for `$VER:`** — on Liberation the game executable's own build
   stamp (1994-04-08) disproved its 1992 directory record in one line, where
   Prey needed a whole second release of the game to settle the same question.
   **And if there is no `$VER:`, look for a bare build banner**: Banshee's is
   23 bytes between an `rts` and the next routine, `8/7-94 12:59 CD32 slutp`,
   and it settles a nineteen-month discrepancy on its own. Then **subtract**:
   if a trustworthy clock brackets the wrong one and the wrong one's span fits
   inside the window, its *relative* times are a real write log and can be read
   file by file.
6. **Read `s/Startup-Sequence`, the whole of `c/`, and the whole of `libs/`.**
   Every `$VER:`. Then diff `c/` against the boot script and see what ships
   without being run. **If there is no `c/`, list the root** — [Gloom] keeps
   `freeanim` and `setpatch` there and the boot script names them with no path.
   **And hash every one of them**: two files have now been shown to circulate
   between unrelated studios as single copies (`SetPatch` 39.6 on Marvin and
   Legends, `freeanim` on Liberation and Gloom). **Look for a `.bak` beside the
   boot script**; on Gloom it is the previous release's script, pressed.
   **And read the boot script as a program rather than as a launcher** — three
   discs now have something in it that is not about launching the game, and on
   [Banshee] it is a five-line branch that executes a script off a volume
   called `DebugDisk:` if one is present. It survived because it is not in the
   executable, so nothing about building the executable would have removed it.
7. **Parse the first stage as a hunk file** — hunk count, memory flags,
   relocation counts, symbols — then run the greps of section 4: count
   `4E AE` first, because it decides how you read everything else. Then
   histogram `00 DF F0 xx` rather than searching for the base address, or you
   will miss a program that writes every register absolutely. **And check
   whether there are two executables**: Prey's front end and its game are
   separate programs that talk over message ports, and Liberation's game runs
   three more (`CityGen`, `PlotGen`, `BuildingGen`) plus a fourth for the
   intro. **Then find where the library bases are kept.** If they sit in one
   A5-relative block, tracking the last `movea.l d16(a5),a6` while walking the
   code turns the whole ambiguous LVO histogram into one exact list per
   library — 181 calls into nine named lists, in one pass.
   **And check for `HUNK_DEBUG` before you do any of it.** [Microcosm]'s
   executable carries 78 of them: a `HEADDBGV01` index and 77 `HCLN` line
   tables, one per assembler source file, each naming its file
   (`CDCODE/CDXLINT.S`, `FRAMEHANDLERS/NONINTERACTIVE256.S`,
   `COPPER/DOUBLEEBITCOPPERLIST.S`) and the offset where its code begins. That
   is the whole architecture of the program for the cost of parsing one hunk
   type, before a single instruction is disassembled, and it tells you which
   region to look at for anything you want. **Verify a few of the offsets
   against the disassembly rather than trusting the decode** — the start field
   is variable width and the line-delta stream desynchronises on some modules,
   so quote first-code offsets and module names, and do not quote sizes you
   have not checked.
8. **Census the file set for packing before you scan for magic, because a
   magic scan can return nothing on a disc that is 65 % packed.** [Legends]
   scans clean for every magic in section 5 and has 79 of 111 files packed.
   The two free tells are entropy (every packed file above 6.7, every raw
   palette below 5.8) and a **first longword equal to `filesize` or
   `filesize - 4`**, which is a container header with no name. Then scan for
   `RNC`, `IMP!`, `ATN!`, `PP20` and `XPKF` — all of
   them, in one pass.** `RNC` alone would have reported Speris as
   uncompressed while 6.8 of its 8.5 MB sat behind `IMP!`. If there is
   nothing, say so and move on. If there is, **find the decruncher in the
   loader rather than a description of the format on the internet**: grep the
   executable for the magic as an immediate (`0C 90`/`0C 93` + the constant),
   disassemble what follows, and transcribe it. On Speris that was 350 bytes
   and it worked on the first run. Then check every file's self-check — RNC's
   CRC, the Imploder's pair of pointers landing on zero together.
9. **Census the file set**: sizes, entropy, zlib ratio, last non-zero byte.
    **And check the obvious header lengths against the file size** — `14 +
    packed == filesize` identified CrunchMania's container on all 115 of Gloom's
    packed files before a bit was decoded, and `4 + 2 * n == filesize`
    identified a four-byte period/length header on all 24 of its raw samples.
    A relation that holds across a whole family is worth more than a magic
    number.
   Fixed sizes and partial occupancy tell you the memory map — **and then read
   the padding, because it is often not zero.** Hash the tails across a family
   while you are there; a family that splits into two or three tail hashes is
   a build split you now know about for the cost of one line.
10. **Look for the loader's or the editor's own table.** Dragonstone's is a
    run of filenames and an index table in the loader; Marvin's is a
    fixed-offset trailer in every level file and a plain-text disk map
    compiled into the executable. Both are dense runs of same-length strings.
    **Grep the whole disc for `/` and for its own directory names.**
11. **Check every file for a `HUNK_SYMBOL` table**, not only the executables.
    Data files wrapped in hunk format, and in-house libraries, keep theirs.
12. **Disassemble the copper lists** before looking at any pixels — and if
    there are none *stored*, look for the code that **builds** one: a `lea` of a
    template followed by a copy loop into a chip buffer, or a loop emitting
    `move.w #$106,(a0)+` / `move.w #$180+2n,(a0)+` pairs. [Gloom] keeps an
    816-byte template it patches and copies, plus two lists it generates at run
    time — one for the palette and one that **is the framebuffer**. If neither
    exists, autocorrelate wide, then render at several plane counts and look.
    **And count four bytes per pixel in any display allocation**: that is a
    copper instruction, not a pixel.
13. **Compare the language files** against each other, and read their *names*,
    before reading any of them.
14. **Diff the music files against each other** before analysing any one of
    them; the common prefix is the player.
15. **Find out whether the title exists on the other console, or on floppy,
    and diff the two releases byte for byte.** — and before you can do that,
    **read the loader's paths for evidence of the earlier release.** [Speris]
    is a floppy game whose CD32 build assigns `speris-1:` … `speris-4:` to
    `cd0:` and then addresses all 32 of its data files by the floppy volume
    each used to live on. That reconstructs the disk layout for free. Then
    **sort the files by timestamp and check whether the groups match**: on
    that disc the whole data set was crunched in under three minutes and the
    time order reproduces the four-floppy grouping exactly. Two independent
    witnesses to the same layout, and neither costs anything. This is the highest-value step
    on the list and it is the last one added, because it is the only one that
    can tell you that something you already believed is wrong. On Prey it
    turned 1,213 "wrong clock" timestamps into a real build date, confirmed a
    113-file subsystem split from a completely independent direction, showed
    what an AGA upgrade actually changed in the artwork, produced the first
    non-ISOCD master on this format, and demonstrated that the `.TM` block is
    a different artefact on each console. Two releases of one game are worth
    more than two unrelated discs.
16. **Check every path the executables name against the directory.** Every
    one is a plain string; the ones that are missing are cut content that the
    code still believes in, and the files on the disc that no string names are
    leftovers. On Prey this found two absent files and four unused tools in
    about a minute.
17. **Grep every unpacked file for `FORM` + `8SVX` and for `M.K.`** — not
    only the files that look like audio. [Legends] eight IFF samples are
    sitting inside three of its five level executables with their `NAME` and
    `ANNO` chunks intact, which names both the artist's filenames and the tool
    (`Protracker 3.10`). It costs one `find` for four bytes. **[Microcosm]**
    pays it again: four effects are embedded as whole IFF 8SVX files inside the
    overlays, and their `ANNO` chunks read `AudioMasterIV` on two and
    `Audio Engineer` on the other two, naming a development tool that appears
    nowhere else on the disc. **Two discs for two, and both times the `ANNO`
    chunk was the payload.** Look also at *which* names survived: on that disc
    the tracker modules' 22-byte sample-name fields were blanked by the packer
    **except for the `.IFF` extension**, so a file whose samples all read
    `.IFF` has been through a converter, and the handful that escaped are the
    composer's real library.
18. **If there are headerless files that look like waveforms, get the rate out
    of the executable** — the `AUDxPER` immediates — and check the `AUDxLEN`
    immediates against the file sizes. On a disc with no audio track this is
    the whole soundtrack. **And if a huge file has a small file of the same
    name beside it, read the small one first**: Liberation's `.LOG` is nothing
    but a list of 32-bit offsets into the `.SAM` next to it, ending on the file
    size, and it gives 1,248 clip boundaries, the per-clip sample rates and —
    through its `0xFFFFFFFF` entries — the 63 lines that were never recorded.
19. **When one file is most of the disc, parse it before anything else, and
    parse it with a resynchroniser.** [Microcosm] is 92.3 % one 483 MB file, and
    everything interesting about the title is inside it: a per-frame header with
    an **eleven-frame look-ahead size table** so the loader can size buffers
    without seeking, a chunk vocabulary of two, and **three nested checksums per
    frame that all sum to the ASCII constant `'COSM'`** and are enforced at run
    time. Two things to take away. First, **a big file may be a container with
    its own directory**, and the look-ahead table is what makes a stream
    streamable on a 2x drive — look for it. Second, **write the walker so that
    it resynchronises on the frame magic instead of stopping**: on that disc a
    naive walker parsed 65 % of the file and reported the rest as corrupt, when
    the ten unparsed gaps were interleaved PCM and the frames resumed cleanly
    after each one. 99.821 % of the file parsed once the walker could recover.
20. **Find the checksum before you trust your parse, and then run it over every
    record.** The `'COSM'` constant above came out of the disassembly of the
    `CD_READXL` interrupt in seven instructions, and running it over all 30,707
    frame headers — zero failures — is what turned a plausible header layout
    into a verified one. A container that checks itself hands you a test oracle
    for free; a container that does not still usually has a field that must
    chain (an offset plus a length landing on the next offset), which is the
    same thing more cheaply.
21. **Ask whether the game runs the *same* asset twice.** Duplicate SHA-1s
    across a directory cost one pass and have found, on Liberation alone, four
    byte-identical backup executables the loader deliberately names as
    fallbacks, one 30 KB animation stored twice inside the same archive by
    accident, and a whole duplicated ending directory.
22. **When a container you recognise fails its own checksum, do not call the
    file corrupt.** [HeroQuest II] is stock RNC ProPack 1 — 18-byte header, both
    CRC-16s present, `18 + packed == filesize` on all 88 whole-file blocks — and
    a stock decoder produces output of **exactly the right length** that fails
    the unpacked CRC on every file. The container is right and the *stream* is
    obfuscated: every literal byte XORed with the low byte of a 16-bit key that
    rotates one bit right after each non-empty literal run. Two instructions in
    the game's own decruncher (`eor.b d5,-1(a5)` and `ror.w #1,d5`) are the whole
    specification. **Decode it anyway and look at the output** — a table of
    32-bit offsets showing up as `d0 d0 d5 78 d0 d0 d5 78` is a constant XOR
    announcing itself — and then **solve the key rather than searching for it**:
    CRC-16/ARC is linear over GF(2), so one decode with key 0 plus a
    provenance array turns 65,536 candidate decodes into 128 precomputed CRCs.
    Expect a brute-force search to produce about one false positive against a
    16-bit CRC, and check any recovered key on a second file. (Section 5.)

22b. **If a disc contains prose with a date in it, test the date against the
    directory before you use the prose for anything else.** [James Pond 2]'s
    boot script is 3,922 bytes of which twenty-one are the launcher; the rest is
    a signed comment making three checkable claims, and all three pass. It says
    the script was written at **1:30am on 14.07.93** and four files are stamped
    00:03:13 to 01:18:00 that morning. It says *"it's now Sunday 15th August
    1993, at 10:05am"* — 1993-08-15 **was** a Sunday, and three directory
    records are stamped 10:41, 10:42 and 10:49, 36 to 45 minutes later. It
    complains that *"Friday 13th was so bad for us"* while converting animation
    — 1993-08-13 **was** a Friday, and `Intro.cdxl` is stamped 21:33:05 that
    evening.

    ```
    python3 -c "import datetime; print(datetime.date(1993,8,15).strftime('%A'))"
    Sunday
    ```

    Three checks, three `strftime` calls. **And if the prose survives, the rest
    of it has earned a hearing**: that same comment names four development tools
    that leave no other trace on the disc — 16-bit TARGA captures taken with the
    red and blue cables swapped, an ARexx script written to fix them, an A3000
    that died mid-conversion, and a NEC CD-ROM drive on an A4000/040 with beta
    driver software — and it explains a measurable property of the disc's
    largest asset (the CDXL audio arrived as "2 big AIFF sound samples", which
    is why it is one mono stream played on two Paula channels).

    **The general rule: a comment is evidence, and it is falsifiable evidence.**
    Test it like a `$VER:`.

23. **Read the credits screen before reading the code.** It is free, it is
    almost always in the clear, and on [Gloom] it names four development tools
    of which the disc independently confirms three: the cruncher
    (`DECRUNCHING CODE BY THOMAS SCHWARZ` — every packed file is CrunchMania),
    the utility language (`UTILITIES CODED IN BLITZ BASIC 2` — the boot script's
    Workbench icon has `DefaultTool = blitz2:blitz2`), and the paint package
    (`RENDERED IN DPAINT3 AND DPAINT4` — four palettes still begin with Deluxe
    Paint's default sixteen colours). On [Legends] the same trick ran the other
    way, from the mastering tool's preparer field to a photograph in the credits.
    On [HeroQuest II] it runs the same way again — preparer `Kevin Dudley`, and
    the credit scroll's first entry is `Programming / Kevin Dudley` — and the
    credits are **a single bitplane 320 x 3,100**, which renders as two
    superimposed texts at any other depth. **If a credits bitmap looks
    double-exposed, try one plane.** That disc's credits also *omit* something:
    the music player linked into the executable says
    `Imagitec ProTracker Replay Routine (C) 1991 Imagitec Design Ltd`, a
    different studio, and no screen in the game names it. **Diff the credits
    against the strings in the code; both directions pay.**
    **Grep for the game's own title in capitals** and read what is around it.

23b. **Read the boot script as a program, and read the strings of whatever it
    dispatches to.** Four discs now have something in the boot script that is
    not about launching a game, and on [James Pond 2] the script *is* the
    program: `Lab select` plants a label, three `if` blocks switch on an
    environment variable, and `Skip select BACK` jumps back unconditionally — a
    main loop at the shell level, offering a game, a 2 m 43 s cartoon and an
    electronic book as three equal branches, forever, with no exit.

    Two mechanics are worth recognising on sight. The dispatch is through
    **`ENV:`**, which is why `Assign >NIL: ENV: Ram:` is the third line and is
    load-bearing for the whole disc — without it there is no `ENV:` on a
    read-only volume and none of the three branches ever matches. And **one of
    the three tokens appears nowhere else in the script**: `FI5H`. Reading only
    the script leaves the book looking unreachable; reading `RoboSelect`'s
    strings finds `RoboSelection\0Cartoon\0FI5H\0RoboCod\0` in one run at
    offset `0x85e` and settles it in one command. **A boot script's tokens are
    half of the evidence; the program that writes the variable is the other
    half.**

24. **Render the title logo and read it, because the game may be called
    something else.** [HeroQuest II]'s retail logo screen is the only place on
    the disc where the licence appears (`Heroquest © 1994 Hasbro International
    Inc. ... in association with Games Workshop` — there is no such string
    anywhere in the executable or the text files) **and the subtitle it draws is
    `MASTERS`**, on a disc that calls the game `Legacy of Sorasil` in its volume
    identifier, its application identifier, its three floppy volume names and all
    91 paths in its loader. A licence notice and a previous title, both as
    pixels. **Decode the logo screens before assuming the strings are the whole
    naming story.**

    **And decode the pictures the game does *not* show.** [Banshee]'s largest
    image — 640 × 512 interlaced HAM8, 327,680 bytes — is inside a 274 KB
    executable that **nothing on the disc names**, and reaching it means
    noticing that the file's entropy is 7.84, unwrapping three RNC ProPack
    method 2 streams, and reading the geometry out of the copper list beside
    them. **Render every image on the disc, not only the ones the loader
    lists.**

25. **Fix the hunk/file offset convention before you quote a single address, and
    put it in the README.** This is the largest source of silent error on the
    format. An AmigaDOS executable's absolute constants are **hunk offsets** that
    `LoadSeg` relocates; the same numbers as *file* offsets point at unrelated
    bytes, and the two differ by the header length (0x28 on a three-hunk file
    with no resident list). On [Guardian], `move.l #$8b8,$dff080` installs a
    copper list at **hunk 2 + 0x8b8**, not at `$8b8` and not at file `0x8b8` —
    and the only way to know that is the `HUNK_RELOC32` entry covering that
    longword. **Parse the relocation tables first and build a query: "which hunk
    is this constant an offset into, and what file offset is that?"**
    `tools/relocs.py --at` in
    [cd32-guardian-doc](https://github.com/vs-sr-dev/cd32-guardian-doc) does
    exactly that, and it also answers the complementary question — a constant
    with *no* relocation covering it is a literal, and reading it as an address
    is the mistake.

    The same applies to a disassembler's PC-relative targets, which come out in
    whatever coordinates you fed it. And note that **the Capstone M68K backend
    prints wrong-but-plausible immediates and displacements on 68020 code**: the
    raw byte column is the authority, and every constant that reaches
    documentation has to be re-read from it.

26. **Before concluding anything about a title's renderer, ask three questions of
    the Blitter, in this order.** They cost one grep each and between them they
    separate every mechanism this document has met.

    * **Is `BLTCON1` written at all?** No write means no area fill — so a
      polygon engine is doing something else.
    * **What is `BLTSIZE`'s height, and what are the modulos?** Height equal to
      the plane count with modulos of `bytes_per_row − width` is one operation
      per scanline across an interleaved bitmap ([Guardian]).
    * **Is the minterm `$CA` with `USEA` clear?** That is a cookie-cut whose only
      per-pixel input is `BLTAFWM`/`BLTALWM`, i.e. a span fill.

    **A caveat on the third question, from the disc that made it necessary.**
    Minterm `$CA` on its own does **not** identify a cookie-cut: [Banshee]
    writes `BLTCON0 = $0FCA` four times with **`USEA` set**, and that is the
    ordinary masked bob blit (`D = AB + ¬AC`, A the mask, B the sprite, C the
    background). Guardian's span fill is the same minterm with `USEA` **clear**
    and `BLTADAT` loaded once outside the loop. **Read the channel-enable bits,
    not the minterm.**

    And then ask the question section 4 asks: **where does the frame end up?**
    Five answers so far — a planar bitmap written by the Blitter ([Guardian]),
    pre-rendered planar sprites blitted by view ([Liberation]), video encoded
    planar offline ([Microcosm]), a copper list with one `MOVE` per pixel
    ([Gloom]), and an ordinary planar bitmap with no 3D at all (the rest,
    including [Banshee], where the three questions took ten minutes and gave
    the boring answer — **which is worth recording as a result**, because the
    point of the test is to reach it cheaply, not to find something exotic).

27. **Record a Commodore-era file's `$VER:`, not only its hash — the hash is
    not evidence of a shared shelf.** Eleven discs, six `SetPatch` binaries, and
    a matching hash always means a matching version and never means anything
    else; three of the four multi-disc version groups pair unrelated studios and
    unrelated publishers. Section 4 has the table. What a match identifies is
    which distribution a build machine had.

28. **If the title has another SKU, diff the media, not just the file lists.**
    [Guardian]'s A1200 data floppy contains **24 of the CD32 disc's files byte for
    byte**, and finding them costs a substring search for each file's first 64
    bytes followed by an extension of the match. What that bought: the floppy's
    zone layout, confirmation of the CD32 zone table's arbitrary eleven-element
    permutation from a completely independent direction, and the compression rule
    as a controlled experiment rather than a correlation. **A cracked dump is
    still worth diffing** — the crack is on the boot disk and the data disk is
    usually the original's.

29. **Run the container magic scan at every offset and validate each hit by
    decoding it, in addition to the entropy column.** [Fire & Ice] hides 29
    PowerPacker streams inside files that are themselves PowerPacker streams,
    and **no whole-file and no 8 KB windowed entropy anywhere on that disc
    exceeds 7.5 bits/byte** — the embedded blobs are 496 to 3,896 bytes inside
    files of 105 KB to 410 KB, far too small to move an average. Entropy caught
    Guardian and Banshee because their embedded data was hundreds of kilobytes;
    it is a sufficient signal and not a necessary one. A decode-validated magic
    scan cannot produce a false positive and costs one pass. (Section 5.)

30. **Recover a bitmap's stride from the data instead of guessing it, and check
    the answer against the file size.** On [Fire & Ice] nothing stores the
    geometry of anything. Scoring every candidate stride by mean vertical
    byte difference gives a sharp minimum at 8 bytes for the tile banks (28 %
    of the all-strides mean, against 45 % for the runner-up), which is 16
    pixels across four interleaved planes; 16 rows of 8 bytes is 128 bytes, and
    **every one of the seven tile files is an exact multiple of 128**. The
    arithmetic confirming the statistic is what makes it safe to render, and
    the render then confirmed the world tags — `SN01` is snow, `FO01` is
    foliage. `tools/geomguess.py` and `tools/tilesheet.py` in
    cd32-fireandice-doc. (Section 7.)

31. **Scan for a base-address load in all eight address-register forms, not
    one or two.** [Universe] loads Akiko's base into `a5` (`4bf9`) and `a2`
    (`45f9`); the scan this document had been carrying since Guardian matched
    only `41f9` (`a0`) and `2c7c` (`a6`) and returned **zero on a disc with
    five sites**. There are eight encodings of `lea $x.l,An` (`41f9 43f9 45f9
    47f9 49f9 4bf9 4df9 4ff9`) and eight of `movea.l #$x,An` (`207c` …
    `2e7c`). The same applies to `$dff000`, to `$bfe001` and to any other base
    a title might park somewhere unexpected. `tools/akiko2.py` in
    cd32-universe-doc. **A negative result from a two-encoding scan is not a
    negative result.** (Section 4.)

32. **Look for a dispatch table before assuming the game is hard-coded.** The
    shape is short and recognisable: `lea $disp(pc),An`, a few instructions
    turning a byte into an index, `asl #2` and `jsr (An,Dn.w)`, followed
    immediately by a run of `bra.w`. The **opcode count is not stored
    anywhere** — it is the length of that run, and it ends at the first word
    that is not `0x6000`. [Universe] has 16 opcodes in one table and 41
    entries in another; scanning for the `bra.w` run *without* reference to
    the code that jumps into it finds both, and finds them faster.

    Two details that decide whether you have read it right. The index may be
    the **complement** of the opcode (`neg.b` + `subq #1`), which is what
    makes Universe's commands `$F0`–`$FF` and every lower byte inline data.
    And a handler that adds a constant to a **variable** rather than to a
    register is advancing a program counter: that variable is the VM's PC, and
    the constant is the instruction length. (Sections 4 and 6.)

33. **On a text-heavy disc, fix the string-table model before believing the
    text total.** Assume nothing about a length field, about offsets being
    monotonic, or about there being one record shape. On [Universe] the naive
    model found 26 tables and 61 KB; correcting all three assumptions found 49
    tables and 180 KB, and the raw scan over the fully unpacked leaves found
    **602 KB**. Then state the denominator — on disc or resident, they differ
    by a factor of two. (Section 9.)

34. **Render a planar image one plane at a time before deciding the geometry
    is wrong.** Six coherent monochrome images and two solid stencils is a
    different diagnosis from six streams of noise, and it takes one loop. On
    [Universe] a colour render of a six-plane picture came out as structured
    noise and the geometry was correct all along — the palette had 32 entries
    and the display was Extra-Half-Brite. (Section 7.)

35. **Check the byte order of every IFF-shaped file, not just its magic.** IFF is
    defined big-endian and a file that starts with `FORM` is assumed to obey that.
    [Gunship 2000] has **41 files that do not**: its own form types — `SCRN`,
    `SCNR`, `WRLD`, `SHIN`, `SHIP`, `THTR`, `WSYS` — store every chunk size in
    Intel order, so a standard reader reports a **3.4 GB FORM inside a 3 KB
    file** and a census records them as corrupt. Read little-endian, the chunk
    walk lands exactly on the last byte, on all 41.

    The test is one line and it cannot give a false positive: walk the chunks
    both ways and accept the byte order whose walk ends at the file end. Do it
    for every `FORM` on the disc, because the split can run *within* one disc —
    on Gunship every picture is correct big-endian and only the game's own forms
    are reversed, which is what makes the finding mean something. A reversed
    byte order is direct evidence of which architecture the authoring tool ran
    on, and it is better evidence than a timestamp because a clock can be set
    and a byte order cannot be faked by accident (open item 24).

    `tools/iffle.py` in `cd32-gunship2000-doc`. Watch the tolerance: allow the
    walk to end one byte short, because an archive may append a terminator (on
    Gunship, `0xFF`, 45 times out of 45).

36. **Read a hunk file's relocation table before deciding it is a program.** A
    file beginning `00 00 03 F3` is an AmigaDOS executable to every census, and
    it may be nothing of the sort. [Gunship 2000]'s `cd32rez` is 641,768 bytes
    with **one CODE hunk and exactly fifteen relocations, all fifteen pointing
    at the first sixty bytes**, which are a fifteen-entry pointer table
    terminated by `FFFFFFFF`. The other 641,596 bytes are 526 concatenated RNC
    streams. It is a resource archive that does no fixup of its own: it declares
    its group pointers as relocations and lets `LoadSeg` patch them while
    loading.

    The signal is the ratio. A real program of that size has thousands of
    relocations (`gs2.run`: 6,595 in 197 KB). Fifteen in 641 KB, all in the
    first sixty bytes, means the hunk header is a wrapper. `tools/relocs.py
    FILE --list 0` prints them; if they all land in a short prefix, read that
    prefix as a table and check whether the first entry points at the byte after
    the table ends. On `cd32rez` it does, exactly.

    This is the mirror of step 25's other use. Step 25 says a constant *not*
    covered by a relocation is a literal; this says a file whose relocations are
    *only* a prefix is data with an executable's hat on.

37. **Read the root directory record's own date and compare it with the
    earliest file, with the sign.** Step 3 of this list already says to compare
    the **PVD** date against the file dates, and [Gunship 2000] made that pay by
    turning up the set's only inversion. [Superfrog] shows the PVD is not the
    only date worth that treatment: its PVD is a normal 25m22s **newer** than the
    newest file, and its **root directory record is 1994-08-17 16:41:45, seven
    days and nineteen hours OLDER than the earliest of the 242 files it
    indexes** — stored identically in the PVD's copy of the record, in the
    extent's own `.` entry and in its `..` entry, while all 21 subdirectories
    are dated with the files.

    **THE SECOND POINT EXISTS NOW, AND IT IS THE NORMAL CASE.** [Myth]'s root
    directory record reads 1992-12-21 16:59:24: **one second older than the
    newest of the five files it indexes** and 1h46m46s newer than the oldest,
    stored identically in the same three places, with its one subdirectory dated
    with its file. Its PVD is a normal +11m33s.

    Both discs were cut with **ISOCD 1.04**, so the one thing the baseline
    settles immediately is that **[Superfrog]'s seven-day-old root record is not
    a tool artefact** — the same tool version writes a contemporaneous record on
    the other disc. What it cannot yet separate is a reused staging directory
    from a hand-set date. Two points; report the third with the sign, and
    **report it especially when it is normal**, because that is how this closes.
    (Sections 1 and 3.)

38. **Check every file length against the capacities of removable media before
    running any scan.** [Myth] has five files, and three of them are **901,120
    bytes each — 80 tracks x 2 sides x 11 sectors x 512 bytes, one
    double-density Amiga floppy disk, exactly.** The CD32 release is the 1992
    three-floppy release pressed whole, bootblocks and unused blocks included,
    with an 18 KB shim that emulates a floppy drive out of CD sectors.

    The lengths worth recognising on sight: **901,120** (Amiga DD), **1,802,240**
    (Amiga HD), **368,640** and **737,280** (PC 5.25-inch), **1,474,560** (PC
    1.44 MB), and any exact multiple of them. When one turns up, the disc is one
    level deeper than it looks and four things change at once:

    * **the census is inside the image, not in the ISO.** [Myth]'s asset
      directory is a table of `(offset, length)` longwords in **block 2** of each
      floppy image, which is exactly where a trackloader's bootblock reads it
      from. 28 chunks across three images, none of them a file.
    * **the bootblock is a document.** Its checksum tells you whether Kickstart
      would boot the disk (all three of Myth's validate; one declares `DOS\0`
      and two declare type zero), and its text tells you who wrote it — Myth's
      say `(c) 1992 System 3 arcade software ltd` and `(c) 1991 Dave Colclough`,
      which is where the game's real year and its programmer come from.
    * **the unused blocks are evidence.** 6.36 % of Myth's on-disc bytes are
      outside every chunk-table entry and only 2 % of that is zero: a `SYS3` fill
      pattern, 8-bit PCM, and **a complete copy of Commodore's `ConClip 37.7`**
      with its `$VER:` string, which is the only `$VER:` on the whole disc. That
      is what was on the physical media before the game was written to it.
    * **the floppy-origin rule stops being an inference.** Section 5's rule is
      normally read off disk-swap prompts, volume names or device paths; here the
      floppies *are* the payload, and the rule is at [12 of 12].

    **[Alfred Chicken] is the first UNDETERMINED case, and it stays at
    [12 of 12] rather than becoming 13.** The disc compresses — seven RNC
    ProPack streams as files, four more inside the executable — but **it points
    at no floppy ancestor at all**: zero `DF0:`–`DF3:`, zero `CD0:`, no
    disk-change prompt, no installer, no `.bak`, and no file of a removable-media
    length. What it does name is three volumes that belong to the machine it was
    *built* on: `JJSDISK:` (tested for and branched around in the shipped boot
    script), `alf2:` (in a format string), and `Hard0:` (in an RCS keyword).

    That is a memory of a **development** machine, not of a shipping medium, and
    the honest reading is that the antecedent holds and the consequent is not
    checkable from the disc. Counting it as a thirteenth confirmation would be
    incrementing rather than measuring. **The rule needs a case like this
    written down, because it is the shape a real counterexample would have.**

    Cheap, and it happens before anything else: sort the file lengths and look
    for a round medium. (Sections 1, 5.)

39. **Date the master against the copyright year in the block it carries, not
    only against its own timestamps.** The CD32-era `.TM` block reads
    `Copyright (c) 1993 - Commodore Electronics Ltd.`, and [Prey CD32] ships the
    same bytes as a dated file, `/CD32.TM`, 1993-06-10. So **any CD32-era volume
    whose PVD predates mid-1993 and which carries that block is lying about its
    date**, and a `grep` for `Commodore Electronics` settles it.

    [Myth] is where this first paid, and it is the hard case: the PVD says
    1992-12-21 and the game genuinely is from 1992, so the date looked
    defensible until the banner was read. The same argument applies unchanged to
    [Banshee] and [Marvin], the two other discs stamped 1992-12-21.

    The general form is worth more than the instance: **a disc carries dated
    third-party material, and third-party material cannot be older than the
    volume that holds it.** Version strings in shipped Commodore commands,
    `$VER:` dates, library versions and trademark banners are all upper bounds
    on how old a master can be, and they are independent of whatever clock the
    build machine had. (Sections 1, 2, 3.)

40. **If the disc is physical, read it twice by two different paths and compare
    them — and make every sector prove its own identity.** [Alfred Chicken] is
    the first disc in this set read from plastic rather than from an image file,
    and neither obvious path could read all of it.

    `ReadFile` on `\\.\E:` returns the *logical volume*, so it stops at the
    declared volume size — 227 sectors short of the end of this disc's data
    track — and it was the only path on this drive that could read LBA 0..15.
    Raw `IOCTL_CDROM_RAW_READ` transfers with TrackMode `CDDA` reach every
    sector, but that mode returns the bytes **as they physically sit on the
    disc**, which on a data track means **scrambled** (ECMA-130 annex B: the
    12-byte sync in the clear, everything from byte 12 XORed with a 15-bit LFSR
    whose first output bytes are `01 80 00 60`). Descrambling is a dozen lines
    and it gives back the real sector: header, 2,048 bytes of user data, EDC and
    ECC.

    Three things follow, and all three are free once the descrambling is done:

    * **the sector mode can be verified instead of assumed.** Every `.cue` in
      this set says `MODE1/2048` and no disc had ever been checked. The
      descrambled header's fourth byte is the mode; on this disc it reads 1 on
      all 902 sectors read that way, not sampled;
    * **every sector proves its own address.** The MODE1 header contains its own
      MSF. On this drive, two consecutive dumps of the same 918 sectors returned
      two *different* wrong answers — sixteen all-zero sectors at LBA 0..15 in
      one run, LBA 0..4 carrying the headers of LBA 241..245 in the next. The
      drive returns stale or misplaced data on the first transfer after a seek.
      **A dumper that writes 2,048 bytes per sector without looking cannot see
      this at all.** Check sync, header address and EDC on every sector and
      re-read the failures; after that the read was stable with zero retries and
      zero errors;
    * **the two paths can be cross-checked where they overlap.** Here that was
      LBA 16..690, 675 sectors, and they agreed byte for byte — a guarantee no
      image in this set had before. Refuse to write the image if they disagree.

    Also read, once, and none of it available from a file: the TOC
    (`IOCTL_CDROM_READ_TOC_EX`), the **MCN** and the per-track **ISRC**
    (`IOCTL_CDROM_READ_Q_CHANNEL`, formats `0x02` and `0x03`), pre-emphasis and
    channel-count bits from CONTROL, and the real pregaps. And **measure the
    drive's read offset** by searching for the sync pattern rather than
    hardcoding it — on this drive it is −24 bytes, six samples, and it is a
    property of the drive, not of the disc. Say so, so that nothing downstream
    mistakes it for one. (Sections 1, 10.)

41. **Does the trailing 32/232 run and the image overrun ever get confused,
    and has an earlier disc's overrun been mis-read?** [James Pond 2] has a
    trailing unclaimed run of **32** inside its declared volume *and* an image
    overrun of **150**, and the prediction written for it aimed at the wrong
    one of the two. They are separate quantities: the trailing run takes two
    values across nineteen discs (32 and 232, correlating with the preparer
    field) and the overrun has taken thirteen (0, 80, 86, 87, 103, 106, 150,
    152, 152, 152, 180, 225, 227). **Say which one you mean, every time.**

    And that disc raises a question about the overrun that an image cannot
    answer: **its 150-sector overrun is numerically identical to the
    `PREGAP 00:02:00` its cue declares on track 02.** Either the master pads
    the data run up to the pregap (which is what [Alfred Chicken] proved from
    the plastic) and the burner generates the pregap from the directive, or the
    ripper wrote the pregap into the tail of track 1 *and* declared it, in
    which case a disc burnt from that cue is 150 sectors too long. At least one
    earlier image in the set also has a 150-sector overrun and its track-2
    pregap was never checked against it. **On any disc read from plastic, check
    the overrun against the next track's pregap explicitly** — it costs one
    subchannel read and it would close this for the whole set.

42. **How many discs ship `lowlevel.library` and `nonvolatile.library`, and are
    they the same builds?** Every OS-friendly CD32 title has to ship both, and
    they are Commodore's, so a hash table across the set would be the cheapest
    cross-disc fingerprint available — the same trick that found `SetPatch` 39.6
    circulating between Marvin and [Legends] and `freeanim` between Liberation
    and [Gloom]. [James Pond 2] carries `lowlevel.library` at **6,944** bytes
    and [Alfred Chicken] at **6,920**, with different SHA-1s, which is two
    points and a difference. The pipelines do not commit their extracted trees,
    so nobody can do this from the repositories as they stand. **Re-extract
    `libs/` and `c/` from every image and hash them once**; it produces a column
    for the whole set rather than a fact about one disc.

## Contributing from a pipeline

When a new title turns up something about the *format* rather than the title:

1. Add it to the relevant section here rather than to the title's repository,
   and link to it from the title's README.
2. Mark it **[all]** or **[2 of N]** only if you have actually checked the
   other discs. Otherwise name the disc it came from.
3. If it contradicts what is written here, **correct the text and say so in
   place** — the history is more useful attached than removed.
4. Update the baseline table in section 10 and the order of work in section 11.
5. Answer the open items below, or say that you checked and it did not apply.

State what is measured and what is inferred, and keep the measurements in the
document. **And when a control disc contradicts something here, correct it in
place and mark the correction** — two of the entries above are corrections and
they are more useful than the claims they replace.

## Open across the format

Marked **ANSWERED** where a disc has settled it; the answer stays here with
the disc that gave it.

1. **ANSWERED, twice over — where does the object file after the trademark
   banner come from?** All three discs have **all three SHA-1s identical**,
   across fourteen months, three studios and three engines. And Prey settles
   the mechanism: it ships **`/CD32.TM`**, an ordinary 2,048-byte file in the
   root dated 1993-06-10, referenced by nothing, whose SHA-1 is the trademark
   sector's. Commodore distributed the block to developers **as a file**, and
   that file already contained the `exec` object code with its debug symbols.
   The stale-buffer accident happened once, at Commodore.

   Also answered: **it is not always at sector 21.** Prey's is at 6021, the
   PVD says so, and the `20` this section used to read as the path-table LBA
   is a constant. Corrected in place.

   **ANSWERED, and it is the mismatch this entry was waiting for — do the
   bytes ever differ?** Yes. **Speris, a CD32 disc mastered in 1996 with
   ISOCD 1.04, carries 22,152 bytes of `cdtv.device` 35.2** — SHA-1
   `fd3e764e6393974dea05612909e25ddb2124eb8b`, byte for byte the `/CDTV.TM`
   of the 1992 CDTV master of Prey, three and a half years and one console
   away. No Commodore banner anywhere on it.

   So the block is **not console-determined**, as this document previously
   concluded. It is whatever `.TM` file the person cutting the master fed to
   the tool, and ISOCD copies it without looking. The three matching CD32
   hashes describe how widely one file circulated, not a property of the
   format. Corrected in place in section 2.

   **What replaces it: how often does this happen?** One CD32 disc with the
   CDTV block makes it possible; a second would make it a habit. Hash the
   block on every disc — the four known values are in section 2 and the check
   takes thirty seconds.

2. **ANSWERED — is the duplicated PVD a habit of ISOCD?** No: it is the one
   habit that crosses tools. The CDTV Prey master was written by something
   that is **not** ISOCD — space-padded strings, empty preparer field, real
   separate optional path tables, a modification date, upper-case 8.3 names,
   path tables placed *after* the files — and it still writes the primary
   volume descriptor twice at 16 and 17 with the terminator at 18. Everything
   else this document attributed to ISOCD really is ISOCD's, and now has a
   negative control.

   **What replaces it: which tool wrote the CDTV master?** It signs nothing.
   The preparer field is 128 spaces. Identifying it, or finding a second disc
   with the same habits, is the next useful thing. (Section 1.)

3. **ANSWERED by Commodore's own documentation — what is
   `freeanim.library`?** The *Amiga CD32 Developer Notes* (19 May 1993) put
   it in chapter 3: it is the CD32 ROM library that controls the **boot
   animation**. `OpenLibrary` tells the animation to begin shutting down and
   returns immediately; `CloseLibrary` waits for it to finish; the gap between
   them is where the title is supposed to initialise. **There is no function
   call because there is no function** — the pair *is* the interface, which is
   why four discs show six opens and zero calls. The notes also tell
   developers not to error-check it (so it works on a plain Amiga with a
   CD-ROM, where the library is absent) and to open it before touching the
   display, which is why it is always opened first. Recorded in full in
   section 4.

   **What replaces it:** `c/rmtm` on CDTV — same job, same position in the
   boot script, still not disassembled — and whether `freeanim.library` ever
   grew the `audio.device` behaviour the notes warned it might.

   *(Superseded: the entry below is what this looked like from the discs
   alone.)* Seven sightings across four discs and it is on none of them, so it is resident
   in Kickstart or the CD32 extended ROM. It is opened and never called, every
   time, always at the moment the program claims the machine. New from Prey:
   its `ReadArgs` template is **`/auto/close/wait`**, in `c/freeanim` and in
   `cdgsxl` 1.48's own data hunk — so the interface has at least the notions
   AUTO, CLOSE and WAIT. Opening it *is* the operation, which fits a library
   whose open releases the memory held by the CD32 boot animation. Still
   unconfirmed and still absent from the usual documentation. (Section 4.)

4. **ANSWERED for now — how common is a first stage that makes zero library
   calls?** Not common; it is one of two extremes. Dragonstone: 0 library
   calls, AmigaDOS dead, ISO 9660 parsed by hand, Akiko driven directly.
   Marvin: **169 library calls, 39 LVOs, ten libraries, three devices**, and
   the operating system alive underneath the whole game. Speris sits in
   between and closer to Marvin: **72 library calls in 1.6 MB**, five
   libraries, AmigaDOS used for file access and the hardware driven directly
   for everything else — and one of its four programs, `speris-logos`, makes
   **zero**. Three discs, and the useful reading is that the count varies by
   two orders of magnitude. Count the `4E AE` before assuming anything. Dragonstone's hand-written ISO parser is still worth documenting
   here **if a third disc has one too**. (Section 4.)

5. **ANSWERED for one disc, and the test was fixed along the way — do other
   CD32 titles actually use AGA?** **Prey's CD32 release does.** Eight
   bitplanes on ten IFF screens, 256 colours, impossible on ECS — and the CDTV
   release of the same game is the control at five planes and 32 colours.

   The colour-depth half of the test **was wrong** and the CDTV disc caught
   it: it looked only for nibble-doubling (`v * 17`), while that disc writes
   4-bit values as `v << 4`, so every one of its ECS palettes scored as
   24-bit. Corrected in section 7; accept both conventions. Re-run, 6 of 14
   CD32 screens carry values needing more than four bits per gun and all six
   CDTV screens carry none.

   Dragonstone writes `FMODE = 0` and Marvin's palettes contain no value above
   `0x0FFF`, so **AGA used as a deeper ECS** remains the common case.
   **[Liberation] is the fourth data point and the most extreme**: it makes no
   AGA call at all — `LoadRGB4` four times, `LoadRGB32` never — and writes no
   display register of any kind, because it runs inside an Intuition screen. On
   this format an Amiga game with a CD32 sticker is the norm, not the exception.

   **And no disc yet uses Akiko in the game — six CD32 discs now, and the best
   remaining candidate said no.** [Liberation] is a 1994 first-person polygon
   engine by two experienced Amiga programmers with 169 MB to spend, and it has
   **zero** pointer loads of `$00B80000`, zero references to the C2P port and
   zero `$C0DE0000` across all twenty-five of its hunk files. It also explains
   itself twice over: the two CD32-only libraries are opened behind a single
   runtime flag and neither open is fatal, and the renderer is a Blitter
   program drawing pre-rendered planar sprites, so there was no chunky buffer
   for a C2P pass to convert. **The question stays open, but the shape of the
   answer is now visible: as long as the same binary has to run on an A1200,
   Akiko is a second display path nobody could afford.** The disc that settles
   it, if one exists, will be a CD32-exclusive title. (Sections 4 and 7.)

   **THE PREDICTION WAS TESTED AND IT FAILED. [Microcosm] is the
   CD32-exclusive title, and it does not use Akiko either.** It has no floppy
   ancestor and no A1200 path at all: it displays **eight bitplanes** (a
   `BPLCON0` value that does not exist below AGA), writes `FMODE`, `BPLCON3`
   with `LOCT` and `BPLCON4`, and opens `nonvolatile.library` and
   `lowlevel.library` unconditionally with `beq` straight to a fatal error —
   none of Liberation's single guard flag, no fallback, nothing that could run
   on a stock Amiga. It is exactly the disc this entry was waiting for.

   Measured: **zero occurrences of `$00B80038` in every executable byte on the
   disc** — 254 KB of executable plus seventeen overlays, 9.5 MB in total — and
   zero for `AKIKO`/`akiko` as strings. The twelve hits for the bare pattern
   `00 B8 00 00` are all the same two words of one shared data table repeated
   across six overlays, which is precisely the false positive this document
   warns about; the 489 hits for `00 B8 00 38` across the whole 523 MB image are
   all inside the 483 MB of compressed video, where every four-byte sequence
   occurs by chance.

   **And this disc gives the mechanism rather than only the count, which is
   what makes it worth more than a seventh negative.** Its video decoder
   (`DECRUNCH/DECRUNCHER.S`) writes **planar bitplanes directly**: ten unrolled
   `move.l (a3)+,(a0)+` per row, a 40-byte row stride, and `adda.w #$1680` —
   5,760 = 40 x 144, exactly one bitplane — at the end of each plane. The video
   on the disc is *stored* planar. There is no chunky pixel anywhere in the
   playback path for Akiko to convert; feeding it through the C2P port would
   mean converting planar to chunky in order to convert it back.

   **So the reasoning about FMV titles inverts.** A decoded-video game looked
   like the best remaining Akiko candidate because a decoder emits chunky by
   nature — but an encoder can be made to emit planar offline, once per frame,
   on a workstation, and a 1994 studio with SGI machines obviously did. A game
   that **rasterises at run time** cannot do that. Seven CD32 discs, seven
   negatives, and the candidate set that remains is CD32-exclusive titles with a
   *real-time* renderer. (Sections 4 and 7.)

   **THE REAL-TIME RENDERER TURNED UP AND IT IS ALSO A NEGATIVE — AND IT CHANGES
   THE QUESTION.** [Gloom] (1995) is a texture-mapped first-person shooter whose
   **textures, sprites and HUD are all 8-bit chunky**: 65 x 64 chunky texture
   records, chunky sprite frames with 0 as transparent, chunky HUD pixels
   compiled into the executable. It rasterises every frame at run time. It is
   the disc this entry was asking for on the "is there chunky data" axis, and
   Akiko is **zero**: no `$00B80038`, no `$00B80000` pointer load, no
   `$C0DE0000`, in the raw image, in all 131 extracted files and in all 115
   decrunched files, and no `akiko` string. Its 45 bare `00 B8 00 xx` hits
   include eight consecutive entries of one descending 16-bit table.

   **The mechanism is new and it is what makes this worth more than a ninth
   negative.** Gloom's 3D view is **displayed as a copper list with one `MOVE`
   per pixel** (section 7). The bitplanes hold a fixed descending ramp of colour
   indices; the copper reloads the colour registers for every rendered row, with
   `BPLCON4`'s `BPLAM` and the `BPLCON3` bank alternating so each row reads out
   of one half of AGA's 256 registers while the other half is being filled. The
   value the renderer writes is therefore **a 12-bit `$0RGB` colour, not a pixel
   index** — picked out of one of sixteen pre-shaded copies of the level palette.

   So the useful question is no longer "does the title rasterise in chunky?" —
   Gloom does nothing else — but **"does the frame ever have to become
   bitplanes?"** A chunky-to-planar converter is only worth anything when there
   is a planar destination, and this title arranged not to have one. **Nine CD32
   discs, nine negatives**, and the four reasons are now: planar assets and a
   planar display (four discs), a Blitter renderer over pre-rendered planar
   sprites (Liberation), video encoded planar offline (Microcosm), and **a
   framebuffer that is a copper list** (Gloom). The candidate that remains is
   narrower than before: a CD32-exclusive title that rasterises in chunky *and*
   displays through bitplanes. (Sections 4 and 7.)

   **TENTH DISC, TENTH NEGATIVE, AND IT IS THE PLAINEST ONE YET.**
   [HeroQuest II] (1994) is not a candidate on any axis, and it is worth a
   paragraph for exactly that reason: a Blitter-driven isometric board game
   whose every asset is planar and whose destination is a planar bitmap never
   has a chunky pixel to convert. Measured to zero — no `$00B80038`, no
   `$00B80000` pointer load, no `$C0DE0000`, in the 52.5 MB image, in all 97
   files and in all 111 decrunched blocks.

   It also gives **the clean AGA negative this document has had only once
   before**: no `BPLCON3`, `BPLCON4`, `FMODE` or `DIWHIGH` anywhere on the disc;
   `LoadRGB4` and `LoadRGB32` both never called, because `graphics.library` is
   opened and never called *at all*; five bitplanes, six in Extra-Half-Brite
   with `KILLEHB` clear; and a start-up routine that blanks exactly 32 colour
   registers. **Two discs of ten now use no AGA feature whatever**, and both are
   floppy ports — so "AGA used as a deeper ECS" has an "AGA not used at all"
   tail, and it is worth checking for before reaching for a palette file.

   **ELEVENTH DISC, ELEVENTH NEGATIVE — AND IT IS THE ONE THIS ENTRY HAD BEEN
   ASKING FOR.** The candidate this entry narrowed to after Gloom was "a
   CD32-exclusive title that rasterises in chunky *and* displays through
   bitplanes". [Guardian] (1994) is the first half of that exactly: **CD32-first**
   (its floppy SKU exists but the CD32 master is the earlier artefact this
   document can date), no floppy loader inherited, nothing on the disc
   compressed, and a **genuine real-time triangle rasteriser** — the first in the
   set. It displays through bitplanes: 320 x 200 at four interleaved planes under
   a six-plane HUD panel.

   Measured to zero: no `$00B80038`, no `$00B80000` pointer load in either
   opcode form, no `$C0DE0000`, no `akiko` string, in the 2.75 MB image and in
   all 61 files. The 31 bare `00 B8 00` hits inside the executable are all in the
   data hunk, all the same four bytes `00 b8 00 78`, and there are **zero in
   152 KB of code**.

   **And the second half of the candidate is where the prediction broke: it does
   not rasterise in chunky.** It never rasterises in *anything* — there is no
   intermediate representation of the frame at all. The renderer computes each
   polygon scanline's span, looks its ends up in a 43,520-byte table to get
   `BLTAFWM`/`BLTALWM`, and issues **one Blitter cookie-cut** (`BLTCON0 = $07CA`,
   `BLTADAT = $FFFF`, minterm `D = (A AND B) OR (NOT A AND C)`) with `BLTSIZE`'s
   height set to **4** so the operation covers all four interleaved planes of that
   row in one go. There is no chunky buffer, no `bset`/`bclr` plotter, and **no
   `BLTCON1` write anywhere in the program**.

   So the candidate set narrows again and it is now very small: **a CD32 title
   that computes pixel values in a linear buffer and then has to get them into
   bitplanes.** Five discs now answer "where does the frame end up?" and none of
   the five leaves a chunky-to-planar step anywhere for the hardware to do:
   planar assets into a planar display (four discs), a Blitter over pre-rendered
   planar sprites (Liberation), video encoded planar offline (Microcosm), a
   framebuffer that is a copper list (Gloom), and **a Blitter cookie-cut straight
   into planar memory (Guardian)**.

   The honest summary after eleven discs, with the best candidate in the set now
   spent: **no commercial CD32 title examined here uses the console's headline
   feature, and the reason is not that the programmers could not — it is that the
   Amiga's own Blitter already writes to the format the display reads.** Akiko
   converts chunky to planar; a 1994 Amiga programmer with a polygon engine had no
   reason to be holding chunky in the first place, because the Blitter has been
   the way you fill planar spans since 1985. Chunky is what you get from a *port*
   or from a *texture mapper*, and the one texture mapper here (Gloom) arranged
   its display so that it never needed bitplanes either. (Sections 4 and 7.)

   And it settles a small standing nuisance. The `00 B8 00` false positive that
   Gloom shows as a descending 16-bit table is **ProTracker's chromatic period
   table** — 36 entries from 826 down to 109 at 2^(−1/12) a step, `$00B8` = 184
   as entry 33 — and the same four words appear on both discs. Any Amiga program
   with a tracker replay carries it. (Sections 4 and 7.)

6. **ANSWERED, and the answer is "floppy game plus a soundtrack" — what
   fraction of a CD32 disc does a CD32 game actually use, and on what?**
   Dragonstone: 3.2 % of a 74-minute disc, no CD audio worth the name.
   Marvin: 60.7 %, of which 458 MB is Red Book audio and **38.8 % of the data
   track is the publisher's logo animation**. Prey: 18.0 %, **no Red Book at
   all**, of which 68.6 % is speech stored as data files and 11.5 % is the
   intro animation. Speris: 0.74 %, no audio track. **Legends: 89.4 %, of
   which the game is 0.72 % and the music is 88.6 %.**

   Legends settles it by taking the pattern to its limit: the same amount of
   *game* as Speris, and 65 minutes 36 seconds of Red Book audio over the top,
   filling the disc to the edge. Five discs, and four of the five are a floppy
   game with whatever audio the budget allowed; Prey is still the only one that
   is not.

   **ANSWERED, and the answer is no — but not for the reason expected.**
   [Liberation] has the largest data track on the format by a factor of 1.4:
   **82,502 sectors, 24.8 % of a CD, with the audio only 46.5 %**, which
   inverts the ratio every other disc here shows. Then measure what is *in*
   the data track: **91.2 % of it is digitised speech**, 7.1 % is one family of
   wall sprites, and **everything else — every executable, every library, all
   40 geometry files, both fonts, every text file and every sound bank — is
   2.9 MB.** That is between Dragonstone (2.7 MB) and Speris (4.5 MB).

   So the pattern generalises further than it looked. Across eight discs, the
   *game* is always between 2.7 MB and 13.3 MB, and what varies by two orders
   of magnitude is what got poured on top: Red Book audio on four discs, and
   digitised speech stored as files on the other two, Prey and Liberation.
   **No CD32 title in this set spends the disc on the game.** The remaining
   question is whether one exists at all, and it will not be found by looking
   at data-track size.

   **ANSWERED — one exists, and the pattern survives being answered.**
   [Microcosm] spends **92.27 % of its data track, and 86.4 % of the whole
   disc, on one 483 MB file** that is neither music nor speech: it is 30,707
   frames of video in 261 movies, and it is what the player spends the game
   looking at and steering through. Red Book is 6.4 % of the disc and is never
   played (section 8). That is the first title here where the thing filling the
   disc is the title's own primary content.

   **And yet the 2.7–13.3 MB band holds for an eighth disc.** Strip `cbmbuild`
   and everything else on the volume — the executable, all 32 overlays, the boot
   script — is **9,563,231 bytes**, which lands between Marvin (13.3 MB) and
   Speris (4.5 MB). Eight discs, eight games, all of them between 2.7 MB and
   13.3 MB of code and data, across four years and seven studios. That is now
   the most robust number in this document and it survived the disc that was
   supposed to break it.

   **AND IT SURVIVED THE OPPOSITE TEST TOO.** [Gloom]'s data track is **772
   declared sectors, 0.232 % of a CD** — a third of Speris' record and the
   smallest volume on the format. 1,315,110 bytes on the disc is well below the
   band and would have broken it from underneath. **It does not, because 115 of
   its 131 files are packed at 30 %**: the game unpacks to **3,855,390 bytes =
   3.86 MB**, between Liberation (2.9) and Legends (4.4). Nine discs, nine
   games, four years, eight studios. **Measure the decompressed size** — that is
   the whole difference between the band holding and the band breaking here.

   **AND A TENTH DISC LANDS INSIDE IT WITH THE SAME CORRECTION.**
   [HeroQuest II] is 2.16 MB on the disc and **4.09 MB unpacked** — below the
   band compressed, inside it decompressed, between Gloom and Legends. Its
   occupancy is 50.5 % of a CD, of which 42.8 % is Red Book and 7.6 % is a data
   track that is itself **95.4 % zero**. A fourth kind of thing poured on top,
   then: not audio, not speech, not video, but **nothing at all** — 49.7 MB of
   deliberate emptiness in front of the files (section 1).

   **AND THE ELEVENTH BREAKS THE FLOOR WITH NOTHING TO CORRECT.** [Guardian] is
   **2.25 MB, uncompressed**, and 41.8 % of a CD — 0.40 % game, 41.3 % Red Book.
   There is no packed file to unpack, so unlike Gloom and HeroQuest II the number
   does not come back inside the band. The floor moves to 2.25 MB; the ceiling
   (13.3, Marvin) has not moved in eleven discs, which is the half of the finding
   worth keeping.

   So the finding sharpens rather than dissolving. **The band measures the
   Amiga, not the medium**: 2 MB of chip RAM and a 68EC020 bound how much
   resident code and data a title can have, whatever is on the disc beside it.
   What the occupancy column measures is what got poured on top, and there are
   now three kinds — Red Book audio (four discs), digitised speech as files
   (two), and **streamed video** (one). Ask which of the three a new disc is
   before you read anything into its size.

7. **New — is `MODE1/2048` universal?** All nine discs so far, including a
   1992 CDTV master, a disc with no audio track, a disc with twenty-eight, a
   169 MB one, a **499 MB one** and a **1.6 MB one**. Mode 2 Form 1 is supposed to occur on this
   format; nobody has produced one here yet. Note that [Microcosm] streams 483 MB
   through `CD_READXL` off a plain `MODE1/2048` track, so needing Mode 2 for
   streaming is not a reason to expect it.

8. **New — how many CD32 discs carry a second, Workbench entry point?**
   Marvin ships `<Game>.info` with `DefaultTool = IconX`, `c/IconX`, and a
   sibling AmigaDOS script, so the same disc boots on a console and
   double-clicks on an A1200 desktop. Dragonstone does not. Prey does not
   either — it has `c/IconX`, because it has the whole of Workbench's `C:`,
   but no `.info` at the root and no sibling script. **[Legends] does, in a
   third form**: `/Disk.info` and `/InstallHD.info` are Workbench icons, and
   the root holds a `StartUp-Sequence` and an `AssignInfo` that assign to
   `Work:Legends` — a hard-disk path — beside a complete A1200 hard-disk
   installer the CD32 can never run. **[Liberation] does too, in a fourth
   form**: `/The Game.info` with `DefaultTool = SYS:c/iconx` and a 169-byte
   sibling script that assigns `captiveII:` to the *current directory* rather
   than to `cd0:`. It is a live, correct entry point — and its `DefaultTool`
   points at the **system** `IconX`, which this disc does not ship, so it works
   only where a Workbench already exists. Three of six, and all three are
   different. When a CD32 disc has `.info` files, **read the `DefaultTool`
   path**: it says whether the entry point was meant for the console or for
   the hard-disk user.
   Note that Prey still ships `lowlevel.library` and `nonvolatile.library`,
   which are the A1200 compatibility libraries, and opens the first and not
   the second. **[Microcosm] is the negative case in its purest form**: no
   `.info` anywhere, no `c/`, no `libs/`, one directory holding one five-byte
   file, and both CD32 libraries opened from ROM with no fallback. Three of
   seven now have a second entry point, and the disc that has none is the only
   CD32-exclusive title in the set — which is the correlation you would
   expect and the first evidence for it.

   **[Gloom] is a fifth form and it strengthens the correlation.** `/Gloom.info`
   is a plain Workbench **tool** icon on the game executable — no
   `DefaultTool`, no sibling script, nothing else needed — so the disc
   double-clicks on an A1200 desktop. Beside it are `/Gloom->HD` (the floppy
   release's hard-disk installer, which says `Please insert disk `) and
   `/Gloom->HD.info`. **Four of nine discs now have a second entry point, and
   all four are titles with another SKU.** Read `do_Type` as well as
   `DefaultTool`: a `WBTOOL` icon on the game itself is the cheapest possible
   form of the pattern and has no strings in it to grep for.

   **AND THE CONVERSE IS NOW DEAD.** [HeroQuest II] has another SKU — three
   floppies, named in its boot script and in all 91 of its loader's paths — and
   **no `.info` file anywhere**, no `libs/` and no `devs/`. It is the second
   counterexample after Dragonstone. So "a disc with an icon has another SKU"
   survives at 4 of 4, and "a title with a floppy SKU ships a desktop entry
   point" is **4 of 7** and is not a rule. (Sections 1 and 4.)

   **AND THE FORWARD DIRECTION NEEDS A DISTINCTION, BECAUSE AN ICON NEED NOT BE
   AN ENTRY POINT.** [Guardian] has an `.info` — `/s/startup-sequence.info`, 396
   bytes — and it is **not** a second entry point: it is a `WBPROJECT` icon on the
   *boot script* whose `DefaultTool` is `blitz2:blitz2`, so double-clicking it on
   an A1200 desktop hands the script to Blitz Basic. The disc has another SKU (an
   A1200 floppy release), so the correlation is not broken; but the icon is
   evidence of the **development tool**, not of a desktop entry point, and
   counting it as one would have been wrong.

   So the check has three outcomes, not two: **no `.info`; an `.info` that runs
   the game (`WBTOOL` on the executable, or `WBPROJECT` + `IconX` on a script);
   and an `.info` that runs a development tool.** Read `do_Type` *and* the
   `DefaultTool` path, and if the tool is not `IconX` or the game, you have found
   a build-chain fingerprint rather than an entry point — which on a disc with no
   credits screen may be the only one there is.

9. **New, and now four for four — how much of the *development* survives on
   a typical disc?** The CDTV Prey master carries **`c/WACK`, Commodore's
   low-level debugger** — breakpoints, single-step, disassembly, serial
   console — and `c/BOOKIT` from the *CDTV Survival Kit*, which states in its
   own banner that it may not be freely distributed, on a pressed retail disc.
   The same studio's next master carried Commodore's factory hard-disk
   formatter instead. Two masters, two different pieces of Commodore's
   internal tooling, neither swept. Prey carries: two files the executables still name and
   that are not on the disc, one of them a CDXL for the publisher's logo that
   was replaced by a still image eleven minutes before the master; seven
   consecutive sprite banks and one door animation missing from the middle of
   their numbered series; `XLFIRST.old`, superseded a month earlier and
   pressed anyway; the intro animation shipped under the name `Test`; four
   development tools that nothing runs, including Commodore's factory hard-disk
   formatter and a rival CDXL player from the mastering house; uncleared
   converter buffers in every animation file; the videotape timecode still
   burnt into the digitised actors; and `/CD32.TM`. Marvin
   carries: the floppy release's complete disk map as plain text inside the
   CD32 executable; a per-level author, comment and source-path trailer in
   all 64 level files; uncleared editor buffers in every one of them; three
   working levels and a test music file that are in no index; a development
   tool in `c/` that nothing runs; and an easter-egg directory containing a
   working demo, 550 lines of its 68020 source, and a signed note inviting
   whoever finds it to read them. Dragonstone carries a cut level's blank
   slot and a floppy prompt. **[Legends] carries the A1200 release's complete
   hard-disk installer** — script, ASCII-art dialogs, the `4.7 MB` figure and
   a `Format DRIVE DF0:` — plus the two boot files it installs, a version
   string reading `Version 0.99` in all five level executables, eighteen
   `SIGN MESSAGE n` placeholders and fifteen `XXXXXXXXXXXXXXXXXXXXX` records
   in the shipped text, `trackdisk.device` and `arp.library` on a disc with no
   floppy, a `QWERTYUIOP` keyboard table, `EMPTY PAL` slots in every level's
   palette table, eight IFF samples with their tracker's `ANNO` chunk intact,
   photographs of the development team, and a sixth floppy volume that nothing
   claims. **[Liberation] carries**: the previous title of the game in every
   path on the disc and in a boot-script comment that uses both names in one
   sentence; a **384-word note to translators** with the author's direct phone
   number, for a translation that never shipped, next to 23 accented glyphs in
   both fonts that nothing prints; **both authors' surnames inside the
   random-citizen name table**, beside Sagan, Cherryh, Gaiman, Gibson and four
   of the six Pythons; a **demo build's refusal** (`[Sorry, this is only a 1
   disk demo.]`) compiled into the retail binary as a dialogue record; three
   test 3D objects written in the same second and named by nothing
   (`FatAnt.x3d`); three pre-split geometry files, one byte-identical to its
   replacement; a `freeanim` one-liner in `c/` that nothing runs; a
   commented-out command in the boot script with a note explaining why; the
   four floppy volume names and the save-disk volume of the A1200 release; a
   floppy-path fallback compiled into a generator; every developer comment in
   three source text files; three filenames the code still opens that are not
   on the disc; and 30 KB of one animation stored twice in the same archive.
   **[Microcosm] carries**: a retail volume identifier of **`CDTV_TEST`** with
   every other free-text descriptor field empty; the 483 MB video file named
   **`cbmbuild`**, after the Commodore build it was made for, on a disc whose
   credits thank `COMMODORE` and `SILICON GRAPHICS`; **`/filelist.i` and
   `/filelist.s`, eleven bytes each, each containing its own filename**, the
   stubs of the generator that produced the 3,444-line `CDCODE/FILELIST.S`
   table that is 56.6 % of all the code in the program; the whole **debug
   console** — printer, number formatter, its own one-bitplane copper list and a
   console task — linked into the release build, with that copper list installed
   at start-up and the string `internal hardware error` inlined **195 times**
   across the executable and the overlays as the only error message the product
   has; **two assets named in the loader's file table and marked absent with a
   presence flag the loader honours** (`cd0:briefing.*` and `cd0:eolb4.*`),
   with `LEVELS/EOLBDIE4.S`, `EOLBTWEEN4.S` and `EOLBKILLYOU4.S` still linked in
   and holding real code; **77 assembler source file names** in the debug hunks;
   a hidden cheat page threatening to *"suck the colour from the nice
   graphics"*; four sound effects whose IFF `ANNO` chunks name **AudioMaster IV**
   and an *"Audio Engineer"*; tracker modules under the composer's working names
   (`cossi1.6`, `doooohhh`, `yyyy`, `graymm`); level names from someone's map
   notes (`X JUNCTION1`, `QUESTIONABLE STRAIGHT`, `JUMP RESTART`); and five
   typos in the shipped mission text including the same pressure suit called
   `S2-21` on one screen and `SS-21` on another.

   **[Gloom] carries**: the floppy release's whole **hard-disk installer**
   (`Gloom Harddrive Installer`, `Please insert disk `, `gloomprog:`,
   `gloomdata:`) as a root file the CD32 can never usefully run; **two floppy
   prompts compiled into the CD32 executable** (`please insert gloom data disk`
   and `please write enable the gloom data disk!` — a CD is never
   write-enabled); `s/startup-sequence.bak`, the previous release's boot script;
   `/gloomgame`, 32 bytes of `gamegamegame…` that no string on the disc names,
   which is the floppy release's save file; a **demo build's refusal**
   (`sorry...not available in demo`) in the retail binary, the second disc here
   to do that after Liberation; **ten debug colour flashes** — `COLOR00` set to
   a distinctive colour and a 65,536-iteration `dbra` — of which one is
   `AllocMem`'s entire failure path, after which the code writes through a null
   pointer; `CHAT MODE ENABLED`; a twelve-character obscenity in the music
   player's data segment; **224 `FFFF` palette slots per texture bank**, 5.4 KB
   of them; and a **missing zone number** — the maps and textures are numbered
   1, 3 and 4 with no 2 anywhere, while the deathmatch arenas are numbered 1, 2
   and 3 with no gap.

   **[HeroQuest II] carries**: a retail **title screen that still calls the game
   `MASTERS`** while every string on the disc calls it *Legacy of Sorasil*, and
   which is also the only place the Hasbro / Games Workshop licence appears at
   all; the publisher's logo screen **twice**, the copy in the wrong directory
   and named by nothing being the same picture **with the copyright line
   deleted** (220 bytes different out of 40,000, all in plane 0, rows 192–199);
   `Level.Map`, a tenth dungeon map named at the end of the loader's file table
   and absent from the disc; `Please insert Legacy of Sorasil Patch`, a floppy
   prompt untranslated in all three languages, naming a **fourth volume** that
   nothing assigns; a complete `Lock`/`Examine`/`UnLock` **disk-swap wait loop
   with no `bsr`, `jsr`, `jmp` or longword reference to it anywhere**; the whole
   **ending of the game untranslated** in the German and French builds
   (eighteen consecutive strings, byte-identical to the English); nine
   placeholders including `76543210`; an empty container slot, three more
   pointing at end-of-file, and a map-cell byte that is zero in all nine
   dungeons; **three Red Book tracks nothing can play**; `BLUEBITS` and
   `GREENBITS` symbols with no code behind them; a save that **stores 24 bytes
   and reads 238 back**; and the string **`FrogAndParrot`** — a pub on Division
   Street in Sheffield, five minutes from Gremlin's offices — held in a register
   across the call that loads the saved position.

   **[Guardian] carries** far less than any of them, and is the new answer to
   this entry's inverted question. It has no `c/`, no `libs/`, no `devs/` and no
   `l/`, so there is no swept-in Workbench, no unused command and no piece of
   Commodore tooling; no hard-disk installer, no floppy prompt, no demo refusal,
   no debug console, no symbol table and no source file names. What it does carry
   is: **`PIRATES FUCK OFF`**, a NUL-terminated string immediately after the
   copyright notice at the very top of the code hunk, referenced by nothing; a
   **live buffer-overrun canary** — the longword `$68456c50`, ASCII `hElP`,
   written at the last longword of seven chip allocations and **verified at run
   time by seven `cmpi.l` sites**, the first *working* debug facility this
   document has found in a retail build rather than a dead one; **`WAS `** and
   **`GON `**, four printable bytes each, sitting immediately in front of the two
   strings the save code does address and addressed by nothing themselves; a
   **twelfth zone's complete asset set** (`split12`, `spr12` — the largest sprite
   bank on the disc — `sprhead12`, `map12`) plus `map00`, `map99`, `dither00` and
   `dither98`, **179,796 bytes, 8.0 % of the volume**, against a zone table with
   eleven records; and **`dither99.iff`**, the artist's Deluxe Paint working file
   for the dither sheet with its `GRAB` hot-spot and six `CRNG` colour-cycling
   ranges intact, pressed beside the stripped binary the game actually reads. Its
   sixteen `CMAP` entries are the binary's sixteen colours, nibble for nibble.

   **No disc yet examined on this format was swept**, across 1992 to
   1996 and ten studios. At this point the finding is the rule, not the
   exception, and the useful question has inverted: **is there a CD32 disc
   that *was* cleaned up, and what does one look like?** Eleven discs, eleven
   answers, and the closest thing to a clean one is now [Guardian] — which is also
   the disc with the least identifying information of any in the set: empty
   preparer, no credits screen, no `$VER:`, and **no person named anywhere on it**
   except a hand-lettered signature ending in `94` drawn across a planet on the
   title screen.

   Which suggests the next refinement of the question. The discs that carry the
   most are the ones with a **`c/` and a `libs/`** — a directory somebody
   populated by copying — and the two that carry least (Gloom, Guardian) have
   neither. **"Was this disc swept?" may be the wrong question; "did anybody ever
   copy a directory onto it?" may be the right one.**

10. **New — how often does a CD32 title carry its engine as separate shared
    libraries, and how often does it run other programs?** [Liberation] does
    both: `libs/` holds three in-house libraries (`vector` the Blitter
    renderer, `tridee` the geometry, `math` a 512-entry sine table, an integer
    square root and a perspective divide that retries on `divs.w` overflow),
    all three signed `(C) Wyvern 1992` with their own version numbers, and the
    game launches `CityGen`, `PlotGen` and `BuildingGen` as separate
    executables — with **byte-identical backup copies of all four that the
    loader names as fallbacks**. Marvin ships one in-house library
    (`color_fx.library`) and runs one unused tool; nothing else here does
    either. **Read `libs/` for anything that is not one of Commodore's five
    modules, and grep the executable for its own directory names**: an engine
    with its own `$VER:` is an engine you can date independently of the game,
    and here it dates to a year before the console.

11. **New — how many CD32 titles put state somewhere that survives a reset,
    and where?** [Liberation] is the only disc here that mounts a device from
    its boot script: `ramdrive.device` as `RRD:`, from a `Devs/Mountlist` on
    the disc, made bootable with a one-line startup sequence and relabelled
    `Ram_Reset`, so a warm reset boots a warning program instead of the game.
    It *also* opens `nonvolatile.library` and calls all four of its vectors
    once each, *also* names `RAM:Game.DAT`, and *also* carries the floppy
    release's `Lib-Saves` volume name. Four mechanisms on one disc, and which
    one holds the actual save is unresolved because the warning program's text
    is behind the decruncher above. Across the nine discs the save systems are
    a password (Dragonstone, Legends), a password plus `nonvolatile` (Marvin),
    `nonvolatile` plus floppy save-disk code (Speris), none at all (both Preys),
    **`nonvolatile` alone and unguarded** ([Microcosm]), **`nonvolatile` alone
    with the base null-checked at every use** ([Gloom]) and this. Gloom's is the
    variant to expect on a disc that also ships on floppy: the open is
    unguarded, but every call site starts `move.l <base>,d0 / beq`, so the game
    runs with its save system silently absent.
    **And check the lengths against each other.** Gloom stores its record with
    `moveq #2,d0` into `StoreNV` and then copies **five longwords** out of what
    `GetCopyNV` returns, which under Commodore's documented register conventions
    is a two-byte store and a twenty-byte read. Worth checking on any other disc
    that uses the library.
    **Check `Devs/` before assuming there is nothing there: it is one
    directory and most discs do not have one.**

12. **New — how do CD32 titles that stream actually stream, and does anyone
    else use `CD_READXL`?** [Microcosm] is the first disc here to use the
    console's own XL mode for anything: `CD_CONFIG` sets both the read speed and
    the XL read speed to **150 sectors per second** and then `CD_INFO` reads them
    back and **refuses to run unless the drive reports 150 in both fields**;
    `CD_READXL` then DMAs a 483 MB stream into a ring of buffers with
    `CDCODE/CDXLINT.S` chaining the next buffer at every block boundary. Beside
    it, two smaller idioms worth looking for on any streaming disc: a
    **`TD_ADDCHANGEINT`** door-open interrupt, and a **`CD_READ` issued with
    `io_Length = 1` and immediately `AbortIO`'d**, which is a head seek built out
    of a read.

    Marvin and Prey both ship third-party CDXL players (`cdgsxl`) and neither
    game calls `CD_READXL` itself. So the count is one of nine — and on [Gloom]
    the drive is not opened at all — and the open
    question is whether that is because streaming was rare or because the
    third-party players hid it. **Histogram the `io_Command` immediates on every
    disc** (`3?7c 00nn 001c`); it is one grep and it settles what a title asks
    the drive to do.

    **And there is an arithmetic reason CDXL turns up only for logos and
    intros, worth doing before concluding anything about a studio's taste:
    CDXL is uncompressed.** A frame costs `width/8 * height * planes` whatever
    is in it, so the format's ceiling is fixed by geometry alone —
    320 x 144 at 8 planes is 46,080 bytes, which is **6.67 fps** at the 307,200
    bytes/s a 2x drive delivers, and 30,707 frames of it would be **1,349 MB**.
    That is why the two CDXL streams in this set are short and small
    (Prey CD32: 619 frames at 240 x 96 x 7; Marvin: one publisher logo) and why
    [Microcosm] wrote its own container instead: at 15,699 bytes/frame measured
    it fits 30,707 frames of the same geometry in 460 MB.

    **Compute the CDXL cost of a title's footage before asking why it did not
    use CDXL.** Two multiplications, and on a feature-length stream the answer
    is usually that it would not have fitted on the disc at all. (Sections 4,
    7 and 8.)

13. **New — what does a title's own container look like when it is not a file
    system?** [Microcosm] puts 261 movies and 30,707 frames in one file with no
    directory: each frame carries a **look-ahead table of the next eleven frame
    sizes**, a stream id, a chunk count, a frame index that restarts at each
    movie, and **three checksums that all sum to the ASCII constant `'COSM'`**.
    The only index anywhere is a 3,444-line generated table compiled into the
    executable giving 48-byte records of `{offset, length, buffer sizes}` per
    2 MB segment.

    That shape — no directory, a per-record look-ahead, and integrity constants
    the runtime enforces — is what a 2x drive and 2 MB of chip RAM push you
    towards, and it is the opposite of the "one file per asset" layout on the
    other seven discs (1,439 files on Prey, 1,453 on Prey CDTV). **When a disc
    has very few files, expect the structure to have moved inside one of
    them**, and look for the index in the executable rather than on the disc.
    Whether any other CD32 title does this is unknown; nothing else here has
    fewer than 47 files.

    [Microcosm]'s is the minimal case and worth recording as the floor: app
    name **`MCOSM`**, item name **`core`**, a ten-byte record allocated
    `MEMF_CLEAR` if it does not exist, whose **first word is read out, kept in
    the globals, incremented and written straight back on every single
    launch** — a run counter in the console's NVRAM. All three failure branches
    print `internal hardware error` and stop. The library is opened with
    version 0 and `beq` to a fatal error, with none of Liberation's guard flag:
    on a CD32-exclusive title the compatibility hedging simply is not there, and
    **the presence or absence of that guard is a cheap test for whether a disc
    ever expected to run on an A1200**.

14. **New — is mastering practice a publisher habit or a studio one?**
    [Legends] (Krisalis Software / Guildhall, 1996) and [Gloom] (Black Magic
    Software / Guildhall, 1995) are the first two discs here with the same
    **publisher**, a year apart. If any of this were a publisher-level habit
    they should look alike. They agree on **nothing**: preparer field named
    versus empty, application identifier set versus empty, timestamps impossible
    versus real, 28 audio tracks versus none, Bytekiller versus CrunchMania,
    `SetPatch` 39.6 versus 40.3, a `c/` directory versus none, passwords versus
    `nonvolatile.library`, eight planes versus seven, and different `Disk.info`
    bytes. The one habit they share — shipping the other SKU's hard-disk
    installer — is a decision about what was in the build directory.

    Meanwhile the files that *are* shared cross publishers instead: Gloom's
    `freeanim` is Mindscape's, and Legends' `SetPatch` is 21st Century's. **On
    this format the unit of shared practice is the developer's tool shelf, not
    the label on the box.**

    **ANSWERED, AND THE TOOL-SHELF ANSWER NEEDED CORRECTING TOO.** [Banshee] is
    the second same-label pair — Core Design, three months from Dragonstone —
    and it is the better control of the two because both discs are documented to
    the same depth and the predictions were written before the measurements.
    Eight matches, nine mismatches, and **which** ones matched is the result:

    | | Dragonstone | Banshee | |
    |---|---|---|---|
    | Preparer | `Sajjad Majid` | `D J Pocock` | ✗ |
    | `c/SetPatch` | 40.14, 13,200 B | byte-identical | ✓ |
    | `.TM` block | the common 2,048 B | byte-identical | ✓ |
    | Cruncher | RNC ProPack 1 | RNC ProPack 1, and Dragonstone's decoder ran 37/37 first try | ✓ |
    | Fixed-size buffers | 90.9 % used | 96.1 % used | ✓ |
    | Library calls in the loader | **0** | **71, 33 LVOs** | ✗ |
    | ISO 9660 parsing | by hand | `dos.library` | ✗ |
    | Overlay header | `DNLD` | absent | ✗ |
    | File-table format | fixed-width names + index table | variable-length records | ✗ |
    | Text encoding | CP437 | CP437 (for two of four languages) | ✓ |
    | Text control codes | `FF FE FC FD` | `FF FE` | ✗ |
    | Akiko `$B80000` | **drives the drive** | **zero** | ✗ |
    | Akiko C2P port | zero | zero | ✓ |

    Every match is attributable to something **wider** than the label:
    Commodore's developer distribution (the `.TM` block), the AmigaOS release on
    the build machine (the `SetPatch` version — and the table in section 4 shows
    three of the four multi-disc version groups pair *unrelated* studios, so
    that match carries no label information at all), and the Amiga commercial
    tool market (RNC ProPack). Every mismatch is a component somebody wrote.

    So the tool-shelf answer stands but has to be stated more narrowly: **the
    shelf is the Amiga scene's, not a studio's and not a label's**, and nothing
    in this comparison is evidence of a shared build kit.

    **And the one cross-disc regularity it did turn up is a unit nobody had
    proposed: the person who ran the mastering tool.** Banshee's preparer field
    is character for character [Liberation]'s — a different studio and a
    different publisher — and those two discs are the only ones in twelve that
    leave a **232**-sector trailing zero run instead of 32, in volumes of 1,687
    and 82,502 sectors. Two variables, two discs, perfect correlation, no third
    disc yet. It is falsifiable for the price of one field comparison, and it is
    the first time any layout anomaly here has lined up with a named individual.
    (Sections 1, 4, 7, 9 and 10.)

    **AND THE THIRD POINT HOLDS IT.** [Universe] is Core Design, 1994, the
    first time this question has had three discs from one label instead of two.
    The prediction, written first, was that the matches would again be exactly
    the things attributable to something wider than the label. They are:

    | | Dragonstone | Banshee | Universe | |
    |---|---|---|---|---|
    | Preparer | `Sajjad Majid` | `D J Pocock` | `D J Pocock` | 2 of 3, and the pair crosses labels |

    **AND THE SIXTEENTH DISC SUPPLIES THE MECHANISM, WHICH MEANS THE QUESTION
    HAD THE WRONG SHAPE.** [Superfrog] and [The Speris Legacy] are the two Team
    17 discs — different studios, two years apart, different genres — and two
    predictions were written before either was measured, deliberately pointing
    opposite ways. Both landed:

    * **The cruncher follows the label.** Both discs use the **Imploder**, and
      the decruncher transcribed from Speris's own shipped 68000 routine decodes
      all 96 of Superfrog's files **unmodified**, in-place pointer landing on
      zero every time. So "the cruncher follows the label" now spans **two
      labels**, and one of them has cross-studio evidence rather than being one
      studio three times.
    * **The `.TM` block follows the tool.** Superfrog's is byte-identical to the
      twelve ISOCD discs and **not** to Speris's 22,152 bytes of `cdtv.device` —
      same label, different block.

    Same disc, same label, opposite answers, both predicted. And the disc says
    *why*: its preparer field names **Kenny Grant** and `s/T17Menu`'s `$VER:`
    names **`Kenny G`** as the author of that menu, while none of the six game
    programs carries a `$VER:` or a build banner at all. **The person who cut the
    master and the people who wrote the game are demonstrably different hands, on
    one disc, from two fields.**

    So the question "studio, label or neither" presumes a single owner and there
    is not one. **Different artefacts have different owners, and the owner is
    readable per artefact:**

    | artefact | owner | evidence |
    |---|---|---|
    | cruncher | **the label** | two Team 17 discs, two studios, two years, one packer; five other studios, five other crunchers. **[Myth] adds a label with no prior**, using one packer — its own programmer's — so it is consistent and cannot separate label from studio, because System 3 is both |
    | `.TM` block | **the mastering tool** | **sixteen discs, twelve labels, identical bytes** |
    | preparer field, trailing run | **the operator, or a bureau** | `Pocock` 232 on 5 of 5; everyone else 32 on **14 of 14**. **[Myth]'s field names a company with a phone and fax number, and [Alfred Chicken]'s names a second one, `Abersoft`** — so "operator" needs widening to include a contractor, and two contractors in nineteen discs is no longer a single anomaly. **[Alfred Chicken] is also the first same-publisher test of the correlation and it survives**: Mindscape's other disc, [Liberation], *is* Pocock with 232, and this one is Abersoft with 32 — so the field follows the work, not the label. **And [James Pond 2] closes the "who is it?" half of the question**: preparer `Dean Ashton`, trailing run 32, and the man is on the disc in the first person — a signed, dated comment in the boot script — *and* is the game's own conversion programmer by both credit screens. So the box holds a fifth kind of owner, **the studio's own programmer**, and it says nothing about role: it says who was at the keyboard |
    | colour depth, save system, music format | **the studio** | Speris and Superfrog disagree on all three; **[Myth] makes it three discs agreeing on none of them** — 5/4-plane ECS output, no save system at all, OctaMED |

    **What to do on the next same-label pair:** stop asking which single owner
    build practice has, and instead assign each artefact to the step that
    produced it — the game build or the mastering run — before comparing. And
    look for a disc that names the operator *and* the authors, because that is
    what turns the assignment from an inference into a measurement.

    **[Myth] separates the steps by timestamp, which no earlier disc could.**
    Its three floppy images and its boot script were written in one 2m53s burst;
    the CD-specific loader was written **alone, 1h44m34s later**; the master was
    cut 11m33s after that. So the build artefacts (Bytekiller, the `DAVE`
    container, the chunk tables, the trackloader), the conversion artefacts (the
    Akiko driver, the forced protection key, a one-byte patch to a memory probe)
    and the mastering artefacts (the ISO volume, the preparer field, the `.TM`
    block, the 50 MiB hole, the 32-sector run) are separated *by the disc's own
    dates* rather than by inference. **Sort the directory by timestamp and look
    for a record that stands alone: that is where the conversion is.**
    | `c/SetPatch` | 40.14, 13,200 B | identical | **identical** | matches, and Fire & Ice on another label has it too |
    | `.TM` block | the common 2,048 B | identical | **identical** | matches, sixteen discs have it |
    | Cruncher | RNC ProPack 1 | RNC ProPack 1 | **RNC ProPack 1** | matches, three for three |
    | Akiko `$B80000` | **drives the drive** | zero | **drives the drive** | 2 of 3 |
    | Akiko C2P | zero | zero | zero | matches, every disc |
    | Colour depth | 12-bit | **8 bits per gun, AGA** | **12-bit, EHB, `FMODE = 0`** | differs |
    | Text encoding | CP437 | CP437 + a private Danish set | **CP437, clean** | matches, three for three |
    | Save system | password | **none at all** | **EEPROM over hand-written I2C** | differs |
    | Executable format | AmigaDOS hunk + `DNLD` overlays | AmigaDOS hunk | **a private relocatable format** | differs |
    | Library calls after boot | 0 | 71 | **0** | 2 of 3 |

    So the answer from this item **survives its third point**: every match is
    the `.TM` block, the Kickstart on the build machine, the commercial tool
    market or the code page, and every mismatch is a component somebody wrote.
    The one match not yet explained away as wider than the label is the
    **cruncher** — three for three inside Core Design, against five different
    crunchers across the other studios. That is the only same-label regularity
    left standing and it is worth one more Core disc.

    A footnote on the premise, because it changes how much the result is worth:
    Banshee's disc says its two makers worked in **Danish** — a fourth language,
    a `8/7-94` build banner, the hero renamed `Svend` — and its credits thank
    "the rest at Core" as a third party. So it is a same-*label* control with an
    external team, not a same-studio one. That does not weaken the finding; it
    sharpens the question it answers, which is whether a build kit travels with
    a publishing deal. It does not.

15. **Still open, and now two negatives down — why do three discs leave a large
    zero gap in front of their files, and does it mean anything?**
    [Banshee] is the second disc to stream Red Book while the game runs and have
    **no front gap at all** (first file at LBA 24), after [Guardian]. The
    seek-optimisation reading has two negatives against it and nothing for it.

    The three discs that have the gap: [Prey CD32] 6,000 sectors between the
    descriptor terminator and its path tables, 10.0 % of the image.
    [Microcosm] 15,000 sectors between its root directory and its first file,
    5.87 % of the volume. **[HeroQuest II] 24,272 sectors — 49.7 MB, 95.42 % of
    a 25,436-sector volume** — between its root directory at 22 and its first
    file at 24,295, with all 97 files and seven directory extents fitting in the
    1,109 sectors that follow.

    All three are zero, so there is nothing to read. Two candidate readings have
    turned up and neither is settled. Microcosm's 15,000 sectors is exactly 200
    seconds of CD frames against a 203.0-second audio track. HeroQuest II's
    layout puts every file the game loads within about 1,100 sectors of the
    audio tracks, on a title that plays Red Book *while* loading, on a console
    with one head — which would make the gap a seek optimisation, but nothing in
    the executable says so.

    **AND THE FIRST TEST OF THE SECOND READING CAME BACK NEGATIVE.** [Guardian]
    plays Red Book *while the game runs* — twelve tracks, read straight out of the
    disc's own table of contents, on a console with one head — and has **no front
    gap at all**: first file at LBA 23, whole volume in 1,138 sectors. If the gap
    were a seek optimisation for Red-Book-during-play, this is the disc that most
    needed one. Three discs still have the gap, none is explained, and one
    candidate mechanism is now one negative down.

    **What to do on the next disc:** report every unclaimed run with its LBA
    range, not just the largest or the trailing one; and if there is a front
    gap, check whether the title streams Red Book during play and where its
    files sit relative to track 2. (Section 1.)

16. **New — is `ISOCD 1.03` distinguishable from `1.04` in any way at all?**
    Nine masters here say 1.04. [HeroQuest II], June 1994, says **1.03** — two
    months *after* Liberation's 1.04 — so the versions overlapped and the
    number is not a date.

    Every habit section 1 attributes to 1.04 is present in 1.03: duplicate PVD
    at 16 and 17 with the terminator at 18, optional path-table pointers filled
    with the mandatory ones, NUL padding on every string field, NUL
    modification/expiry/effective dates, mixed-case file names, path tables
    before the files, an image longer than the declared volume, and a 32-sector
    trailing run of zeros. **Nothing observable separates them.**

    The one thing that disc does differently is the front gap in item 15, and
    whether that is the tool or the operator is exactly what a second 1.03 disc
    would settle. **Record the version string on every disc**; it costs nothing
    and it is currently a variable with one sighting. (Section 1.)

17. **New — when a title ships on CD *and* floppy, which came first, and can a
    disc say?** [Guardian] is the first title here where the CD32 release looks
    like the *earlier* artefact, and the disc gets some of the way and then stops.

    What it gives: a master cut **1994-08-04**, a live boot script running `game`,
    and beside it `s/startup-sequence.bak` — the previous script, pressed —
    running a program called **`sw`**, which is the name of the executable on that
    title's A1200 floppy release. So a build called `sw` existed before the CD32
    master and had already been renamed by it.

    What it does not give: any date for the floppy SKU. The executable carries
    **no `$VER:` at all** — the first in this set with a real DATA hunk and no
    version string — its own directory record is at the MS-DOS epoch, and the only
    floppy images available are a cracked release whose dates are the cracker's,
    with the data disk in a `GARD` trackloader format that has no filesystem and
    therefore no timestamps.

    **What to do on the next such disc:** grep the executable for `$VER:` first,
    because on Liberation one string settled a two-year discrepancy; then look for
    a `.bak` beside the boot script; then diff the media (step 27). Two of the
    three worked here and the one that would have settled it is the one that was
    absent. (Sections 3, 4 and 10.)

18. **New — what is the 1980 epoch actually telling you?** This document has
    listed MS-DOS day zero as "the file came through a PC filesystem" since
    Marvin. [Guardian] shows it behaves exactly like the AmigaDOS 1978 epoch:
    **the day number is uptime.** Its one outlier is `1980-01-09 23:17:58` — day
    9, roughly nine days of uptime on a machine keeping PC time with an unset
    clock — against 60 files and six directories stamped inside one seven-second
    window on a machine whose clock was right.

    Two discs, two files each on one and one file on the other, so the reading is
    not yet firm. But it changes what the epoch is evidence *of*: not "this file
    was copied through DOS at some point" but "this file came off a machine whose
    clock had never been set, and that machine was keeping PC time" — which is a
    statement about a *second build machine*, and on Guardian that machine built
    the program while a different one held every asset. **Sort the 1980 dates and
    read the day numbers as a log, exactly as you would for 1978.** (Section 3.)

19. **New — is `1992-12-21` a sixth epoch?** Two unrelated discs carry it, in
    overlapping quarter-hours of the same afternoon, from different halves of
    the disc:

    ```
    [Banshee]  41 file records            1992-12-21 15:11:46 .. 15:27:34
    [Marvin]   PVD                        1992-12-21 15:15:40
    [Marvin]   all nine directory records 1992-12-21 15:24:31 .. 15:26:43
    ```

    On Banshee it comes from the *source* file system and on Marvin from the
    *mastering* machine, and the two studios and publishers are unrelated. A
    dead battery on an Amiga gives 1978, not this.

    The shape that fits is a machine with **no battery-backed clock**, where
    AmigaDOS restores the date from the boot volume at every boot and the time
    runs forward from there — so every session starts at one fixed date and the
    time of day is a function of uptime alone, exactly as the 1978 and 1980
    epochs behave. That would make this a **non-zero stored base**, a sixth
    epoch, and it predicts other discs carrying other fixed dates with plausible
    times of day.

    Neither repository can test it. **Record the time of day whenever a wrong
    date turns up, not just the date, and check it against this pair.**
    (Section 3.)

    **First negative: [Fire & Ice] (2026 pipeline).** Twenty-nine files, ten of
    them on a wrong clock, and `1992-12-21` appears nowhere — no file record, no
    directory record, no PVD, at any time of day. The ten wrong ones are at the
    **MS-DOS FAT epoch** (1980-01-05, 1980-01-08 x7, 1980-03-09) rather than at a
    restored non-zero base, which is a different shape and does not bear on this
    item either way. Still open; one negative out of thirteen.

    **And that disc adds a sub-question of its own.** Its 1980 group spans
    sixty-four days. Read as uptime on one machine that is a two-month
    uninterrupted session; read as three sessions from a fixed base of
    1980-01-01 the uptimes are 4, 7 and 68 days. Neither shape is comfortable,
    and the FAT epoch is now the **second-most common wrong clock** on the format
    after 1978. Guardian had one such file; Fire & Ice has ten, which is the
    first sample big enough to look at. **On the next disc, count the 1980 files
    separately from the 1978 ones and record their spread, not just their
    presence.**

20. **FIVE FOR FIVE, ACROSS TWO COUNTRIES, AND THE ONE FILE-LEVEL LEAD IS DEAD —
    the 232-sector trailing run is a person.**

    **[Gunship 2000] is the fifth.** MicroProse, 1994, preparer `D J Pocock`,
    **232 sectors**, predicted in writing before the filesystem was parsed. The
    group is now Liberation (82,502 sectors declared), Banshee (1,687),
    Fire & Ice (1,270), Universe (2,429) and Gunship 2000 (80,735) — a **65 : 1**
    span inside the group, five studios, five publishers, and now **two
    countries**, because Gunship is the first non-British label here. Ten discs
    at 32 under nine other names.

    **AND THE UNIVERSE LEAD IS REFUTED, TWICE.** Universe's contribution to this
    item was a *file-level* one: `C/FreeAnim` (3,492 B, `449c6100…`) and
    `C/noopenwb` (204 B, `e0538ef1…`) are byte-identical on Universe and
    Liberation, which were then the only two Pocock masters with a `c/`, and the
    reading was a build kit travelling between studios. Both halves fail:

    * **[Dragonstone] carries the identical pair**, and Dragonstone's preparer is
      `Sajjad Majid`. **[Gloom] carries the same `FreeAnim`** — 3,492 bytes,
      SHA-1 `449c610071ace58d…`, in its root as `/freeanim` rather than in a
      `c/` — and Gloom's preparer name is **empty**. So that binary is on four
      discs under **three different preparer values**, and it never separated
      the group at all.
    * **Gunship 2000, the fifth Pocock master, has a `c/` with eleven files and
      neither of those two is in it.** What its `c/` shares with the group is
      stock Commodore material — `Assign` 3,220 B (also Liberation, Banshee),
      `execute` 4,432 B (also Banshee), `SetPatch` 13,200 B (five discs including
      a non-Pocock one).

    So the correlation is back to being **purely field-level, with no mechanism
    attached**, and stronger than ever as a correlation. Everything previously
    excluded stays excluded and Gunship re-excludes it: volume size, ISOCD
    version (1.04 on all fifteen), audio track count (the group now spans 2–23,
    the rest 0–28), studio, publisher, field padding, duplicate PVD, `.TM` block,
    record order, `;1` suffixes, root extent. Image overrun is 78 on Gunship,
    which **widens** the Pocock range to 78–103 and leaves Dragonstone's 106
    outside it — still not a clean separation, exactly as Universe found.

    **What would settle it:** a sixth Pocock master, or a 232 under a different
    name. The latter kills it outright. (Sections 1, 4, 7, 9 and 10.)

    The original entry, kept because the reasoning is still the reasoning:

20a. **PROMOTED TO A FINDING, AND STILL UNEXPLAINED — the 232-sector trailing
    run is a person.** Ten discs at 32 across a 331 : 1 span of volume sizes;
    **three at 232, and those three are the only ones whose preparer field reads
    `D J Pocock`** ([Liberation], 82,502 sectors; [Banshee], 1,687;
    **[Fire & Ice], 1,270**). Three studios, three publishers, one name, and a
    65 : 1 range of volume sizes inside the group. The third was **predicted in
    writing before the volume was parsed** and came in exactly as predicted, so
    the correlation now has predictive value.

    What is still open is the mechanism. Nothing else separates the three from
    the ten: same `ISOCD 1.04 by Pantaray` signature, same NUL padding, same
    duplicate PVD, same trademark block; image overruns of 87 and 86 against 150
    and 227 on discs that leave 32. 232 − 32 = 200 sectors = 409,600 bytes and
    nothing on any of the three is that size. **A fourth `Pocock` disc is worth
    less than it looks — what would move this is anything else the three share
    and the ten do not.** (Sections 1 and 10.)

    **FOUR FOR FOUR, AND THE FOURTH WAS MEASURED FOR THE MECHANISM RATHER THAN
    FOR THE NUMBER.** [Universe], Core Design 1994, declares 2,429 sectors and
    leaves **232, all zero, at LBA 2,197-2,428** - 9.6 % of its volume, again
    predicted in writing first. Ten discs at 32, four at 232, and the four are
    the four `D J Pocock` masters.

    Newly ruled out on that disc, and all of them cheap: **image overrun**
    (80 sectors, so the group reads 103/86/87/80 - but Dragonstone's 106 falls
    inside that range, so there is no clean separation); **directory record
    order** (strict ISO 9660 ASCII); **`;1` version suffixes** (present,
    ordinary); **root directory extent** (4,096 bytes); **audio track count**
    (23, and the group now spans 2 to 23 while the non-Pocock discs span 0 to
    28).

    **And one positive lead, which is a file rather than a field.** Universe's
    `C/FreeAnim` and `C/noopenwb` are **byte-identical to Liberation's,
    timestamps to the second included** - and those two are the only Pocock
    masters with a `c/` directory at all. Two unrelated studios, one operator,
    the same two utility binaries out of the same directory. It does not cover
    Banshee or Fire & Ice, which ship neither file, so it does not explain the
    232; but it is the first artefact of any kind that links two Pocock discs
    and no other disc in the set, and it moves the question from "what does the
    tool do differently" towards "what was in the directory the tool was
    pointed at". **On the fifth `Pocock` master, hash `c/` before parsing
    anything.**

21. **New — how often is a whole program pressed and never reached?** [Banshee]
    presses `picture.exe`, 274,764 bytes and **9.5 % of its data track**, which
    the boot script does not run, the game does not name, the loader's 37-entry
    file table does not list, and whose name does not appear anywhere else in
    the volume. Inside it is the largest image on the disc.

    This document has plenty of *files* nothing reads and several *commands*
    nothing runs; a complete second executable with its own display code, its
    own packer and its own picture is a different scale of leftover. **Diff the
    executables against everything that could launch one** — the boot script,
    the `.info` `DefaultTool`s, and every path string in the game — and count
    what is left. (Sections 4, 6 and 7.)

22. **Does the empty directory mean anything?** [Banshee] ships `/icons`,
    2,048 bytes, containing nothing, on a disc with **no `.info` file of any
    kind** and therefore no Workbench entry point. ISOCD wrote its record 27
    seconds before `/C`'s, so it existed in the source tree. Open item 8 counts
    the discs with a second Workbench entry point; this is the first with the
    *shape* of one and none of the content. (Sections 1 and 4.)

    **Second and third instances, and they are different in kind.**
    [Fire & Ice] ships **two** empty directories, `/Initial` and `/Misc`,
    written seven seconds apart and twenty minutes after the other five, i.e.
    **the last two things made in that session**. That disc does have a
    Workbench entry point, so these are not orphaned icon directories; they are
    two names somebody created and never filled, three weeks before the master
    was cut. Two discs of thirteen, three directories, and the pattern so far is
    that the empty one is always among the *last* records written. **Record the
    creation order of directories, not just their emptiness.**

23. **New — how far apart are two builds of the same program, and what does the
    difference cost?** [Fire & Ice] presses **two whole executables**, `FirePAL`
    and `FireNTSC`, 410,184 and 409,820 bytes, timestamped **2 minutes 8 seconds
    apart**. They are one program built twice: identical hunk structure,
    identical relocation counts, code hunks agreeing for 154 bytes and then
    diverging because every absolute address has shifted by 364. The entire
    behavioural difference is **23 scanlines of copper list** (240 `WAIT`s
    against 217, the same 193-line play area, a 47- against 24-line panel below
    it) and one string in the options panel. 400 KB of a disc that had 232 spare
    sectors and a third of a CD unused, so nothing was being economised.

    No other disc here ships a PAL/NTSC pair, and none branches at run time
    either. **Check for a second executable whose name differs only by a video
    standard, and if there is one, diff it on content rather than on bytes** —
    a byte diff of two hunk files whose code lengths differ tells you nothing.
    (Sections 6 and 7.)

24. **New — is the MS-DOS 1980 epoch a mastering-chain fingerprint?**
    [Guardian] carried one file at `1980-01-09 23:17:58`; [Fire & Ice] carries
    **ten**, spread over 1980-01-05, 1980-01-08 (seven files inside 8 hours,
    four of them inside 3m08s) and 1980-03-09. Both discs were cut with ISOCD,
    which is a DOS program, so the obvious reading is a PC staging tree with an
    unset clock — but two discs is not a pattern and the sixty-four-day spread
    on Fire & Ice fits neither "one long uptime" nor "three sessions from a
    fixed base" comfortably.

    This matters because it is the epoch most likely to be misread as an
    inherited build date. Fire & Ice is the first disc here where inheritance
    was **genuinely plausible before the check** — it is a 1992 floppy game — and
    the disc still refuted it, because 1980 predates the Amiga and because a
    CD32-only tool sits inside the 1980 group. **Count the 1980 files separately,
    record their spread, and check whether anything in the group could not
    predate the CD32.** (Section 3.)

    **THE BEST AVAILABLE TEST WAS RUN AND CAME BACK EMPTY — AND HANDED OVER A
    BETTER PROBE.** The hypothesis needs a publisher whose main platform is DOS.
    [Gunship 2000] is MicroProse, the most DOS-first label in this set, and it
    has **zero 1980 files and zero 1978 files**: 148 dated records over 24
    calendar days, 1993-12-20 to 1994-04-19, every one of them coherent. The
    prediction, written before the sort, was that it would have *more* than
    Fire & Ice's ten. It has none.

    But the same disc proves the DOS side of the pipeline a different way, and
    the evidence is in the data rather than in the directory. Gunship's pictures
    are **76 correct big-endian IFF**, and its own form types — `SCRN`, `SCNR`,
    `WRLD`, `SHIN`, `SHIP`, `THTR`, `WSYS` — are **41 files that store every
    chunk size little-endian**, so a standard reader sees a 3.4 GB FORM inside a
    3 KB file. Read Intel-order the chunk walk lands exactly on the last byte, on
    all 41. And `logo.pix` is a **`PBM `** form with a `TINY` chunk — PC
    DeluxePaint's chunky format — the only chunky picture on the disc.

    **So: byte order beats timestamps as a probe for a DOS-side pipeline.** A
    clock can be set; a byte order cannot be faked by accident. Added to the
    order of work as step 35. Whether Guardian's and Fire & Ice's 1980 files are
    accompanied by little-endian data is untested and costs one run of
    `iffle.py`.

25. **A NEGATIVE FROM THE GENRE MOST LIKELY TO GIVE A POSITIVE — how common is a
    script interpreter, and what does its opcode space look like?**

    **[Gunship 2000] says no, and it is a good no.** A mission-based simulator
    with campaigns, objectives, briefings and an endgame was the second-best
    candidate after a point-and-click, and the prediction written before the scan
    said a dispatch table would be there. `dispatch.py` finds **zero** tables of
    the Universe shape in all four programs. The only `bra.w` run on the disc is
    **10 entries at `gs`+0x1122 with 10 distinct handlers**, with nothing
    dispatching into it by complemented index — too small and too isolated to be
    an interpreter.

    What it does instead is the alternative worth naming: the front end is
    **data-driven by IFF**. 25 `SCRN` files carry `SCHD` headers and 39 `AREA`
    chunks of screen coordinates, and the program walks them. A game can have
    missions, branching and an endgame without a bytecode VM by putting the
    structure in a chunk format instead. **Check for a data-driven screen format
    before concluding a game is hard-coded, not only for a VM.**

    The original entry:

25a. **New - how common is a script interpreter, and what does its opcode space
    look like?** [Universe] is the first disc here with a genuine bytecode VM:
    16 opcodes reached through `lea $12(pc),a6 / neg.b d0 / subq #1 / andi #$ff
    / asl #2 / jsr (a6,d0.w)`, so the index is the **complement** of the opcode
    and the commands are `$F0`-`$FF` with every lower byte inline data. Each
    handler advances an explicit program counter in `$62e(a5)` by its own
    instruction length. Two further dispatch forms sit beside it: a 41-entry
    table (40 distinct handlers) indexed by a signed word read out of a data
    record, and a list of longwords in which a **positive value is a code
    address to call and a negative one is an index** into the engine's
    123-entry export table.

    Thirteen earlier discs had jump tables and none had a VM; Liberation had a
    text generator with a small language of its own and Microcosm a container
    with a directory. **The cheap test is step 32 of the order of work:** find
    runs of `bra.w` without reference to the code that jumps into them. What is
    open is how common this is - one disc is not a rate - and whether the
    genre predicts it. A point-and-click is the obvious place to look next.
    (Sections 4 and 6.)

26. **New - does a disc that switches the OS off have to reimplement the CD32's
    own services, and how far does that go?** [Universe] calls `SuperState()`
    and clears `INTENA`/`DMACON` in a 757-byte loader, and after that point it
    has **zero library and zero device calls**. Everything the ROM would have
    provided comes back as something hand-written: the CD-ROM driver (Akiko
    `$B80004`-`$B80024` plus a CIA-B interrupt handler), the save system
    (bit-banged I2C to the serial EEPROM at `$B80030`, where eight other discs
    call `nonvolatile.library`), and the executable loader (a private
    relocatable format with 16-bit word offsets, replacing `LoadSeg`).

    Dragonstone is the other disc here that kills the OS and drives Akiko, and
    it uses a password save rather than the EEPROM. So the sample is two, the
    behaviours differ, and the question is whether "no OS" predicts "EEPROM by
    hand" or whether Universe is on its own. **Count `OpenDevice` first, and if
    it is zero, look at `$B80000` before concluding the title has no CD audio
    and no save.** (Sections 4 and 8.)

27. **New - how much text is a point-and-click, and is 602 KB typical?** Section
    9 had no denominator for thirteen discs because the text was always a
    garnish. [Universe] gives one: **602,344 bytes of prose, 6.53 % of the
    resident image and 13.70 % of the bytes on disc**, in four complete
    languages with the shares 21.7 / 25.2 / 24.7 / 22.4 % and **nothing
    untranslated** on the records that align four ways.

    One disc is one point. What would make it a baseline is a second
    text-driven title, and what would make it interesting is a text-driven
    title where the shares are *not* balanced - which is what a localisation
    that ran out of time looks like. (Section 9.)

28. **New - eighteen files named by a shipped executable and absent from the
    disc: cut, or another SKU?** [Universe]'s `code.prg` names `block1_1.np`
    through `block5_4.np` and `capt.np` - 18 of the 56 game-file names in its
    table, 32 % - and none is in the volume. The rest of the table is exact,
    including the seven non-contiguous `scene*.dat` names, so it is not a table
    that lists optimistically; and **`block5` is listed before `block4`**,
    which is what a hand-edited table looks like.

    This document has several discs with a handful of named-and-absent files
    (Liberation 3, Legends 1, Microcosm 2) and one with a whole zone's assets
    present-but-unreachable (Fire & Ice). A third of a loader table pointing at
    nothing is a different scale. The disc cannot settle whether they were cut
    from this release, belong to the A1200 floppy release, or belong to the PC
    release the game's own intro script mentions - **only a second SKU can**,
    and step 28 of the order of work says how to compare it. (Sections 4 and 6.)

29. **New - is a fixed-length zero run a reliable structural separator?**
    [Universe] separates the four language blocks inside one blob with a run of
    **exactly 160 zero bytes**, every time, with no header, count or index
    anywhere. The constant length is the whole signal: variable padding would
    be unrecognisable, and 160 is short enough to be missed by a scan looking
    for large free runs. On the same disc, `copper.prg` uses zero runs the
    other way round - two regions of exactly 12,800 bytes that are **reserved
    instruction slots** rather than separators, 3,200 of them each, 16 per
    scanline for 200 lines.

    So a long zero run inside an unpacked blob is worth measuring rather than
    skipping, and the two readings are told apart by whether the length is a
    round multiple of something the display needs. (Sections 7 and 9.)

30. **New — what is a fixed-length zero hole in front of the files for, and does
    a round number separate the cases?** Four discs now leave a gap between the
    volume descriptors and the first file: [Prey CD32] 6,000 sectors,
    [Microcosm] 15,000, [HeroQuest II] 24,272 (95.4 % of the volume) and
    **[Gunship 2000] 51,200 — which is 104,857,600 bytes, exactly 100 MiB, every
    byte zero**. It is *inside* the declared volume, so ISOCD counted it
    deliberately.

    **[Myth] is the fifth, and the second round binary number: 25,600 sectors =
    52,428,800 bytes = exactly 50.000000 MiB, every byte zero, 94.86 % of its
    declared volume** — the largest share the anomaly has ever taken, on the
    smallest volume it has ever appeared in. Two exact binary reservations on
    two unrelated masters, both cut with ISOCD 1.04, both in front of the files,
    one 100 MiB and one 50 MiB.

    That is now enough to name the shape of the answer: it looks like a
    **reserved-space figure typed into the mastering tool in megabytes**. The
    test is cheap and specific — **a sixth disc with a front hole, and its size
    in MiB**. If the sizes keep landing on round binary values the parameter is
    real; if a 1.03 master produces one, the parameter is not new to 1.04.

    The three earlier gaps are odd numbers and were never explained. Gunship's
    is a round binary number to the byte, and that changes what kind of thing it
    can be: a round reservation is something **asked for**, not something a
    layout algorithm produces. The reading this document has been carrying —
    seek optimisation for Red Book during play — was already refuted four times
    (Guardian, Banshee, Fire & Ice, Universe, the last two being the most
    audio-heavy discs here) and is refuted again from a new direction: Gunship's
    files sit *after* the hole, at the outer edge of a 45 %-full disc, which is
    backwards for a seek argument.

    What would settle it: another ISOCD master with a round-number gap, or a
    second pressing of any of these four with a different one. What is worth
    doing on every disc meanwhile: **build the sector map against the declared
    volume size and report every unclaimed run with its LBA range and whether it
    is zero, before opening a single file.** A 100 MiB hole is invisible to a
    file census and obvious in a sector map. (Sections 1 and 10.)

31. **New — how much of a disc is a second game, and does anything launch it?**
    [Gunship 2000] ships a complete, playable **Pirates! Gold** demo that nothing
    runs: `pirates.demo` is a full alternative boot script with CD32 front-panel
    language detection (`c/getlang`, 104 bytes, returns `RETURN_WARN` for
    German), two 383 KB executables differing only in one hunk, a self-contained
    disk font, **15 IFF 8SVX samples buried inside a chip DATA hunk**, and a
    21.6 MB CDXL intro. The disc's actual `s/startup-sequence` never calls it,
    and the one line that would have launched it is commented out with its
    template instruction still attached — `;pirates 2 <TAB> ; replace 5 with the cd
    music track number` — where someone had already replaced the 5 with a 2 and
    left the note.

    The video *is* reachable (`gs` carries `Press RED button to view Pirates!
    Gold intro`), so **13.1 % of the disc advertises a demo the disc will not
    launch**. This is a different scale from open item 21's "a whole program
    pressed and never reached": that was one executable, this is a second
    product with its own boot chain, localisation, assets and audio.

    Two things follow for the next disc. First, **read every script on the disc,
    not only the one AmigaDOS runs** — `pirates.demo` is 386 bytes and it is the
    single most informative file on this master. Second, **a commented-out line
    is evidence, and its comment is evidence about the comment** — the stale
    "replace 5" says the line was edited by hand and then disabled, which is a
    different story from a line that was never enabled. (Sections 4 and 6.)

    **AND THE NEXT DISC ANSWERED THE FIRST HALF OF THE QUESTION.** [Superfrog]
    is **50.5 % Superfrog, 39.6 % a *Super Stardust* demo and 7.4 % an *Arcade
    Pool* demo**, and unlike Gunship's Pirates! Gold **all three are launched** —
    by a front-end menu that is a program, `s/T17Menu`, which writes
    `ram:T17.bat` and lets the startup-sequence `Execute` what it wrote. So the
    answer to "does anything launch it" is now yes on one disc and no on
    another, and the two are told apart by one thing: **whether there is a
    dispatcher**. Look for one before concluding a second game is unreachable.

    The measurement that matters for everything else: **on a compilation, every
    size figure has to name which game it is about.** Superfrog's disc is
    17,404,587 bytes resident and the game is 13,336,690 of it; quoting the disc
    total would have overstated the game by 31 % and broken the band for the
    wrong reason. (Sections 4, 10.)

32. **New — where else is the music, when it is neither a tracker module nor
    Red Book?** [Superfrog] has no audio track, **zero ProTracker modules and
    zero OctaMED modules** at every byte offset with the headers validated, and
    **37 modules** anyway — in **The Player**'s own replayer format, `P41A` and
    `P40B`, whose four-byte magic *is* the version string. Neither of the two
    scans this document tells you to run can see it.

    That is a fifth home for the music beyond the four section 8 listed, and the
    general shape of the problem is worth stating: **a replayer format whose
    magic is its own version string is invisible to a tracker scan and to a
    cruncher scan simultaneously.** How many other such formats shipped on this
    platform is unknown; The Player alone has at least six versions.

    **What to do on the next disc:** if there is no Red Book and no tracker
    magic, look at the **first four bytes of the files whose names say music**
    before concluding anything. On Superfrog a file literally named
    `P40.INGAME1` begins `P40B`, which is the cheapest identification available.
    (Section 8.)

33. **New — is a root directory record dated before its own contents normal?**
    [Superfrog]'s root directory record reads **1994-08-17 16:41:45**, seven
    days and nineteen hours before the earliest of the 242 files it indexes, and
    it is the only record on the disc from that date; all 21 subdirectories are
    dated with the files. It is stored identically in three places, so it is not
    a read error, and the **PVD** on the same disc behaves normally — 25m22s
    newer than the newest file.

    **PARTLY ANSWERED, by [Myth], and the answer is that it is not the tool.**
    Myth's root directory record is 1992-12-21 16:59:24, **one second older than
    the newest of the five files it indexes** and 1h46m46s newer than the oldest
    — stored identically in the same three places, with its single subdirectory
    dated with its file. That is what a normal root record looks like, and Myth
    was cut with **ISOCD 1.04, the same version as Superfrog**. So the anomaly
    belongs to Superfrog's master and not to the mastering tool.

    What two points still cannot separate is a **reused staging directory** from
    a **hand-set date**. Read the field on the third and fourth disc; the
    baseline now exists to compare against. (Sections 1, 3.)

34. **New — can a decoder be verified without the format being understood?**
    [Superfrog]'s Super Stardust demo ships four assets **in both forms**:
    packed in `CRM/`, unpacked in `RAW/`, same names. The `PaCK` header is proven
    on 9 of 9 files and the declared unpacked size matches the `RAW/` sibling
    **exactly** on all four where one exists — so a candidate decoder can be
    checked byte-for-byte against a known-good output without anyone knowing
    what the codec does.

    That is a stronger validation setup than any cruncher in this set has had,
    including the ones with checksums, because a checksum proves self-consistency
    and this proves correctness. **When a disc ships both forms of the same
    asset, that pairing is worth more than a CRC — look for it before writing a
    decoder.** The `PaCK` codec itself is still unread. (Section 5.)

35. **New — is the zero hole a reserved-space figure typed in megabytes?**
    Five discs leave a gap between the volume descriptors and the first file:
    [Prey CD32] 6,000 sectors, [Microcosm] 15,000, [HeroQuest II] 24,272,
    **[Gunship 2000] 51,200 = exactly 100 MiB** and **[Myth] 25,600 = exactly
    50.000000 MiB**. Two of the five are round binary numbers to the byte, on
    unrelated masters from unrelated publishers, both cut with ISOCD 1.04, both
    in front of the files.

    A round reservation is something asked for, not something a layout algorithm
    produces, and two of them make "somebody typed 100" and "somebody typed 50"
    the cheapest available explanation. **The test is a sixth front hole and its
    size in MiB**; a hole on an ISOCD 1.03 master would additionally say the
    parameter is not new to 1.04. (Sections 1, 10.)

36. **New — does the preparer field sometimes name a bureau rather than a
    person?** [Myth]'s reads `ROB NORTHEN COMPUTING, UK. TEL: + 44 428 707771
    FAX: + 44 428 707772` — a firm with contact details, a fourth shape for a
    field this document has read on nineteen discs as "the operator". Trailing run
    32, so the layout correlation is untouched.

    If CD32-era masters were routinely cut by contractors, the `D J Pocock`
    group stops being a puzzle: one name on five masters from five unrelated
    studios and five unrelated publishers, findable nowhere on any of them, is
    what a bureau operator looks like from inside the data. **The test is another
    disc naming a firm in that field, or a `D J Pocock` disc that names a firm
    anywhere else in its payload.**

    And there is a second, sharper question inside it. Rob Northen Computing
    wrote **RNC ProPack**, which is on seven of the nineteen discs here — and the
    master it cut **does not use it**, packing with Bytekiller written by the
    game's own programmer instead. One negative, one for one. **On the second
    Rob-Northen-prepared disc, ask immediately whether it uses RNC ProPack**: two
    negatives would start to say the mastering step and the packing step never
    touch, which is exactly what open item 14 is trying to establish.
    (Sections 1, 5.)

37. **New — what is in the unclaimed blocks of a shipped floppy image?**
    [Myth] presses three 880 KiB disks whole, and **172,010 bytes — 6.36 % of
    its on-disc total — lie outside every entry of the images' own chunk
    tables**. Only 3,428 of those bytes are zero. The identified part is a
    `SYS3` fill pattern, a run of 8-bit PCM, and a complete copy of Commodore's
    `ConClip 37.7`; the unidentified part is **156,292 bytes of entropy 7.6-7.8
    in three runs at the tails of the three disks**, which is the same band as
    the disc's Bytekiller streams.

    The economical reading is a previous build's data left on the physical
    media, but no `DAVE` header validates anywhere in those runs and the
    headerless form of the stream can only be found by trying every candidate
    end, which was not run over 156 KB. **An exhaustive bare-stream end search
    over those three runs would settle it, and a stream that decodes with a zero
    checksum there would be a discarded asset from an earlier build of a shipped
    game** — which no disc in this set has produced yet. (Sections 3, 5.)

38. **New — how many audio tracks does a game actually reach, against how many
    the disc has?** [Alfred Chicken] is the first disc where the denominator is
    measured rather than inherited: nine audio tracks, read from the TOC. The
    numerator is not statically readable. The game opens `cd.device` (two
    `OpenDevice` against exactly two named devices) but writes **no**
    `CD_PLAYTRACK`, `CD_TOCLSN`, `CD_TOCMSF` or `CD_PLAYMSF` as an immediate
    into `io_Command` anywhere — the commands are assembled at run time, exactly
    as its blitter control words and copper lists are.

    A candidate was found and rejected, and the rejection is the useful part: an
    ascending word run `0001 0002 … 001F` sitting immediately after an `rts`. A
    nine-entry slice of it looks exactly like a track table; it runs to 31 and
    keeps going. **A dynamic trace would settle this and static reading will
    not.** The four known answers to *how* a game reaches its tracks (read the
    TOC and filter on CONTROL; name tracks as constants; bypass the OS through
    Akiko; use `cd.device`) do not include "and it reaches this many of them".
    (Sections 1, 8.)

39. **New — is a version-control keyword a better dating instrument than a
    `$VER:`, and how often does one survive into a shipped binary?**
    [Alfred Chicken] carries two expanded RCS `$Header:` keywords, one in each
    game executable:

    ```
    $Header: Hard0:alfred/rcs/amiga.c,v 1.1 93/11/19 16:40:55 JJS Exp $
    $Header: Hard0:alfred/intro/intro/rcs/amiga.c,v 1.1 92/09/29 17:57:54 JJS Exp $
    ```

    A `$VER:` is typed by a person and can say anything; **an RCS keyword is
    stamped by the version control system at check-out**, so it records a real
    event, and it carries four fields where a `$VER:` carries two — a
    filesystem path, a revision, a timestamp **and a user name**. Here it gave
    the build machine's disk, the project layout, the developer's initials, and
    the fact that the two executables are builds of one code base **fourteen
    months apart** — which is what explains why one ships a hardware debugger
    and the other does not.

    No other disc in this set has been checked for RCS or SCCS keywords, because
    until now there was no step that looked for them. `tools/idstrings.py` in
    [Alfred Chicken]'s repository searches for `$Header:`, `$Id:`, `$Revision:`,
    `$Date:`, `$Author:`, `$Log:` and `@(#)` alongside `$VER:`. **Running it
    over the other seventeen images costs nothing and may date several of them
    independently of their PVDs.** (Sections 5, 9.)

40. **New — when a disc has no text at all, what is the string-table model?**
    Four models were known: an offset table into flat strings ([Universe]),
    everything inline in code ([Gunship 2000]), separate text files parsed at run
    time ([Superfrog]), and a relocated page index over position-prefixed record
    chains ([Myth]). **[Alfred Chicken] is a fifth: there is no table, because
    there is no text.**

    Zero prose bytes in every asset file on the disc — 148,157 bytes of level
    archives, tile banks, maps and an icon, and not one byte of it. The 0.607 %
    of the disc that is prose belongs to Commodore's shipped commands (19.6 %),
    a SAS/C runtime and a debugger (78.8 %). **The game's own title exists on
    the disc exactly once in a form a human reads, and it is a 320×184
    four-bitplane picture.**

    The three string-table traps this document lists — length not stored,
    entries repeating and pointing backwards, a zero entry being a kept empty
    slot — **do not apply when there is no table**, and saying so is the result
    rather than a failed check. The measure that *did* apply was the empty-slot
    count, moved onto the thing this disc does have: **72 of 563 tiles across
    seven banks are shipped and never placed by any map**, 12.8 %, with one bank
    throwing away 36.1 %. (Sections 9, 6.)
