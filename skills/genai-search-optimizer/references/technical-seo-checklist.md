# Technical SEO Checklist

A compact technical SEO checklist focused on what gates AI Overviews and AI Mode visibility. Items here are foundational SEO; AI search visibility flows from them, not from AI-specific tactics.

Primary sources: "Maintaining your website's SEO" and the Search Essentials technical requirements at developers.google.com/search/docs.

## 1. Baseline eligibility

```text
[ ] Page is indexable (no noindex meta or X-Robots-Tag).
[ ] Page is not blocked by robots.txt.
[ ] Page is not behind auth, paywall, or geo-block for Googlebot.
[ ] Page is snippet-eligible (no nosnippet, max-snippet:0, or data-nosnippet on key content).
[ ] Page returns 200 OK for crawler requests.
[ ] Redirect chains are short (one hop preferred; 301 for permanent moves, 302 for temporary).
[ ] No soft 404s on important URLs.
```

## 2. Crawl posture

```text
[ ] robots.txt is reachable, valid, and does not block important resources (CSS, JS, images).
[ ] XML sitemap exists, lists important URLs, and is referenced in robots.txt.
[ ] Sitemap entries have accurate lastmod values for frequently updated content.
[ ] Crawl budget is healthy: for very large sites, prioritize important pages in sitemaps and block low-value parameter URLs with robots.txt rules.
[ ] Search Console site is verified and the URL is inspectable.
```

## 3. Indexing posture

```text
[ ] Canonical tag points to the canonical version of the URL.
[ ] Self-referencing canonical present when no alternate canonical is needed.
[ ] hreflang annotations present and consistent if the site is multi-lingual or multi-regional.
[ ] Duplicate content is consolidated via canonicals, 301s, or parameter handling.
[ ] No important content is rendered only behind a click that hides it from initial render.
```

## 4. JavaScript rendering

```text
[ ] Primary content is present in the rendered HTML Googlebot sees.
[ ] No critical resources are blocked by robots.txt.
[ ] Lazy-loaded content does not depend on user interaction Googlebot cannot perform.
[ ] Infinite scroll patterns have a paginated alternative or other crawlable structure.
[ ] Hydration errors do not strip primary content on render.
```

## 5. Page experience

```text
[ ] HTTPS enabled with a valid certificate; no mixed content warnings.
[ ] Mobile-friendly: layout, tap targets, font sizes appropriate for mobile.
[ ] Core Web Vitals signals reviewed in Search Console; field data preferred over lab data.
[ ] Largest Contentful Paint (LCP) target met.
[ ] Interaction to Next Paint (INP) target met.
[ ] Cumulative Layout Shift (CLS) target met.
[ ] Layout does not push primary content below intrusive interstitials.
```

## 6. On-page semantics

```text
[ ] One H1 that reflects the page topic.
[ ] Heading hierarchy is logical and matches the document structure.
[ ] Title element is specific and matches the page content.
[ ] Meta description is informative and not duplicated across many pages.
[ ] Internal links use descriptive anchor text.
[ ] External links to untrusted or paid destinations use rel="nofollow" or rel="sponsored" as appropriate.
[ ] Semantic HTML is used where it helps human readability and accessibility (do not over-engineer).
```

## 7. Images

```text
[ ] Important images have descriptive, accurate alt text.
[ ] File names are descriptive when reasonable.
[ ] Image hosting page provides context for the image.
[ ] Image dimensions and formats are appropriate for the viewport.
[ ] Image metadata (caption, license) added where useful.
[ ] AI-generated product images include IPTC DigitalSourceType TrainedAlgorithmicMedia metadata where applicable.
[ ] Image sitemap entry or inline metadata as appropriate for the site type.
```

## 8. Video

```text
[ ] Video is hosted on a page that supports discovery (not buried behind interactions Googlebot cannot perform).
[ ] Video sitemap entry or structured data where the site has many videos.
[ ] Thumbnail is high-quality and representative.
[ ] Transcript or descriptive surrounding content is available where useful.
```

## 9. Structured data

```text
[ ] Schema.org markup added only for supported rich result types relevant to the page.
[ ] Markup validates with Google's Rich Results Test.
[ ] No markup for content that is not visible on the page.
[ ] No speculative AI-search schema; structured data is not required for generative AI search visibility.
```

## 10. Site moves and migrations

```text
[ ] Permanent URL moves return 301 to the new URL.
[ ] Temporary moves return 302.
[ ] Internal links updated to point at the new URL, not the redirect chain.
[ ] Search Console Change of Address used for full site moves.
[ ] Sitemaps updated to reflect the new URLs.
```

## 11. Search Console monitoring

```text
[ ] Site verified in Search Console.
[ ] Coverage / Page Indexing report reviewed for blockers.
[ ] Performance report reviewed for top queries and pages.
[ ] Manual actions and security issues reports reviewed.
[ ] Core Web Vitals report reviewed.
```

## How to use this checklist

- Use Pass / Fail / Unknown per item.
- For Fail and Unknown items affecting the audited URL, list them in the action plan with severity.
- Do not treat the checklist as a ranking algorithm. Items here support eligibility and crawl health; they do not guarantee visibility in AI Overviews or AI Mode.
