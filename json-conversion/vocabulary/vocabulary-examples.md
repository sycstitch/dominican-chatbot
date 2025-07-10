### Master JSON Structure with Examples

This document outlines the final data structure for each term in the knowledge base. It is designed to be both robust and clean, following two main principles:

1.  **The "One Term, One Object" Rule:** Every top-level object in the JSON array represents one unique word or phrase. Grouped entries from the source text must be split into individual objects. (Refer to second example in this document.)
2.  **Core vs. Specialist Keys:** To avoid clutter, the schema is divided into two types of keys:
    * **Core Keys:** These are fundamental attributes that **must** be present in every single entry, even if their value is an empty array `[]`. This ensures the data has a consistent, predictable shape. Core keys include: `term`, `tags`, `usage`, `usage_max`, `meanings`.
    * **Specialist Keys:** These are optional keys for rare metadata. They should **only** be included in an entry if they contain relevant data. This keeps the file clean. Specialist keys include: `etymology`, `explicitness_level`, `social_notes`, and `regional_variants`.

### Key-Value Pair Glossary

This is the dictionary for our data model, explaining what each key represents.

* **`term` (string):** The unique, primary word or phrase being defined. This is the main identifier for the object.
* **`tags` (array of strings):** Used for classification. Values can include parts of speech (`noun`, `adjective`, `phrase`), categories (`animal`, `food`, `anatomy`), and content warnings (`offensive`, `profanity`).
* **`usage` (number):** The commonality score of the term, taken from the source data.
* **`usage_max` (number):** The maximum possible value for the usage score (typically 10).
* **`meanings` (array of objects):** The core data payload. It's an array to allow for multiple distinct meanings for a single term. Each object inside contains:
    * **`context` (string):** A brief explanation of the situation or context in which this specific meaning is used.
    * **`definition_long` (string):** The full, descriptive definition of the term for this meaning.
    * **`definition_short` (string):** A concise, one-or-two-word gloss of the meaning.
    * **`example_dominican` (string or array of strings):** An example sentence or dialogue using the term. An array is used for dialogues.
    * **`example_standard_spanish` (string or array of strings):** The equivalent example in standard Spanish.
    * **`example_english` (string or array of strings):** The English translation of the example.
    * **`synonyms` (array of objects):** A list of equivalent terms. Each object has two keys: `term` (the synonym itself) and `dialect` (its origin, e.g., "Standard Spanish", "Puerto Rico").
    * **`antonyms` (array of strings):** A list of terms with the opposite meaning.
* **`etymology` (object):** A **Specialist Key** used only when a term has a known origin. Contains:
    * **`original_word` (string):** The source word from which the term was derived (e.g., "Full jean").
    * **`notes` (array of strings):** A narrative description of the term's historical origin.
* **`explicitness_level` & `explicitness_level_max` (number):** **Specialist Keys** used only for profane or sensitive terms to score their intensity.
* **`social_notes` (string):** A **Specialist Key** for interesting social or cultural trivia about the term's usage (e.g., "Used more among wawawa's").
* **`regional_variants` (array of objects):** A **Specialist Key** reserved for future use to document true *lexical* variants (different words for the same thing) used in *specific* regions *within* the Dominican Republic.

---
### 1. The Base Structure (Simple Entry)
This example for `abimbao` demonstrates the core structure that every entry must follow.

**BEFORE (Original Text):**
```
1. Abimbao - This term describes someone who has just been beaten and has visible swelling as a result / beaten up.
EX: "Juan y Manuel pelearon, yo no sé por qué, pero Manuel ta abimbao."
GS: "Juan y Manuel pelearon, yo no sé por qué, pero Manuel está mal herido."
EN: "Juan and Manuel had a fight, I don't know why, but Manuel is beaten up."
SYN: Golpeado / Mal herido
ANT:-
Usage: 8 / 10
```

