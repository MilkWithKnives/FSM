<script lang="ts">
 import Seo from '$lib/Seo.svelte';
 import LocationLinks from '$lib/LocationLinks.svelte';
 import { rate, priceLabel } from '$lib/pricing';
 const service = rate('drone');
 const aerial = '/uploads/drone/dji_0015';
 const srcset = (ext: string) => [800, 1400, 2000].map(w => `${aerial}-${w}.${ext} ${w}w`).join(', ');
 // TODO: Confirm current FAA Part 107 certification before publishing a compliance claim.
 // The existing FAQ says FAA-licensed, but the repo has no specific Part 107 evidence.
 // TODO: Confirm aerial-photo turnaround; the confirmed 24-hour commitment is for listing photos.
</script>
<Seo title="Aerial Drone Photography | Full Scope Media · East Lansing, MI"
 description={`Aerial property photography from Full Scope Media. ${priceLabel(service)}. ${service.qualifier} Pair aerial views with residential photos or a video walkthrough.`}
 image={`${aerial}-2000.jpg`} />
<section class="relative h-[60vh] overflow-hidden">
 <picture>
  <source type="image/avif" srcset={srcset('avif')} sizes="100vw" />
  <source type="image/webp" srcset={srcset('webp')} sizes="100vw" />
  <img src={`${aerial}-2000.jpg`} srcset={srcset('jpg')} sizes="100vw" alt="Aerial view of a property and its surrounding landscape" fetchpriority="high" class="absolute inset-0 w-full h-full object-cover" />
 </picture>
 <div class="absolute inset-0 bg-black/40 flex flex-col items-center justify-center text-white text-center px-6">
  <p class="text-xs tracking-[0.4em] uppercase mb-4 opacity-70">Services</p>
  <h1 class="text-5xl md:text-7xl font-light" style="font-family: var(--font-serif)">Aerial Drone</h1>
 </div>
</section>
<section class="py-24 px-8 lg:px-20 max-w-6xl mx-auto">
 <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
  <div>
   <p class="text-xs tracking-[0.4em] uppercase text-gray-500 mb-6">The property in context</p>
   <h2 class="text-3xl md:text-4xl font-light mb-8" style="font-family: var(--font-serif)">Show how the home sits on the land.</h2>
   <p class="text-sm text-gray-500 leading-relaxed mb-6">Aerial photos show the setting, outdoor spaces and relationship to the surrounding landscape. They complement the rooms and details shown in your listing photos.</p>
   <p class="text-sm text-gray-500 leading-relaxed mb-6">Choose aerial photos alongside <a href="/photos" class="underline">Basic residential photography</a> or a <a href="/videos" class="underline">video walkthrough</a>. Each service has its own flat rate.</p>
   <p class="text-sm text-gray-500 leading-relaxed mb-8">Discuss the views you need and your delivery date with me when booking.</p>
   <a href="/contact" class="btn btn-neutral rounded-none tracking-widest text-xs px-8">BOOK A DRONE SHOOT</a>
  </div>
  <div>
   <p class="text-xs tracking-widest uppercase text-gray-500 mb-6">Aerial photography</p>
   {#each service.inclusions as item}<p class="text-sm text-gray-600 mb-4">{item}</p>{/each}
   <div class="pt-8 border-t border-gray-100">
    <p class="text-3xl font-light mb-4" style="font-family: var(--font-serif)">{priceLabel(service)}</p>
    <p class="text-sm text-gray-600">{service.qualifier}</p>
   </div>
  </div>
 </div>
</section>
<LocationLinks />
<section class="bg-neutral text-white py-24 px-8 text-center">
 <h2 class="text-4xl md:text-5xl font-light mb-8" style="font-family: var(--font-serif)">Plan your aerial views</h2>
 <a href="/contact" class="btn btn-outline btn-sm rounded-none tracking-widest text-xs border-white text-white hover:bg-white hover:text-black px-10">GET IN TOUCH</a>
</section>
