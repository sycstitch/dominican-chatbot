### ### 1. One Term, Multiple Meanings, One Example (e.g., `Agentao`)

**Goal:** Explicitly associate the single example block with the correct definition.

**BEFORE (Ambiguous):**
```
10. Agentao - Arrogant
---
DEF2: Bold.
EX: "Después que compraste ese carro tú ta' muy agentao."
GS: "Después que compraste ese carro, tú estás muy arrogante."
EN: "You became very arrogant after you bought that car."
SYN: Arrogante / Atrevido
ANT: Humilde
Usage: 8/10
```

**AFTER (Manually Edited & Unambiguous):**
```
10. Agentao
DEF: Arrogant.
EX: "Después que compraste ese carro tú ta' muy agentao."
GS: "Después que compraste ese carro, tú estás muy arrogante."
EN: "You became very arrogant after you bought that car."
SYN: Arrogante / Atrevido
ANT: Humilde
Usage: 8/10
---
DEF2: Bold.
```
* **Change:** The first definition is now explicitly labeled with `DEF:`. The example block is placed directly under the first definition it belongs to.
* **Result:** It is now clear that the second definition, "Bold," has no example. The parser script will no longer have to guess.

---

### ### 2. One Term, Multiple Meanings, Multiple Examples (e.g., `Ahorita`)

**Goal:** Create two distinct definition blocks, each with its own corresponding example block.

**BEFORE (Ambiguous):**
```
11. Ahorita - In DR it could mean "later" or "a while ago", but never "right now".
EX: "Yo voy comprar comida ahorita."
GS: "Yo voy a comprar comida más tarde."
EN: "I am going to buy food later."
EX2: "Yo compré comida ahorita."
GS2: "Yo compré comida hace un rato."
EN2: "I bought food a while ago."
SYN: Mas tarde / Hace un rato
ANT:-
Usage: 10 / 10
```

**AFTER (Manually Edited & Unambiguous):**
```
11. Ahorita
DEF: Later (in the near future).
NOTE: In Dominican Spanish, this term has two distinct meanings, but neither means "right now".
EX: "Yo voy comprar comida ahorita."
GS: "Yo voy a comprar comida más tarde."
EN: "I am going to buy food later."
SYN: Mas tarde
Usage: 10/10
---
DEF2: A while ago (in the recent past).
EX2: "Yo compré comida ahorita."
GS2: "Yo compré comida hace un rato."
EN2: "I bought food a while ago."
SYN2: Hace un rato
```
* **Change:** The narrative definition is split into two clear `DEF:` and `DEF2:` blocks. The note is preserved in a `NOTE:` field. Each example block (`EX:` and `EX2:`) is placed directly under the definition it illustrates.
* **Result:** The parser can now clearly create two `meanings` objects, each with its correct definition and example set.

---

### ### 3. Multiple Terms, One Example (e.g., `Fuñirse / ...`)

**Goal:** Enforce the "One Term, One Entry" rule by splitting the entry and assigning the single example only to its correct term.

**BEFORE (Ambiguous):**
```
633. Fuñirse / Joderse / Mamarse / Bebérsela / Mascarla - To fuck up / To be in trouble.
EX: "Si tú no tiene' dinero, te la bebite porque yo no te voy a comprar na'."
GS: "Si tú no tienes dinero, estás en problemas yo no te voy a comprar nada."
EN: "If you don't have money, you fucked up because I won't buy anything for you."
...
Usage:
- Fuñirse - 7/10
- Joderse - 9/10
...
```

**AFTER (Manually Edited & Unambiguous):**
```
633. Fuñirse
DEF: To fuck up / to be in trouble.
Usage: 7/10
Level of explicitness: 2/10

634. Joderse
DEF: To fuck up / to be in trouble.
Usage: 9/10
Level of explicitness: 3/10

635. Mamarse
DEF: To fuck up / to be in trouble.
Usage: 7/10
Level of explicitness: 6/10

636. Bebérsela
DEF: To fuck up / to be in trouble.
EX: "Si tú no tiene' dinero, te la bebite porque yo no te voy a comprar na'."
GS: "Si tú no tienes dinero, estás en problemas yo no te voy a comprar nada."
EN: "If you don't have money, you fucked up because I won't buy anything for you."
Usage: 6.5/10
Level of explicitness: 0/10

637. Mascarla
DEF: To fuck up / to be in trouble.
Usage: 8/10
Level of explicitness: 0/10
```
* **Change:** The single entry is split into five separate entries. The example block is placed *only* with `Bebérsela`, the term it actually demonstrates. The specific `Usage` and `Level of explicitness` data is correctly distributed to each new entry.
* **Result:** All five terms are now distinct, unambiguous entries. Your re-numbering script will fix the sequence perfectly after this edit.



---


Of course. It's a great idea to consolidate the rules into a single checklist before you begin the full manual edit. This will ensure consistency across the entire document.

Here are the data standardization rules we've established for refactoring your `domislang.txt` file:

---

### **Rules for Standardizing `domislang.txt`**

#### I. General Entry Structure

* **One Primary Term Per Entry:** Every numbered entry must represent only **one** unique term.
    * If an entry lists multiple, lexically different words (e.g., `Bajo a boca / Tufo`), it **must be split** into separate, individually numbered entries.
* **Multiple Meanings Separator:** To represent multiple distinct meanings for a **single term**, separate each meaning block with `---` on its own line.

#### II. Term Formatting

* **Group Variants:** Terms that are simple gender (`-o`/`-a`) or minor phonetic variations of each other should be kept together in a single entry line (e.g., `Agallú / Agalludo / Agallúa / Agalluda`).
* **Standard Spelling Format:** For terms that include both a dialectal and a standard spelling, use the format `Dialectal Term(s) (Standard Term(s))`.
    * Example: `Aplatarse (Aplastarse)`
    * Example: `Aplatanao' / Aplataná (Aplatanado / Aplatanada)`

#### III. Content and Example Formatting

* **Explicit Definitions:** Every definition must start on a new line and be prefixed with `DEF:`. Subsequent definitions for the same term should be prefixed with `DEF2:`, `DEF3:`, and so on.
* **Explicit Example Placement:** Each block of examples (`EX:`, `GS:`, `EN:`) **must be placed directly under the specific `DEF:` block it illustrates**. If a definition does not have an example, it should not have an example block.
* **Contextual Notes:** Use `NOTE:` on a new line to capture important metadata, such as `NOTE: Offensive` or explanations of grammatical quirks.

#### IV. Metadata Consistency

* **Universal USAGE Score:** Every definition block (`DEF:`, `DEF2:`, etc.) **must have its own `USAGE:` line**. If an original entry has one score, it should be applied to all definitions derived from it.
* **Standard USAGE Format:** The key must be capitalized (`USAGE:`), and the value must have no spaces (`8/10`).

#### V. Guiding Principles

* **Data Authenticity:** Do not invent or fabricate examples. It is better for an entry to have no example than an inauthentic one.
* **Numbering Workflow:** Ignore the numbering sequence during your manual edits. After all content edits are complete, the `renumber_entries.py` script will be used to fix the entire sequence in one final pass.