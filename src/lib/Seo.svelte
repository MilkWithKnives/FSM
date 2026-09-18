<script lang="ts">
	import { page } from '$app/stores';
	import { siteUrl } from '$lib/business';

	const siteName = 'Full Scope Media LLC';
	const defaultImage = `${siteUrl}/eye-og.png`;

	let {
		title,
		description,
		ogTitle = title,
		ogDescription = description,
		image = defaultImage,
		type = 'website',
	}: {
		title: string;
		description: string;
		ogTitle?: string;
		ogDescription?: string;
		image?: string;
		type?: string;
	} = $props();

	// Preserve studio metadata; real estate titles have one source of truth.
	const socialTitle = $derived($page.url.pathname.startsWith('/studio') ? ogTitle : title);
	const canonical = $derived(`${siteUrl}${$page.url.pathname}`);
	// Social scrapers need absolute image URLs — normalize relative paths.
	const ogImage = $derived(image.startsWith('http') ? image : `${siteUrl}${image}`);
</script>

<svelte:head>
	<title>{title}</title>
	<meta name="description" content={description} />
	<meta name="robots" content="index, follow" />
	<link rel="canonical" href={canonical} />

	<!-- Open Graph -->
	<meta property="og:type" content={type} />
	<meta property="og:site_name" content={siteName} />
	<meta property="og:url" content={canonical} />
	<meta property="og:title" content={socialTitle} />
	<meta property="og:description" content={ogDescription} />
	<meta property="og:image" content={ogImage} />
	<meta property="og:locale" content="en_US" />

	<!-- Twitter / X -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content={socialTitle} />
	<meta name="twitter:description" content={ogDescription} />
	<meta name="twitter:image" content={ogImage} />
</svelte:head>
