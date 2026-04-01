# Profile comparisons

Plain-language notes on how changing the taste profile changes the top recommendations, and why that matches the scoring rules.

## High-energy happy pop vs chill lofi (acoustic)

**What changed:** The happy-pop run favors **Sunrise City** first (pop + happy + high energy, lower acousticness when the user dislikes acoustic). The chill-lofi run favors **Library Rain** and **Midnight Coding** (lofi + chill + moderate energy + acoustic taste).

**Why it makes sense:** Genre and mood each add fixed points, so the catalog separates “party pop” from “study lofi” immediately. Energy similarity then fine-tunes inside that lane, and the acoustic flag pushes lofi listeners toward tracks with higher `acousticness`.

## High-energy happy pop vs deep intense rock

**What changed:** Pop users see **Sunrise City** and **Gym Hero** near the top; rock users see **Storm Runner** first, with **Gym Hero** appearing later because it shares **intense** mood and high energy but not the rock genre tag.

**Why it makes sense:** The **+2** genre gate is strong. Intense, high-energy pop can still rank well for rock fans as a “mood and energy” compromise, but it should not beat a true genre+mood rock match when that row exists.

## Chill lofi vs deep intense rock

**What changed:** Lofi profiles surface low-energy, chill, acoustic-leaning tracks. Rock profiles jump to **Storm Runner** and other high-energy, intense material; lofi rows fall to the bottom.

**Why it makes sense:** Both genre and mood differ, so the two profiles almost never fight for the same winner. Energy similarity reinforces that split (targets 0.4 vs 0.95).

## Edge case: high energy + “sad” mood (pop) vs high-energy happy pop

**What changed:** With **sad** mood and a **pop / sad** track in the catalog, **Sad Phone Glow** can take first place (genre + mood + reasonable energy fit). **Gym Hero** still sits near the top on **genre + energy** alone because it is a very close energy match without the sad tag. With **happy** mood, **Sunrise City** typically wins thanks to the extra mood match over **Gym Hero**.

**Why it makes sense:** The model only uses exact mood **string** equality. When no row shares that mood, genre and energy dominate and a “sad” request looks ignored—adding diverse rows is as important as tuning weights.

## Optional weight experiment (energy doubled)

**What changed:** If `WEIGHT_ENERGY_SIMILARITY` is increased, songs very close to the user’s target energy gain more ground. Profiles with **no** mood match see bigger jumps between close energy tiers.

**Why it makes sense:** Ranking is always “sum of parts.” Blowing up one part makes that dimension act like a louder voice in the meeting—similar to real products tuning engagement signals over explicit taste statements.
