<script lang="ts">
 import { page } from '$app/stores';
 import { serviceRates } from '$lib/pricing';
 import { siteUrl, businessJsonLd } from '$lib/business';
 const services = $derived(serviceRates.filter(service => service.path === $page.url.pathname && service.path !== '/contact'));
 const graph = $derived(services.map(service => ({
  '@type': 'Service', '@id': `${siteUrl}${service.path}#${service.id === 'commercial' ? 'commercial' : 'service'}`,
  name: service.name, serviceType: service.name, url: `${siteUrl}${service.path}`,
  provider: { '@id': `${siteUrl}/#business` }, areaServed: businessJsonLd.areaServed,
  description: [...service.inclusions, service.qualifier].filter(Boolean).join('. '),
  ...(!service.inquireOnly && service.price !== null ? { offers: {
   '@type': 'Offer', price: service.price, priceCurrency: 'USD', url: `${siteUrl}/pricing`,
   description: service.qualifier || service.inclusions.join('. '),
  }} : {}),
 })));
</script>
<svelte:head>
 {#if graph.length}{@html `<script type="application/ld+json">${JSON.stringify({ '@context': 'https://schema.org', '@graph': graph }).replace(/</g, '\\u003c')}<\/script>`}{/if}
</svelte:head>
