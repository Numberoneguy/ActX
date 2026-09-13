# ActX Tab Placeholders
`ActX` tab placeholders (Eaglercraft 1.8.8).

---

## position and yes

* `%x%` – player's x coordinate (integer)
* `%y%` – player's y coordinate (integer)
* `%z%` – player's z coordinate (integer)
* `%x1%` – player's x coordinate (3 decimals, e.g., `124.532`)
* `%y1%` – player's y coordinate (3 decimals)
* `%z1%` – player's z coordinate (3 decimals)
* `%coords%` – player's x, y, and z coordinates formatted together as integers
* `%coords_exact%` – player's x, y, and z coordinates formatted together with 3 decimals
* `%facing%` – 16-point direction (local `actx.direction.*`)

---

## world and le eco

* `%dimension%` – current dimension name or id
* `%world%` – dimension name player is currently in
* `%day%` – day phase (local `actx.day.phase.*`)
* `%biome%` – biome name at player position
* `%weather%` – current world weather state (`Storm`, `Rain`, or `Clear`)
* `%difficulty%` – world difficulty setting name
* `%player_count_dimension%` – total players currently in the player's current dimension

---

## player stats (including combats)

* `%player%` – player's username
* `%display_name%` – player's formatted display name
* `%gamemode%` – player's current gamemode name
* `%health%` – player health
* `%max_health%` – maximum health
* `%hp%` – alias of `%health%`
* `%max_hp%` – alias of `%max_health%`
* `%absorption%` – absorption hearts amount
* `%food%` – food level
* `%hunger%` – alias of `%food%`
* `%armor%` – total armor defense value
* `%xp%` – current experience level
* `%xp_level%` – alias of `%xp%`
* `%xp_progress%` – experience progress percentage towards next level
* `%potions%` – list of active potion effects with levels or `None`
* `%mob_kills%` – total mob kills count
* `%player_kills%` – total player kills count
* `%deaths%` – total death count

---

## scoreboard and the teams

* `%team%` – formatted player name with team prefix and suffix
* `%team_name%` – registered internal team name or `???` if none
* `%prefix%` – team color prefix string
* `%suffix%` – team color suffix string
* `%is_op%` – operator status as `Operator` or `Visitor`
* `%is_op1%` – operator status with symbol (`✦` or `✖`)

---

## oijrtfjoritio

* `%online%` – total online players on server
* `%max_players%` – maximum player limit
* `%online_ratio%` – online players formatted with max limit (`online/max`)
* `%slots_left%` – remaining open player slots on server
* `%ping%` – server connection latency
* `%tps%` – server ticks per second formatted to 2 decimals (old versions only have one decimal)
* `%uptime%` – server total uptime duration
* `%host%` – server owner or host name
* `%animation:<id>%` – custom animated text frame placeholder (make on yourself at Options --> ACT --> Animation Stuffs)
