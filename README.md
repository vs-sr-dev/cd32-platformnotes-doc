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
| 2 | **The `.TM` block** — outside the file system, *not* always at sector 21, not always 2,048 bytes, and **not determined by the console either** |
| 3 | Timestamps: **five** epochs to recognise, why the outliers are the finding, and checking the descriptor's date against the files it indexes |
| 4 | The boot chain, the `$VER:` strings, `freeanim.library`, and the two greps and one histogram that decide how you read the executable |
| 5 | Compression — starting with whether there is any, then **RNC, the Imploder and Bytekiller**, why **a magic scan that finds nothing proves nothing**, and getting the decruncher out of the loader |
| 6 | Hunk files, toolchain fingerprints, symbol tables that survived, and data wrapped in hunk format |
| 7 | Planar geometry without a copper list, interleaved versus separated, autocorrelation, HAM6 in a CDXL, the **corrected** palette test, and a disc that answers the AGA question **twice** |
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
| [Prey: An Alien Encounter, CD32](https://github.com/vs-sr-dev/cd32-prey-doc) | **1993** | KirkMoreno Multimedia / Almathera, UK+DK — one track and **no audio track at all**, 1,439 files, nothing compressed, 18 % of the disc used, an hour of speech streamed as 1,225 identical 60 KB files, and the first disc here that genuinely uses AGA |
| [Prey: An Alien Encounter, **CDTV**](https://github.com/vs-sr-dev/cd32-prey-doc/blob/main/docs/09-cdtv-1992.md) | **1992** | The same game a year earlier. **The first disc here not mastered with ISOCD**, the first CDTV title, the oldest master, and the control that corrected two claims about the others. 1,453 files, **1,201 of them byte-identical to the CD32 release** |
| [The Speris Legacy](https://github.com/vs-sr-dev/cd32-thesperislegacy-doc) | **1996** | Binary Emotions / Team 17, UK — the newest dated master here and the smallest disc: one track, **0.74 % of a CD**, 47 files, 35 of them Imploder-crunched, 24-bit AGA palettes in every level. **The disc that showed the `.TM` rule was wrong** |
| [Dragonstone](https://github.com/vs-sr-dev/cd32-dragonstone-doc) | 1994/1995 | Core Design, UK — an Amiga floppy game ported to CD32: two tracks, 91 files, 84 RNC-crunched, 3 % of the disc used, no OS involvement after the first stage |
| [Marvin's Marvellous Adventure](https://github.com/vs-sr-dev/cd32-marvinsmarvellousadventure-doc) | 1994/1995 | Infernal Byte Systems / 21st Century, DE+UK — twelve tracks, 212 files, **nothing compressed**, 61 % of the disc used, ten libraries opened and AmigaDOS alive throughout |
| [Legends](https://github.com/vs-sr-dev/cd32-legends-doc) | **1996** | Krisalis Software / Guildhall, UK — one data track and **twenty-eight audio tracks**, 111 files, **89.4 % of the disc used and only 0.72 % of it by the game**, a six-floppy A1200 release copied onto a CD with its hard-disk installer still on it, and 79 files packed by a cruncher with **no magic number at all** |

These are about as unlike each other as Amiga CD titles can be — 1992 to 1996,
0.74 % of a disc to 89.4 % of one, 47 files to 1,453 — which makes the handful
of things they agree on worth more than the count suggests. And the two 1996
discs are the sharpest pair: Speris and Legends have games of almost exactly
the same size, and one of them fills the rest of the CD with music while the
other leaves 99 % of it empty.

**And the discs that corrected this document are the ones worth having.** The
CDTV Prey master is not an independent sample at all: it is the *same game* on
the previous console, which is exactly why it could show that two things
already written down were wrong. A block of 1,213 timestamps read as a dead
clock battery turned out to be a real build date inherited from that master,
and a palette test that looked for only one way of writing a 4-bit value into
a byte scored every ECS palette on it as 24-bit colour.

**Then Speris corrected the correction, and Legends corrected section 5.** A
scan for every compression magic this document knew returned nothing on a disc
where 79 of 111 files are packed, because the container has no magic number at
all. Four of these things are marked as corrections in place, and they are more
useful than the claims they replaced.

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

**Four of the five CD32-era discs have the identical 2,048 bytes** — whole
sector, banner and object file, all three SHA-1s — across four studios, four
publishers, four engines and thirty-eight months.

And the third of them says where they came from. **Prey's CD32 master ships
`/CD32.TM`**: an ordinary file in the root directory, 2,048 bytes, dated
**10 June 1993**, referenced by nothing on the disc, whose SHA-1 is the
trademark sector's.

> Commodore distributed the trademark block to CD32 developers **as a file**,
> and that file already contained the fragment of Exec's source. The
> stale-buffer accident happened once, at Commodore; every disc since has
> copied the result.

**Then the CDTV release of the same game showed that the block is not the same
artefact on both consoles — and a fourth CD32 disc then showed it is not the
console that decides.** Same pointer, same `'TM'` tag, same constant —
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

It also killed two positional rules this document had written down. **It is
not at sector 21** (Prey CD32 puts it at 6021), and it is **not always the
sector after the L path table** (the CDTV master's path tables are at 48,633
and the block is at 48,621). Find the `'TM'` tag, read the length and the LBA
after it, and dump exactly that. Never compute the position.

At that point the conclusion here was that the block's contents depend on the
console. **They do not.**

### The correction: a CD32 disc carrying the CDTV driver

**The Speris Legacy is a CD32 disc, cut with ISOCD 1.04 on 10 January 1996,
and its `.TM` block is 22,152 bytes of `cdtv.device` 35.2** — SHA-1
`fd3e764e6393974dea05612909e25ddb2124eb8b`, **byte for byte the `/CDTV.TM` of
the 1992 CDTV Prey master**, three and a half years and one console away.
There is no Commodore banner anywhere on it, and nothing on the disc ever
reads the block.

> Commodore shipped developers a `.TM` file per console. ISOCD copies the
> bytes it is handed into the reserved area and writes the length and LBA into
> the descriptor; it does not know or care which file it got. **The `.TM`
> block is whatever the person cutting the master fed to the tool** — not a
> property of the console, and not a property of the format.

Which downgrades the identical CD32 hashes from evidence about the format to
evidence about **how widely one particular file circulated**. That is still
worth recording, and section 2 keeps all the hashes, because a mismatch is
still the interesting result — **this was the first, and it took four discs to
find it.**

The question that replaces it: **how often does this happen?** One CD32 disc
with the CDTV block makes it possible; a second would make it a habit. Legends
is not it — it carries the Commodore banner, so the score stands at **four to
one**. And still open from before: **which tool mastered the CDTV disc?** It
signs nothing.

**The same mechanism turns out to cover more than the `.TM` block.** Legends'
`c/SetPatch` is byte for byte Marvin's — SHA-1
`4d4aae988310b07726329e436b2250c0f769ddff`, 7,364 bytes, two studios, two
publishers, two years. Commodore's system files circulated as single copies
and studios passed them around, so **hash the binaries in `c/`, not only their
`$VER:` strings**.

## Contributing from a pipeline

When a new title turns up something about the *format* rather than the title,
add it here rather than to the title's repository, mark it honestly, correct
what it contradicts in place, and update the baseline table and the order of
work. Section 11 of the notes has the full rules and the open items.

And if the title exists on more than one Amiga CD format, **document both and
diff them byte for byte**. It is now step 15 of the order of work, and it is
the only step that has ever caught this document being wrong.
