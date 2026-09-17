# -*- coding: utf-8 -*-
"""The Power Drive (CD32) column for the section 10 table.

The twentieth disc: US Gold, mastered by Rob Northen Computing with ISOCD 1.04
on a PVD date of 1992-12-21 that the disc's own `.TM` block falsifies — the
fourth disc with that afternoon, the same preparer and the same 50-MiB hole as
Myth. One MODE1/2352 track of 38,133 sectors, 68.39 % zero; 161 files, 135 of
them RNC ProPack 1 closing 135 of 135; 89.73 % of the file bytes are six cars
in 583 headerless frames of 240 x 150 x 5 planes with a 32-colour palette
each, dated December 1994; a loader that drives Akiko for the CD and the NVRAM
through base registers and never touches the C2P port — checked, for the
first time, in the register-relative form.
"""

TITLE = "**Power Drive (1994/1995)**"

CELLS = {
 "Publisher / studio":
   "**`USGOLD`** in the PVD publisher field, a label new to this set. **No "
   "studio is named in any byte of text**: the developer's name exists on the "
   "disc only as pictures — six 320 × 200 × 8-plane screens (`denton3..6.bit`, "
   "`fullneon.bit`, `offneon.bit`) and six more in `dendes.bin` that render "
   "as the words **`DENTON DESIGNS`** in chrome over a starfield. The preparer "
   "is `Rob Northen Computing` with ISOCD 1.04, the same string as Myth's in "
   "mixed case; the packer is RNC, so for the first time the preparer's company "
   "and the cruncher's author coincide on one disc. The credits screen is a "
   "photograph of a team around a rally car with no text in the bitmap",

 "Master cut":
   "**PVD 1992-12-21 15:14:49, falsified by the `.TM` block's © 1993** — the "
   "fourth disc with that afternoon (Banshee, Marvin, Myth), the first sharing "
   "a preparer with another (Myth). Root record 15:12:16, `s/` **19:17:20 the "
   "same day**: a volume cut at 15:14 indexing a directory written at 19:17, so "
   "the stamps are not one clock's. First bulk write 15:19:00–15:19:40 (49 "
   "files) — inside the 15:1x window section 3 asked for. **A second day, "
   "1992-12-22, 92 files from 15:08:38 — fourteen seconds after the first "
   "day's first stamp (15:08:24)**: two boots, the date advanced by one. "
   "Content dated 1994-12-07/-10/-15 on 13 files (the car frames); three "
   "files dated 1984-02 (`rally`, `rboot.bin`, `rmenus.rnc`), the last one "
   "carrying the same stamp inside a PKZIP on the disc. **161 of 162 records "
   "have an even second** (FAT resolution); the odd one is the ZIP",

 "Tracks":
   "**1 — data only (`MODE1/2352`)**, `INDEX 01 00:00:00`, no audio track",

 "Data track sectors":
   "**38,133 in the image — 89,688,816 raw bytes, an exact multiple of 2,352**; "
   "37,983 declared; 150 past the volume (148 zero + **2 malformed at the tail**, "
   "bad EDC/ECC, one with mode byte 164 and a non-BCD MSF — the dump's tail). "
   "Every one of the 38,133 verified on sync, header address, EDC and ECC",

 "Audio":
   "none — no Red Book track; 27 IFF 8SVX samples inside the two music "
   "players, all 8,363 Hz, 8.86 s of sample data, every `ANNO` `Oktalyzer "
   "V1.1`, every `NAME` a `.WAV`",

 "Share of a 333,000-sector CD":
   "11.45 % (38,133 sectors); **68.39 % of the track is zero** (26,078 sectors), "
   "of which **25,600 = 50.000000 MiB at LBA 22–25621 is the same hole, at "
   "the same LBA, as Myth's**; 32.24 % of the declared volume is files",

 "Files / directories":
   "**161 / 1** (`s/`, holding the seven-byte boot script); 161 distinct SHA-1; "
   "0 of 161 hashes cross any of 121 other repositories",

 "Bytes on disc / unpacked":
   "**25,080,102** on disc; 135 RNC files 1,626,621 → 8,533,036 (× 5.246); "
   "**22,504,992 (89.73 %) are the seven `*dat.bin`/`*pal.bin` pairs** of 1994, "
   "unpacked already; the 1992 game is 6.49 % of the file bytes packed",

 "Compression":
   "**RNC ProPack method 1 on 135 of 161 files, 135 of 135 closing on both "
   "CRCs** (by magic == by extension), expansion **× 5.246**, the highest of the "
   "RNC discs; nothing nested; the 14 frame files, the six `.bit`, `dendes.bin`, "
   "`rboot.bin` and the ZIP unpacked. The loader unpacks in place (a0 = a1) with "
   "its own decoder after `NVIOEND`",

 "PVD system id":
   "`CDTV` (the ISOCD habit)",

 "PVD application id":
   "blank",

 "Cue `CATALOG`":
   "none in the cue (one `FILE`, one `TRACK`, one `INDEX`)",

 "Mastering tool":
   "**ISOCD 1.04** by Pantaray, in the preparer field; two byte-identical PVDs "
   "at 16 and 17, terminator at 18; path tables at 20 (L) / 19 (M)",

 "Preparer field":
   "**`Rob Northen Computing, UK. Tel: + 44 428 707771 Fax: + 44 428 707772 - "
   "ISOCD 1.04 by Pantaray, Inc. USA -`** — Myth's string in mixed case "
   "(Myth's is upper) — the third company entry in the field and the first "
   "company to appear twice; trailing run 182 sectors (180 zero + the 2 "
   "malformed) past 37951, inside the image's 150-sector overrun",

 "Duplicate PVD":
   "yes — sectors 16 and 17 byte-identical (`cmp`; the control 17 vs 18 differs "
   "at byte 1)",

 "Volume starts at LBA":
   "root directory extent **25622**, behind the 25,600-sector hole; the first "
   "file at 25626 (`ariz.rnc`)",

 "`.TM` block at":
   "sector 21, 2,048 B, reached from the PVD's application-use area: tag `TM`, "
   "constant 0x0014, length 0x800, LBA 0x15 — the majority form",

 "`.TM` contents":
   "**identical** — all three SHA-1s match (`c5ffcef2…` / `8d841151…` / "
   "`690aae24…`): the **eighteenth of the nineteen CD32-era discs with the "
   "Commodore banner** (Speris carries `cdtv.device`; Prey CDTV has no banner). "
   "`Copyright (c) 1993`, which falsifies "
   "the PVD's 1992. No `.TM` file in the root",

 "Unclaimed sectors in the volume":
   "**25,783 in 2 runs**: sector 21 × 25,601 (the `.TM` block, then the "
   "50.000000-MiB hole, every byte zero) and 37951 × 182 (180 zero, 2 "
   "malformed). 12,350 claimed + 25,783 unclaimed = 38,133",

 "Timestamps":
   "**three clocks in one directory**: 1984-02-01 (2 files, 13:29:36 and "
   ":48), 1984-02-10 (1), **1992-12-21 (53 + `s/`) and 1992-12-22 (92)**, "
   "1994-12-07 (10), -10 (2), -15 (1). Every 1992 record's second is even but "
   "the ZIP's (15:12:01) — FAT stamps on a tree the Amiga then mastered; the "
   "neighbours' 1992-12-21 stamps are odd freely, so the FAT hop is this disc's. "
   "The ZIP's two members (`RMENUS.RNC` 1984-02-10 11:50:46, `WALT.RNC` "
   "1992-12-21 17:32:22) are byte-identical to the disc's files and carry the "
   "disc's exact record stamps. The `.bin` itself is dated 1996-12-24 — the dump",

 "SetPatch":
   "none — no `c/`, no `libs/`, no `SetPatch`; the boot script is `rally` and "
   "nothing else",

 "First stage":
   "`s/startup-sequence` (7 B: `rally`) → **`rally`, a 440-byte one-hunk CODE "
   "file, 0 relocations**: colours to black, bitplane DMA off, two "
   "`AllocMem($1A000, CHIP)` — the first rejected unless it avoids "
   "$28000–$41FFF — `dos.library` **`Open`/`Read`/`Close` of `rboot.bin` twice** "
   "into the two blocks, `SuperState()`, 50 frames on `VPOSR`, `jmp` into the "
   "first block. Four coloured halt loops (yellow no memory, red no dos, green "
   "no file, blue short read)",

 "Game executable":
   "**`rboot.bin`, 99,510 B of raw 68000 code with no hunk header** (`lea "
   "$DFF000,a6; DMACON $03F0; INTENA $3FFF; CIA-B ICR; INTREQ`), which "
   "**copies itself to $28000** and its CD driver to $120000, and is a "
   "device library with its own end-of-module labels — `CDIOEND` (twice: the "
   "driver assembled at two origins), `DOSIO` (bitmaps, 30-char BSTR volume "
   "names), `FDIOEND` (a floppy **MFM sector encoder**, `$44894489`, $440-byte "
   "sectors), `RDSK`/`PART`/`HDIOEND` (a RigidDiskBlock parser), `NVIOEND` "
   "(the I²C EEPROM driver) — Myth's four-back-end shim by the same author, "
   "grown to 99 KB for a console with one CD drive. Its main line loads "
   "`gmusic.rnc` then `music.rnc` to $178800, then **`rmenus.rnc` to $155000 "
   "and jumps there**; `rmenus` (103,232 B raw, the menu program, holding the "
   "names of 153 files and the five-language table) loads **`walt.rnc` to "
   "$1000** (95,188 B raw, entry `jmp $106BC` = file offset $F6BC) and the "
   "six 1992 car files to $110000. Files are opened **by path, case-"
   "insensitively, through a directory table the driver builds** (command 5 of "
   "16); no `CD001` and no root-extent constant in the loader",

 "Libraries opened":
   "**one — `dos.library`, by `rally`, for two `Open`/`Read`/`Close`**; then "
   "`SuperState()` and nothing again. `rboot.bin` makes no library call and "
   "opens no device: Exec, `INTENA` and `DMACON` are cleared in its first six "
   "instructions",

 "`freeanim.library`":
   "absent — no `libs/` at all",

 "Akiko":
   "**driven directly for the drive AND the NVRAM; C2P port untouched, and "
   "checked in the register-relative form for the first time.** `$00B80000` → "
   "a5 three times (the fourth drive-driver: Dragonstone, Universe, Myth, Power "
   "Drive), `$00B80030` → a2 twice (the second I²C user after Universe); 0 "
   "absolute `$B80038`/`$3C`; `$C0DE0000` **0 as code, 6 as bitmap bytes inside "
   "`*dat.bin`** (`ff ff ff ff c0 de 00 00 1f ff`). `akiko2.py --follow` walks "
   "the code from each load through `bsr`/`Bcc`/`jsr d16(pc)`/`jsr abs.l` "
   "(`--base 0x28000`): **46 + 45 accesses from the a5 loads reach `$04 $08 $10 "
   "$14 $18 $19 $1A $1D $1F $20 $24` and nothing else; 21 + 13 from the a2 "
   "loads reach `$30` only; 32 dispatch handlers closed by hand: C2P 0.** The "
   "94 `$38`/`$3C` displacements on any register all close: 80 on a6 (the "
   "driver's variables), 4 on a5 (an MFM sector's data checksum in the floppy "
   "encoder), 10 in data. Nothing on the disc is chunky, so nothing converts",

 "Colour":
   "**32-colour RGB888 palettes, one per frame** — 96 bytes of 8-bit triples for "
   "every one of 1,403 frames; the loader clears **`FMODE` ($DFF1FC)**, an AGA "
   "register, so it assumes AGA; the 320 × 200 × 8-plane logo screens carry no "
   "palette in the file. No copper list read",

 "Graphics":
   "**headerless planar, closed by lag measurement and a render the owner "
   "recognised**: the six cars are **583 frames of 240 × 150 × 5 contiguous "
   "planes** (22,500 + 28 B of padding = 11 CD sectors; row stride 30 found as "
   "the equality-rate peak, the plane boundary as a 0.0 % dip after row 300) "
   "with a palette per frame; `usg` is **820 frames of 224 × 80 × 5** (frame "
   "800 reads `PRODUCTION`); six `.bit` and six 64 KiB slots of `dendes.bin` "
   "are **320 × 200 × 8** (stride 40, plane 8,000) — the studio logo twelve "
   "times, two of them twice byte for byte; **59 of the 135 unpacked RNC files "
   "are 51,200 B = 320 × 256 × 5** (50 stage backdrops, `credits` — a "
   "photograph — `main`, `sel`, `options`, `enda`, `endb`, `wire`, `xopt`, "
   "`shaust2`). 74 unpacked stage/car data files left OPAQUE. The frames' byte "
   "values above 31 (62–73 %) rule out chunky before any render",

 "Text encoding":
   "ASCII 0x20–0x7E, `0xFF`-terminated labels, no accents (`CONTRASENA`, "
   "`UBEN`, `PAROLA DORDINE`)",

 "Languages":
   "**five — EN, FR, DE, ES, IT — as five absolute pointers at the end of each "
   "of 121 menu-item records** in `rmenus` (loaded at $155000), the labels in a "
   "pool of `0xFF`-terminated strings; **a word shared between languages is "
   "the same pointer twice** (FR shares EN's in 48 of 121, DE 46, ES 40, IT "
   "41; 39 records point all five at one label). A seventh string model for "
   "section 9. The six cars are named in a 7-pointer table with their prices "
   "(`MINI COOPER S` 25000 … `TOYOTA CELICA TURBO 4WD` 65000)",

 "Music":
   "**two Oktalyzer players wrapped in one-hunk CODE files with the samples "
   "linked in** — `music` (12 × 8SVX, 4.15 s) for the menus, `gmusic` (15, "
   "4.71 s, with `SKID1`, `GRVSKID1`, `BANG`) for the game — loaded to the same "
   "address $178800 in turn; every sample 8,363 Hz, `ANNO` `Oktalyzer V1.1`, "
   "`NAME` a `.WAV` file. No `M.K.`, no Red Book",

 "Save system":
   "**the CD32 EEPROM by hand**: `lea $B80030,a2` (45f9) twice in `rboot.bin`'s "
   "`NVIO` module, 34 accesses to the I²C port — the second disc after Universe, "
   "and for the same reason: no Exec left to call `nonvolatile.library`. What "
   "it stores was not read",

 "Cut content":
   "**a floppy MFM sector encoder, a hard-disk `RDSK`/`PART` parser and a "
   "second assembly of the CD driver** in a loader for a CD-only console, none "
   "of them reachable from the main line; `rboot.bin` read twice by `rally` "
   "with the second copy unused; a backward-copy loop never reached; a "
   "fast-RAM probe branched over; **`PD100295.ZIP`, a PC's PKZIP 2.0 archive "
   "whose two members are the disc's own `rmenus.rnc` and `walt.rnc`**; "
   "`trashcan.inf`, a Workbench `DiskObject` (`E3 10 00 01`) with no Trashcan "
   "drawer; `dendes.bin`'s slots 0 and 1 duplicating `offneon.bit` and "
   "`fullneon.bit`; `fgbr1.rnc` listed twice in `rmenus`; the FMODE clear on a "
   "game whose art is five planes",
}
