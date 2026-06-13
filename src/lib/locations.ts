import { getProperty, type Property } from './properties';

export type Location = {
	/** URL slug under /real-estate-photographer/<slug> */
	slug: string;
	city: string;
	state: string;
	/** <title> tag */
	title: string;
	/** meta description */
	description: string;
	/** page H1 */
	heading: string;
	/** Slug of a real, locally-shot property used to anchor the page with genuine work. */
	featuredSlug: string;
	/** Distinct intro copy — written per city, not templated. */
	intro: string[];
	/** Real neighborhoods/areas we shoot in this city. */
	neighborhoods: string[];
};

export const locations: Location[] = [
	{
		slug: 'okemos',
		city: 'Okemos',
		state: 'MI',
		title: 'Real Estate Photographer in Okemos, MI | Full Scope Media',
		description:
			'Professional real estate photographer serving Okemos, MI. Full Scope Media shoots photography, video, and aerial drone for Okemos listings — edited and delivered in 24 hours. See our recent Okemos work.',
		heading: 'Real Estate Photographer in Okemos, MI',
		featuredSlug: '4442-greenwood-dr-okemos-mi-48864',
		intro: [
			'Okemos homes sell on lifestyle as much as square footage — the mature lots, the proximity to top-rated Okemos schools, the quick reach to Meridian Mall and the Red Cedar River. Our job is to make a buyer feel all of that before they ever schedule a showing.',
			'We recently photographed 4442 Greenwood Dr right here in Okemos: a full photo and video package covering every room, the exterior, and the surrounding neighborhood. The gallery below is the actual delivered work — not stock — so you can see exactly what your Okemos listing would look like.',
			'From Indian Hills and Tihart to the newer builds off Jolly and Okemos Road, we know how to light and frame Okemos properties to compete with the best listings in Ingham County.',
		],
		neighborhoods: ['Indian Hills', 'Tihart', 'Chippewa Hills', 'Ferndale', 'Okemos Road corridor'],
	},
	{
		slug: 'lansing',
		city: 'Lansing',
		state: 'MI',
		title: 'Real Estate Photographer in Lansing, MI | Full Scope Media',
		description:
			'Professional real estate photographer serving Lansing, MI. Full Scope Media shoots photography, video, and aerial drone for Lansing listings — edited and delivered in 24 hours. See our recent Lansing work.',
		heading: 'Real Estate Photographer in Lansing, MI',
		featuredSlug: '1904-carvel-ct-lansing-mi-48910',
		intro: [
			"Lansing is a city of character — from the historic homes of the Westside and Moores Park to the revitalized lofts of REO Town and Old Town. Each neighborhood photographs differently, and a one-size-fits-all shoot leaves money on the table.",
			'Our recent shoot at 1904 Carvel Ct in Lansing is below — a complete photo and video package. It shows how we handle the kind of cozy, well-kept Lansing home that moves fast when it is presented properly online.',
			'Whether it is a capital-area condo, a Groesbeck bungalow, or a riverfront property, we shoot Lansing listings for agents who want their photos to be the reason a buyer clicks.',
		],
		neighborhoods: ['REO Town', 'Old Town', 'Westside', 'Moores Park', 'Groesbeck'],
	},
];

export const getLocation = (slug: string): Location | undefined =>
	locations.find((l) => l.slug === slug);

export const locationProperty = (l: Location): Property | undefined => getProperty(l.featuredSlug);
