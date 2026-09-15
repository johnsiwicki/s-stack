---
name: old-accordion-to-accordion-style-converter
description: Convert legacy Foundation ul.accordion / li.accordion-navigation accordions and older .th-accordion panels into the modern Treehouse div.accordion-style native details/summary HTML. Use when transforming old accordion markup for Treehouse CMS pages.
license: MIT
metadata:
  author: johnsiwicki
  category: client
  status: reusable
  version: "0.1.0"
---

# Accordion converter

Convert old Treehouse / Foundation accordion HTML into native `details` / `summary`.

Handles:

- Foundation: `ul.accordion`, `li.accordion-navigation`, `a href="#panelN"`, `div#panelN.content`
- Treehouse: `div.th-accordion`, `div.th-accordion-panel`, `span.th-accordion-title`, `div.th-accordion-panel-content`

## Input

The source accordion HTML. If the page already contains `core_accordion.css`, say the stylesheet link only needs to appear once.

## Output wrapper

One outer wrapper for every converted item, then the stylesheet **once**:

```html
<div class="accordion-style">
  ... all <details> items ...
</div>
<link rel="stylesheet" href="https://cdn.treehouseinternetgroup.com/cms_core/css/core_accordion.css">
```

Never emit the stylesheet per item.

## Image item

```html
<details>
  <summary>TITLE</summary>
  <div class="accordion-style__content">
      <div class="row">
      <div class="columns medium-3">
      <img class="border" src="IMG_SRC" alt="ALT_TEXT" loading="lazy"/>
      </div>
      <div class="columns medium-7">
      PARAGRAPHS
      </div>
      </div>
  </div>
</details>
```

## Imageless item

```html
<details>
  <summary>TITLE</summary>
  <div class="accordion-style__content">
      PARAGRAPHS
  </div>
</details>
```

Do not invent images or empty `columns medium-3` wrappers. Mix variants item by item.

## Foundation mapping

| Source | Target |
| --- | --- |
| Text inside `h3` inside `a href="#panelN"` | Plain text in `summary`; drop `a` and `h3` |
| `img` inside `columns medium-4` | `columns medium-3`; `<img class="border" src="IMG_SRC" alt="ALT_TEXT" loading="lazy"/>` |
| Contents of `columns medium-8` | `columns medium-7`, paragraphs and links verbatim |

Drop `id="panelN"`, `active`, `data-accordion`, old `a` wrappers, old `h3`. Add `open` only if asked.

## `.th-accordion` mapping

| Source | Target |
| --- | --- |
| Text in `span.th-accordion-title` | Plain text in `summary` |
| `div.th-accordion-panel-content` | `PARAGRAPHS` verbatim |

Drop `svg.th-accordion-arrow`, `clear`, `data-*` on the outer accordion, and empty content blocks that are only `&nbsp;`. Mention if cruft was removed.

## Image src rule

Strip this prefix from image `src` values only:

`https://cdn.treehouseinternetgroup.com`

Do not strip it from the stylesheet href. Leave already-root-relative paths alone. Do not rewrite filenames.

## Preservation

Keep paragraph text and order, inline links, `strong`/`em`, `ul.arrows`, lists, entities, and tokens such as `[company]`. `summary` is plain text only.

If a source panel has `div.columns` and the output uses the image variant, warn that nested Foundation columns need an intervening `.row`.

## Response

Return the HTML in a fenced `html` block. Commentary only for stylesheet duplicates, removed empty panels, nested-column warnings, or malformed source.
