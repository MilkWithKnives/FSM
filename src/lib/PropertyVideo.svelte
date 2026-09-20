<script lang="ts">
	import type { Property } from '$lib/properties';
	import { heroFallback } from '$lib/images';
	let { property }: { property: Property } = $props();
</script>

{#if property.video}
	<h2 class="text-2xl font-light mb-4" style="font-family: var(--font-serif)">{property.address} · {property.city}</h2>
	<!-- These property films have no supplied caption track. Add verified captions if they contain speech. -->
	<!-- svelte-ignore a11y_media_has_caption -->
	<video controls playsinline preload="none" poster={heroFallback(property)} aria-label="Video tour of {property.address}, {property.city}" class="w-full aspect-video bg-black">
		<source src={property.video} type="video/mp4" />
		<a href={property.video}>Watch the video tour of {property.address}</a>
	</video>
{/if}
