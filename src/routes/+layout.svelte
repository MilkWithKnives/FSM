<script lang="ts">
	import logo from '$lib/assets/logo.svg';
	import '../app.css';
	import { page } from '$app/stores';
	import { locations } from '$lib/locations';
	import { businessJsonLd } from '$lib/business';

	let { children } = $props();

	let mobileOpen = $state(false);

	const navLinks = [
		{ href: '/portfolio', label: 'Portfolio' },
		{ href: '/pricing', label: 'Pricing' },
		{ href: '/faq', label: 'FAQ' },
		{ href: '/about', label: 'About' },
		{ href: '/journal', label: 'Journal' },
		{ href: '/contact', label: 'Contact' },
	];

	function isActive(href: string) {
		return $page.url.pathname === href;
	}

	$effect(() => {
		if (mobileOpen) {
			document.body.style.overflow = 'hidden';
		} else {
			document.body.style.overflow = '';
		}
	});
</script>

<svelte:head>
	<!-- Favicons are declared in app.html. -->
	<!-- Per-page title/description/OG are rendered by the <Seo> component on each route. -->
	<!-- Analytics is handled by Google Tag Manager (GTM-N8RVSFDH) in app.html. -->

	<!-- Local Business JSON-LD (single source of truth in $lib/business.ts) -->
	{@html `<script type="application/ld+json">${JSON.stringify(businessJsonLd)}<\/script>`}
</svelte:head>

