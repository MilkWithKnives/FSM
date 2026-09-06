<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { siteUrl } from '$lib/business';

	let { data } = $props();
	const post = $derived(data.post);
	const url = $derived(`${siteUrl}/journal/${post.slug}`);
	const structuredData = $derived({
		'@context': 'https://schema.org',
		'@graph': [
			{
				'@type': 'BlogPosting',
				'@id': `${url}#article`,
				url,
				headline: post.title,
				description: post.description,
				image: [post.image.src],
				inLanguage: 'en-US',
				mainEntityOfPage: { '@type': 'WebPage', '@id': url },
				author: { '@type': 'Organization', '@id': `${siteUrl}/#business`, name: 'Full Scope Media LLC', url: `${siteUrl}/about` },
				publisher: { '@id': `${siteUrl}/#business` },
			},
			{
				'@type': 'BreadcrumbList',
				itemListElement: [
					{ '@type': 'ListItem', position: 1, name: 'Real Estate Media', item: `${siteUrl}/real-estate-photography` },
					{ '@type': 'ListItem', position: 2, name: 'Journal', item: `${siteUrl}/journal` },
					{ '@type': 'ListItem', position: 3, name: post.title, item: url },
				],
			},
		],
	});
</script>

<Seo title="{post.title} | Full Scope Media" description={post.description} image={post.image.src} type="article" />

<svelte:head>
	{@html `<script type="application/ld+json">${JSON.stringify(structuredData).replace(/</g, '\\u003c')}<\/script>`}
</svelte:head>

<article class="journal-article">
	<header>
		<nav aria-label="Breadcrumb" class="breadcrumbs">
			<a href="/real-estate-photography">Real Estate Media</a>
			<span aria-hidden="true">/</span>
			<a href="/journal">Journal</a>
			<span aria-hidden="true">/</span>
			<span aria-current="page">{post.title}</span>
		</nav>
		<p class="eyebrow">Insights &amp; Ideas</p>
		<h1>{post.title}</h1>
		<p class="byline">By <a href="/about">Full Scope Media LLC</a></p>
		<figure>
			<img src={post.image.src} alt={post.image.alt} width={post.image.width} height={post.image.height} fetchpriority="high" />
			{#if post.image.caption}<figcaption>{post.image.caption}</figcaption>{/if}
		</figure>
		{#each post.intro as paragraph}<p class="body-copy">{paragraph}</p>{/each}
	</header>

	<nav aria-label="In this article" class="contents">
		<p class="eyebrow">In this article</p>
		<ul>
			{#each post.sections as section (section.id)}
				<li><a href="#{section.id}">{section.heading}</a></li>
			{/each}
		</ul>
	</nav>

	{#each post.sections as section (section.id)}
		<section id={section.id} aria-labelledby="{section.id}-heading">
			<h2 id="{section.id}-heading">{section.heading}</h2>
			{#each section.paragraphs as paragraph}<p class="body-copy">{paragraph}</p>{/each}
			{#if section.items}
				<ul class="checklist">
					{#each section.items as item}<li>{item}</li>{/each}
				</ul>
			{/if}
			{#if section.links}
				<ul class="article-links">
					{#each section.links as link}<li><a href={link.href}>{link.label}</a></li>{/each}
				</ul>
			{/if}
		</section>
	{/each}

	<aside class="related" aria-labelledby="related-heading">
		<h2 id="related-heading">Related guides and services</h2>
		<ul class="article-links">
			{#each post.related as link}<li><a href={link.href}>{link.label}</a></li>{/each}
		</ul>
		<a href="/journal" class="back-link">← Back to the Journal</a>
	</aside>
</article>

<style>
	.journal-article { max-width: 880px; margin: 0 auto; padding: 48px clamp(20px, 5vw, 48px) 80px; }
	.breadcrumbs { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 40px; font-size: 12px; line-height: 1.6; color: #666; white-space: normal; }
	.eyebrow { margin-bottom: 16px; font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: #666; }
	h1 { font-size: clamp(36px, 6vw, 62px); line-height: 1.1; font-weight: 300; }
	h2 { margin-bottom: 20px; font-size: clamp(28px, 4vw, 36px); line-height: 1.2; font-weight: 300; }
	.byline { margin-top: 24px; font-size: 13px; color: #666; }
	figure { margin: 32px 0; }
	figure img { display: block; width: 100%; height: auto; }
	figcaption { margin-top: 12px; font-size: 12px; line-height: 1.6; color: #666; }
	.body-copy, .checklist { font-size: 16px; line-height: 1.85; color: #444; }
	.body-copy + .body-copy { margin-top: 18px; }
	.contents { margin: 36px 0 44px; padding: 24px; background: #f8f8f8; }
	.contents ul, .article-links { display: flex; flex-direction: column; gap: 12px; font-size: 14px; line-height: 1.65; }
	a { text-decoration: underline; text-underline-offset: 4px; }
	a:hover { color: #111; }
	a:focus-visible { outline: 2px solid currentColor; outline-offset: 4px; }
	section { margin-top: 40px; scroll-margin-top: 96px; }
	.checklist { list-style: disc; padding-left: 24px; margin-top: 20px; }
	.checklist li + li { margin-top: 10px; }
	.article-links { margin-top: 20px; }
	.related { margin-top: 52px; padding-top: 32px; border-top: 1px solid #e5e5e5; }
	.back-link { display: inline-block; margin-top: 28px; font-size: 14px; }
</style>
