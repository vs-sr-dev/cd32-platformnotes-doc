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
| 2 | **The Commodore trademark block** — outside the file system, *not* always at sector 21, and where the object file after the banner actually comes from |
| 3 | Timestamps: **four** epochs to recognise, and why the outliers are the finding |
| 4 | The boot chain, the `$VER:` strings, `freeanim.library`, and the two greps and one histogram that decide how you read the executable |
| 5 | Compression — starting with whether there is any |
| 6 | Hunk files, toolchain fingerprints, symbol tables that survived, and data wrapped in hunk format |
| 7 | Planar geometry without a copper list, interleaved versus separated, autocorrelation, palettes as an AGA test |
| 8 | Red Book, raw Paula samples, tracker modules, in-house players, and getting a headerless stream's sample rate out of the executable |
| 9 | Text encodings, password systems, placeholders, and reading the file *names* |
| 10 | Baselines, disc by disc, side by side |
| 11 | The order of work that worked |

Findings confirmed on every disc so far are marked **[all]** or **[N of N]**;
those confirmed on fewer are marked **[N of M]**. Everything else is named
after the disc it came from, and is the kind of thing to test rather than
assume.

## Discs it is drawn from

| Disc | Master | What it is |
|---|---|---|
| [Prey: An Alien Encounter](https://github.com/vs-sr-dev/cd32-prey-doc) | **1993** | KirkMoreno Multimedia / Almathera, UK+DK — one track and **no audio track at all**, 1,439 files, nothing compressed, 18 % of the disc used, an hour of speech streamed as 1,225 identical 60 KB files, and the only disc so far that genuinely uses AGA |
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |
| [Marvin's Marvellous Adventure](https://github.com/vs-sr-dev/cd32-marvinsmarvellousadventure-doc) | 1994/1995 | Infernal Byte Systems / 21st Century, DE+UK — twelve tracks, 212 files, **nothing compressed**, 61 % of the disc used, ten libraries opened and AmigaDOS alive throughout |

The three are about as unlike each other as CD32 titles can be, which makes
the handful of things they agree on worth more than a count of three suggests.

## The question this repository was split out to answer, and its answer

**The trademark block belongs to no file.** No directory record covers it; the
only pointer to it is a field in the primary volume descriptor's application-use
area that is normally empty. Every CDTV and CD32 disc has it, because Commodore
required it, and a sector map built from the file system shows it as free space.

The first ~1,100 bytes are an ASCII-art Commodore copyright banner. What
follows, at offset `0x44C`, is **876 bytes of unlinked AmigaDOS object file**:
compilation unit `exec`, 268 bytes of 68000 code defining `AddPort`, `GetMsg`,
`PutMsg`, `FindPort`, `ReplyMsg` and `WaitPort`, with `HUNK_SYMBOL` intact and
local labels (`REMHEAD.033`, `ENABLE.031/032/034`) that are Commodore's own
Exec assembler macros expanded by line number.

**All three discs have the identical 2,048 bytes** — whole sector, banner and
object file, all three SHA-1s — across three studios, three publishers, three
engines and fourteen months.

And the third disc says where they came from. **Prey ships `/CD32.TM`**: an
ordinary file in the root directory, 2,048 bytes, dated **10 June 1993**,
referenced by nothing on the disc, whose SHA-1 is the trademark sector's.

> Commodore distributed the trademark block to CD32 developers **as a file**,
> and that file already contained the fragment of Exec's source. The
> stale-buffer accident happened once, at Commodore; every disc since has
> copied the result.

Prey also corrects the section's own title. **It is not at sector 21** — it is
at LBA 6021, because that disc's volume starts at 6019, and the PVD says so.
The rule that holds is *the sector immediately after the L path table*. Read
the pointer; never assume 21.

The questions that replace it: does a CDTV title from 1991 or 1992 carry a
`CDTV.TM`, and do the bytes ever differ? Section 2 has the three hashes and
checking them takes thirty seconds. **A mismatch is now the interesting
result.**

## Contributing from a pipeline

When a new title turns up something about the *format* rather than the title,
add it here rather than to the title's repository, mark it honestly, correct
what it contradicts in place, and update the baseline table and the order of
work. Section 11 of the notes has the full rules and the open items.
