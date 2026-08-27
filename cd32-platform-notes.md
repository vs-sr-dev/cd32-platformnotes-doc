# Amiga CD32 / CDTV platform notes — a checklist for the next disc

A running checklist, carried from one Amiga CD documentation pipeline to the
next and added to by each. It currently rests on **four discs**, so most of it
is still marked with the title it came from: treat it as a list of things to
*test*, not a list of things that are true of the format.

The fourth is the **CDTV release of a title whose CD32 release is also here**,
which is the most productive single thing that has happened to this document:
it supplied a control for claims that had been made on one disc's evidence,
and **two of them were wrong**. Both are corrected in place below, and both
corrections are marked. If you can get two releases of the same game on two
generations of the format, do that before you generalise anything.

Findings are marked:

* **[all]** — checked on every disc covered so far.
* **[N of M]** — checked on N of the M discs covered.
* *named after a disc* — seen once, not yet generalised.

The three discs are as unlike each other as CD32 titles can be, which
makes the handful of things they agree on worth more than the count
suggests.

## Discs this rests on

| Disc | Year | What it is |
|---|---|---|
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |
| [Marvin's Marvellous Adventure](https://github.com/vs-sr-dev/cd32-marvinsmarvellousadventure-doc) | 1994/1995 | Infernal Byte Systems / 21st Century, DE/UK — twelve tracks, 212 files, **nothing compressed**, 61 % of the disc used, ten libraries opened and AmigaDOS alive throughout |
| [Prey: An Alien Encounter, CD32](https://github.com/vs-sr-dev/cd32-prey-doc) | **1993** | KirkMoreno Multimedia / Almathera, UK+DK — **one track and no audio track at all**, 1,439 files, nothing compressed, 18 % of the disc used, an hour of speech streamed as 1,225 identical 60 KB files, and the only disc so far that genuinely uses AGA |
| [The Speris Legacy](https://github.com/vs-sr-dev/cd32-thesperislegacy-doc) | **1996** | Binary Emotions / Team 17, UK — one track, **no audio track**, 47 files, **0.74 % of the disc used**, Imploder-crunched at 2:1, genuine 24-bit AGA palettes in every level, and the disc that **broke this document's rule about what the `.TM` block contains** |
| [Legends](https://github.com/vs-sr-dev/cd32-legends-doc) | **1996** | Krisalis Software / Guildhall, UK — **28 audio tracks**, 111 files, **0.72 % of the disc used for the game and 88.6 % for the music**, a six-floppy A1200 game copied onto a CD with its hard-disk installer still on it, 79 files packed by a cruncher with **no magic number at all**, and a front end that re-implements `LoadSeg` |
| [Prey: An Alien Encounter, **CDTV**](https://github.com/vs-sr-dev/cd32-prey-doc/blob/main/docs/09-cdtv-1992.md) | **1992** | The same game a year earlier, published by KirkMoreno alone. **The first disc here not mastered with ISOCD**, the first CDTV disc, the oldest master by fourteen months, and the control that corrected two claims about the other three. 1,453 files, of which **1,201 are byte-identical to the CD32 release** |

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
is **`Game`**. Three discs, three different kinds of answer to the same box:
the title, the genre, and the medium's most generic possible noun. The field
carries no information about the disc and a great deal about who typed it.

If `s/Startup-Sequence` is missing, the disc is not bootable on a stock
machine and something else is going on — check for a CDTV-only boot path or a
disc that was never meant to boot.

**String fields may be malformed and nothing cares.** **[3 of 3]** Every
string field in all three PVDs is NUL-padded rather than space-padded;
Dragonstone's volume identifier is mixed case (`DragonStone`), Marvin's is
`MMA_CD32` with an underscore, Prey's is `Prey`. ISO 9660 asks for
d-characters, upper case, space-padded. Do not use strictness as a signal of
anything.

**Read the cue sheet for a `CATALOG` line — and then read the number.**
Marvin's has one (`5012635300344`) and Prey's has one (`5024913000068`), both
UK EAN-13s; Dragonstone's has none. **Speris has `CATALOG 0000000000000`** —
thirteen zeros, syntactically valid and meaning nothing. The field has three
states, not two, and the presence of the line is not evidence of a catalogue
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
```

**And check the name against the game's own credits, because sometimes it is
there.** [Legends] `Richard Teather` is on the disc twice: in this field, and
in a 320 x 200 digitised **photograph** captioned `RICHARD TEATHER (AMIGA)`
under the heading `THE PROGRAMMERS`. The person who ran the mastering tool is
the person the credits screen calls the Amiga programmer, and the two halves
of the disc agree without either knowing about the other. Four discs of six
name a person here; it is the cheapest attribution on the format and it is
worth cross-checking against whatever credit screen the game has.

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
medium (`Game`), the CDTV master nothing, Speris nothing. Six discs, four
conventions.

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

**A fourth habit, worth a line because the number repeats.** ISOCD leaves the
image longer than the volume it declares, and the overrun is **152 sectors of
zeros on three of the five ISOCD discs** — Marvin (6,833 in the image, 6,681
declared), Speris (2,455 / 2,303) and Legends (2,404 / 2,252). Dragonstone
overruns by 106 and Prey CD32 not at all, so it is not invariant; but a
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

**Count the unclaimed sectors inside the volume.** [Marvin] 32, all zero, at
the end. [Prey CD32] **32, all zero, at the end.** [Speris] **32, all zero, at
the end** — LBA 2271–2302 of a 2,303-sector volume. **Three ISOCD discs,
exactly 32 every time**, across 1993, 1995 and 1996 and volumes ranging from
2,303 to 59,787 sectors, and the one non-ISOCD master has none. That is now a
fingerprint you can use on its own, and it costs one sector map.

**A dump can be much larger than the disc.** [Prey CDTV] the image is 119,988
sectors and the declared volume is 48,637; the 71,351 sectors after it —
146 MB, **58 % of the file you were given** — hold no ISO structure, no
readable string, and a short repeating byte pattern. It is a dump artefact.
Always build the map against the declared size, and say what the remainder
is rather than assuming it is content.

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

### On CD32-era discs: four discs, the same bytes

**All three SHA-1s match, byte for byte, on four of the five CD32-era discs**
— Dragonstone, Marvin, Prey CD32 and **[Legends]**:

```
SHA-1  c5ffcef2a5e33d2df606185823cd95d1c174d65f   the whole sector, 2048 bytes
SHA-1  8d84115154d70360b3469acc99cdad3db0ed2c92   banner only, bytes 0x000..0x44C
SHA-1  690aae24a96b69659066e691d0b07db301260572   object file, bytes 0x44C..0x7B8
```

Four studios, four publishers, four engines with nothing in common, and
**thirty-eight months** between Prey's CD32 master (1993-11-29) and Legends'.
Same 2,048 bytes, in a sector nothing on any of them reads.

**And a fifth CD32-era disc has none of it.** See the correction below before
treating those three hashes as anything more than four sightings of one
widely-copied file. The score is now **four discs with the Commodore banner
and one with the CDTV driver** — which is worth keeping in that form, because
it is the ratio, not the identity, that this section is actually measuring.

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

Which downgrades the three matching CD32 hashes from evidence about the
*format* to evidence about **how widely one particular file circulated**.
They are still worth recording, and a mismatch is still the interesting
result: **this is the first mismatch, and it took four discs to find.**

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
3. **Keep recording the three CD32 hashes.** Three discs across fourteen
   months agree; a mismatch is the interesting result.
4. On a CDTV disc, **record the driver version**. One CDTV disc cannot say
   whether `CDTV.TM` is always `cdtv 35.2 (6.2.91)` or tracks the master date.

`tools/tmsector.py` in
[cd32-prey-doc](https://github.com/vs-sr-dev/cd32-prey-doc) finds the `'TM'`
tag, reads the declared length and LBA, and dumps whatever is there, on both
layouts; the copies in the Dragonstone and Marvin repositories assume sector
21 and 2,048 bytes.

---

## 3. Timestamps — four epochs, and the outliers are the finding

**Sort the directory by timestamp before you read a single file.** It is free
and it has paid on every disc.

ISO 9660 directory records store the year as an offset from 1900. There are
**four epochs to recognise**, not one:

| Reads | Means |
|---|---|
| 1978-01-01 + mm:ss, or 1978-01-*nn* | AmigaDOS `DateStamp` day zero — an Amiga whose clock was never set. The day number is days of uptime |
| 1980-01-01 or a few weeks after | **MS-DOS `FAT` day zero** — the file came through a PC filesystem |
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

**Compare the PVD creation date with the newest file.** [Prey] the last file
written was the title screen at 21:03:54 on 1993-11-29 and the PVD says
21:15:11 — **eleven minutes and seventeen seconds** between the last asset and
the master. The two executables were linked the previous evening, twelve
minutes apart. That single subtraction dates the end of the project to the
minute, and on this disc it also explains a leftover: the executable still
names a CDXL animation for the publisher's logo, and what shipped in its place
is a still image finished eleven minutes before the master (section 4).

---

## 4. The boot chain

Kickstart mounts the volume and runs `s/Startup-Sequence` as a shell script.
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
38.8 (13.2.92) is in `c/` for exactly that.

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
```

The SetPatch version is not the machine's: Marvin ships a 3.0-era SetPatch
and runs it on a CD32's 3.1 ROM. Five discs, four versions, no agreement.

**And hash the binary, not only the version string.** [Legends] `c/SetPatch`
is **byte for byte Marvin's** — SHA-1
`4d4aae988310b07726329e436b2250c0f769ddff`, 7,364 bytes — across two studios,
two publishers and two years. Like the `.TM` block, Commodore's system files
circulated as single copies and studios passed them around; a matching hash
tells you which copy a studio had, and a *mismatching* one at the same version
would be the interesting result.

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

Eight sightings across five discs, **no function call to the library in any of
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

Still worth a grep on every disc — `grep -c freeanim` over `c/` and the first
stage — because *where* a title opens it says how the title is structured.

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

**And there is a third position between them.** [Prey] the first stage makes
64 library calls and touches **no** custom-chip register at all; the game
makes 120 across 44 LVOs, keeps AmigaDOS alive, opens six libraries and
`cd.device` — and simultaneously programs Paula and the Blitter by absolute
address, 448 times. OS-hosted and hardware-driving at once. A **two-process
split** is worth watching for on its own: Prey's first stage and its game
executable are separate files that talk over message ports (`kennport`,
`gameport`) with four-character longword commands (`'kenn'`, `'shut'`,
`'done'`, `'jazz'`).

**Akiko is untouched on all three discs. [3 of 3]** The console's headline
feature — chunky-to-planar in hardware — is used by nothing here except the
easter-egg demo a programmer left on Marvin's disc, which is not the game.

Two more things to check while you are in the executable:

* **Which `OpenLibrary`?** [Marvin] all eleven opens go through
  **`OldOpenLibrary` (LVO −408)**, not `OpenLibrary` (−552), so no version is
  requested and none is checked. [Prey] the same — ten opens across two
  executables, all −408, zero −552. **[2 of 2 where it was checked.]** A
  program using −552 tells you what it minimally needs.
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
[Prey] the same, on a much larger disc: 1,439 files, 122 MB, **zero** hits for
`RNC`, `PP20`, `IMP!` or `XPKF` over the whole image. A CD32 disc has 650 MB
and a 2× drive; a studio that decided the read time was cheaper than the
decompression time was making a reasonable call, and **two discs out of five
made it**. The three that packed were all floppy games moved onto CD with
their floppy-era loaders intact — which is the pattern, now **[3 of 3]**:
**compression on this format tracks the floppy origin, not the disc.**

**And do not stop at `RNC`.** [Speris] returns nothing for `RNC` and 35 files
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

**Three crunchers so far.** RNC ProPack on Dragonstone, the Imploder on
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

**Game overlays are usually not hunk files.** Look for a short custom header
instead. [Dragonstone] uses a sixteen-byte one:

```
offset 0   'DNLD'
offset 4   load address        ($00020000)
offset 8   end of the initialised code/data area
offset 12  entry point         (always load + 0x10)
```

which is what a loader that has already killed AmigaDOS needs and no more.

### The loader's file table is worth finding early

**[3 of 3]** [Legends] the same shape again: 57 NUL-terminated names in one
run at hunk `0x19CC` of the front end — six floppy volume names, then every
file it can open, in index order. All 51 filenames exist on the disc and three
are spelled with capitals the disc does not use. And the *level* executables
carry the complementary trick: a filename **template** with a literal `x` in
it (`LEVEL4/SPRITESx.PAK`) and a separate compiled string naming the contents
of each bank. **Grep for `/` and for the disc's own directory names**, and
grep for uppercase forms of them too.

[Dragonstone] The resident loader carries a run of fixed-width NUL-terminated
filenames followed by a table of 16-bit indices into them, dimensioned by
level. Finding it gave up, in one read: the complete list of data files, the
load order, **21 filenames spelled with the wrong case** relative to the disc
(harmless on an Amiga, fatal on a case-sensitive host), and a **row of seven
`0xFFFF` entries where a cut level used to be**. Look for a dense run of
same-length names before you disassemble the loader.

---

## 7. Graphics

**Assume planar until proved otherwise** — **[4 of 4]**, and on all four
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

So AGA colour depth is used on **three** discs of six, and two of the three
use it everywhere. But **the plane count is still the claim that needs no
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

**And corroborate it in the code, which is cheap and unambiguous.** [Speris]
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

**Beware the byte pattern `00 B8 00` as evidence of Akiko.** [Speris] has 32
of them and uses Akiko not at all: every one is inside a palette or an offset
table. The test that means something is a **pointer load** —
`movea.l #$B80000,An`, `lea $B80000,An` — or a reference to `$B80038`, the
C2P port, or the `$C0DE0000` identification constant. All four are zero here.

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

**First: check whether there is a Red Book track at all.** [Prey] there is
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
* **Raw 8-bit signed PCM** for Paula samples, usually stored **uncompressed**
  because there is nothing to gain on a few kilobytes — so these are often the
  only files on the disc that are not packed, which makes them easy to spot in
  a census.
* **Streamed raw PCM as ordinary files** — [Prey] 1,225 files of exactly
  61,440 bytes, 75.3 MB, 68.6 % of everything on the disc. See below.
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

**The sample rate is in the executable, as a Paula period.** There is nowhere
else for it to be in a headerless file. Search for immediates written to
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

## 9. Text

**Do not assume anything about the encoding — determine it, because it says
where the text was written.** The first two discs go opposite ways and both
are informative; the third has almost no text at all.

* [Dragonstone] IBM **CP437**: `é` is `0x82`, `ß` is `0xE1`. The text was
  authored on a PC and carried across as bytes.
* [Marvin] **ISO 8859-1** throughout, in all four language files and in the
  `©` of the boot script and the `´` in the executable's own error messages:
  `è` `0xE8`, `ß` `0xDF`, `Ü` `0xDC`. Authored on an Amiga.
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

**Placeholders survive.** [Marvin] the language files' password section holds
a fourteen-character string and a line of instruction; the instruction is
translated into all four languages and the string is not, because it is the
template the real password is copied over at runtime. It shipped, four times.
A string that is the right *length* for a field and the wrong *content* is a
placeholder, not data.

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

## 10. Baselines

Six discs, and they bracket the format rather than agreeing on it. Prey CD32
and Prey CDTV are the same game on the two consoles, so that pair is a control
rather than two independent samples. Speris and Legends are both 1996 releases
and they sit at opposite ends of the disc-occupancy column: 0.74 % and 89.4 %.
Their *games* are the same size.

| | Dragonstone (1995) | Marvin's Marvellous Adventure (1995) | **Prey CD32 (1993)** | **Prey CDTV (1992)** | **The Speris Legacy (1996)** | **Legends (1996)** |
|---|---|---|---|---|---|---|
| Publisher / studio | Core Design, UK | 21st Century / Infernal Byte, UK+DE | Almathera / KirkMoreno, UK+DK | **KirkMoreno alone** | Binary Emotions / Team 17, UK | **Krisalis Software / Guildhall, UK** |
| Master cut | 1994/1995 | 1994/1995 | **1993-11-29 21:15:11** | **1992-09-02 15:05:26** | **1996-01-10 20:47:52** | **stamped 1992-03-06 18:12:02 — impossible** |
| Tracks | 1 data (`MODE1/2048`) + 1 audio | 1 data (`MODE1/2048`) + **11** audio | 1 data (`MODE1/2048`), **no audio track** | 1 data, **no audio track** | 1 data (`MODE1/2048`), **no audio track** | 1 data (`MODE1/2048`) + **28** audio |
| Data track sectors | 1,741 (1,635 declared) | 6,833 (6,681 declared) | **59,787 (59,787 declared — equal)** | 48,637 declared **in a 119,988-sector dump** | 2,455 in the image, **2,303 declared** | 2,404 in the image, **2,252 declared** |
| Audio | 118.08 s, 8,856 sectors | **2,600.9 s**, 195,068 sectors | 0 s Red Book; **3,820 s of PCM in files** | 0 s Red Book; **3,922 s of PCM in files** | 0 s Red Book; **12 ProTracker modules** | **3,936.1 s**, 295,209 sectors |
| Share of a 333,000-sector CD | ~3.2 % | **60.7 %** | 18.0 % | 14.6 % | **0.74 %** | **89.4 %** — game 0.72 %, music 88.6 % |
| Files / directories | 91 / 2 | 212 / 9 | **1,439 / 24** | **1,453 / 20** | **47 / 10** | 111 / 7 |
| Bytes on disc / unpacked | 2,721,914 / 10,284,352 | 13,251,697 / — | 109,786,031 / — | 99,327,202 / — | 4,514,540 / **8,543,154** | 4,351,859 / **11,836,224** |
| Compression | RNC ProPack 1, 84 of 91 files, 25.7 % | **none at all** | **none at all** | **none at all** | **Imploder `IMP!`, 35 of 47 files, 52.8 %** | **Bytekiller, no magic number**, 79 of 111 files, 35.2 % |
| PVD system id | `CDTV` | `CDTV` | `CDTV` | `CDTV` (correctly, this time) | `CDTV` | `CDTV` |
| PVD application id | `DragonStone` (the title) | `Platformer` (the genre) | `Game` (the medium) | **empty** | **empty** | `Legends` (the title) |
| Cue `CATALOG` | absent | `5012635300344` | `5024913000068` | — (no cue) | **`0000000000000`** — thirteen zeros | `5012323060062` |
| Mastering tool | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) | **not ISOCD — unidentified** | ISOCD 1.04 (Pantaray) | ISOCD 1.04 (Pantaray) |
| Preparer field | `Sajjad Majid - ...` | `Stewart.. - ...` | `Almathera - ...` | **empty** | **empty name**, tool signature only | `Richard Teather (Programmer) - ...` — **and he is in the credits screen** |
| Duplicate PVD | yes, sectors 16 and 17 | yes, sectors 16 and 17 | yes, sectors 16 and 17 | **yes** — the one habit that crosses tools | yes, sectors 16 and 17 | yes, sectors 16 and 17 |
| Volume starts at LBA | 20 | 20 | **6019 — 6,000 zero sectors first** | 19; **path tables at 48,633, after the files** | 19 | 19 |
| `.TM` block at | sector 21, 2,048 B | sector 21, 2,048 B | **6021**, 2,048 B, and again as `/CD32.TM` | **48,621, 22,152 B**, and it *is* `/CDTV.TM` | **21, 22,152 B** — eleven sectors | 21, 2,048 B |
| `.TM` contents | trademark banner + 876 B `exec` object | identical | identical | **`cdtv.device` 35.2, Carl Sassenrath — no banner anywhere** | **`cdtv.device` 35.2 — the CDTV driver, on a CD32 disc** | trademark banner + 876 B `exec` object — **the fourth identical copy** |
| Unclaimed sectors in the volume | — | 32, all zero | **32, all zero** | none | **32, all zero** | **32, all zero** |
| Timestamps | AmigaDOS 1978 epoch, except 3 files | real 1994 dates; dirs 1992; **2 files at the MS-DOS 1980 epoch** | four epochs: 131 at 1978, **1,213 inherited from the CDTV build**, 84 Commodore stamps, 43 real | one 4½-minute session, all real | **all real**; four sittings, Dec 1995 and Jan 1996 | **all 118 read 1992-03-06**; four sittings, and the PVD is stamped before nine of its files |
| SetPatch | 40.14 (7.10.93) | 39.6 (8.9.92) | 40.12 (16.9.93) | none — `bookit` + `rmtm` instead | **40.16 (14.2.94) — ships, never run** | **39.6 (8.9.92) — byte-identical to Marvin’s** |
| First stage | 1 hunk, 3 relocations, **0 library calls**, Akiko direct | 6 hunks all chip, 4,278 relocations, **169 library calls**, no Akiko | 1 hunk any-mem, 245 relocations, 64 library calls, **0 hardware registers** | **324 bytes**: open dos, load the game | none — a **7-line** script, 4 of them `assign` | none — a **9-line** script; `ShutDown`, `SetPatch`, 6 `assign` |
| Game executable | (same file) | (same file) | 1 hunk, **5,323 relocations**, 120 library calls, **448 register writes** | 71,316 B, and a **324-byte** first stage | 1 hunk, **1,647,128 B in chip**, 3,404 relocations, 72 library calls | 1 hunk, 37,848 B **in chip**, 1,020 relocations, 60 library calls |
| Libraries opened | none | 10, via `OldOpenLibrary` | 6, via `OldOpenLibrary` | `cdtv.device`, `bookmark.device` | 5: graphics, dos, intuition, lowlevel, nonvolatile | 3: dos, intuition, graphics (+ `cd.device`, `ciaa`/`ciab.resource`) |
| `freeanim.library` | opened by `c/FreeAnim` | opened **first** by the game, never called | opened by the first stage; `c/freeanim` ships unused | **not present — `c/rmtm` instead, and it is run** | opened by `c/FreeAnim`; **not on the disc** — it is in CD32 ROM | **opened by `c/ShutDown` in order to `RemLibrary` it** |
| Akiko | driven directly | untouched | untouched | n/a (CDTV) | untouched | untouched |
| Colour | `FMODE = 0`, ECS path on AGA silicon | **all palettes 12-bit** | **6 of 14 screens exceed 12-bit** | all 12-bit, as ECS requires | **24-bit palettes in all 16 levels**, 6 planes | **front end 8 planes / 256 colours / 24-bit; levels 4-5 planes / 32 colours / 12-bit** |
| Graphics | interleaved planar, 3 and 4 planes | interleaved planar, 6 planes (one file separated) | **separated planar**, 4 planes; ILBM at **8 planes** | same frames, 4 planes; ILBM at **5 planes** | interleaved planar, 6 planes; 16×16 tiles + **3 property planes** each | **separated planar**, 8 planes; 16x16 font glyphs also separated |
| Text encoding | CP437, with two files in a third encoding | ISO 8859-1, all four languages | 7-bit ASCII, and there is almost none | 7-bit ASCII, and even less of it | 7-bit ASCII, 30-char fixed lines, **no apostrophe in the font** | 7-bit ASCII; **accents and eszett dropped**, not transliterated |
| Languages | 3 (EN/FR/DE) | 4 (EN/DE/FR/IT) | 1 (EN), with Danish filenames | 1 (EN), same Danish filenames | 1 (EN) | 3 (EN/DE/FR) |
| Music | 1 CD track + 1 ProTracker module | 11 CD tracks + 12 in-house `.pc` modules | **1,225 raw PCM files at 19,705 Hz** | **1,258 of the same files**, 178 scenes | **12 ProTracker modules** — 8 files, 4 embedded | **28 CD tracks** + 1 ProTracker module + 8 IFF 8SVX in the level code |
| Save system | password, 64-char alphabet, bit field | password table + CD32 `nonvolatile.library` | **none** | **none** | CD32 `nonvolatile.library` **and** floppy save-disk code | password, 8 characters; **no `nonvolatile.library`** |
| Cut content | level 4, `0xFFFF` row in the loader table | 3 unlisted working levels, 1 unused music file | 7 sprite banks, 1 door animation, 2 files the code still names, **scene 0 dropped** | the same 7 sprite banks and door are already missing here | template level name in all 16; a **corrupt `BGFX` tag that shipped**; a crunched level in a stale buffer | `Legends_Disk4:` named by nothing, 18 `SIGN MESSAGE n` placeholders, 15 `XXXX` records, `EMPTY PAL` slots |

---

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
   directory dates.
6. **Read `s/Startup-Sequence`, the whole of `c/`, and the whole of `libs/`.**
   Every `$VER:`. Then diff `c/` against the boot script and see what ships
   without being run.
7. **Parse the first stage as a hunk file** — hunk count, memory flags,
   relocation counts, symbols — then run the greps of section 4: count
   `4E AE` first, because it decides how you read everything else. Then
   histogram `00 DF F0 xx` rather than searching for the base address, or you
   will miss a program that writes every register absolutely. **And check
   whether there are two executables**: Prey's front end and its game are
   separate programs that talk over message ports.
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
    there are none, autocorrelate wide, then render at several plane counts
    and look.
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
    (`Protracker 3.10`). It costs one `find` for four bytes.
18. **If there are headerless files that look like waveforms, get the rate out
    of the executable** — the `AUDxPER` immediates — and check the `AUDxLEN`
    immediates against the file sizes. On a disc with no audio track this is
    the whole soundtrack.

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
   `0x0FFF`, so **AGA used as a deeper ECS** remains the common case. And **no
   disc yet uses Akiko in the game** — that is the open question worth chasing.
   (Section 7.)

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
   is not. **The remaining question is narrower and better: does any CD32 title
   spend the disc on the game rather than on the soundtrack?**

7. **New — is `MODE1/2048` universal?** All six discs so far, including a
   1992 CDTV master, a disc with no audio track and a disc with twenty-eight.
   Mode 2 Form 1 is supposed to occur on this format; nobody has produced one
   here yet.

8. **New — how many CD32 discs carry a second, Workbench entry point?**
   Marvin ships `<Game>.info` with `DefaultTool = IconX`, `c/IconX`, and a
   sibling AmigaDOS script, so the same disc boots on a console and
   double-clicks on an A1200 desktop. Dragonstone does not. Prey does not
   either — it has `c/IconX`, because it has the whole of Workbench's `C:`,
   but no `.info` at the root and no sibling script. **[Legends] does, in a
   third form**: `/Disk.info` and `/InstallHD.info` are Workbench icons, and
   the root holds a `StartUp-Sequence` and an `AssignInfo` that assign to
   `Work:Legends` — a hard-disk path — beside a complete A1200 hard-disk
   installer the CD32 can never run. Two of five, and the second one is not a
   second entry point so much as **the floppy release's whole install path,
   copied over unedited**. When a CD32 disc has `.info` files, check whether
   they are an alternative way in or a fossil.
   Note that Prey still ships `lowlevel.library` and `nonvolatile.library`,
   which are the A1200 compatibility libraries, and opens the first and not
   the second. (Sections 1 and 4.)

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
   claims. **No disc yet examined on this format was swept**, across 1992 to
   1996 and five studios. At this point the finding is the rule, not the
   exception, and the useful question has inverted: **is there a CD32 disc
   that *was* cleaned up, and what does one look like?**
