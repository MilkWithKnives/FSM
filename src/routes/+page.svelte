<script lang="ts">
 import Seo from '$lib/Seo.svelte';
 import { serviceRates, rate, priceLabel } from '$lib/pricing';
 import { properties } from '$lib/properties';
 import { heroFallback } from '$lib/images';
 import Testimonials from '$lib/Testimonials.svelte';
 import LocationLinks from '$lib/LocationLinks.svelte';
 import PersonalService from '$lib/PersonalService.svelte';
 import EyeMotif from '$lib/EyeMotif.svelte';
 const local = properties.filter(property => ['East Lansing', 'Lansing', 'Okemos'].includes(property.city));
</script>
<Seo title="East Lansing Real Estate Photographer | Full Scope Media"
 description={`Real estate photography in East Lansing. Basic starts at ${priceLabel(rate('basic'))} with a CubiCasa floor plan and 24-hour delivery. Work directly with your photographer.`} />
<main class="root-content pt-[100dvh]">
 <section class="py-20 px-8 lg:px-20 max-w-6xl mx-auto">
  <p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-6">Full Scope Media · East Lansing, Michigan</p>
  <h1 class="text-4xl md:text-6xl font-light mb-8" style="font-family: var(--font-serif)">Real estate photography in East Lansing</h1>
  <p class="text-sm text-gray-600 leading-relaxed max-w-2xl">Interior and exterior photography that gives buyers a clear view of the property. Basic starts at {priceLabel(rate('basic'))}, with a CubiCasa floor plan included and photos delivered within 24 hours. {rate('basic').qualifier}</p>
  <a href="/real-estate-photography" class="btn btn-neutral rounded-none tracking-widest text-xs mt-8">EXPLORE REAL ESTATE MEDIA</a>
 </section>
 <PersonalService />
 <section class="py-16 px-8 lg:px-20 max-w-6xl mx-auto">
  <div class="mb-10"><EyeMotif /></div>
  <h2 class="text-3xl md:text-4xl font-light mb-10" style="font-family: var(--font-serif)">Choose the services your property needs</h2>
  <div class="grid md:grid-cols-2 gap-8">
   {#each serviceRates.filter(service => !service.inquireOnly) as service}
    <article class="border-t border-gray-100 pt-6"><h3 class="text-xl font-light mb-3"><a href={service.path} class="underline underline-offset-4">{service.name}</a></h3><p class="text-sm text-gray-600">{service.inclusions.join(' · ')}. {service.qualifier}</p></article>
   {/each}
  </div>
  <a href="/pricing" class="inline-block mt-8 underline underline-offset-4">View all à la carte rates</a>
 </section>
 <section class="py-16 px-8 lg:px-20 max-w-6xl mx-auto">
  <h2 class="text-3xl md:text-4xl font-light mb-10" style="font-family: var(--font-serif)">Local properties, delivered work</h2>
  <div class="grid md:grid-cols-3 gap-8">
   {#each local as property}<a href="/portfolio/{property.slug}"><img src={heroFallback(property, 800)} alt={`${property.address}, ${property.city}`} width="800" height="533" class="w-full aspect-[3/2] object-cover" /><p class="text-sm mt-4">{property.address} · {property.city}</p></a>{/each}
  </div>
 </section>
 <Testimonials />
 <LocationLinks />
 <section class="bg-neutral text-white py-20 px-8 text-center">
  <h2 class="text-3xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Tell me about your next listing</h2>
  <a href="/contact" class="btn btn-outline rounded-none text-white border-white">BOOK A SHOOT</a>
  <p class="text-sm mt-8">Looking for web design or brand work? <a href="/studio" class="underline underline-offset-4">Visit the Studio</a>.</p>
 </section>
</main>
