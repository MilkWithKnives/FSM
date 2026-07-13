import { error } from '@sveltejs/kit';
import { getLocation, locationProperty } from '$lib/locations';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	const location = getLocation(params.city);
	if (!location) throw error(404, 'Location not found');
	return { location, property: locationProperty(location) };
};
