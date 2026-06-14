export const siteUrl = 'https://fullscope-media.com';

const description =
	'Full Scope Media LLC is a full-service real estate media studio — photography, cinematic video tours, aerial drone, floor plans, Matterport 3D tours, and virtual staging — serving East Lansing, Mid-Michigan, and the Metro Detroit area.';
const image = `${siteUrl}/portfolio/622-vine-st-st-joseph-mi-49085/01-2000.jpg`;

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
	name: 'Full Scope Media LLC',
	description,
	url: siteUrl,
	email: 'info@fullscope-media.com',
	telephone: '+1-989-577-9513',
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
	serviceType: [
		'Real Estate Photography',
		'Cinematic Video Tours',
		'Aerial Drone Photography',
		'3D Tours (Matterport & Zillow 3D Home)',
		'Floor Plans (CubiCasa)',
		'Virtual Staging',
	],
	priceRange: '$$',
	image,
	sameAs: ['https://instagram.com/full.scope.media'],
};