<div class="drawer">
	<input id="nav-drawer" type="checkbox" class="drawer-toggle" bind:checked={mobileOpen} />

	<div class="drawer-content flex flex-col min-h-screen">

		<!-- NAVBAR -->
		<nav class="navbar fixed top-0 z-50 bg-white border-b border-gray-100 px-3 lg:px-8 h-16 min-h-[4rem]">

			<!-- START: hamburger (mobile) | logo (desktop) -->
			<div class="navbar-start">
				<!-- Hamburger: mobile only -->
				<label for="nav-drawer" class="btn btn-ghost btn-square btn-sm lg:hidden" aria-label="Open menu">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16" />
					</svg>
				</label>
				<!-- Logo: desktop only (in start position) -->
				<a href="/" class="hidden lg:flex items-center gap-3" aria-label="Full Scope Media LLC">
					<img src={logo} alt="Full Scope Media LLC logo" class="h-9 w-auto rounded-sm" />
					<span class="text-sm font-semibold tracking-[0.12em] leading-tight" style="font-family: var(--font-brand)">FULL SCOPE<br/>MEDIA</span>
				</a>
			</div>

			<!-- CENTER: logo (mobile) | nav links (desktop) -->
			<div class="navbar-center">
				<!-- Logo: mobile only (centered) -->
				<a href="/" class="lg:hidden" aria-label="Full Scope Media LLC">
					<img src={logo} alt="Full Scope Media LLC" class="h-8 w-auto rounded-sm" />
				</a>

				<!-- Nav links: desktop only -->
				<ul class="hidden lg:flex items-center gap-6">
					<li>
						<div class="dropdown dropdown-hover">
							<div tabindex="0" role="button" class="text-xs tracking-wider uppercase text-gray-500 hover:text-black transition-colors cursor-pointer flex items-center gap-1 py-1">
								Services
								<svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
								</svg>
							</div>
							<ul class="dropdown-content z-10 menu bg-white shadow-lg border border-gray-100 rounded-none p-2 w-44 mt-1">
								<li><a href="/photos" class="text-xs tracking-wider uppercase text-gray-500 hover:text-black rounded-none">Photos</a></li>
								<li><a href="/videos" class="text-xs tracking-wider uppercase text-gray-500 hover:text-black rounded-none">Videos</a></li>
								<li><a href="/3d-tours" class="text-xs tracking-wider uppercase text-gray-500 hover:text-black rounded-none">3D Tours</a></li>
								<li><a href="/floor-plans" class="text-xs tracking-wider uppercase text-gray-500 hover:text-black rounded-none">Floor Plans</a></li>
								<li><a href="/virtual-staging" class="text-xs tracking-wider uppercase text-gray-500 hover:text-black rounded-none">Virtual Staging</a></li>
							</ul>
						</div>
					</li>
					{#each navLinks as link}
						<li>
							<a
								href={link.href}
								class="text-xs tracking-wider uppercase transition-colors {isActive(link.href) ? 'text-black border-b border-black pb-0.5' : 'text-gray-500 hover:text-black'}"
							>
								{link.label}
							</a>
						</li>
					{/each}
				</ul>
			</div>

			<!-- END: Book Us button (always) -->
			<div class="navbar-end">
				<a href="/contact" class="cta" aria-label="Book us">
					<span>BOOK US</span>
					<svg width="15" height="10" viewBox="0 0 13 10" aria-hidden="true">
						<path d="M1,5 L11,5"></path>
						<polyline points="8 1 12 5 8 9"></polyline>
					</svg>
				</a>
			</div>
		</nav>

		<!-- PAGE CONTENT -->
		<main class="pt-16 flex-1">
			{@render children()}
		</main>

		<!-- FOOTER -->
		<footer class="bg-white border-t border-gray-100 py-12 lg:py-16 px-6 lg:px-20">
			<div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-10">
				<div class="col-span-2 md:col-span-1">
					<a href="/" class="flex items-center gap-3 mb-4">
						<img src={logo} alt="Full Scope Media LLC" class="h-12 w-auto rounded-sm" />
						<span class="text-sm font-semibold tracking-[0.12em] leading-tight" style="font-family: var(--font-brand)">FULL SCOPE<br/>MEDIA</span>
					</a>
					<p class="text-sm text-gray-500 leading-relaxed">Luxury real estate photography & media. East Lansing, MI.</p>
				</div>
				<div>
					<p class="text-xs tracking-widest uppercase text-gray-500 mb-4">Navigate</p>
					<ul class="space-y-2.5">
						<li><a href="/portfolio" class="text-sm text-gray-600 hover:text-black transition-colors">Portfolio</a></li>
						<li><a href="/about" class="text-sm text-gray-600 hover:text-black transition-colors">About</a></li>
						<li><a href="/faq" class="text-sm text-gray-600 hover:text-black transition-colors">FAQ</a></li>
						<li><a href="/journal" class="text-sm text-gray-600 hover:text-black transition-colors">Journal</a></li>
						<li><a href="/contact" class="text-sm text-gray-600 hover:text-black transition-colors">Contact</a></li>
					</ul>
				</div>
				<div>
					<p class="text-xs tracking-widest uppercase text-gray-500 mb-4">Services</p>
					<ul class="space-y-2.5">
						<li><a href="/photos" class="text-sm text-gray-600 hover:text-black transition-colors">Photography</a></li>
						<li><a href="/videos" class="text-sm text-gray-600 hover:text-black transition-colors">Video Tours</a></li>
						<li><a href="/3d-tours" class="text-sm text-gray-600 hover:text-black transition-colors">3D Tours</a></li>
						<li><a href="/floor-plans" class="text-sm text-gray-600 hover:text-black transition-colors">Floor Plans</a></li>
						<li><a href="/virtual-staging" class="text-sm text-gray-600 hover:text-black transition-colors">Virtual Staging</a></li>
						<li><a href="/pricing" class="text-sm text-gray-600 hover:text-black transition-colors">Pricing</a></li>
					</ul>
				</div>
				<div>
					<p class="text-xs tracking-widest uppercase text-gray-500 mb-4">Contact</p>
					<a href="tel:+19895779513" class="text-sm text-gray-600 hover:text-black transition-colors block">(989) 577-9513</a>
					<a href="mailto:info@fullscope-media.com" class="text-sm text-gray-600 hover:text-black transition-colors block mt-1">info@fullscope-media.com</a>
					<p class="text-sm text-gray-600 mt-1">East Lansing, MI</p>
					<a href="https://instagram.com/full.scope.media" class="text-xs tracking-widest uppercase text-gray-500 hover:text-black transition-colors mt-3 inline-block">@full.scope.media</a>
				</div>
			</div>

			<!-- AREAS WE SERVE -->
			<div class="max-w-6xl mx-auto mt-10 pt-8 border-t border-gray-100">
				<p class="text-xs tracking-widest uppercase text-gray-500 mb-4">Areas We Serve</p>
				<ul class="flex flex-wrap gap-x-6 gap-y-2">
					{#each locations as loc}
						<li>
							<a href="/real-estate-photographer/{loc.slug}" class="text-sm text-gray-600 hover:text-black transition-colors">
								Real Estate Photographer in {loc.city}
							</a>
						</li>
					{/each}
				</ul>
			</div>

			<!-- SOCIAL ICONS -->
			<div class="max-w-6xl mx-auto mt-10 pt-8 border-t border-gray-100 flex flex-col sm:flex-row justify-between items-center gap-6">
				<p class="text-xs text-gray-500">© 2026 Full Scope Media LLC. All rights reserved.</p>

				<div class="social-login-icons">
					<!-- X / Twitter -->
					<div class="socialcontainer">
						<div class="icon social-icon-1-1">
							<svg viewBox="0 0 512 512" height="1.7em" xmlns="http://www.w3.org/2000/svg" fill="currentColor">
								<path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"/>
							</svg>
						</div>
						<div class="social-icon-1">
							<svg viewBox="0 0 512 512" height="1.7em" xmlns="http://www.w3.org/2000/svg" fill="white">
								<path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"/>
							</svg>
						</div>
					</div>
					<!-- Instagram -->
					<div class="socialcontainer">
						<div class="icon social-icon-2-2">
							<svg fill="currentColor" viewBox="0 0 448 512" height="1.5em" xmlns="http://www.w3.org/2000/svg">
								<path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/>
							</svg>
						</div>
						<div class="social-icon-2">
							<svg fill="white" viewBox="0 0 448 512" height="1.5em" xmlns="http://www.w3.org/2000/svg">
								<path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/>
							</svg>
						</div>
					</div>
					<!-- Facebook -->
					<div class="socialcontainer">
						<div class="icon social-icon-3-3">
							<svg viewBox="0 0 384 512" fill="currentColor" height="1.6em" xmlns="http://www.w3.org/2000/svg">
								<path d="M80 299.3V512H196V299.3h86.5l18-97.8H196V166.9c0-51.7 20.3-71.5 72.7-71.5c16.3 0 29.4 .4 37 1.2V7.9C291.4 4 256.4 0 236.2 0C129.3 0 80 50.5 80 159.4v42.1H14v97.8H80z"/>
							</svg>
						</div>
						<div class="social-icon-3">
							<svg viewBox="0 0 384 512" fill="white" height="1.6em" xmlns="http://www.w3.org/2000/svg">
								<path d="M80 299.3V512H196V299.3h86.5l18-97.8H196V166.9c0-51.7 20.3-71.5 72.7-71.5c16.3 0 29.4 .4 37 1.2V7.9C291.4 4 256.4 0 236.2 0C129.3 0 80 50.5 80 159.4v42.1H14v97.8H80z"/>
							</svg>
						</div>
					</div>
					<!-- GitHub -->
					<div class="socialcontainer">
						<div class="icon social-icon-4-4">
							<svg fill="currentColor" viewBox="0 0 496 512" height="1.6em">
								<path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/>
							</svg>
						</div>
						<div class="social-icon-4">
							<svg fill="white" viewBox="0 0 496 512" height="1.6em">
								<path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/>
							</svg>
						</div>
					</div>
				</div>

				<p class="text-xs text-gray-500">East Lansing, MI</p>
			</div>
		</footer>

	</div>

	<!-- MOBILE DRAWER MENU -->
	<div class="drawer-side z-[60]">
		<label for="nav-drawer" class="drawer-overlay" aria-label="Close menu"></label>
		<div class="bg-white min-h-full w-[280px] p-6 flex flex-col">
			<div class="flex justify-between items-center mb-8">
				<a href="/" class="flex items-center gap-3" aria-label="Full Scope Media LLC" onclick={() => mobileOpen = false}>
					<img src={logo} alt="Full Scope Media LLC" class="h-9 w-auto rounded-sm" />
					<span class="text-sm font-semibold tracking-[0.12em] leading-tight" style="font-family: var(--font-brand)">FULL SCOPE<br/>MEDIA</span>
				</a>
				<label for="nav-drawer" class="btn btn-ghost btn-square btn-sm" aria-label="Close menu">
					<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12" />
					</svg>
				</label>
			</div>
			<ul class="flex flex-col gap-5">
				<li><a href="/portfolio" class="text-base tracking-wider text-gray-800" onclick={() => mobileOpen = false}>Portfolio</a></li>
				<li>
					<p class="text-xs tracking-widest uppercase text-gray-500 mb-3">Services</p>
					<ul class="flex flex-col gap-3 pl-3">
						<li><a href="/photos" class="text-sm tracking-wider text-gray-700" onclick={() => mobileOpen = false}>Photos</a></li>
						<li><a href="/videos" class="text-sm tracking-wider text-gray-700" onclick={() => mobileOpen = false}>Videos</a></li>
						<li><a href="/3d-tours" class="text-sm tracking-wider text-gray-700" onclick={() => mobileOpen = false}>3D Tours</a></li>
						<li><a href="/floor-plans" class="text-sm tracking-wider text-gray-700" onclick={() => mobileOpen = false}>Floor Plans</a></li>
						<li><a href="/virtual-staging" class="text-sm tracking-wider text-gray-700" onclick={() => mobileOpen = false}>Virtual Staging</a></li>
					</ul>
				</li>
				<li><a href="/pricing" class="text-base tracking-wider text-gray-800" onclick={() => mobileOpen = false}>Pricing</a></li>
				<li><a href="/faq" class="text-base tracking-wider text-gray-800" onclick={() => mobileOpen = false}>FAQ</a></li>
				<li><a href="/about" class="text-base tracking-wider text-gray-800" onclick={() => mobileOpen = false}>About</a></li>
				<li><a href="/journal" class="text-base tracking-wider text-gray-800" onclick={() => mobileOpen = false}>Journal</a></li>
				<li><a href="/contact" class="text-base tracking-wider text-gray-800" onclick={() => mobileOpen = false}>Contact</a></li>
			</ul>
			<div class="mt-auto pt-8">
				<a href="/contact" class="btn btn-neutral w-full rounded-none tracking-widest text-xs" onclick={() => mobileOpen = false}>BOOK US</a>
			</div>
		</div>
	</div>
</div>

<style>
  /* ── Navbar Book Us CTA (Uiverse: alexmaracinaru) ── */
  .cta {
    position: relative;
    padding: 10px 16px;
    display: inline-flex;
    align-items: center;
    transition: transform 0.2s ease;
    border: none;
    background: none;
    cursor: pointer;
    text-decoration: none;
  }

  .cta::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    display: block;
    border-radius: 50px;
    background: #b1dae7;
    width: 40px;
    height: 40px;
    transition: width 0.3s ease, background 0.3s ease;
  }

  .cta span {
    position: relative;
    font-family: var(--font-sans);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #234567;
  }

  .cta svg {
    position: relative;
    margin-left: 10px;
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke: #234567;
    stroke-width: 2;
    transform: translateX(-5px);
    transition: transform 0.3s ease;
  }

  .cta:hover::before {
    width: 100%;
    background: #9fd0e0;
  }

  .cta:hover svg {
    transform: translateX(0);
  }

  .cta:active {
    transform: scale(0.95);
  }

  @media (prefers-reduced-motion: reduce) {
    .cta, .cta::before, .cta svg {
      transition: none;
    }
  }

  /* ── Social icon bounce animation ── */
  .social-login-icons {
    display: flex;
    align-items: center;
    gap: 10px;
    -webkit-box-reflect: below 4px linear-gradient(transparent, #00000030);
  }

  .socialcontainer {
    height: 80px;
    overflow: hidden;
  }

  .social-icon-1,   .social-icon-1-1,
  .social-icon-2,   .social-icon-2-2,
  .social-icon-3,   .social-icon-3-3,
  .social-icon-4,   .social-icon-4-4 {
    width: 46px;
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50px;
    margin: 17px 0 0 0;
  }

  /* Idle state: plain dark circle */
  .social-icon-1-1,
  .social-icon-2-2,
  .social-icon-3-3,
  .social-icon-4-4 {
    background-color: transparent;
    transition-duration: 0.4s;
  }

  .icon svg {
    fill: #555;
    transition: fill 0.3s ease;
  }
  .socialcontainer:hover .icon svg {
    fill: #111;
  }

  /* Colored hover icons start invisible */
  .social-icon-1 svg,
  .social-icon-2 svg,
  .social-icon-3 svg,
  .social-icon-4 svg {
    opacity: 0;
    transition: opacity 0.5s ease 0.2s;
  }
  .socialcontainer:hover .social-icon-1 svg,
  .socialcontainer:hover .social-icon-2 svg,
  .socialcontainer:hover .social-icon-3 svg,
  .socialcontainer:hover .social-icon-4 svg {
    opacity: 1;
  }

  /* X / Twitter */
  .social-icon-1 {
    background-color: #000;
    transition: transform 0.4s cubic-bezier(0.46, -0.78, 0.5, 1.56);
  }
  .socialcontainer:hover .social-icon-1 { transform: translateY(-63px); }

  /* Instagram */
  .social-icon-2 {
    background: linear-gradient(72.44deg, #ff7a00 11.92%, #ff0169 51.56%, #d300c5 85.69%);
    transition: transform 0.4s cubic-bezier(0.46, -0.78, 0.5, 1.56);
  }
  .socialcontainer:hover .social-icon-2 { transform: translateY(-63px); }

  /* Facebook */
  .social-icon-3 {
    background: #316ff6;
    transition: transform 0.4s cubic-bezier(0.46, -0.78, 0.5, 1.56);
  }
  .socialcontainer:hover .social-icon-3 { transform: translateY(-63px); }

  /* GitHub */
  .social-icon-4 {
    background: linear-gradient(180deg, #81229066 0%, #4d227c 91%);
    transition: transform 0.4s cubic-bezier(0.46, -0.78, 0.5, 1.56);
  }
  .socialcontainer:hover .social-icon-4 { transform: translateY(-63px); }
</style>
