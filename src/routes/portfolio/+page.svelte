<svelte:head>
	<title>Portfolio | Full Scope Media LLC · Real Estate Photography East Lansing, MI</title>
	<meta name="description" content="Browse Full Scope Media LLC's real estate photography and video portfolio — featuring properties across East Lansing, Lansing, Okemos, and Metro Detroit." />
	<meta property="og:title" content="Portfolio | Full Scope Media LLC" />
	<meta property="og:description" content="Real estate photography and video portfolio across East Lansing, Lansing, and greater Michigan." />
</svelte:head>

<script lang="ts">
	const projects = [
		{
			address: 'Hagadorn Rd',
			area: 'East Lansing, MI',
			tag: 'Photos + Video',
			img: 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1400&q=85&auto=format&fit=crop',
		},
		{
			address: 'Hamilton Rd',
			area: 'Okemos, MI',
			tag: 'Photos',
			img: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1400&q=85&auto=format&fit=crop',
		},
		{
			address: 'Aurelius Rd',
			area: 'Lansing, MI',
			tag: 'Photos',
			img: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1400&q=85&auto=format&fit=crop',
		},
		{
			address: 'Lake Dr',
			area: 'East Lansing, MI',
			tag: 'Photos + Video',
			img: 'https://images.unsplash.com/photo-1613977257363-707ba9348227?w=1400&q=85&auto=format&fit=crop',
		},
		{
			address: 'Marsh Rd',
			area: 'Haslett, MI',
			tag: 'Photos + Video + Aerial',
			img: 'https://images.unsplash.com/photo-1449844908441-8829872d2607?w=1400&q=85&auto=format&fit=crop',
		},
		{
			address: 'Grand River Ave',
			area: 'Grand Ledge, MI',
			tag: 'Photos + Aerial',
			img: 'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=1400&q=85&auto=format&fit=crop',
		},
	];
</script>

<!-- PAGE HEADER -->
<section class="pt-16 pb-6 px-5 md:px-10 lg:px-20 max-w-7xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-3">Our Work</p>
	<h1 class="text-4xl md:text-6xl font-light" style="font-family: var(--font-serif)">Portfolio</h1>
</section>

<!-- FEATURED CAROUSEL -->
<section class="w-full">
	<div class="carousel w-full">
		{#each projects as project, i}
			<div id="slide-{i}" class="carousel-item relative w-full">
				<!-- Image -->
				<div class="w-full aspect-[4/3] sm:aspect-[16/9] md:aspect-[21/9] overflow-hidden">
					<img
						src={project.img}
						alt="{project.address}, {project.area}"
						loading={i === 0 ? 'eager' : 'lazy'}
						class="w-full h-full object-cover"
					/>
				</div>

				<!-- Gradient + text overlay -->
				<div class="absolute inset-0 bg-gradient-to-t from-black/65 via-black/10 to-transparent pointer-events-none"></div>
				<div class="absolute bottom-0 left-0 right-0 p-5 sm:p-8 md:p-12 text-white pointer-events-none">
					<p class="text-xs tracking-[0.3em] uppercase mb-1 opacity-70">{project.tag}</p>
					<p class="text-xl sm:text-3xl md:text-4xl font-light" style="font-family: var(--font-serif)">{project.address}</p>
					<p class="text-sm opacity-60 mt-1">{project.area}</p>
				</div>

				<!-- Prev / Next arrows -->
				<div class="absolute inset-0 flex items-center justify-between px-3 sm:px-6">
					<a
						href="#slide-{i === 0 ? projects.length - 1 : i - 1}"
						aria-label="Previous"
						class="btn btn-circle btn-sm bg-white/20 border border-white/30 text-white hover:bg-white hover:text-black hover:border-white transition-all backdrop-blur-sm"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
						</svg>
					</a>
					<a
						href="#slide-{i === projects.length - 1 ? 0 : i + 1}"
						aria-label="Next"
						class="btn btn-circle btn-sm bg-white/20 border border-white/30 text-white hover:bg-white hover:text-black hover:border-white transition-all backdrop-blur-sm"
					>
						<svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
							<path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
						</svg>
					</a>
				</div>

				<!-- Slide counter (top right) -->
				<div class="absolute top-4 right-4 sm:top-6 sm:right-8 text-white/60 text-xs tracking-widest pointer-events-none">
					{String(i + 1).padStart(2, '0')} / {String(projects.length).padStart(2, '0')}
				</div>
			</div>
		{/each}
	</div>

	<!-- Dot navigation -->
	<div class="flex justify-center items-center gap-2 py-5 border-b border-gray-100">
		{#each projects as project, i}
			<a
				href="#slide-{i}"
				aria-label="Go to {project.address}"
				class="w-1.5 h-1.5 rounded-full bg-gray-300 hover:bg-black transition-colors duration-200"
			></a>
		{/each}
	</div>
</section>

<!-- FULL PORTFOLIO GRID -->
<section class="px-5 md:px-10 lg:px-20 py-16 md:py-24 max-w-7xl mx-auto">
	<div class="flex flex-col">
		{#each projects as project, i}
			<div class="group grid grid-cols-1 md:grid-cols-2 gap-0 border-t border-gray-100 {i === projects.length - 1 ? 'border-b' : ''}">
				<div class="overflow-hidden aspect-[16/10] {i % 2 === 1 ? 'md:order-2' : ''}">
					<img
						src={project.img}
						alt="{project.address}, {project.area}"
						loading="lazy"
						class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
					/>
				</div>
				<div class="flex flex-col justify-center px-5 py-10 md:px-12 md:py-16 {i % 2 === 1 ? 'md:order-1' : ''}">
					<p class="text-xs tracking-[0.3em] uppercase text-gray-400 mb-4">{project.tag}</p>
					<h2 class="text-2xl md:text-4xl font-light mb-2" style="font-family: var(--font-serif)">{project.address}</h2>
					<p class="text-sm text-gray-500 mb-8">{project.area}</p>
					<a href="/contact" class="text-xs tracking-widest uppercase border-b border-black pb-1 hover:opacity-60 transition-opacity w-fit">Inquire About This Property</a>
				</div>
			</div>
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
