# HUMAN_QUERY_PROTOCOL

Purpose:
turn deep P/A/E archaeology into useful human answers without losing truth.

## Step 1 — identify the human question

Examples:
- "Зачем P2?"
- "Почему A3 нужен, если есть A2?"
- "P5 сейчас работает?"
- "Что было до A-Ultra?"
- "Почему A0 то ведёт в E0, то в A1?"
- "Кто реально хранит правду?"
- "Что сейчас активное?"

Do not immediately answer from memory if durable recovery evidence exists.

## Step 2 — determine required depth

### HUMAN_SIMPLE
Use when the user asks for a plain explanation.

Output:
one short metaphor or causal sentence first.

Example:
"P2 — это слой, который превращает крупную причинную карту P1 в достаточно мелкие шаги для дальнейшей сборки."

### HUMAN_HISTORY
Use when the user asks "как дошли до этого?".

Output:
timeline with 3–7 meaningful transitions.

### ENGINEERING_DEEP
Use when exact contracts, packet names, versions or authority boundaries matter.

Output:
source refs, versions, route/status labels.

## Step 3 — answer in layers

Preferred order:

1. ONE-LINE HUMAN ANSWER
2. WHY IT EXISTS
3. HOW IT EVOLVED
4. WHAT IT MAY / MAY NOT DO
5. CURRENT EVIDENCE STATUS
6. IMPORTANT UNKNOWN OR CONFLICT
7. optional technical depth

## Step 4 — never hide uncertainty

Use:
- "мы точно знаем..."
- "исторически было..."
- "похоже по evidence..."
- "это пока HOLD..."
- "этого мы пока не знаем..."

Do not use:
- invented certainty;
- "очевидно" where evidence is partial;
- percentages as truth unless they are clearly recovery-confidence estimates.

## Step 5 — distinguish existence from activation

When asked "есть ли канал?":
answer existence separately from activation.

Example:
"P5 существует и хорошо восстановлен исторически, но его current default state recovered as disabled unless explicitly enabled."

## Step 6 — distinguish local from global

When one channel says "latest/current" but another later channel contradicts it:

say:
"Это current/local truth внутри этой ветки/эпохи. Глобальный current требует reconciliation."

Do not silently pick a winner.

## Step 7 — human language first

Do not begin with packet IDs unless the question asks for them.

Translate:
admissibility authority
→ "кто имеет право сказать: материал уже достаточно законен/доказан, чтобы нести дальше?"

Translate:
sealed handoff
→ "нотариально упакованный переход без права переписать смысл."

Translate:
source-bound ladder
→ "лестница мелких шагов, каждый из которых знает, откуда он взялся."
