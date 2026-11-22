# Contributing

A new skill should add a genuinely different **design direction**, not just a new background color. Keep style, palette, layout and social composition independent.

## Required files

```text
styles/your-new-style/
├── SKILL.md          # Agent Skills-compliant YAML header + concrete directions
├── demo.html         # self-contained, offline static study with no external tracking
└── preview.png       # generated screenshot of that exact study, 1280×800
```

Use only supported frontmatter keys: `name`, `description`, optional `license`, `compatibility`, `allowed-tools`, `metadata`. Put `preview: preview.png` and descriptive category/era values within `metadata` as strings. Folder and frontmatter `name` must match. Write descriptions as **when to invoke** the skill, not empty adjectives.

Every style specification must clearly describe: its historical/art reference; typography, geometry and image treatment; canonical `--color-*` tokens; semantic component states; responsive rules; accessible contrast/keyboard/focus behavior; specific forbidden patterns; an honest sample invocation. Do not copy historic copyrighted compositions, trademarks or third-party photos without permission.

To add a skill: edit its folder and add an entry to `manifest.json`, regenerate `gallery/index.html` using `python tools/build_gallery.py`, regenerate its PNG with `python tools/render_previews.py --only styles/your-new-style`, then run `python tools/validate_skills.py` and visually inspect both the preview and the page at narrow widths. Commit the related docs and screenshot changes. If the new style uses added images, provide source attribution/license in that folder.

Contributions that are palette swaps of existing previews, ship illegible decorative type or violate functional accessibility are not a good fit.
