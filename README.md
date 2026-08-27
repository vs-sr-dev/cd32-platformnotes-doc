# cd32-platformnotes-doc

**The canonical Amiga CD32 / CDTV platform checklist**, carried from one
documentation pipeline to the next and added to by each.

→ **[cd32-platform-notes.md](cd32-platform-notes.md)**

Each Amiga CD title I document produces two things: a repository about that
disc, and whatever it taught me about the *format*. The second kind of finding
does not belong to any one title, and keeping a copy of it in every pipeline is
a recipe for three copies that disagree. This repository is the single copy.
Pipelines link here rather than fork it.

## What it covers

A working checklist for opening an unfamiliar CD32 or CDTV disc: what to look
at first, what the numbers should be, which traps cost real time, and what is
measured versus what is inferred.

| Section | |
|---|---|
| 1 | Identifying the disc, why the system identifier says `CDTV`, and what the mastering tool leaves behind |
| 2 | **Sector 21** — the Commodore trademark block, outside the file system, and what follows the banner |
| 3 | Directory timestamps, the AmigaDOS epoch, and reading the build session out of them |
| 4 | The boot chain, the `$VER:` strings, and the two greps that say how a loader reaches the CD |
| 5 | RNC ProPack: header, the method-1 bit stream, zlib as a diagnostic, fixed unpacked sizes |
| 6 | Hunk executables, toolchain fingerprints, custom overlay headers, and the loader's file table |
| 7 | Copper lists, interleaved planar bitmaps, `FMODE`, chip-RAM images, finding geometry with no header |
| 8 | Red Book tracks, raw Paula samples, tracker modules |
| 9 | Text encodings — and why CP437 on an Amiga is a finding — control codes, comparing language files |
| 10 | Baselines, disc by disc |
| 11 | The order of work that worked |

Findings confirmed on every disc so far are marked **[all]**; those confirmed
on fewer are marked **[N of M]**. Everything else is named after the disc it
came from, and is the kind of thing to test rather than assume. With one disc
covered, that is currently almost all of it — the marks are here so the second
pipeline has somewhere to put its answers.

## Discs it is drawn from

| Disc | Year | What it is |
|---|---|---|
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, and no OS involvement at all after the first stage |

## The result that made this repository worth splitting out

**Sector 21 belongs to no file.** No directory record covers it; the only
pointer to it on the whole disc is a field in the primary volume descriptor's
application-use area that is normally empty. Every CDTV and CD32 disc has it,
because Commodore required the trademark block, and a sector map built from the
file system shows it as free space.

On the one disc opened so far, the Commodore copyright banner is followed by
**876 bytes of unlinked AmigaDOS object file**: compilation unit `exec`, 268
bytes of 68000 code defining `AddPort`, `GetMsg`, `PutMsg`, `FindPort`,
`ReplyMsg` and `WaitPort`, with `HUNK_SYMBOL` intact and local labels
(`REMHEAD.033`, `ENABLE.031/032/034`) that are Commodore's own Exec assembler
macros expanded by line number. Commodore's message-port source, compiled and
pressed onto a game disc in 1994.

Either the trademark block Commodore handed to developers was itself built by
concatenating the banner with a stale buffer — in which case a piece of the
Amiga operating system has been pressed onto discs of this format for years and
nobody has said so — or it is specific to one master. **Checking a new disc
against the three SHA-1s in section 2 is a thirty-second job**, and it is
exactly the kind of question that has to live in one place to ever get
answered.

## Contributing from a pipeline

When a new title turns up something about the *format* rather than the title,
add it here rather than to the title's repository, mark it honestly, correct
what it contradicts in place, and update the baseline table and the order of
work. Section 11 of the notes has the full rules and the open items.
