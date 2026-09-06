export const siteUrl = 'https://fullscope-media.com';

const description =
	'Full Scope Media LLC is a full-scope media studio in East Lansing, MI. Real estate media — photography, cinematic video tours, aerial drone, floor plans, Matterport 3D tours, and virtual staging — plus web design & build, local SEO, brand photography, and systems integration for small businesses across Michigan.';
const image = `${siteUrl}/portfolio/622-vine-st-st-joseph-mi-49085/01-2000.jpg`;

const services = [
	{ name: 'Real Estate Photography', path: '/photos', id: 'service' },
	{ name: 'Cinematic Video Tours', path: '/videos', id: 'service' },
	{ name: 'Aerial Drone Photography', path: '/videos', id: 'aerial-drone-service' },
	{ name: '3D Tours (Matterport & Zillow 3D Home)', path: '/3d-tours', id: 'service' },
	{ name: 'Floor Plans (CubiCasa)', path: '/floor-plans', id: 'service' },
	{ name: 'Virtual Staging', path: '/virtual-staging', id: 'service' },
	{ name: 'Web Design & Development', path: '/studio/web-design', id: 'service' },
	{ name: 'Local SEO & Google Business Profile Optimization', path: '/studio/web-design', id: 'seo-service' },
	{ name: 'Brand & Product Photography', path: '/studio/photography', id: 'service' },
	{ name: 'Systems & Data Integration', path: '/studio/systems', id: 'service' },
];

/**
 * Canonical machine-readable description of the business (schema.org LocalBusiness).
 *
 * Single source of truth, used in two places:
 *   1. Rendered inline as JSON-LD in the <head> (see +layout.svelte) for search engines.
 *   2. Served as a standalone document at /business.jsonld and advertised to AI agents
 *      via the `describedby` Link response header (see hooks.server.ts) so an agent can
 *      fetch a stable, machine-readable profile without scraping HTML.
 */
export const businessJsonLd = {
	'@context': 'https://schema.org',
	'@type': 'LocalBusiness',
	'@id': `${siteUrl}/#business`,
	name: 'Full Scope Media LLC',
	description,
	url: siteUrl,
	email: 'rchampion@fullscope-media.com',
	telephone: '+1-989-525-7768',
	address: {
		'@type': 'PostalAddress',
		addressLocality: 'East Lansing',
		addressRegion: 'MI',
		postalCode: '48823',
		addressCountry: 'US',
	},
	geo: {
		'@type': 'GeoCoordinates',
		latitude: 42.737,
		longitude: -84.4839,
	},
	areaServed: [
		'East Lansing',
		'Lansing',
		'Okemos',
		'Grand Ledge',
		'Mid-Michigan',
		'Bay City',
		'Saginaw',
		'Midland',
		'Kalamazoo',
		'Battle Creek',
		'Ann Arbor',
		'Jackson',
		'Metro Detroit',
		'Michigan',
	],
	hasOfferCatalog: {
		'@type': 'OfferCatalog',
		name: 'Full Scope Media services',
		itemListElement: services.map((service) => ({
			'@type': 'Offer',
			itemOffered: {
				'@type': 'Service',
				'@id': `${siteUrl}${service.path}#${service.id}`,
				name: service.name,
				serviceType: service.name,
				url: `${siteUrl}${service.path}`,
				provider: { '@id': `${siteUrl}/#business` },
			},
		})),
	},
	priceRange: '$$',
	image,
	sameAs: ['https://instagram.com/full.scope.media'],
};
