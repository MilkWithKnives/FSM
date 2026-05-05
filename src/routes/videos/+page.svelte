<svelte:head>
	<title>Real Estate Video Tours | Full Scope Media LLC · East Lansing, MI</title>
	<meta name="description" content="Cinematic real estate video tours in East Lansing and greater Michigan. Professional property films delivered in 3–5 days. Aerial drone integration available." />
	<meta property="og:title" content="Real Estate Video Tours | Full Scope Media LLC" />
	<meta property="og:description" content="Cinematic real estate video tours with aerial drone integration. Serving East Lansing and greater Michigan." />
</svelte:head>

<script lang="ts">
	const videos = [
		{
			title: 'Hagadorn Rd · East Lansing',
			tag: 'Cinematic Tour',
			thumbnail: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=900&q=80&auto=format&fit=crop',
		},
		{
			title: 'Lake Dr · East Lansing',
			tag: 'Property Tour + Aerial',
			thumbnail: 'https://images.unsplash.com/photo-1613977257363-707ba9348227?w=900&q=80&auto=format&fit=crop',
		},
		{
			title: 'Grand River Ave · Grand Ledge',
			tag: 'Lifestyle Film',
			thumbnail: 'https://images.unsplash.com/photo-1449844908441-8829872d2607?w=900&q=80&auto=format&fit=crop',
		},
	];

	const includes = [
		'2–4 minute cinematic walkthrough',
		'Professional narration or music scoring',
		'Interior + exterior coverage',
		'Aerial drone integration available',
		'Optimized for MLS, social media, and web',
		'Delivered within 3–5 business days',
	];
</script>

<!-- HERO -->
<section class="relative h-[60vh] overflow-hidden">
	<img
		src="https://images.unsplash.com/photo-1613977257363-707ba9348227?w=1800&q=85&auto=format&fit=crop"
		alt="Real estate video production"
		class="absolute inset-0 w-full h-full object-cover"
	/>
	<div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
		<p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Services</p>
		<h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Video Tours</h1>
	</div>
</section>

<!-- INTRO -->
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
		<div>
			<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-6">Cinematic Property Films</p>
			<h2 class="text-3xl md:text-4xl font-light leading-snug mb-8" style="font-family: var(--font-serif)">
				Move buyers before they ever visit.
			</h2>
			<p class="text-sm text-gray-500 leading-relaxed mb-6">
				A great property video doesn't just show a home — it tells its story. Our cinematic video packages combine smooth motion, thoughtful composition, and expert color grading to produce films that feel like they belong in a luxury magazine.
			</p>
			<p class="text-sm text-gray-500 leading-relaxed mb-10">
				Listings with video receive significantly more engagement online. Add aerial drone footage for a complete, immersive package that sets your listing apart from every other property in the market.
			</p>
			<a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">BOOK A VIDEO SHOOT</a>
		</div>
		<div>
			<p class="text-xs tracking-widest uppercase text-gray-400 mb-6">Every Video Includes</p>
			<ul class="flex flex-col gap-3 mb-10">
				{#each includes as item}
					<li class="flex items-start gap-3 text-sm text-gray-600">
						<span class="text-black mt-1">—</span>
						{item}
					</li>
				{/each}
			</ul>
			<div class="pt-8 border-t border-gray-100">
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-2">Starting At</p>
				<p class="text-3xl font-light" style="font-family: var(--font-serif)">$480</p>
				<a href="/pricing" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity mt-4 inline-block">View Full Pricing</a>
			</div>
		</div>
	</div>
</section>

<!-- VIDEO SHOWCASE -->
<section class="px-8 lg:px-20 pb-28 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-10 text-center">Recent Productions</p>
	<div class="flex flex-col gap-8">
		{#each videos as video}
			<div class="group relative overflow-hidden aspect-[16/9] cursor-pointer">
				<img
					src={video.thumbnail}
					alt={video.title}
					class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
				/>
				<div class="absolute inset-0 bg-black/30 flex flex-col items-center justify-center text-white">
					<!-- Play button -->
					<div class="w-16 h-16 rounded-full border border-white/70 flex items-center justify-center mb-4 group-hover:bg-white/20 transition-colors">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 ml-1" fill="white" viewBox="0 0 24 24">
							<path d="M8 5v14l11-7z" />
						</svg>
					</div>
					<p class="text-lg font-light" style="font-family: var(--font-serif)">{video.title}</p>
					<p class="text-xs tracking-widest uppercase mt-1 opacity-70">{video.tag}</p>
				</div>
			</div>
		{/each}
	</div>
	<div class="text-center mt-12">
		<a href="/contact" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity">Inquire About Video Production</a>
	</div>
</section>

<!-- CTA -->
<section class="bg-neutral text-white py-24 px-8 text-center">
	<h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Let's Film Your Property</h2>
	<a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
