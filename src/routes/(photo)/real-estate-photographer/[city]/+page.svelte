<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { propertyArea } from '$lib/properties';
	import {
		photoSrcset,
		photoFallback,
		heroFallback,
		PHOTO_SIZES_FULL,
		PHOTO_SIZES_GALLERY,
	} from '$lib/images';

	let { data } = $props();
	const { location, property } = $derived(data);

	// Gallery from the real, locally-shot property (skip the first — it's the hero).
	const gallery = $derived(
		property ? property.selected.slice(1, 10).map((n) => ({ slug: property.slug, n })) : [],
	);
</script>

<Seo
	title={location.title}
	description={location.description}
	ogTitle={location.heading}
	ogDescription={location.description}
	image={property ? `/portfolio/${property.slug}/01-2000.jpg` : undefined}
/>

<!-- HERO -->
<section class="relative h-[60vh] min-h-[400px] overflow-hidden">
	{#if property}
		<picture>
			<source type="image/avif" srcset={photoSrcset(property.slug, property.selected[0], 'avif')} sizes={PHOTO_SIZES_FULL} />
			<source type="image/webp" srcset={photoSrcset(property.slug, property.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
			<img
				src={heroFallback(property)}
				srcset={photoSrcset(property.slug, property.selected[0], 'jpg')}
				sizes={PHOTO_SIZES_FULL}
				alt="Real estate photography in {location.city}, {location.state} — {property.address}"
				fetchpriority="high"
				class="absolute inset-0 w-full h-full object-cover"
			/>
		</picture>
	{/if}
	<div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Full Scope Media</p>
		<h1 class="text-3xl sm:text-4xl md:text-6xl font-light max-w-3xl leading-tight" style="font-family: var(--font-serif)">
			{location.heading}
		</h1>
	</div>
</section>

<!-- INTRO -->
<section class="py-16 md:py-24 px-6 lg:px-20 max-w-4xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-6">Serving {location.city}, {location.state}</p>
	<h2 class="text-2xl md:text-4xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
		Listing photography that sells {location.city} homes.
	</h2>
	{#each location.intro as paragraph}
		<p class="text-base text-gray-600 leading-relaxed mb-5">{paragraph}</p>
	{/each}

	<p class="text-sm text-gray-500 leading-relaxed mt-8">
		<span class="text-gray-700 font-medium">Neighborhoods we shoot in {location.city}:</span>
		{location.neighborhoods.join(' · ')}
	</p>

	<div class="mt-10 flex flex-wrap gap-4">
		<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">BOOK A {location.city.toUpperCase()} SHOOT</a>
		<a href="/pricing" class="btn btn-outline rounded-none tracking-widest text-xs px-8">VIEW PRICING</a>
	</div>
</section>

<!-- LOCAL WORK GALLERY -->
{#if property && gallery.length}
	<section class="bg-gray-50 py-16 md:py-24 px-6 lg:px-20">
		<div class="max-w-7xl mx-auto">
			<div class="text-center mb-12">
				<p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-3">Recent Work in {location.city}</p>
				<h2 class="text-2xl md:text-4xl font-light" style="font-family: var(--font-serif)">{property.address}, {location.city}</h2>
				<p class="text-sm text-gray-500 mt-2">{property.tag} · {property.photoCount} photos delivered</p>
			</div>
			<div class="columns-1 sm:columns-2 lg:columns-3 gap-4 space-y-4">
				{#each gallery as item (item.slug + item.n)}
					<a href="/portfolio/{item.slug}" class="block overflow-hidden break-inside-avoid">
						<picture>
							<source type="image/avif" srcset={photoSrcset(item.slug, item.n, 'avif')} sizes={PHOTO_SIZES_GALLERY} />
							<source type="image/webp" srcset={photoSrcset(item.slug, item.n, 'webp')} sizes={PHOTO_SIZES_GALLERY} />
							<img
								src={photoFallback(item.slug, item.n)}
								srcset={photoSrcset(item.slug, item.n, 'jpg')}
								sizes={PHOTO_SIZES_GALLERY}
								alt="Real estate photography in {location.city}, {location.state}"
								loading="lazy"
								decoding="async"
								class="w-full object-cover hover:scale-105 transition-transform duration-500"
							/>
						</picture>
					</a>
				{/each}
			</div>
			<div class="text-center mt-10">
				<a href="/portfolio/{property.slug}" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity">View Full {location.city} Gallery</a>
			</div>
		</div>
	</section>
{/if}

<!-- CTA -->
<section class="bg-neutral text-white py-20 md:py-24 px-6 text-center">
	<h2 class="text-3xl md:text-5xl font-light mb-6" style="font-family: var(--font-serif)">Have a listing in {location.city}?</h2>
	<p class="text-sm opacity-70 mb-8 max-w-xl mx-auto">Photos, video, and aerial drone — edited and delivered in 24 hours.</p>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