**AFTER (Desired JSON):**
```json
{
  "term": "abimbao",
  "tags": ["adjective"],
  "usage": 8,
  "usage_max": 10,
  "meanings": [
    {
      "context": "General use, describing a person's physical state after a fight or accident.",
      "definition_long": "Describes someone who has been beaten and has visible swelling or injuries as a result.",
      "definition_short": "beaten up",
      "example_dominican": "Juan y Manuel pelearon, yo no sé por qué, pero Manuel ta abimbao.",
      "example_standard_spanish": "Juan y Manuel pelearon, yo no sé por qué, pero Manuel está mal herido.",
      "example_english": "Juan and Manuel had a fight, I don't know why, but Manuel is beaten up.",
      "synonyms": [
        { "term": "Golpeado", "dialect": "Standard Spanish" },
        { "term": "Mal herido", "dialect": "Standard Spanish" }
      ],
      "antonyms": []
    }
  ]
}
```
**Key Pairs Explained (for this example):**
* This entry demonstrates the **Core Schema**. All keys present are Core Keys that must exist in every object.
* The `meanings` array contains only one object, as "abimbao" has only one primary meaning.
* The `synonyms` key is structured as an array of objects, correctly classifying "Golpeado" and "Mal herido" as `Standard Spanish` dialect terms.

---
### 2. Handling Etymology & Grouped Terms
This example for `fullín` shows how to use a Specialist Key (`etymology`) and how to correctly apply the "One Term, One Object" rule.

**BEFORE (Original Text):**
```
200. Fullín / Fundillo / Fuí - Butt.
History: The U.S. Marines who occupied the Dominican Republic in the first intervention in 1916, saw the voluptuous Dominican women
wearing tight jeans, so they would say: "Wow, what a full jean"
Original word: Full jean
EX: "Tienes el fullín sucio."
GS: "Tienes el tresero sucio."
EN: "You have dirt on your butt."
SYN: Trasero
ANT:-
Usage: 7/10
```

**AFTER (Desired JSON - Creates *Three* Separate Objects):**
```json
[
  {
    "term": "fullín",
    "tags": ["noun", "anatomy", "profanity"],
    "usage": 7, "usage_max": 10,
    "etymology": {
      "original_word": "Full jean",
      "notes": ["Derived from the phrase \"full jean,\" supposedly used by U.S. Marines during the 1916 occupation to describe women in tight jeans."]
    },
    "meanings": [{
      "context": "Refers to a person's buttocks, often used informally.",
      "definition_short": "Butt / Buttocks",
      "example_dominican": "Tienes el fullín sucio.",
      "example_standard_spanish": "Tienes el trasero sucio.",
      "example_english": "You have dirt on your butt.",
      "synonyms": [
        { "term": "fundillo", "dialect": "Dominican" },
        { "term": "fuí", "dialect": "Dominican" },
        { "term": "trasero", "dialect": "Standard Spanish" }
      ],
      "antonyms": []
    }]
  },
  {
    "term": "fundillo",
    "tags": ["noun", "anatomy", "profanity"],
    "usage": 7, "usage_max": 10,
    "meanings": [{
      "context": "Refers to a person's buttocks, often used informally.",
      "definition_short": "Butt / Buttocks",
      "synonyms": [
        { "term": "fullín", "dialect": "Dominican" },
        { "term": "fuí", "dialect": "Dominican" },
        { "term": "trasero", "dialect": "Standard Spanish" }
      ],
      "antonyms": []
    }]
  },
  {
    "term": "fuí",
    "tags": ["noun", "anatomy", "profanity"],
    "usage": 7, "usage_max": 10,
    "meanings": [{
      "context": "Refers to a person's buttocks, often used informally.",
      "definition_short": "Butt / Buttocks",
      "synonyms": [
        { "term": "fullín", "dialect": "Dominican" },
        { "term": "fundillo", "dialect": "Dominican" },
        { "term": "trasero", "dialect": "Standard Spanish" }
      ],
      "antonyms": []
    }]
  }
]
```
**Key Pairs Explained (for this example):**
* The single `BEFORE` entry was correctly split into **three separate objects** for `fullín`, `fundillo`, and `fuí`.
* The `etymology` object is included as a **Specialist Key** only in the `fullín` entry, as the origin story applies specifically to that term.
  * Check: if chatbot can track the etymology of 'fundillo' and 'fuí' back to 'fullín'.

