# Audit Checklist

Use this as a fillable form when auditing a page or a small set of representative URLs against Google's official generative AI search guidance. The agent should fill each section inline and finish with the action plan.

## 1. Frame

```text
Site type:
URL or content target:
Goal (impressions, clicks, AI Overview citations, conversions, error fixes):
Baseline data available (Search Console, rankings, errors):
User-stated framing (SEO, AEO, GEO, AI Overviews, AI Mode):
Reframe note if needed: Optimizing for AI search is still SEO.
```

## 2. Baseline eligibility

For each item, mark Pass, Fail, or Unknown. If anything fails, fix it before doing content work.

```text
Indexable (no noindex, robots.txt block, or auth wall):
Snippet-eligible (no nosnippet or data-nosnippet blocking key content):
HTTPS:
Mobile-friendly:
JS-rendered content crawlable:
Canonical tag sane:
Sitemap entry present:
Search Console verified:
```

## 3. Content classification

```text
Commodity vs non-commodity:
Evidence for the verdict (quote or summarize):
People-first vs AI-first:
Originality signals (first-hand experience, original data, expert credentials, named author, update date):
Coverage and depth verdict:
Format fit (images, video, tables, examples where helpful):
Helpful, reliable, people-first self-check verdict:
```

## 4. Technical findings

For each finding, set severity: blocker, major, minor, polish.

```text
Title:
Meta description:
Headings hierarchy:
Alt text:
Internal linking:
Canonical correctness:
Structured data validity (if present):
Page speed / Core Web Vitals signals:
Duplicate content risk:
Robots.txt and sitemap posture:
JavaScript rendering posture:
Image SEO:
Video SEO:
Other:
```

## 5. Myth-bust pass

Mark any tactic detected. For each detected tactic, cite Google's stated position and propose the foundational SEO equivalent.

```text
llms.txt or ai.txt or AI-targeted Markdown mirrors detected:
Excessive content chunking or fragmenting detected:
AI-flavored rewriting that drifts from the audience detected:
Inauthentic mentions, fake reviews, or bought "PR" placements detected:
Schema-everything cargo-culting detected:
Scaled long-tail page generation detected:
```

## 6. Ecommerce and local signals (if applicable)

```text
Merchant Center feed present and hygienic:
Google Business Profile complete and fresh:
AI-generated product images labeled with IPTC DigitalSourceType TrainedAlgorithmicMedia:
AI-generated product copy labeled as such:
Business Agent or other conversational surfaces relevant:
```

## 7. AI-generated content posture (if applicable)

```text
Disclosure where helpful for reader context:
Meets Search Essentials independent of how it was produced:
Avoids scaled content abuse:
```

## 8. Prioritized action plan

```text
Blockers (fix first):
High-impact actions:
Polish actions:
Myth-bust list (stop or avoid):
30/60/90 day staging (optional):
Open questions / missing data:
```
