# Ecommerce and Local Signals

Use this reference when the audited site is ecommerce, a local business, or has product / service listings that may appear in AI search responses.

Primary sources: Google Merchant Center help center, Google Business Profile help center, and "Optimizing your website for generative AI features on Google Search" at developers.google.com/search/docs/fundamentals/ai-optimization-guide.

## 1. Merchant Center for ecommerce

Generative AI search responses can include product listings and product information for relevant queries. A healthy Merchant Center feed gives products surface area in both AI responses and classic Search.

```text
[ ] Merchant Center account exists and the website is verified and claimed.
[ ] Product feed is submitted and free of disapprovals.
[ ] Required attributes complete: id, title, description, link, image_link, price, availability, brand, gtin, condition.
[ ] Titles match how customers search; avoid keyword stuffing.
[ ] Descriptions are accurate and not duplicated across many SKUs.
[ ] Images meet the Merchant Center image requirements (no overlays, accurate product representation).
[ ] Structured data on product pages matches the feed values.
[ ] Out-of-stock and price changes propagate quickly.
[ ] AI-generated product titles or descriptions are disclosed and labeled as AI-generated per Merchant Center policy.
[ ] AI-generated product images include IPTC DigitalSourceType TrainedAlgorithmicMedia metadata.
```

## 2. Google Business Profile for local

Generative AI search responses can include local business information for relevant queries. A complete and fresh Business Profile is the primary signal.

```text
[ ] Business Profile claimed and verified.
[ ] Primary category set correctly; secondary categories selected only when accurate.
[ ] Service area and address (where applicable) are accurate.
[ ] Hours of operation, including holiday hours, kept up to date.
[ ] Phone number, website, and booking links functional.
[ ] Photos uploaded and refreshed periodically.
[ ] Services and products list populated.
[ ] Reviews are responded to (positive and negative).
[ ] Posts used for promotions, events, or updates where relevant.
[ ] Q&A monitored and seeded with common questions answered by the business.
```

## 3. AI-generated content disclosure for ecommerce

```text
[ ] AI-generated product titles and descriptions are labeled as AI-generated when policy requires.
[ ] AI-generated imagery uses the IPTC DigitalSourceType TrainedAlgorithmicMedia metadata.
[ ] Disclosure is presented in a way that does not degrade reader experience.
[ ] Content meets Search Essentials independent of how it was produced.
[ ] Content does not trigger the scaled content abuse policy: avoid mass-generating near-duplicate descriptions across thousands of SKUs without unique value.
```

## 4. On-site product page hygiene

```text
[ ] Each product page has a unique URL, title, and description.
[ ] Primary product image is high-resolution and accurately represents the product.
[ ] Specifications, dimensions, materials, and other structured attributes are present in the page content, not only in the feed.
[ ] Reviews and ratings shown on the page reflect real customer reviews; structured data for reviews follows policy.
[ ] Availability, price, and shipping information are accurate and visible.
[ ] Internal linking surfaces related products and category pages.
```

## 5. On-site local landing page hygiene

```text
[ ] Each location has a unique landing page with NAP (name, address, phone) consistent with the Business Profile.
[ ] Service area, hours, and offerings match the Business Profile.
[ ] Photos and reviews specific to the location, not generic stock.
[ ] Structured data for LocalBusiness or appropriate sub-type, validated.
[ ] Internal links from the main site to each location page.
```

## 6. Emerging agentic surfaces (dated)

This section captures agent-friendly site UX and protocol-level work that may matter for ecommerce in the near term. The space moves fast; review this section quarterly.

Last reviewed: 2026-05-20.

```text
- Browser agents may access the site to gather data for tasks like comparing specs or booking reservations. They typically use rendered visuals, DOM structure, and the accessibility tree.
- Agent-friendly site UX guidance is available at web.dev/articles/ai-agent-site-ux.
- Universal Commerce Protocol (UCP) at ucp.dev is an emerging protocol intended to let Search agents perform commerce tasks. Adoption is early; treat support as experimental.
- Google's Business Agent is a conversational experience on Google Search for some brand profiles; check eligibility and availability before recommending.
- Do not represent agentic protocols as ranking factors today. The skill should mention them as forward-looking context, not as visibility levers.
```

## 7. Refusal patterns specific to ecommerce and local

Refuse these patterns when proposed:

- Mass-generating near-duplicate product descriptions per keyword variant.
- Buying or seeding fake reviews for products or business profiles.
- AI-generating product imagery without the required IPTC metadata or disclosure.
- Adding LocalBusiness markup for service areas the business does not actually serve.
- Stuffing the Business Profile primary category with secondary topics for "AI visibility."

For each refusal, cite the relevant Merchant Center, Business Profile, or Search Essentials policy and propose the compliant alternative.
