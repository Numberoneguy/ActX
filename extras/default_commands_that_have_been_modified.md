# ActX Modified Default Commands
*Modified default commands and custom gamerules for ActX (Eaglercraft 1.8.8)*

Below is the list of modified vanilla commands and custom gamerules available in ActX to give you more control on your world.

---

## Scoreboard command options

* **Placeholders:** Expanded scoreboard objectives to support placeholders directly within the sidebar.
* **Team Prefixes & Suffixes:** Added support for server-style team prefixes and suffixes.
* **Dummy Scores with Spaces:** Enabled dummy entries containing spaces for objective lists (requires setting a score to function as a placeholder).

### Command Reference & Usage

> **Note:** Color codes using & are fully supported in strings and automatically convert to section symbols (§).

#### Managing Team Prefixes and Suffixes
```text
/scoreboard teams option <team_name> prefix <string>
/scoreboard teams option <team_name> suffix <string>
```
#### Setting a Placeholder Objective Score
```text
/scoreboard players set "&7&oWelcome, &a%online%&7&o!" <objective> <score>
```
---

## Game Rules

Manage game rules in-game using this basic thing o algo.
```text
/gamerule <rule> <value>
```
### Gamerules with new gamerulleesssss

* **announceJoin** (default: true)
  Toggles join messages when players enter the world. Set to false for quieter notifications.
* **announceLeave** (default: true)
  Toggles leave messages when players exit the world. Set to false for quieter notifications.
* **announceAdvancements** (default: true)
  Toggles global chat broadcasts when a player unlocks an advancement.
* **allowHunger** (default: true)
  Toggles the hunger mechanism. Set to false to prevent players from losing saturation or hunger.
  > Note on allowHunger: If players have already lost hunger/saturation when set to false, their hunger bar will immediately refill.
* **respawnRadius** (default: 16)
  Defines the maximum block distance around the spawn point where players can randomly respawn.
* **spawnProtectionRadius** (default: 16)
  Defines the block radius protected around the world spawn point.
* **pvp** (default: true)
  Toggles player vs player combat damage. Set to false to keep players in survival mode without PvP combat.
* **WorldEdit** (default: false)
  Toggles built-in WorldEdit only for host (will flood your chat if set to true but when you auto-complete).
* **doImmediateRespawn** (default: false)
  Skips the death screen and immediately respawns players upon dying.
* **doTntExplodes** (default: true)
  Toggles whether TNT can be primed and exploded.
* **doFallDamage** (default: true)
  Toggles fall damage for players. Set to false to remove the fall damage
* **doAuth** (default: true)
  Adds authentication since eaglercraft is a cracked client.
* **chatMessageLimit** (default: 0)
  Sets a chat message character/rate limit (set to 0 to disable).

  _Also when a player tries to use `/kick` on you. It will prevent the player from kicking the owner and send a error message saying "You can't kick the host!" and this goes for other commands like `/mute`, and `/ban` (people who are operators try to bypass the kick command via command block but I also prevented the command block from kicking the host)_
