# Aurora X — Android Studio / IntelliJ Theme

A pure-AMOLED dark theme with blue/purple aurora tones, ported to Android Studio
and every IntelliJ-platform IDE (IntelliJ IDEA, PyCharm, WebStorm, etc.).

It ships two pieces:
- `Aurora X.icls` — the **editor color scheme** (syntax highlighting for 30+ languages,
  terminal, diff, console, inspections, warnings).
- `Aurora X.theme.json` + `META-INF/plugin.xml` — the **UI theme** (windows, toolbars,
  tabs, lists, dialogs, status bar all recolored to true black + aurora accents).

Author: **Ayoub Zulfiqar** — https://ayoubzulfiqar.com · contact@ayoubzulfiqar.com

## Install — from the release plugin (recommended)
1. Download `aurora-x-android-3.0.0.zip` from the
   [Releases](https://github.com/ayoubzulfiqar/Aurora-X/releases) page (tag `android-v3.0.0`).
2. Android Studio / IDE → **Settings** → **Plugins** → ⚙ → **Install Plugin from Disk…**
3. Select the `.zip`, restart the IDE.
4. **Settings** → **Editor** → **Color Scheme** → pick **Aurora X** (editor scheme).
5. **Settings** → **Appearance & Behavior** → **Appearance** → **Theme** → pick **Aurora X** (UI).

## Install — editor scheme only (no plugin)
Copy `Aurora X.icls` into your IDE's colors folder:
- Linux: `~/.config/Google/AndroidStudio*/colors/` (or `~/.AndroidStudio*/config/colors/`)
- macOS: `~/Library/Application Support/Google/AndroidStudio*/colors/`
Then **Settings** → **Editor** → **Color Scheme** → ⚙ → **Import Scheme…** → select the file.

## Install — from source (this repo)
```bash
git clone -b android https://github.com/ayoubzulfiqar/Aurora-X.git
cd Aurora-X
# Build the plugin zip with the IntelliJ Gradle toolchain (requires Android Studio / IntelliJ SDK):
./gradlew buildPlugin      # produces build/distributions/aurora-x-*.zip
```
Or just place `Aurora X.theme.json`, `Aurora X.icls` and `META-INF/plugin.xml` under
`resources/` of your own plugin module.

## License
GPL-3.0-only. © Ayoub Zulfiqar.
