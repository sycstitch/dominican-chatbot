### 1. "abimbao" (A Simple Entry)

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
  "meanings": [
    {
      "part_of_speech": "adjective",
      "context": "General use, describing a person's physical state after a fight or accident.",
      "definition_long": "Describes someone who has been beaten and has visible swelling or injuries as a result.",
      "definition_short": "beaten up",
      "example_dominican": "Juan y Manuel pelearon, yo no sé por qué, pero Manuel ta abimbao.",
      "example_standard_spanish": "Juan y Manuel pelearon, yo no sé por qué, pero Manuel está mal herido.",
      "example_english": "Juan and Manuel had a fight, I don't know why, but Manuel is beaten up.",
      "synonyms": ["Golpeado", "Mal herido"],
      "antonyms": []
    }
  ],
  "usage": 8,
  "usage_max": 10
}
```

---
### 2. "pámpara" (Multiple Distinct Meanings)

**BEFORE (Original Text):**
```
334. Pámpara - It can mean "cool", but also "a thing" depending on the context. It refers to something positive, something great, mostly used in the hood.
EX: "Tengo la pámpara prendía."
GS: "Yo estoy en llamas / Yo soy el major aquí / Yo tengo lo mejor aquí."
EN: "I am on fire / I am the best."

EX2: "¿Y esa pámpara?"
GS2: "¿Qué es eso?".
EN2: "What's that thing / What happened with that?"
SYN: Cosa / Asombroso / Genial
ANT:-
Usage: 7/10
```

**AFTER (Desired JSON):**
```json
{
  "term": "pámpara",
  "meanings": [
    {
      "part_of_speech": "adjective",
      "context": "Used to describe a person's state or a situation as being excellent or impressive.",
      "definition_long": "A state of being cool, 'on fire', or the best in a given situation.",
      "definition_short": "cool / on fire",
      "example_dominican": "Tengo la pámpara prendía.",
      "example_standard_spanish": "Yo estoy en llamas / Yo soy el mejor aquí / Yo tengo lo mejor aquí.",
      "example_english": "I am on fire / I am the best.",
      "synonyms": ["Asombroso", "Genial"],
      "antonyms": []
    },
    {
      "part_of_speech": "noun",
      "context": "Used informally to refer to an unspecified object or situation.",
      "definition_long": "An unspecified thing, object, or situation, often used in a question.",
      "definition_short": "a thing",
      "example_dominican": "¿Y esa pámpara?",
      "example_standard_spanish": "¿Qué es eso?",
      "example_english": "What's that thing / What happened with that?",
      "synonyms": ["Cosa"],
      "antonyms": []
    }
  ],
  "usage": 7,
  "usage_max": 10
}
```

---
### 3. "El pipo / El fuete / El gueso" (Grouped Terms)

**BEFORE (Original Text):**
```
605. El pipo / El fuete / El gueso - The following phrase is used
to express surprise, similar to "Wow" or "Dang".
EX: "¡El pipo! ¿Qué le pasó a tu carro?
GS: "Wow! ¿Qué le pasó a tu carro?"
EN: "Dang! What happened to your car?"
SYN: Wow
ANT:-
Usage:
- El pipo / El fuete - 9 / 10
- El gueso - 9 / 10 (Used more among wawawa's)
Level of explicitness: 1 / 10 (all of them)
```

**AFTER (Desired JSON - Creates *Three* Separate Objects):**
```json
[
  {
    "term": "el pipo",
    "group": "expression of surprise",
    "meanings": [
      {
        "part_of_speech": "interjection",
        "context": "Used to express surprise, similar to 'wow' or 'dang'.",
        "definition_short": "Wow! / Dang!",
        "example_dominican": "¡El pipo! ¿Qué le pasó a tu carro?",
        "example_standard_spanish": "¡Wow! ¿Qué le pasó a tu carro?",
        "example_english": "Dang! What happened to your car?",
        "synonyms": ["Wow"],
        "antonyms": []
      }
    ],
    "usage": 9,
    "usage_max": 10,
    "explicitness_level": 1,
    "explicitness_level_max": 10,
    "social_notes": "Often used interchangeably with 'el fuete'."
  },
  {
    "term": "el fuete",
    "group": "expression of surprise",
    "meanings": [
      {
        "part_of_speech": "interjection",
        "context": "Used to express surprise, similar to 'wow' or 'dang'.",
        "definition_short": "Wow! / Dang!",
        "example_dominican": "¡El fuete! ¿Qué le pasó a tu carro?",
        "example_standard_spanish": "¡Wow! ¿Qué le pasó a tu carro?",
        "example_english": "Dang! What happened to your car?",
        "synonyms": ["Wow"],
        "antonyms": []
      }
    ],
    "usage": 9,
    "usage_max": 10,
    "explicitness_level": 1,
    "explicitness_level_max": 10,
    "social_notes": "Often used interchangeably with 'el pipo'."
  },
  {
    "term": "el gueso",
    "group": "expression of surprise",
    "meanings": [
      {
        "part_of_speech": "interjection",
        "context": "Used to express surprise, similar to 'wow' or 'dang'.",
        "definition_short": "Wow! / Dang!",
        "example_dominican": "¡El gueso! ¿Qué le pasó a tu carro?",
        "example_standard_spanish": "¡Wow! ¿Qué le pasó a tu carro?",
        "example_english": "Dang! What happened to your car?",
        "synonyms": ["Wow"],
        "antonyms": []
      }
    ],
    "usage": 9,
    "usage_max": 10,
    "explicitness_level": 1,
    "explicitness_level_max": 10,
    "social_notes": "This term is noted as being used more among 'wawawa's'."
  }
]
```

---
### 4. "Hacer un serrucho" (Multi-line Dialogue Example)

**BEFORE (Original Text):**
```
476. Hacer un serrucho - When in a group, everyone contributes money for drinks, parties, or specific purchases / To collect money.
EX:
- "¿Ustedes fueron al río a beber?"
- "Si."
- "Pero tú dijiste que no tenías dinero."
- "Yo no tenía mucho dinero, pero los muchachos y yo hicimos un serrucho."
- "Ah okay."
SYN: Hacer una recolecta
Usage: 10 / 10
```

**AFTER (Desired JSON):**
```json
{
  "term": "hacer un serrucho",
  "meanings": [
    {
      "part_of_speech": "phrase",
      "context": "Used when a group of people pool their money together for a shared purchase or activity.",
      "definition_long": "The act of a group contributing money for drinks, parties, or other specific shared purchases.",
      "definition_short": "to pool money",
      "example_dominican": [
        "–¿Ustedes fueron al río a beber?",
        "–Si.",
        "–Pero tú dijiste que no tenías dinero.",
        "–Yo no tenía mucho dinero, pero los muchachos y yo hicimos un serrucho.",
        "–Ah okay."
      ],
      "example_standard_spanish": [
        "–¿Ustedes fueron al río a beber?",
        "–Sí.",
        "–Pero tú dijiste que no tenías dinero.",
        "–Yo no tenía mucho dinero, pero los muchachos y yo hicimos una recolecta.",
        "–Ah okay."
      ],
      "example_english": [
        "–Did you go to the river to drink?",
        "–Yes.",
        "–But you said you didn't have any money.",
        "–I didn't have much money, but the boys and I pooled our money.",
        "–Oh okay."
      ],
      "synonyms": ["Hacer una recolecta"],
      "antonyms": []
    }
  ],
  "usage": 10,
  "usage_max": 10
}
```

---
### 5. "Ir 'como una carretilla'" (Implicit Multiple Meanings)

**BEFORE (Original Text):**
```
477. Ir "como una carretilla" - It literally means "to go like a wheelbarrow", but in DR means "To speak fast" or "To go fast".
EX:
- "Dame tu número."
- "809876..."
- "Tú va' como una carretilla, dime otra ve', ma' al paso."
SYN: Ir rápido
ANT: Ir lento
Usage: 8/10
```

**AFTER (Desired JSON):**
```json
{
  "term": "ir como una carretilla",
  "meanings": [
    {
      "part_of_speech": "phrase",
      "context": "Describing the speed of someone's speech.",
      "definition_long": "A phrase used when someone is speaking too quickly.",
      "definition_short": "To speak very quickly",
      "example_dominican": [
        "–Dame tu número.",
        "–809876...",
        "–Tú va' como una carretilla, dime otra ve', ma' al paso."
      ],
      "example_standard_spanish": [
        "–Dame tu número.",
        "–809876...",
        "–Estás hablando muy rápido, dime otra vez, más lento."
      ],
      "example_english": [
        "–Can I have your phone number?",
        "–809876...",
        "–You are talking too fast, tell me one more time, but slower."
      ],
      "synonyms": ["Hablar rápido"],
      "antonyms": ["Hablar lento"]
    },
    {
      "part_of_speech": "phrase",
      "context": "Describing the physical speed of a person or vehicle.",
      "definition_long": "A phrase used when a person or vehicle is moving very quickly. It literally means \"to go like a wheelbarrow\".",
      "definition_short": "To go fast",
      "example_dominican": [
        "–¿Viste a ese motorista?",
        "–Sí, ¡iba como una carretilla!"
      ],
      "example_standard_spanish": [
        "–¿Viste a ese motociclista?",
        "–Sí, ¡iba muy rápido!"
      ],
      "example_english": [
        "–Did you see that motorcyclist?",
        "–Yes, he was going really fast!"
      ],
      "synonyms": ["Ir rápido"],
      "antonyms": ["Ir lento"]
    }
  ],
  "usage": 8,
  "usage_max": 10
}