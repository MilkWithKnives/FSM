<script lang="ts">
	import { page } from '$app/stores';
	import { buildBreadcrumbs } from '$lib/breadcrumbs';

	// page.data includes the leaf page's load data during SSR and client navigation.
	const trail = $derived($page.status < 400 ? buildBreadcrumbs($page.url.pathname, $page.data) : []);
	const structuredData = $derived(trail.length > 1 ? {
		'@context': 'https://schema.org',
		'@type': 'BreadcrumbList',
		itemListElement: trail.map((crumb, index) => ({
			'@type': 'ListItem',
			position: index + 1,
			...crumb,
		})),
	} : undefined);
</script>

<svelte:head>
	{#if structuredData}
		{@html `<script type="application/ld+json">${JSON.stringify(structuredData).replace(/</g, '\\u003c')}<\/script>`}
	{/if}
</svelte:head>
