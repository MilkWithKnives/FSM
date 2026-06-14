import type { RequestHandler } from '@sveltejs/kit';
import { businessJsonLd } from '$lib/business';

// Stable, machine-readable profile of the business, advertised to agents via the
// `describedby` Link header in hooks.server.ts. Served as application/ld+json so
// crawlers and AI agents can consume the schema.org LocalBusiness data directly.
export const GET: RequestHandler = () => {
	return new Response(JSON.stringify(businessJsonLd, null, 2), {
		headers: {
			'Content-Type': 'application/ld+json',
			'Cache-Control': 'max-age=3600',
		},
	});
};
