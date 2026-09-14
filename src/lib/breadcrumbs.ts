import { siteUrl } from './business';
import type { JournalPost } from './journal';
import type { Location } from './locations';
import type { Property } from './properties';

export type Breadcrumb = {
	name: string;
	item: string;
};

type BreadcrumbData = {
	post?: Pick<JournalPost, 'title'>;
	property?: Pick<Property, 'address'>;
	location?: Pick<Location, 'city'>;
};

const labels: Record<string, string> = {
	faq: 'FAQ',
	'3d-tours': '3D Tours',
};

// Dynamic names come from the current page's load data, never from its slug.
const dynamicLabels: Record<string, (data: BreadcrumbData) => string | undefined> = {
	journal: (data) => data.post?.title,
	portfolio: (data) => data.property?.address,
	'real-estate-photographer': (data) => data.location?.city,
};

const slugLabel = (slug: string): string =>
	labels[slug] ?? slug.split('-').map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');

/** Build a public URL trail; route groups are absent from pathname by design. */
export function buildBreadcrumbs(pathname: string, data: BreadcrumbData = {}): Breadcrumb[] {
	const segments = pathname.split('/').filter(Boolean);
	if (!segments.length) return [];

	const trail: Breadcrumb[] = [{ name: 'Home', item: `${siteUrl}/` }];

	// Article breadcrumbs mirror the existing visible navigation exactly.
	if (segments[0] === 'journal' && segments.length > 1) {
		trail[0] = { name: 'Real Estate Media', item: `${siteUrl}/real-estate-photography` };
	}

	for (const [index, segment] of segments.entries()) {
		let name = slugLabel(segment);
		let path = `/${segments.slice(0, index + 1).join('/')}`;

		if (index === 1 && Object.hasOwn(dynamicLabels, segments[0])) {
			const loadedName = dynamicLabels[segments[0]](data);
			// Missing records must not become fabricated slug-based breadcrumbs.
			if (!loadedName) return [];
			name = loadedName;
		}

		// This directory has no index page; link to the real photography landing page.
		if (index === 0 && segment === 'real-estate-photographer') {
			name = 'Real Estate Photography';
			path = '/real-estate-photography';
		}

		trail.push({
			name,
			item: `${siteUrl}${index === segments.length - 1 ? pathname : path}`,
		});
	}

	return trail;
}
