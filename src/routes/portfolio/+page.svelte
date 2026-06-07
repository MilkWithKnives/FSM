<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { onMount } from 'svelte';
	import { properties, propertyArea } from '$lib/properties';
	import {
		photoSrcset,
		heroFallback,
		PHOTO_SIZES_FULL,
		PHOTO_SIZES_HALF,
	} from '$lib/images';

	const INTERVAL_MS = 6000;
	const total = properties.length;

	let current = $state(0);
	let hovered = $state(false);
	let documentHidden = $state(false);
	let reducedMotion = $state(false);

	const paused = $derived(hovered || documentHidden || reducedMotion);

	function goto(i: number) {
		current = ((i % total) + total) % total;
	}
	function next() { goto(current + 1); }
	function prev() { goto(current - 1); }

	$effect(() => {
		if (paused) return;
		const id = setInterval(() => goto(current + 1), INTERVAL_MS);
		return () => clearInterval(id);
	});

	onMount(() => {
		const onVis = () => { documentHidden = document.hidden; };
		document.addEventListener('visibilitychange', onVis);

		const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
		const onMQ = () => { reducedMotion = mq.matches; };
		onMQ();
		mq.addEventListener('change', onMQ);

		return () => {
			document.removeEventListener('visibilitychange', onVis);
			mq.removeEventListener('change', onMQ);
		};
	});

	function onKey(e: KeyboardEvent) {
		if (e.key === 'ArrowRight') next();
		else if (e.key === 'ArrowLeft') prev();
	}
</script>

<Seo
	title="Portfolio | Full Scope Media LLC · Real Estate Photography East Lansing, MI"
	description="Browse Full Scope Media LLC's real estate photography and video portfolio — featuring properties across East Lansing, Lansing, Okemos, and Metro Detroit."
	ogTitle="Portfolio | Full Scope Media LLC"
	ogDescription="Real estate photography and video portfolio across East Lansing, Lansing, and greater Michigan."
/>

<!-- PAGE HEADER -->
<section class="pt-16 pb-6 px-5 md:px-10 lg:px-20 max-w-7xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-3">Our Work</p>
	<h1 class="text-4xl md:text-6xl font-light" style="font-family: var(--font-serif)">Portfolio</h1>
</section>

<!-- AUTO-ADVANCING HERO CAROUSEL -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<div
	class="relative w-full select-none"
	role="group"
	aria-roledescription="carousel"
	aria-label="Featured properties"
	onmouseenter={() => hovered = true}
	onmouseleave={() => hovered = false}
	onfocusin={() => hovered = true}
	onfocusout={() => hovered = false}
	onkeydown={onKey}
