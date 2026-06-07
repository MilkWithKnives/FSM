<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { properties, propertyArea } from '$lib/properties';
	import {
		photoSrcset,
		photoFallback,
		heroFallback,
		PHOTO_SIZES_FULL,
		PHOTO_SIZES_GALLERY,
	} from '$lib/images';

	const heroProperty = properties[0];

	// One photo from each property's gallery, in mixed order
	const gallery = properties.flatMap((p) =>
		p.selected.slice(1, 4).map((n) => ({ slug: p.slug, n, address: p.address, area: propertyArea(p) })),
	);

	const includes = [
		'40+ fully edited, high-resolution images',
		'Wide-angle architectural exterior shots',
		'Interior room-by-room coverage',
		'Natural and artificial light optimization',
		'Sky replacement when needed',
		'Web + print resolution files',
		'Online gallery delivered in 24–48 hours',
	];
</script>

<Seo
	title="Real Estate Photography | Full Scope Media LLC · East Lansing, MI"
	description="Professional real estate photography in East Lansing and greater Michigan. 40+ fully edited photos, delivered in 24–48 hours. Serving Lansing, Okemos, and Metro Detroit."
	ogTitle="Real Estate Photography | Full Scope Media LLC"
	ogDescription="40+ fully edited real estate photos delivered in 24–48 hours. Serving East Lansing and greater Michigan."
/>

<!-- HERO -->
<section class="relative h-[60vh] overflow-hidden">
	<picture>
		<source type="image/webp" srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
		<img
			src={heroFallback(heroProperty)}
			srcset={photoSrcset(heroProperty.slug, heroProperty.selected[0], 'jpg')}
			sizes={PHOTO_SIZES_FULL}
			alt="Real estate photography"
			fetchpriority="high"
			class="absolute inset-0 w-full h-full object-cover"
		/>
	</picture>
	<div class="absolute inset-0 bg-black/35 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Services</p>
		<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Photography</h1>
	</div>
</section>

<!-- INTRO -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
		<div>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-6">What We Deliver</p>
			<h2 class="text-3xl md:text-4xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
				Images that make buyers stop scrolling.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-6">
				Our photography packages are built around one goal: making your listing impossible to ignore. Using professional-grade equipment, careful staging consultation, and expert post-processing, we deliver images that are both technically perfect and emotionally compelling.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-10">
				Every shoot is tailored to the property — we don't use a one-size-fits-all approach. Whether it's a compact downtown condo or a sprawling lakeside estate, we find the angles and light that tell that home's unique story.
			</p>
			<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">BOOK A SHOOT</a>
		</div>
		<div>
			<p class="text-xs tracking-widest uppercase text-gray-400 mb-6">Every Package Includes</p>
			<ul class="flex flex-col gap-3">
				{#each includes as item}
					<li class="flex items-start gap-3 text-sm text-gray-600">
						<span class="text-black mt-1">—</span>
						{item}
					</li>
				{/each}
			</ul>
			<div class="mt-8 pt-8 border-t border-gray-100">
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-2">Starting At</p>
				<p class="text-3xl font-light" style="font-family: var(--font-serif)">$480</p>
				<a href="/pricing" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity mt-4 inline-block">View Full Pricing</a>
			</div>
		</div>
	</div>
</section>

<!-- GALLERY -->
<section class="px-8 lg:px-20 pb-28 max-w-7xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-10 text-center">Sample Work</p>
	<div class="columns-1 sm:columns-2 lg:columns-3 gap-4 space-y-4">
		{#each gallery as item, i (item.slug + item.n)}
			<a href="/portfolio/{item.slug}" class="block overflow-hidden break-inside-avoid">
				<picture>
					<source type="image/webp" srcset={photoSrcset(item.slug, item.n, 'webp')} sizes={PHOTO_SIZES_GALLERY} />
					<img
						src={photoFallback(item.slug, item.n)}
						srcset={photoSrcset(item.slug, item.n, 'jpg')}
						sizes={PHOTO_SIZES_GALLERY}
						alt="{item.address}, {item.area}"
						loading="lazy"
						decoding="async"
						class="w-full object-cover hover:scale-105 transition-transform duration-500"
					/>
				</picture>
			</a>
		{/each}
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Ready to Shoot?</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
