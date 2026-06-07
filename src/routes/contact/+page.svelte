<script lang="ts">
	import Seo from '$lib/Seo.svelte';
	import { enhance } from '$app/forms';
	import { onMount } from 'svelte';
	import { properties } from '$lib/properties';
	import { photoSrcset, photoFallback, PHOTO_SIZES_HALF } from '$lib/images';

	const sideProperty = properties[1];
	const sidePhoto = sideProperty.selected[1] ?? sideProperty.selected[0];

	let { form: actionResult } = $props();

	let formData = $state({
		name: '',
		email: '',
		phone: '',
		address: '',
		services: [] as string[],
		date: '',
		message: '',
	});

	const serviceOptions = ['Photography', 'Video Tour', 'Aerial Drone', 'Floorplan', 'Matterport', 'Full Package'];
	const calConfig = '{"layout":"month_view","useSlotsViewOnSmallScreen":"true","theme":"dark"}';

	function toggleService(service: string) {
		if (formData.services.includes(service)) {
			formData.services = formData.services.filter(s => s !== service);
		} else {
			formData.services = [...formData.services, service];
		}
	}

	onMount(() => {
		const s = document.createElement('script');
		s.type = 'text/javascript';
		s.textContent = `
			(function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if(typeof namespace === "string"){cal.ns[namespace] = cal.ns[namespace] || api;p(cal.ns[namespace], ar);p(cal, ["initNamespace", namespace]);} else p(cal, ar); return;} p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
			Cal("init", "interior-exterior-photos", {origin:"https://app.cal.com"});
			Cal.ns["interior-exterior-photos"]("ui", {"theme":"dark","cssVarsPerTheme":{"light":{"cal-brand":"#ffffff"},"dark":{"cal-brand":"#000000"}},"hideEventTypeDetails":false,"layout":"month_view"});
		`;
		document.head.appendChild(s);
	});
</script>

<Seo
	title="Book a Shoot | Full Scope Media LLC · Real Estate Photography East Lansing, MI"
	description="Book a real estate photography or video shoot with Full Scope Media LLC. Serving East Lansing, Lansing, Okemos, and greater Michigan. Get in touch today."
	ogTitle="Book a Shoot | Full Scope Media LLC"
	ogDescription="Book a real estate photography or video shoot in East Lansing, MI. Get in touch with Full Scope Media LLC today."
/>

<!-- HEADER -->
<section class="pt-20 pb-16 px-8 lg:px-20 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-4">Get In Touch</p>
	<h1 class="text-5xl md:text-7xl font-light mb-10" style="font-family: var(--font-serif)">Book a Shoot</h1>

	<div class="flex flex-col sm:flex-row items-start sm:items-center gap-6">
		<button
			data-cal-link="full.scope.media/interior-exterior-photos"
			data-cal-namespace="interior-exterior-photos"
			data-cal-config={calConfig}
			class="btn btn-neutral rounded-none tracking-widest text-xs px-12"
		>
			SCHEDULE A SHOOT
		</button>
		<p class="text-xs text-gray-400 tracking-wide">Opens availability calendar — confirmation sent automatically</p>
	</div>
</section>

<div class="border-t border-gray-100 max-w-6xl mx-auto px-8 lg:px-20"></div>