>
	<div class="relative w-full aspect-[4/3] sm:aspect-[16/9] md:aspect-[21/9] overflow-hidden bg-gray-100">
		{#each properties as project, i (project.slug)}
			<div
				class="absolute inset-0 transition-opacity duration-[1200ms] ease-in-out {i === current ? 'opacity-100 z-10' : 'opacity-0 z-0'}"
				aria-hidden={i === current ? 'false' : 'true'}
				aria-roledescription="slide"
				aria-label="{i + 1} of {total}: {project.address}"
			>
				<picture>
					<source type="image/webp" srcset={photoSrcset(project.slug, project.selected[0], 'webp')} sizes={PHOTO_SIZES_FULL} />
					<img
						src={heroFallback(project)}
						srcset={photoSrcset(project.slug, project.selected[0], 'jpg')}
						sizes={PHOTO_SIZES_FULL}
						alt="{project.address}, {propertyArea(project)}"
						loading={i === 0 ? 'eager' : 'lazy'}
						fetchpriority={i === 0 ? 'high' : 'auto'}
						decoding="async"
						class="absolute inset-0 w-full h-full object-cover"
					/>
				</picture>
				<div class="absolute inset-0 bg-gradient-to-t from-black/65 via-black/10 to-transparent pointer-events-none"></div>
				<a
					href="/portfolio/{project.slug}"
					class="absolute bottom-0 left-0 right-0 p-5 sm:p-8 md:p-12 text-white"
					tabindex={i === current ? 0 : -1}
				>
					<p class="text-xs tracking-[0.3em] uppercase mb-1 opacity-70">{project.tag}</p>
					<p class="text-xl sm:text-3xl md:text-4xl font-light" style="font-family: var(--font-serif)">{project.address}</p>
					<p class="text-sm opacity-60 mt-1">{propertyArea(project)}</p>
				</a>
			</div>
		{/each}

		<!-- prev / next controls -->
		<div class="absolute inset-0 flex items-center justify-between px-3 sm:px-6 z-20 pointer-events-none">
			<button
				type="button"
				onclick={prev}
				aria-label="Previous slide"
				class="btn btn-circle btn-sm bg-white/20 border border-white/30 text-white hover:bg-white hover:text-black hover:border-white transition-all backdrop-blur-sm pointer-events-auto"
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
					<path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
				</svg>
			</button>
			<button
				type="button"
				onclick={next}
				aria-label="Next slide"
				class="btn btn-circle btn-sm bg-white/20 border border-white/30 text-white hover:bg-white hover:text-black hover:border-white transition-all backdrop-blur-sm pointer-events-auto"
			>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
					<path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
				</svg>
			</button>
		</div>

		<div class="absolute top-4 right-4 sm:top-6 sm:right-8 z-20 text-white/70 text-xs tracking-widest pointer-events-none">
			{String(current + 1).padStart(2, '0')} / {String(total).padStart(2, '0')}
		</div>
	</div>

	<!-- dot indicators -->
	<div class="flex justify-center items-center gap-2.5 py-5 border-b border-gray-100">
		{#each properties as project, i (project.slug)}
			<button
				type="button"
				onclick={() => goto(i)}
				aria-label="Go to slide {i + 1}: {project.address}"
				aria-current={i === current}
				class="rounded-full transition-all duration-300 {i === current ? 'w-6 h-1.5 bg-black' : 'w-1.5 h-1.5 bg-gray-300 hover:bg-gray-500'}"
			></button>
		{/each}
	</div>
</div>

<!-- SIMPLER PORTFOLIO CARDS -->
<section class="px-5 md:px-10 lg:px-20 py-16 md:py-24 max-w-7xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-3 text-center">All Projects</p>
	<h2 class="text-2xl md:text-3xl font-light text-center mb-12" style="font-family: var(--font-serif)">Selected Work</h2>

	<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10">
		{#each properties as project (project.slug)}
			<a href="/portfolio/{project.slug}" class="group flex flex-col">
				<div class="overflow-hidden aspect-[4/3] bg-gray-100">
					<picture>
						<source type="image/webp" srcset={photoSrcset(project.slug, project.selected[0], 'webp')} sizes={PHOTO_SIZES_HALF} />
						<img
							src={heroFallback(project)}
							srcset={photoSrcset(project.slug, project.selected[0], 'jpg')}
							sizes={PHOTO_SIZES_HALF}
							alt="{project.address}, {propertyArea(project)}"
							loading="lazy"
							decoding="async"
							class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
						/>
					</picture>
				</div>
				<div class="pt-5">
					<p class="text-[10px] tracking-[0.3em] uppercase text-gray-400 mb-1.5">{project.tag}</p>
					<p class="text-xl font-light" style="font-family: var(--font-serif)">{project.address}</p>
					<p class="text-xs text-gray-500 mt-1">{propertyArea(project)}</p>
				</div>
			</a>
		{/each}
	</div>
</section>

<!-- INSTAGRAM SOCIAL -->
<section class="bg-gray-50 py-16 md:py-20 px-5 text-center border-t border-gray-100">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-4">Follow Along</p>
	<h2 class="text-2xl md:text-3xl font-light mb-6" style="font-family: var(--font-serif)">@full.scope.media</h2>
	<a href="https://instagram.com/full.scope.media" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs px-8">FOLLOW ON INSTAGRAM</a>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-20 md:py-24 px-5 text-center">
	<h2 class="text-3xl md:text-5xl font-light mb-6" style="font-family: var(--font-serif)">Work With Us</h2>
	<p class="text-sm text-white/70 mb-8 max-w-md mx-auto">Ready to elevate your next listing? Let's create something extraordinary together.</p>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