---
### 3. Handling Tags & Content Warnings
This example for `bembú` shows how to use specialist keys to flag sensitive content.

**BEFORE (Original Text):**
```
46. Bembú - A person with big lips.
(Offensive)
EX: "Él es bembú."
GS: "El tiene labios grandes."
EN: "He has big lips."
SYN: De labio grandes
ANT:-
Usage: 9/10
```

**AFTER (Desired JSON):**
```json
{
  "term": "bembú",
  "tags": ["noun", "offensive", "anatomy"],
  "usage": 9, "usage_max": 10,
  "explicitness_level": 5, "explicitness_level_max": 10,
  "meanings": [{
    "context": "A derogatory term for a person with large lips.",
    "definition_long": "An offensive term used to describe a person with large lips.",
    "definition_short": "A person with big lips",
    "example_dominican": "Él es bembú.",
    "example_standard_spanish": "El tiene labios grandes.",
    "example_english": "He has big lips.",
    "synonyms": [
      { "term": "De labios grandes", "dialect": "Standard Spanish" }
    ],
    "antonyms": []
  }]
}
```
**Key Pairs Explained (for this example):**
* The `tags` array now includes the `"offensive"` tag, allowing the chatbot logic to identify and handle this term with care.
* The `explicitness_level` **Specialist Key** is added to provide a quantifiable measure of the term's intensity, since it is sensitive.

---
### 4. Handling Regional & Phonetic Variants

#### 4a. Lexical Variants (Future-Proofing)
While no perfect example of a purely regional *lexical* variant was found, the `regional_variants` key is reserved for this purpose to make the model future-proof.

**Example Scenario:**
If a future term `carro` had a known variant `coche` used *only* in the Cibao region of DR, it would be structured like this:
```json
{
  "term": "carro",
  "tags": ["noun", "vehicle"],
  "regional_variants": [
    { "term": "coche", "region": "Cibao" }
  ],
  "meanings": [ ... ]
}
```
**Key Pairs Explained (for this example):**
* The `regional_variants` **Specialist Key** is reserved for true lexical variants—different words for the same concept—that are tied to a specific geographic region *within* the Dominican Republic.

#### 4b. Phonetic Variants (Handled by Logic, NOT Data)
This shows the correct way to handle predictable spelling changes—by **omitting** them from the data, as they will be handled by the application's code.

**BEFORE (Original Text):**
```
154. Cuarto (Sourthern Region) - Cualto (Eastern Region)- Cuaito (Northern Region) - Money.
EX: "No tengo cualto."
GS: "No tengo dinero."
EN: "I have no money."
SYN: Dinero
ANT:-
Usage: 10 / 10
```
**AFTER (Desired JSON - Notice no variants are listed):**
```json
{
  "term": "cuarto",
  "tags": ["noun", "money"],
  "usage": 10, "usage_max": 10,
  "meanings": [{
    "context": "General term for money.",
    "definition_short": "Money",
    "example_dominican": "No tengo cuarto.",
    "example_standard_spanish": "No tengo dinero.",
    "example_english": "I have no money.",
    "synonyms": [
      { "term": "Dinero", "dialect": "Standard Spanish" }
    ],
    "antonyms": []
  }]
}
```
**Key Pairs Explained (for this example):**
* The **intentional omission** of the `regional_variants` key here is the key takeaway. Predictable phonetic shifts like `cuarto` -> `cualto` are not data; they are logical rules that the application code will handle during user input normalization.