# Contributing

**You do not need to write code to contribute.** What this kit is worth is not the number of
documents in it but the number of places where somebody followed them and found out where
they break. That only comes back from the people who used it.

## What to send

Four kinds, each with its own form under [new issue](../../issues/new/choose).

- **A clause that did not hold.** You did what a document said, and what it said would happen
  did not happen.
- **A step that was missing.** The procedure ran out before the work did, and you had to fill
  the gap yourself.
- **A trap the documents do not warn about.** You found it by stepping on it.
- **How you measured your own learning.** The kit has no retention or assessment mechanism on
  purpose — measuring the effect of study is what a teacher needs, and this kit is used by
  someone studying alone. But you are an expert in your own field, and if you decided you
  needed a way to check yourself and built one, **the method is what we want.** Not your
  results, and not your scores. This is the one route by which measurement can enter the kit
  at all.

## What not to send

**Study artifacts.** Profiles, plans, textbooks, notes, sources — they belong to you and to
your field, and the kit takes no field of study into itself. One example sentence drawn from a
particular field costs a document its reusability, which is why the forms ask for the *shape*
of what happened rather than the subject it happened in.

So describe the situation without naming your field. This is the level of detail that helps:

> A single regular expression in the normalization step silently deleted 8.5 KB of body text.
> Nothing failed and nothing warned; the only reason it was caught was a size comparison
> against the original.

What those documents were about does not belong in the report.

## You are probably not starting from a blank page

If you ran a course of study with the kit, the material is already written down.
`toolbox-log.md` holds the effects and traps you recorded as you went, and
`docs/textbook-revisions.md` holds the questions that turned into corrections. **Copy the line.
Do not write an essay.** One entry, stripped of its field, is a complete contribution.

## What happens to it

Reports are read by hand. Something hit once is a note; something hit twice, or hit by two
different people, becomes a clause in the document it belongs to. The kit's rule is that a
document earns a clause by *"we did it this way and it broke here"* — so a report of what
broke and how often is worth more than a suggestion about what would be nicer.

Accepted changes raise the version in `plugins/study-kit/.claude-plugin/plugin.json`. The
plugin cache is keyed by version, so nothing reaches an installed copy without that bump.
That version also feeds the Codex edition. Edit the shared procedures in
`plugins/study-kit/`, or the Codex adaptation in `codex/` and `scripts/build_codex.py`,
then run `python3 scripts/build_codex.py` and commit the generated
`plugins/study-kit-codex/` files too. Do not edit the generated copy directly.
See [the distribution guide](docs/distribution.md) for release checks.

Pull requests are welcome too, under the same rules as the documents themselves: no field
vocabulary anywhere, and **no procedure that has not been measured.** Do not invent traps that
were never hit.

## Two limits, stated plainly

**Sending this needs an account here.** The kit tells you to test a delivery channel on "does
it open without a login" before anything else, and this route does not pass that test. It is
the trade made for keeping everything in one place, with no third-party service and no address
to expose.

**Nothing is collected automatically.** There is no telemetry of any kind. Every line that
arrives is here because a person decided to send it.

## Licensing contributions

Submit only material you have the right to contribute under the applicable
[component license](plugins/study-kit/LICENSE): PolyForm Noncommercial 1.0.0 for
code and CC BY-NC-SA 4.0 for documents and prompts. Identify any third-party
material and its terms. Contributions do not transfer copyright to the maintainer
or automatically grant a separate commercial license.
