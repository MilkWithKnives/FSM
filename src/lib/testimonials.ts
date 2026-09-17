export type Testimonial = {
 quote: string;
 clientName: string;
 role: string;
 city: string;
 propertySlug?: string;
 rating?: number;
};
// TODO: Supply approved real client quotes, names, role/brokerage, city, and optional
// portfolio slug. Only provide a rating when the client actually supplied one (1–5).
// No review source is connected; this is the source of truth.
export const testimonials: Testimonial[] = [];
export const publishedTestimonials = testimonials.filter(item =>
 item.quote.trim() && item.clientName.trim() && item.role.trim() && item.city.trim());
