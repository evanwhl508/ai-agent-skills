---
name: genai-search-optimizer
description: Audit and improve a page or site for visibility in Google's generative AI search (AI Overviews, AI Mode) and Google Search overall, grounded in Google Search Central's official guidance; use to evaluate content quality, diagnose technical SEO blockers, rewrite commodity content into non-commodity people-first content, review structured data and image/video SEO, check local and ecommerce signals, and refuse AEO/GEO myths such as llms.txt files, content chunking, AI-targeted rewrites, inauthentic mentions, and schema cargo-culting.
---

# GenAI Search Optimizer

Use this skill to apply Google Search Central's official guidance on optimizing for generative AI features in Google Search. Treat optimizing for AI Overviews and AI Mode as SEO, not a separate AEO or GEO discipline. Refuse tactics Google has explicitly identified as ineffective and cite the source when refusing.

Output should be practical: a baseline verdict, a content classification, a technical findings list with severity, a myth-bust callout when applicable, and a prioritized action plan with citations.

## Core principles

- Optimizing for AI Overviews and AI Mode is still SEO. Google's generative AI features are grounded in its core ranking and quality systems.
- A page must be indexable and snippet-eligible before it can appear in AI Overviews or AI Mode. Fix baseline eligibility before content advice.
- Non-commodity, experience-led content beats recycled common knowledge. Write for the human audience, not for AI parsers.
- Refuse known myths: llms.txt files, content chunking, AI-targeted rewrites, inauthentic mentions, schema cargo-culting, and scaled long-tail page generation.
- Cite Google Search Central when stating or refuting a tactic so the user can verify.

## Workflow

### 1. Frame

Capture before auditing:

- Site type: blog, docs, ecommerce, local business, news, SaaS marketing, personal portfolio.
- Target: a specific URL, a content draft, a section of the site, or a recurring content type.
- Goal: more impressions, more clicks, more AI Overview citations, more conversions, or fewer technical errors.
- Baseline data if available: Search Console performance, current rankings, known errors.

If the user frames the request as AEO or GEO optimization, reframe explicitly: this is SEO, and Google's official guidance is the basis. Do not silently accept the framing.

### 2. Audit

Confirm baseline eligibility first. If any item below fails, stop content work and fix the baseline. AI Overviews and AI Mode draw from Google's index; pages that cannot be indexed cannot appear.

- Page is indexable: no `noindex`, no robots.txt block, no auth wall.
- Page is eligible to appear with a snippet (no `nosnippet` or `data-nosnippet` blocking the relevant content).
- Site is on HTTPS.
- Site is mobile-friendly (default crawler is mobile).
- Page is reachable by Google's crawler; JS-rendered content is not blocked.
- Sitemap and canonical signals are sane.

Then classify content quality:

- Commodity vs non-commodity. Is this recycled common knowledge or unique experience-led perspective?
- People-first vs AI-first. Does this read for a human audience or for keyword capture?
- Originality signals: first-hand experience, original data, novel synthesis, named author, dated updates.
- Coverage and depth: does the page address the user intent fully?
- Format fit: are images, video, tables, examples used where they help?

For a fill-in audit form, read `references/audit-checklist.md`.

### 3. Diagnose

Audit technical structure and flag findings by severity (blocker, major, minor, polish):

- Title, meta description, headings hierarchy, alt text.
- Internal linking with descriptive anchors.
- Canonical tag correctness.
- Structured data validity if used. Do not add schema markup just for AI search; Google has stated structured data is not required for generative AI search visibility.
- Page speed and Core Web Vitals signals. Reference the report; do not fabricate numbers.
- Duplicate content risk on the site.
- Robots.txt and sitemap entries affecting this URL.
- JavaScript rendering posture if applicable.
- Image and video SEO when media is present.

Run the myth-bust pass. If the user's intent, prior recommendations, or the page itself involves any of the following, flag it, cite Google's stated position, and propose the foundational SEO equivalent:

- llms.txt, ai.txt, or AI-targeted Markdown mirrors.
- Excessive content chunking or fragmenting.
- AI-flavored rewriting that drifts from the audience.
- Inauthentic mentions, fake reviews, or bought "PR" placements.
- Schema-everything cargo-culting beyond rich result eligibility.
- Generating many thin pages per long-tail query.

For the canonical list with citations, read `references/myth-bust-register.md`.

If the site is ecommerce or local, also check:

- Merchant Center feed presence and hygiene.
- Google Business Profile completeness and freshness.
- IPTC `DigitalSourceType` `TrainedAlgorithmicMedia` metadata on AI-generated product images, and labeling AI-generated product copy as such.

For the ecommerce/local detail, read `references/ecommerce-and-local-signals.md`.
For the technical SEO detail, read `references/technical-seo-checklist.md`.

### 4. Rewrite

For content that scored low on non-commodity or people-first:

- Identify the unique angle, first-hand evidence, or expert insight that could anchor the piece.
- Propose a new outline that leads with the angle, not the common-knowledge preamble.
- Show one to three paragraph rewrites where the original is generic.
- Flag sections that should be removed, merged, or replaced with a better format (table, image, list, video).
- Preserve the human reader as the primary audience. Do not rewrite for AI parsing.

For AI-assisted content:

- Recommend disclosure where it adds context for the reader.
- Confirm the content meets Search Essentials and the spam policy on scaled content abuse independent of how it was produced.

For reusable rewrite patterns, read `references/content-rewrite-patterns.md`.

### 5. Plan

Produce a prioritized action plan:

- Blockers: must fix before any content work matters (baseline eligibility, crawl/index errors).
- High-impact: changes likely to move visibility (content originality, technical structure, primary media).
- Polish: small improvements (meta wording, internal links, image alt text).
- Myth-bust list: tactics to stop or avoid, with citation.
- Optional 30/60/90 day staging if the user wants a roadmap.

Each item includes a rationale, a citation to Google's official guidance where applicable, an effort estimate, and a concrete next action.

For the action plan template, read `references/action-plan-template.md`.

## Expected Output

When auditing a page, usually return:

1. Baseline eligibility verdict (indexable, snippet-eligible, technically reachable).
2. Content classification (commodity vs non-commodity, people-first vs AI-first).
3. Technical findings list with severity.
4. Myth-bust callout if any AEO/GEO tactic is in play.
5. Prioritized action plan with Google citations.
6. Optional: rewrite drafts for one to three sections.

When asked a myth-shaped question ("should I add llms.txt?"), answer directly with Google's stated position, decline the tactic, and propose the foundational SEO action the user actually wants.

For small content edits, skip the long audit and return the revised content with a short rationale.

## Source Notes

This skill is unofficial and original synthesis grounded in Google Search Central's public guidance on generative AI search, helpful content, and technical SEO. It is not affiliated with Google.

For canonical source pages, paraphrased principles, and the last review date, read `references/source-notes.md`.
