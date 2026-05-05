import type { RequestHandler } from '@sveltejs/kit';

const siteUrl = 'https://fullscope-media.com';

const pages = [
	{ path: '/', priority: '1.0', changefreq: 'weekly' },
	{ path: '/portfolio', priority: '0.9', changefreq: 'weekly' },
	{ path: '/photos', priority: '0.8', changefreq: 'monthly' },
	{ path: '/videos', priority: '0.8', changefreq: 'monthly' },
	{ path: '/pricing', priority: '0.8', changefreq: 'monthly' },
	{ path: '/about', priority: '0.7', changefreq: 'monthly' },
	{ path: '/journal', priority: '0.7', changefreq: 'weekly' },
	{ path: '/contact', priority: '0.6', changefreq: 'yearly' },
];

export const GET: RequestHandler = () => {
	const today = new Date().toISOString().split('T')[0];

	const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map(p => `  <url>
    <loc>${siteUrl}${p.path}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${p.changefreq}</changefreq>
    <priority>${p.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

	return new Response(xml, {
		headers: {
			'Content-Type': 'application/xml',
			'Cache-Control': 'max-age=3600'
		}
	});
};
