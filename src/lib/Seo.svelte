<script lang="ts">
	import { page } from '$app/stores';

	const siteUrl = 'https://fullscope-media.com';
	const siteName = 'Full Scope Media LLC';
	const defaultImage = `${siteUrl}/portfolio/622-vine-st-st-joseph-mi-49085/01-2000.jpg`;

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
	<meta property="og:title" content={ogTitle} />
	<meta property="og:description" content={ogDescription} />
	<meta property="og:image" content={ogImage} />
	<meta property="og:locale" content="en_US" />

	<!-- Twitter / X -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content={ogTitle} />
	<meta name="twitter:description" content={ogDescription} />
	<meta name="twitter:image" content={ogImage} />
</svelte:head>
