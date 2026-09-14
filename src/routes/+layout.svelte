<script lang="ts">
	import '../app.css';
	import { page } from '$app/stores';
	import { businessJsonLd } from '$lib/business';
	import EyeGate from '$lib/EyeGate.svelte';
	import Breadcrumbs from '$lib/Breadcrumbs.svelte';

	let { children } = $props();

	// The gate must outlive the mid-reveal navigation away from '/', so it renders
	// here (not in the gateway page) and stays mounted until the reveal finishes.
	let revealing = $state(false);
	const showGate = $derived($page.url.pathname === '/' || revealing);
</script>

<svelte:head>
	<!-- Favicons are declared in app.html. -->
	<!-- Per-page title/description/OG are rendered by the <Seo> component on each route. -->
	<!-- Analytics is handled by Google Tag Manager (GTM-N8RVSFDH) in app.html. -->

	<!-- Local Business JSON-LD (single source of truth in $lib/business.ts) -->
	{@html `<script type="application/ld+json">${JSON.stringify(businessJsonLd).replace(/</g, '\\u003c')}<\/script>`}
</svelte:head>

<Breadcrumbs />

<!-- Site chrome lives in the route groups: (photo) carries the real-estate nav/footer,
     (studio) the studio grid chrome. The root is shared head + the eye gate only. -->
{#if showGate}
	<EyeGate onrevealstart={() => (revealing = true)} onrevealend={() => (revealing = false)} />
{/if}

{@render children()}