<!-- INQUIRY FORM + INFO -->
<section class="px-8 lg:px-20 py-20 max-w-6xl mx-auto">
	<p class="text-xs tracking-[0.4em] uppercase text-gray-400 mb-2">Have Questions First?</p>
	<p class="text-sm text-gray-500 mb-12">Send us a detailed inquiry and we'll follow up within 1–2 business days.</p>

	<div class="grid grid-cols-1 md:grid-cols-3 gap-16">

		<!-- FORM -->
		<div class="md:col-span-2">
			{#if actionResult?.success}
				<div class="py-20 text-center">
					<p class="text-4xl font-light mb-4" style="font-family: var(--font-serif)">Thank You</p>
					<p class="text-sm text-gray-500">We've received your inquiry and will be in touch within 1–2 business days.</p>
				</div>
			{:else}
				{#if actionResult?.error}
					<p class="text-sm text-red-600 mb-6 p-4 border border-red-200 bg-red-50">{actionResult.error}</p>
				{/if}

				<form method="POST" class="flex flex-col gap-6" use:enhance>
					<!-- Hidden inputs for selected services -->
					{#each formData.services as s}
						<input type="hidden" name="services" value={s} />
					{/each}

					<div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
						<div class="flex flex-col gap-1">
							<label for="name" class="text-xs tracking-widest uppercase text-gray-400">Full Name *</label>
							<input id="name" name="name" type="text" bind:value={formData.name} required class="input input-bordered rounded-none border-gray-300 focus:outline-none focus:border-black text-sm" placeholder="Jane Smith" />
						</div>
						<div class="flex flex-col gap-1">
							<label for="email" class="text-xs tracking-widest uppercase text-gray-400">Email *</label>
							<input id="email" name="email" type="email" bind:value={formData.email} required class="input input-bordered rounded-none border-gray-300 focus:outline-none focus:border-black text-sm" placeholder="jane@example.com" />
						</div>
					</div>

					<div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
						<div class="flex flex-col gap-1">
							<label for="phone" class="text-xs tracking-widest uppercase text-gray-400">Phone</label>
							<input id="phone" name="phone" type="tel" bind:value={formData.phone} class="input input-bordered rounded-none border-gray-300 focus:outline-none focus:border-black text-sm" placeholder="(989) 555-0100" />
						</div>
						<div class="flex flex-col gap-1">
							<label for="date" class="text-xs tracking-widest uppercase text-gray-400">Preferred Shoot Date</label>
							<input id="date" name="date" type="date" bind:value={formData.date} class="input input-bordered rounded-none border-gray-300 focus:outline-none focus:border-black text-sm" />
						</div>
					</div>

					<div class="flex flex-col gap-1">
						<label for="address" class="text-xs tracking-widest uppercase text-gray-400">Property Address *</label>
						<input id="address" name="address" type="text" bind:value={formData.address} required class="input input-bordered rounded-none border-gray-300 focus:outline-none focus:border-black text-sm" placeholder="123 Hagadorn Rd, East Lansing, MI" />
					</div>

					<div class="flex flex-col gap-2">
						<p class="text-xs tracking-widest uppercase text-gray-400">Services Needed</p>
						<div class="flex flex-wrap gap-2">
							{#each serviceOptions as service}
								<button
									type="button"
									onclick={() => toggleService(service)}
									class="btn btn-sm rounded-none tracking-widest text-xs {formData.services.includes(service) ? 'btn-neutral' : 'btn-outline border-gray-300 text-gray-600 hover:border-black hover:text-black hover:bg-transparent'}"
								>
									{service}
								</button>
							{/each}
						</div>
					</div>

					<div class="flex flex-col gap-1">
						<label for="message" class="text-xs tracking-widest uppercase text-gray-400">Additional Notes</label>
						<textarea id="message" name="message" bind:value={formData.message} rows="5" class="textarea textarea-bordered rounded-none border-gray-300 focus:outline-none focus:border-black text-sm resize-none" placeholder="Tell us about the property, any special requests, or questions you have..."></textarea>
					</div>

					<div>
						<button type="submit" class="btn btn-neutral rounded-none tracking-widest text-xs px-12">SUBMIT INQUIRY</button>
					</div>
				</form>
			{/if}
		</div>

		<!-- INFO SIDEBAR -->
		<div class="flex flex-col gap-10">
			<div>
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-4">Call Us</p>
				<a href="tel:+19895779513" class="text-sm text-gray-700 hover:text-black transition-colors">(989) 577-9513</a>
			</div>
			<div>
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-4">Email Us</p>
				<a href="mailto:info@fullscope-media.com" class="text-sm text-gray-700 hover:text-black transition-colors">info@fullscope-media.com</a>
			</div>
			<div>
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-4">Based In</p>
				<p class="text-sm text-gray-700">East Lansing, Michigan</p>
				<p class="text-xs text-gray-400 mt-1">Serving East Lansing · Lansing · Metro Detroit</p>
			</div>
			<div>
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-4">Turnaround</p>
				<p class="text-sm text-gray-700">Edited photos delivered within 24–48 hours of your shoot.</p>
			</div>
			<div class="border-t border-gray-100 pt-8">
				<p class="text-xs tracking-widest uppercase text-gray-400 mb-4">Follow Along</p>
				<a href="https://instagram.com/full.scope.media" class="text-sm text-gray-700 hover:text-black transition-colors">@full.scope.media</a>
			</div>
			<div class="overflow-hidden aspect-[4/5]">
				<picture>
					<source type="image/webp" srcset={photoSrcset(sideProperty.slug, sidePhoto, 'webp')} sizes={PHOTO_SIZES_HALF} />
					<img
						src={photoFallback(sideProperty.slug, sidePhoto)}
						srcset={photoSrcset(sideProperty.slug, sidePhoto, 'jpg')}
						sizes={PHOTO_SIZES_HALF}
						alt="{sideProperty.address}, {sideProperty.city}, {sideProperty.state}"
						loading="lazy"
						decoding="async"
						class="w-full h-full object-cover"
					/>
				</picture>
			</div>
		</div>

	</div>
</section>
