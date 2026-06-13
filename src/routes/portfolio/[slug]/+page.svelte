<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { onMount } from 'svelte';
	import { propertyFullAddress, propertyArea } from '$lib/properties';
	import {
		photoSrcset,
		photoFallback,
		heroFallback,
		PHOTO_SIZES_FULL,
	} from '$lib/images';

	let { data } = $props();
	const p = $derived(data.property);
	const photos = $derived(p.selected);
	const total = $derived(photos.length);

	let current = $state(0);

	function goto(i: number) {
		current = ((i % total) + total) % total;
	}
	function next() { goto(current + 1); }
	function prev() { goto(current - 1); }

	$effect(() => {
		void p;
		current = 0;
	});

	function onKey(e: KeyboardEvent) {
		if (e.key === 'ArrowRight') next();
		else if (e.key === 'ArrowLeft') prev();
	}

	onMount(() => {
		window.addEventListener('keydown', onKey);
		return () => window.removeEventListener('keydown', onKey);
	});

	// Touch swipe
	let touchStartX = 0;
	function onTouchStart(e: TouchEvent) {
		touchStartX = e.changedTouches[0].screenX;
	}
	function onTouchEnd(e: TouchEvent) {
		const dx = e.changedTouches[0].screenX - touchStartX;
		if (Math.abs(dx) < 40) return;
		if (dx < 0) next(); else prev();
	}
</script>

<Seo
	title="{p.address} · {propertyArea(p)} | Full Scope Media LLC"
	description="Real estate photography for {propertyFullAddress(p)} by Full Scope Media LLC."
	ogDescription="Real estate photography for {propertyFullAddress(p)}."
	image={heroFallback(p)}
/>

<!-- BREADCRUMB + TITLE -->
<section class="px-5 md:px-10 lg:px-20 max-w-7xl mx-auto pt-10 pb-8">
	<a href="/portfolio" class="text-xs tracking-widest uppercase text-gray-500 hover:text-black transition-colors">← All Work</a>
	<div class="mt-6 flex flex-col md:flex-row md:items-end md:justify-between gap-3">
		<div>
			<p class="text-xs tracking-[0.3em] uppercase text-gray-500 mb-2">{p.tag}</p>
			<h1 class="text-3xl md:text-5xl font-light" style="font-family: var(--font-serif)">{p.address}</h1>
			<p class="text-sm text-gray-500 mt-2">{propertyArea(p)} · {p.zip}</p>
		</div>
		<p class="text-xs tracking-widest text-gray-500">{String(current + 1).padStart(2, '0')} / {String(total).padStart(2, '0')}</p>
	</div>
</section>

<!-- FULLSCREEN CAROUSEL -->
<section
	class="relative w-full bg-black select-none"
	aria-roledescription="carousel"
	aria-label="{p.address} photo gallery"
	ontouchstart={onTouchStart}
	ontouchend={onTouchEnd}
>
	<div class="relative w-full h-[60vh] sm:h-[72vh] md:h-[84vh] overflow-hidden">
		{#each photos as n, i (n)}
			<div
				class="absolute inset-0 transition-opacity duration-700 ease-in-out {i === current ? 'opacity-100 z-10' : 'opacity-0 z-0'}"
				aria-hidden={i === current ? 'false' : 'true'}
				aria-roledescription="slide"
				aria-label="Photo {i + 1} of {total}"
			>
				<picture>
					<source type="image/avif" srcset={photoSrcset(p.slug, n, 'avif')} sizes={PHOTO_SIZES_FULL} />
					<source type="image/webp" srcset={photoSrcset(p.slug, n, 'webp')} sizes={PHOTO_SIZES_FULL} />
					<img
						src={photoFallback(p.slug, n)}
						srcset={photoSrcset(p.slug, n, 'jpg')}
						sizes={PHOTO_SIZES_FULL}
						alt="{p.address} photo {i + 1}"
						loading={i === 0 ? 'eager' : 'lazy'}
						fetchpriority={i === 0 ? 'high' : 'auto'}
						decoding="async"
						class="absolute inset-0 w-full h-full object-contain"
					/>
				</picture>
			</div>
		{/each}

		<!-- prev / next -->
		<div class="absolute inset-0 flex items-center justify-between px-3 sm:px-6 z-20 pointer-events-none">
			<button
				type="button"
				onclick={prev}
				aria-label="Previous photo"
				class="btn btn-circle bg-white/15 border border-white/25 text-white hover:bg-white hover:text-black hover:border-white transition-all backdrop-blur-sm pointer-events-auto"
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
					<path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
				</svg>
			</button>
			<button
				type="button"
				onclick={next}
				aria-label="Next photo"
				class="btn btn-circle bg-white/15 border border-white/25 text-white hover:bg-white hover:text-black hover:border-white transition-all backdrop-blur-sm pointer-events-auto"
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
					<path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
				</svg>
			</button>
		</div>

		<div class="absolute top-4 right-4 sm:top-6 sm:right-8 z-20 text-white/70 text-xs tracking-widest pointer-events-none">
			{String(current + 1).padStart(2, '0')} / {String(total).padStart(2, '0')}
		</div>
	</div>

	<!-- thumbnail strip -->
	<div class="bg-black py-4 px-3 sm:px-6 border-t border-white/10">
		<div class="flex gap-2 overflow-x-auto scrollbar-thin">
			{#each photos as n, i (n)}
				<button
					type="button"
					onclick={() => goto(i)}
					aria-label="Show photo {i + 1}"
					aria-current={i === current}
					class="flex-shrink-0 overflow-hidden transition-all duration-300 {i === current ? 'ring-2 ring-white opacity-100' : 'opacity-50 hover:opacity-100'}"
				>
					<img
						src={photoFallback(p.slug, n, 800)}
						alt=""
						loading="lazy"
						decoding="async"
						class="w-20 h-14 sm:w-24 sm:h-16 object-cover block"
					/>
				</button>
			{/each}
		</div>
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-20 md:py-24 px-5 text-center">
	<h2 class="text-3xl md:text-5xl font-light mb-6" style="font-family: var(--font-serif)">Like What You See?</h2>
	<p class="text-sm text-white/70 mb-8 max-w-md mx-auto">
		Let's create imagery like this for your next listing.
	</p>
	<a
		href="/contact"
		class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10"
		>GET IN TOUCH</a
	>
</section>
