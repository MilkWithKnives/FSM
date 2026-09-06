import { error } from '@sveltejs/kit';
import { getJournalPost } from '$lib/journal';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	const post = getJournalPost(params.slug);
	if (!post) error(404, 'Article not found');
	return { post };
};
