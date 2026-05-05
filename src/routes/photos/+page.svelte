<svelte:head>
	<title>Real Estate Photography | Full Scope Media LLC · East Lansing, MI</title>
	<meta name="description" content="Professional real estate photography in East Lansing and greater Michigan. 40+ fully edited photos, delivered in 24–48 hours. Serving Lansing, Okemos, and Metro Detroit." />
	<meta property="og:title" content="Real Estate Photography | Full Scope Media LLC" />
	<meta property="og:description" content="40+ fully edited real estate photos delivered in 24–48 hours. Serving East Lansing and greater Michigan." />
</svelte:head>

<script lang="ts">
	const gallery = [
		'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1613977257592-4871e5fcd7c4?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1565182999561-18d7dc61c393?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=900&q=80&auto=format&fit=crop',
		'https://images.unsplash.com/photo-1449844908441-8829872d2607?w=900&q=80&auto=format&fit=crop',
	];

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

<!-- HERO -->
<section class="relative h-[60vh] overflow-hidden">
	<img
		src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1800&q=85&auto=format&fit=crop"
		alt="Real estate photography"
		class="absolute inset-0 w-full h-full object-cover"
	/>
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
		{#each gallery as src, i}
			<div class="overflow-hidden break-inside-avoid">
				<img
					src={src}
					alt="Property photo {i + 1}"
					class="w-full object-cover hover:scale-105 transition-transform duration-500"
				/>
			</div>
		{/each}
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Ready to Shoot?</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
