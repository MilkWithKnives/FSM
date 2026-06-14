import type { Handle } from '@sveltejs/kit';

// Advertise a machine-readable resource to AI agents via an RFC 8288 Link header.
// `rel="describedby"` points to /business.jsonld (a schema.org LocalBusiness document),
// letting an agent discover a stable, structured profile without scraping the HTML.
// We append rather than set, preserving SvelteKit's own preload Link headers, and only
// add it to HTML page responses (not assets/data endpoints).
export const handle: Handle = async ({ event, resolve }) => {
	const response = await resolve(event);

	if (response.headers.get('content-type')?.includes('text/html')) {
		response.headers.append(
			'Link',
			'</business.jsonld>; rel="describedby"; type="application/ld+json"'
		);
	}

	return response;
};
