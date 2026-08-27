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
| 1 | Identifying the disc, why the system identifier says `CDTV`, and the three ISOCD habits — now with a **non-ISOCD disc** to check them against |
| 2 | **The `.TM` block** — outside the file system, *not* always at sector 21, not always 2,048 bytes, and **not the same artefact on CDTV as on CD32** |
| 3 | Timestamps: **four** epochs to recognise, and why the outliers are the finding |
| 4 | The boot chain, the `$VER:` strings, `freeanim.library`, and the two greps and one histogram that decide how you read the executable |
| 5 | Compression — starting with whether there is any |
| 6 | Hunk files, toolchain fingerprints, symbol tables that survived, and data wrapped in hunk format |
| 7 | Planar geometry without a copper list, interleaved versus separated, autocorrelation, HAM6 in a CDXL, and the **corrected** palette test |
| 8 | Red Book, raw Paula samples, tracker modules, in-house players, and getting a headerless stream's sample rate out of the executable |
| 9 | Text encodings, password systems, placeholders, and reading the file *names* |
| 10 | Baselines, disc by disc, side by side |
| 11 | The order of work that worked — ending with **diff the other release of the same game** |

Findings confirmed on every disc so far are marked **[all]** or **[N of N]**;
those confirmed on fewer are marked **[N of M]**. Everything else is named
after the disc it came from, and is the kind of thing to test rather than
assume.

## Discs it is drawn from

| Disc | Master | What it is |
|---|---|---|
| [Prey: An Alien Encounter, CD32](https://github.com/vs-sr-dev/cd32-prey-doc) | **1993** | KirkMoreno Multimedia / Almathera, UK+DK — one track and **no audio track at all**, 1,439 files, nothing compressed, 18 % of the disc used, an hour of speech streamed as 1,225 identical 60 KB files, and the only disc so far that genuinely uses AGA |
| [Prey: An Alien Encounter, **CDTV**](https://github.com/vs-sr-dev/cd32-prey-doc/blob/main/docs/09-cdtv-1992.md) | **1992** | The same game a year earlier. **The first disc here not mastered with ISOCD**, the first CDTV title, the oldest master, and the control that corrected two claims about the others. 1,453 files, **1,201 of them byte-identical to the CD32 release** |
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |
| [Marvin's Marvellous Adventure](https://github.com/vs-sr-dev/cd32-marvinsmarvellousadventure-doc) | 1994/1995 | Infernal Byte Systems / 21st Century, DE+UK — twelve tracks, 212 files, **nothing compressed**, 61 % of the disc used, ten libraries opened and AmigaDOS alive throughout |

The first three are about as unlike each other as CD32 titles can be, which
makes the handful of things they agree on worth more than a count of three
suggests. The fourth is not an independent sample at all — it is the *same
game* on the previous console — and that is exactly why it is the most useful
disc here: it is the only one that could show that something already written
down was wrong.

**Two things were.** A block of 1,213 timestamps read as a dead clock battery
turned out to be a real build date inherited from the CDTV master, and a
palette test that looked for one way of writing a 4-bit value into a byte
scored every ECS palette on the CDTV disc as 24-bit colour. Both are corrected
in place and marked as corrections.

## The question this repository was split out to answer, and its answers

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

**All three CD32-era discs have the identical 2,048 bytes** — whole sector,
banner and object file, all three SHA-1s — across three studios, three
publishers, three engines and fourteen months.

And the third of them says where they came from. **Prey's CD32 master ships
`/CD32.TM`**: an ordinary file in the root directory, 2,048 bytes, dated
**10 June 1993**, referenced by nothing on the disc, whose SHA-1 is the
trademark sector's.

> Commodore distributed the trademark block to CD32 developers **as a file**,
> and that file already contained the fragment of Exec's source. The
> stale-buffer accident happened once, at Commodore; every disc since has
> copied the result.

**Then the CDTV release of the same game showed that the block is not the same
artefact on both consoles.** Same pointer, same `'TM'` tag, same constant —
and it points at **22,152 bytes at LBA 48,621**, with **no Commodore
trademark banner anywhere on the disc**. What is there is `/CDTV.TM`:

```
cdtv 35.2 (6.2.91)
CDTV Device Driver
Copyright (c) 1990, Commodore-Amiga, Inc.
Created by Carl Sassenrath, Ukiah CA
```

The CDTV device driver, by the designer of AmigaOS's Exec kernel, in the block
the format reserves. So:

> Every CDTV and CD32 disc carries a `.TM` file and a pointer to it in the
> volume descriptor. **What is in that file depends on the console** — and the
> `exec` fragment is therefore a **CD32-era** accident, from before June 1993,
> not something the format has carried since 1991.

It also killed two positional rules this document had written down. **It is
not at sector 21** (Prey CD32 puts it at 6021), and it is **not always the
sector after the L path table** (the CDTV master's path tables are at 48,633
and the block is at 48,621). Find the `'TM'` tag, read the length and the LBA
after it, and dump exactly that. Never compute the position.

The questions that replace it: **which tool mastered the CDTV disc** — it
signs nothing — and is `CDTV.TM` always this same driver build? Section 2 has
the three CD32 hashes and checking them takes thirty seconds. **A mismatch is
still the interesting result.**

## Contributing from a pipeline

When a new title turns up something about the *format* rather than the title,
add it here rather than to the title's repository, mark it honestly, correct
what it contradicts in place, and update the baseline table and the order of
work. Section 11 of the notes has the full rules and the open items.

And if the title exists on more than one Amiga CD format, **document both and
diff them byte for byte**. It is now step 15 of the order of work, and it is
the only step that has ever caught this document being wrong.
