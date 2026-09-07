# Textbook style rules

The clauses used in common by authoring, revision, and auditing. Where the "preferred style
of explanation" in the learner profile conflicts with a clause here, **the profile wins.**
What is here is the default when the profile says nothing.

The clauses below were written for a Korean-language textbook. For another language, clauses
1, 2, 6, 7, and 8 apply as written, while 3, 4, and 5 are rewritten to suit that language's
grammar.

## 1. Write in prose (the most frequently broken clause)

Terms and items laid out as bullets are a summary, not study material. Work out in sentences
why the concept became necessary, how it joins what came before, and what it leads to next.

- Use tables and lists **only to summarize what has already been explained.**
- If a section consists of two lists, that section has not been written yet.

## 2. Section titles as assertions

A noun-phrase title ("Data structures", "Performance comparison") is the language of a table
of contents. Write an assertion so that skimming the titles carries the argument ("How the
same data is held decides how fast the answer comes"). The chapter's "three key sentences"
must be **complete sentences** for the same reason — ending on a noun phrase makes a table of
contents, not a summary.

## 3. Do not write translationese

Use the word order and vocabulary of the target language rather than carrying English
sentence structure across. Where a settled native term exists for a technical word, use it
and **give the original alongside on first appearance.** Keep the original word as-is only
for terms that have no settled translation.

Signs of translationese to watch for, in any language: passive constructions where the actor
is known, nominalized verbs where a verb would do, "it is possible to X" for "X can", and
chains of prepositional phrases that a single clause would carry.

## 4. Do not let punctuation stand in for sentences

Dashes and parentheses are places for an aside, not for joining logic. Several dashes in one
paragraph mean sentences have been left unfinished. Convert as follows.

- A dash that unpacks what precedes it → a comma, or a new sentence
- A dash that joins a reason → "because", "so"
- A dash that contrasts → "whereas", "but"
- A dash carrying an aside → parentheses, or deletion

## 5. Endings and address

- Keep the body of the textbook in one register. Where addressing the learner (guidance,
  review questions) mixes with exposition, settle on one side.
- Do not address the learner specifically ("as a professor, you...", "you, an expert in X,
  ..."). This is the most common route to breaking self-standing prose.

## 6. Metaphor — separate established imagery from decoration

- **Established imagery**: a metaphor whose meaning is declared at the outset and repeated
  with the same meaning throughout the textbook. It is a teaching device that makes a concept
  graspable, so **keep it.**
- **Decorative metaphor**: rhetoric used once and dropped. Figures drawn from death, war, and
  money in particular blur the concept and only make the sentence loud. **Remove them.**

There is one test: is this metaphor used again later, and was its meaning defined somewhere?

## 7. Equations and symbols

- If the depth contract says "as far as the concept," **do not put in derivations.** Give the
  result in one line, the meaning of the symbols, and the picture the equation describes, in
  prose.
- Where three or more symbols appear, **put the definition table first** and the prose after.
  A definition buried in a sentence cannot be looked back to.
- When using a figure, say where the value came from. If it can be checked, give the check
  alongside.

## 8. Self-standing prose (the dual-audience convention)

The textbook must hold for a reader who reads only the textbook.

- Do not presume a particular learner's background ("this is your specialty so it is
  omitted").
- Do not presume the files, tools, or circumstances of a particular project. Where necessary,
  rewrite with a generic name.
- Do not use for the first time, without explanation, a term not yet explained in another
  chapter. A term appearing for the first time is unpacked in the body or sent to a groundwork
  box or a glossary.

## How to check

Clause-by-clause collation is more accurate than a person reading it through. Count what can
be counted first.

```bash
grep -o '—' textbook.html | wc -l              # dash frequency (clause 4)
grep -c '<li>' textbook.html                   # signs of list overuse (clause 1)
sed -n '/<main>/,$p' textbook.html | grep -o '#[0-9A-Fa-f]\{6\}' | wc -l   # hard-coded color in the body
```

Clauses that counting cannot catch (1, 2, 6, 8) go to the
[`textbook-auditor`](../../../agents/textbook-auditor.md) agent.
