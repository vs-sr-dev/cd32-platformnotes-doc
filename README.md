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
| 1 | Identifying the disc, why the system identifier says `CDTV`, and the three habits ISOCD leaves behind |
| 2 | **Sector 21** — the Commodore trademark block, outside the file system, and the object file after the banner |
| 3 | Timestamps: **three** epochs to recognise, and why the outliers are the finding |
| 4 | The boot chain, the `$VER:` strings, `freeanim.library`, and the one grep that decides how you read the executable |
| 5 | Compression — starting with whether there is any |
| 6 | Hunk files, toolchain fingerprints, symbol tables that survived, and data wrapped in hunk format |
| 7 | Planar geometry without a copper list, autocorrelation, palettes as an AGA test |
| 8 | Red Book, raw Paula samples, tracker modules, and in-house players found by diffing |
| 9 | Text encodings, password systems, placeholders, and reading the file *names* |
| 10 | Baselines, disc by disc, side by side |
| 11 | The order of work that worked |

Findings confirmed on every disc so far are marked **[all]**; those confirmed
on fewer are marked **[N of M]**. Everything else is named after the disc it
came from, and is the kind of thing to test rather than assume.

## Discs it is drawn from

| Disc | Year | What it is |
|---|---|---|
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |
| [Marvin's Marvellous Adventure](https://github.com/vs-sr-dev/cd32-marvinsmarvellousadventure-doc) | 1994/1995 | Infernal Byte Systems / 21st Century, DE+UK — twelve tracks, 212 files, **nothing compressed**, 61 % of the disc used, ten libraries opened and AmigaDOS alive throughout |

The two are about as unlike each other as two CD32 titles can be, which makes
the handful of things they agree on worth more than a count of two suggests.

## The question this repository was split out to answer, and its answer

**Sector 21 belongs to no file.** No directory record covers it; the only
pointer to it on the whole disc is a field in the primary volume descriptor's
application-use area that is normally empty. Every CDTV and CD32 disc has it,
because Commodore required the trademark block, and a sector map built from
the file system shows it as free space.

On Dragonstone, the Commodore copyright banner was followed by **876 bytes of
unlinked AmigaDOS object file**: compilation unit `exec`, 268 bytes of 68000
code defining `AddPort`, `GetMsg`, `PutMsg`, `FindPort`, `ReplyMsg` and
`WaitPort`, with `HUNK_SYMBOL` intact and local labels (`REMHEAD.033`,
`ENABLE.031/032/034`) that are Commodore's own Exec assembler macros expanded
by line number. The open question was whether that was one master's accident
or something Commodore shipped to every developer.

**Marvin's Marvellous Adventure has the same 2,048 bytes.** All three SHA-1s
match — whole sector, banner, object file. Different studio, different
country, different engine, master cut a month apart, and nothing in either
game reads the sector.

So the trademark block Commodore distributed was itself built by
concatenating the banner with a stale buffer, and **a fragment of the Amiga
operating system's own source has been pressed onto discs of this format,
with its debug symbols, since at least 1993**.

Two discs is not every disc. The question that replaces it is whether the
bytes ever *differ* — a 1991 CDTV title, a different mastering house, a
non-European pressing. The three hashes are in section 2 and checking them
takes thirty seconds. **A mismatch is now the interesting result.**

## Contributing from a pipeline

When a new title turns up something about the *format* rather than the title,
add it here rather than to the title's repository, mark it honestly, correct
what it contradicts in place, and update the baseline table and the order of
work. Section 11 of the notes has the full rules and the open items.
