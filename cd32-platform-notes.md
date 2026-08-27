# Amiga CD32 / CDTV platform notes — a checklist for the next disc

A running checklist, carried from one Amiga CD documentation pipeline to the
next and added to by each. It currently rests on **one disc**, so almost
everything here is marked with the title it came from: treat it as a list of
things to *test*, not a list of things that are true of the format.

Findings are marked:

* **[all]** — checked on every disc covered so far.
* **[N of M]** — checked on N of the M discs covered.
* *named after a disc* — seen once, not yet generalised.

With M = 1 the first two marks are not yet worth much. They are here so the
second pipeline has somewhere to put its answers.

## Discs this rests on

| Disc | Year | What it is |
|---|---|---|
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |

---

## 1. Identify the disc, and do not trust the obvious fields

A CD32 game is an ordinary ISO 9660 disc with an AmigaDOS volume inside it.
There is **no boot descriptor, no signature file, and no header that says
CD32**. What you check instead:

| Where | What to expect |
|---|---|
| PVD system identifier (offset 8) | `CDTV` — *not* `CD32` |
| `s/Startup-Sequence` | present, and it is the boot script |
| `c/` | AmigaDOS commands: `SetPatch` plus one or two custom tools |
| Sector 21 | the Commodore trademark block (section 2) |
| Track 1 mode | `MODE1/2048` on Dragonstone; Mode 2 Form 1 also occurs |

**The system identifier lies about the machine and it is supposed to.**
Dragonstone is a 1994 CD32 title and its PVD reads `CDTV`, because the CD32
reads CDTV media and a CD32 disc identifies its volume the way a 1991 CDTV
title does. Do not conclude you have a CDTV disc from that field alone.

If `s/Startup-Sequence` is missing, the disc is not bootable on a stock
machine and something else is going on — check for a CDTV-only boot path or a
disc that was never meant to boot.

**String fields may be malformed and nothing cares.** [Dragonstone] Every
string field in the PVD is NUL-padded rather than space-padded, and the volume
identifier is mixed case (`DragonStone`). ISO 9660 asks for d-characters,
upper case, space-padded. Do not use strictness as a signal of anything.

### The mastering tool leaves fingerprints — collect them

The **data preparer** field usually names the tool outright. Dragonstone's
reads:

```
Sajjad Majid - ISOCD 1.04 by Pantaray, Inc. USA -
```

and that tool has a visible habit: **it writes the primary volume descriptor
twice**, at sectors 16 and 17, byte for byte identical, with the terminator at
18. Nothing is wrong; a reader takes the first primary descriptor it finds.
Other tools do other things. Log which tool wrote which disc and what its
layout habits are — this is exactly the kind of thing that only becomes
useful at three discs.

---

## 2. Sector 21 — the Commodore trademark block

**Do this on every CD32 and CDTV disc.** It costs a minute and it is the
highest-yield first move on the format so far.

Sector 21 is **outside the file system**: no directory record covers it, and a
sector map built from the directory shows it as free space. On Dragonstone the
only pointer to it anywhere on the disc is in the PVD's **application-use
area** (offset 883 onward), which is normally empty and here holds:

```
offset 883:  00
offset 884:  46 53 00 00        "FS"
offset 888:  54 4D 00 14        "TM", 0x0014 = 20
offset 892:  00 00 08 00        0x0800 = 2048
offset 896:  00 00 00 15        0x0015 = 21
```

Two two-character tags and then 20, 2048, 21 — the path-table LBA, one
sector's worth of bytes, and the trademark LBA. **Read the application-use
area before assuming it is padding.**

