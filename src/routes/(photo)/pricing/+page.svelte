<script lang="ts">
 import Seo from '$lib/Seo.svelte';
	import Testimonials from '$lib/Testimonials.svelte';
 import { serviceRates, rate, priceLabel } from '$lib/pricing';
</script>
<Seo title="Real Estate Photography Pricing | Full Scope Media · East Lansing, MI"
 description={`Real estate photography starting at ${priceLabel(rate('basic'))}. Basic includes interior and exterior photos, a CubiCasa floor plan and 24-hour delivery. Serving East Lansing and greater Michigan.`} />
<section class="pt-20 pb-16 px-8 lg:px-20 max-w-6xl mx-auto">
 <p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-4">Flat à la carte pricing</p>
 <h1 class="text-5xl md:text-7xl font-light mb-8" style="font-family: var(--font-serif)">Pricing</h1>
 <p class="text-sm text-gray-500 max-w-xl leading-relaxed">Enough photos to do the property justice, with the time and attention it needs. Start with Basic, then choose any other services individually.</p>
</section>
<section class="px-8 lg:px-20 pb-24 max-w-6xl mx-auto" aria-label="Service rates">
 {#each serviceRates as service (service.id)}
 <article class="border-t border-gray-100 py-10 grid md:grid-cols-2 gap-6">
  <div>
   <h2 class="text-2xl md:text-3xl font-light mb-4" style="font-family: var(--font-serif)"><a href={service.path}>{service.name}</a></h2>
   {#each service.inclusions as inclusion}<p class="text-sm text-gray-600 leading-relaxed">{inclusion}</p>{/each}
   {#if service.qualifier}<p class="text-sm text-gray-600 mt-3">{service.qualifier}</p>{/if}
  </div>
  <div class="md:text-right"><p class="text-3xl font-light mb-6" style="font-family: var(--font-serif)">{priceLabel(service)}</p>
   <a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">{service.inquireOnly ? 'INQUIRE' : 'BOOK A SHOOT'}</a>
  </div>
 </article>
 {/each}
 <a href="/faq" class="text-sm underline underline-offset-4">Questions about delivery or booking? Read the FAQ.</a>
</section>

<Testimonials />
