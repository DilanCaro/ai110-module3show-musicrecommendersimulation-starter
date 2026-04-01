# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeRank Classroom Recommender**

---

## 2. Intended Use

This system suggests **up to five songs** from a small CSV catalog for a **single user** at a time. It uses stated preferences only: favorite genre and mood, a target energy level between 0 and 1, and whether the user leans toward acoustic-sounding tracks. It is meant for **learning and demos**, not for a real product, streaming service, or any high-stakes decision.

---

## 3. How the Model Works

### Explain your scoring approach in simple language.  

Each song is described by tags and numbers from the dataset (genre, mood, energy, acousticness, plus unused extras like tempo and valence for now). The user’s profile supplies the same kinds of clues.


The model adds points when the song’s **genre** matches the user’s favorite genre and when the **mood** matches. It rewards songs whose **energy** is close to the user’s target energy: the closer the values, the larger the bonus. Finally, if the user says they like acoustic music, songs with higher acousticness score a bit better; if they do not, songs with lower acousticness score better. After every song has a total score, the system **sorts** from highest to lowest and returns the top results. A short list of “reasons” is saved next to each score so a person can see why a track ranked where it did.

---

## 4. Data

The catalog has **18** hand-authored tracks in `data/songs.csv`. Genres include pop, lofi, rock, jazz, ambient, synthwave, indie pop, metal, country, classical, reggae, hip hop, folk, and punk. Moods include happy, chill, intense, relaxed, focused, moody, and sad. The data reflect a **made-up** mix of artists and tags, not real listening logs, so it is easy to discuss but not representative of global music taste.

---

## 5. Strengths

The design is **simple and inspectable**: you can read the weights and the reason strings and predict how a song will move if you change a preference. For profiles that line up cleanly with the tags—**rock / intense**, **lofi / chill**, **pop / happy**—the top songs usually match intuition. The same scoring core powers both the CLI and the unit-tested `Recommender` class, which reduces hidden bugs.

---

## 6. Limitations and Bias

Exact **string** matching on genre hurts near-misses: **indie pop** does not count as **pop**, so a user who thinks of both as “pop” gets odd gaps. Rare moods (**sad**) leave few matches; the model then leans on **genre and energy**, which can feel like it **ignores** the mood the user named—a small “filter bubble” toward whatever genres dominate their other signals. The catalog is tiny, so **Gym Hero** and other intense pop tracks can stay high for several profiles simply because there are few alternatives at the same energy tier. If this were deployed for real users, **underrepresented** genres and non-English music would likely lose even when human listeners would enjoy them.

---

## 7. Evaluation

Testing used **four** CLI profiles: high-energy happy pop, chill acoustic-leaning lofi, intense rock, and a **conflicting** profile (high energy + **sad** mood, with almost no “sad” mood rows). I checked whether the top five matched the stated vibe and whether explanations mentioned the expected bonuses. **pytest** includes a small fixture catalog that checks the pop/happy/high-energy user gets the pop/happy track first and that `explain_recommendation` returns non-empty text.

**One quantitative-style experiment:** raising `WEIGHT_ENERGY_SIMILARITY` from **1.5** to **3.0** in code (described in the README) increases how much **energy distance** moves the list when genre ties or when mood does not match—rankings shift toward very high- or very low-energy tracks without any new listening data.

**Surprise:** After adding a **pop / sad** row (**Sad Phone Glow**), the conflicting profile finally surfaces a mood-appropriate top pick—but **Gym Hero** still trails close behind on genre and energy alone, which shows how extra catalog diversity changes outcomes without changing the formula.

---

## 8. Future Work

- Add **partial genre** matching or aliases (map indie pop → pop).
- Use **valence** or tempo bands when the user asks for “sad” or “party” vibes.
- Add a **diversity** rule so the top five cannot be five tracks from the same artist or genre.
- Log **implicit feedback** (skips, replays) in a toy simulation to show collaborative effects.

---

## 9. Personal Reflection

Building this made the phrase “it’s just math” concrete: the same dataset felt “smart” or “dumb” depending on weights and tag coverage. Using AI coding tools sped up boilerplate and edge-case brainstorming, but I still had to **check** whether mood strings in the CSV matched the profiles and whether tests encoded fair expectations. The biggest learning moment was seeing a **conflicting profile** still get plausible rankings because genre and energy outweighed a rare mood—real recommenders have the same tension when signals disagree. If I extended the project, I would prioritize fairness and diversity metrics alongside average score so “reasonable” does not always mean “mainstream repeat.”