The first ~1,100 bytes of the sector are ASCII art: `Copyright (c) 1993 -
Commodore Electronics Ltd.`, the Commodore logo drawn in `C`, `/` and `\`, and
a trademark notice.

### Then check what comes after the banner

[Dragonstone] On this disc the banner is followed, at offset `0x44C`, by **876
bytes of unlinked AmigaDOS object file**:

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

**The open question the second disc answers.** If the same bytes appear on
another CDTV or CD32 title, then the trademark block Commodore distributed to
developers was itself built by concatenating the banner with a stale buffer,
and the fragment has been pressed onto discs of this format for years. If they
do not, it is specific to this master. Hash and compare:

```
SHA-1  c5ffcef2a5e33d2df606185823cd95d1c174d65f   sector 21, all 2048 bytes
SHA-1  8d84115154d70360b3469acc99cdad3db0ed2c92   banner only, bytes 0x000..0x44C
SHA-1  690aae24a96b69659066e691d0b07db301260572   object file, bytes 0x44C..0x7B8
```

`tools/tmsector.py` in
[cd32-dragonstone-doc](https://github.com/vs-sr-dev/cd32-dragonstone-doc)
dumps and parses it for any track-1 image. **Record the three hashes for every
disc you open**, whichever way the answer goes.

---

## 3. Timestamps and the AmigaDOS epoch

ISO 9660 directory records store the year as an offset from 1900. Amiga build
machines frequently had no set clock, and **1 January 1978 is day zero of the
AmigaDOS `DateStamp`**. A record reading:

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

**Files that carry a real date came from somewhere else, and that difference is
the finding.** [Dragonstone] Three of 91 files carry genuine 1992 timestamps,
from a machine whose clock was set, two years and four months before the
master — and they are exactly the three files that contain the disc's
hand-written CD driver. Whether that means the driver's *files* were carried
forward or merely their datestamps is unresolved; the point is that the split
was visible for free, before anything was disassembled.

Note also that the **on-disc order is not the write order**. Files are laid out
alphabetically within each directory, so the shared files written last sit at
the lowest LBAs.

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

**Read the `$VER:` string in every `c/` command.** They date the tools and say
whether the command is Commodore's or the studio's:

```
$VER: setpatch 40.14 (7.10.93)     Commodore, the Kickstart 3.1 release
$VER: noopenwb 37.1 (3.11.93)      not Commodore's
```

`SetPatch`'s string table also names every patch it can install, and a CD32
title ships it partly for the `cd.device` ones — `Drive Firmware Patch`,
`CDPatch Interrupt`, `cd CD_SEEK`.

**Watch for a command that opens a library the disc does not contain.**
[Dragonstone] `c/FreeAnim` is a SAS/C 6 program that opens `dos.library`,
`intuition.library` and `freeanim.library` — and the third is not on the disc,
so it is resident in Kickstart or the extended ROM. Its position in the
sequence (after Workbench is suppressed, immediately before the game takes the
machine) points at reclaiming memory held by the CD32 boot animation, but that
reading is not confirmed and the library is not in the usual documentation.
If the next disc runs the same tool, that is worth knowing.

### How the first stage reaches the CD — two greps

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
Paula's low-pass filter, bit 7 the fire-button test) and `00 DF F0 00` (custom
chip base).

**Look for the module-end label.** [Dragonstone] The three files containing the
CD driver each hold the string `CDIOEND`, sitting at the end of a run of zero
bytes exactly where an assembler leaves a section-end symbol. A marker like
that tells you which modules share a hand-written subsystem before you
disassemble any of them — and here it correlated perfectly with the anomalous
timestamps in section 3.

---

## 5. Compression

**RNC ProPack is the default assumption.** Magic is ASCII `RNC` at offset 0
followed by a method byte of 1 or 2. Extensions vary by studio — `.cru` on
Dragonstone, often no extension at all — so scan by magic, not by name.

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

### Expect fixed unpacked sizes

[Dragonstone] Every file of a given type unpacks to exactly the same length
whatever the level (319,488 for the tile bank, 81,920 for a text file, 160,256
for the object map, 32,768 for the object directory), while the last non-zero
byte moves around — 73.9 % to 95.2 % of the buffer used. **The data was padded
to a fixed length before packing, and the fixed length is the buffer the loader
allocates.** That tells you how memory is laid out before you disassemble
anything, and it means the loader never reads a length.

---

## 6. Executables and overlays

AmigaDOS hunk format, magic `00 00 03 F3`. `tools/hunk.py` in the Dragonstone
repository reads the subset that matters: HEADER, CODE, DATA, BSS, RELOC32,
SYMBOL, DEBUG.

Useful tells:

* **Relocation count.** A 50 KB code hunk with three RELOC32 entries is
  position-independent hand-written assembler. Hundreds of them means a C
  program.
* **`HUNK_DEBUG` before the first code hunk, tagged `HEADDBGV01`**, is SAS/C 6.
  `main.c`, `ver6.00` and `_main` in the code hunk confirm it.
* **`HUNK_SYMBOL` survives surprisingly often** and hands you the author's own
  label names for free.

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

[Dragonstone] The resident loader carries a run of fixed-width NUL-terminated
filenames followed by a table of 16-bit indices into them, dimensioned by
level. Finding it gave up, in one read: the complete list of data files, the
load order, **21 filenames spelled with the wrong case** relative to the disc
(harmless on an Amiga, fatal on a case-sensitive host), and a **row of seven
`0xFFFF` entries where a cut level used to be**. Look for a dense run of
same-length names before you disassemble the loader.

---

## 7. Graphics

**Assume interleaved planar until proved otherwise**, and get the proof from
the copper list rather than from the pixels: if `BPLxMOD = (planes - 1) *
bytes_per_row` and consecutive `BPLnPT` values are one row apart, the bitmap is
interleaved. [Dragonstone] Two copper lists on the same disc, one 320 pixels
wide at 3 planes (`BPLxMOD = $50 = 2 * 40`) and one 128 wide at 4
(`BPLxMOD = $30 = 3 * 16`), both agree.

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

---

## 8. Audio

Three places to look, and a CD32 game may use all three:

* **Red Book tracks** — read the cue sheet. Check whether the audio is real
  stereo or mono in a stereo container, where it fades, and how much digital
  silence is padded on. [Dragonstone] one track, 118.08 s, genuine stereo,
  -0.8 dBFS peak, 2.4 s of silence at the tail.
* **Raw 8-bit signed PCM** for Paula samples, usually stored **uncompressed**
  because there is nothing to gain on a few kilobytes — so these are often the
  only files on the disc that are not packed, which makes them easy to spot in
  a census.
* **ProTracker modules** — scan for `M.K.`, `M!K!`, `FLT4`, `4CHN`, `6CHN`,
  `8CHN` at offset 1080 of a candidate. The 20-byte title and the 22-byte
  sample names frequently carry the musician's own filenames verbatim;
  [Dragonstone]'s ending module has a sample slot reading
  `mod.heim(2)xtratune1`.

If a scan for all of those turns up one module and the game clearly has more
music than that, the rest is an in-house player with no magic word — look in
the resident loader first.

---

## 9. Text

**Do not assume Latin-1 because it is an Amiga.** [Dragonstone] The localised
text is **IBM CP437** — `é` is `0x82`, `ß` is `0xE1`, where an Amiga would use
`0xE9` and `0xDF`. That is itself a finding: the text was authored on a PC and
carried across as bytes.

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

**A 64-character alphabet is a password alphabet.** `A-Za-z0-9+-` is six bits
per symbol; where you find it, the save system is a bit field printed six bits
at a time and there is no save file to look for.

---

## 10. Baselines

One disc so far. Fill this in as the second arrives.

| | Dragonstone (1995) |
|---|---|
| Tracks | 1 data (`MODE1/2048`) + 1 audio |
| Data track sectors | 1,741 |
| Audio | 118.08 s, 8,856 sectors |
| Share of a 333,000-sector CD | ~3.2 % |
| Files / directories | 91 / 2 |
| Bytes on disc / unpacked | 2,721,914 / 10,284,352 |
| Compression | RNC ProPack 1, 84 of 91 files, 25.7 % |
| PVD system id | `CDTV` |
| Mastering tool | ISOCD 1.04 (Pantaray) |
| Duplicate PVD | yes, sectors 16 and 17 |
| Sector 21 object file | yes, 876 bytes, unit `exec` |
| Directory timestamps | AmigaDOS epoch, except 3 files |
| First stage | 1 hunk, 3 relocations, **0 library calls**, Akiko direct |
| `FMODE` | written as 0 — ECS path on AGA hardware |
| Text encoding | CP437, with two files in a third encoding |
| Music | 1 CD track + 1 ProTracker module |

---

## 11. The order of work that worked

1. **Read the cue sheet.** Track count, modes, `CATALOG`, pregaps.
2. **Dump the volume descriptors** — including the application-use area, and
   check whether the PVD is duplicated.
3. **Walk the directory and build a sector map.** List what is *not* claimed by
   any file. On this format that is where sector 21 turns up.
4. **Dump sector 21**, hash it in three pieces, and parse whatever follows the
   banner.
5. **Sort the directory by timestamp** before reading a single file. It is free
   and it gives you the build order and the outliers.
6. **Read `s/Startup-Sequence` and the `$VER:` strings in `c/`.**
7. **Parse the first stage as a hunk file**, then run the two greps of
   section 4 — library-call count and `$B80000`.
8. **Scan every file for `RNC`**, unpack, and check every CRC. Do not proceed
   on unverified output.
9. **Census the unpacked set**: sizes, entropy, zlib ratio, last non-zero byte.
   Fixed sizes and partial occupancy tell you the memory map.
10. **Find the loader's file table.** Names, order, case mismatches, and any
    slot that is blanked.
11. **Disassemble the copper lists** before looking at any pixels.
12. **Compare the language files** against each other before reading any of
    them.

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
document.

## Open across the format

1. **Does every CDTV/CD32 disc carry the same object file after the trademark
   banner in sector 21?** Three SHA-1s in section 2; thirty seconds to check.
2. **Is the duplicated PVD a habit of ISOCD specifically**, or of the era?
   Record the data preparer string and the descriptor layout for every disc.
3. **What is `freeanim.library`?** Not on the disc, not in the usual
   documentation; presumed resident in Kickstart or the CD32 extended ROM.
4. **How common is a first stage that makes zero library calls?** Dragonstone's
   walks ISO 9660 by hand to find two files. If that is normal on the format,
   the ISO-parsing routine is worth documenting once, here.
5. **Do other CD32 ports write `FMODE = 0`?** If the answer is "nearly all of
   them", that is a fact about the platform's software rather than about any
   one game.
