import { error } from '@sveltejs/kit';
import { getProperty } from '$lib/properties';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	const property = getProperty(params.slug);
	if (!property) throw error(404, 'Property not found');
	return { property };
};
