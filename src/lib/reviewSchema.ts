import { publishedTestimonials } from './testimonials';
import type { Testimonial } from './testimonials';
export function reviewSchema(city?: string) {
 const items = publishedTestimonials.filter(item => !city || item.city === city);
 if (!items.length) return {};
 const rated = items.filter((item): item is Testimonial & { rating: number } =>
  typeof item.rating === 'number' && Number.isFinite(item.rating) && item.rating >= 1 && item.rating <= 5);
 return {
  review: items.map(item => ({ '@type': 'Review', reviewBody: item.quote,
   author: { '@type': 'Person', name: item.clientName },
   ...(rated.includes(item as Testimonial & { rating: number }) ? { reviewRating: { '@type': 'Rating', ratingValue: item.rating, bestRating: 5, worstRating: 1 } } : {}),
  })),
  ...(rated.length ? { aggregateRating: { '@type': 'AggregateRating',
   ratingValue: rated.reduce((sum, item) => sum + item.rating, 0) / rated.length,
   ratingCount: rated.length, bestRating: 5, worstRating: 1,
  }} : {}),
 };
}
