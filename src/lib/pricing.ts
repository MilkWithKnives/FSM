export type ServiceRate = {
 id: string; name: string; path: string; price: number | null;
 inclusions: string[]; qualifier: string; inquireOnly: boolean;
};
export const serviceRates: ServiceRate[] = [
 { id: 'basic', name: 'Basic — Residential Photos', path: '/photos', price: 150, inclusions: ['Interior and exterior photos', 'CubiCasa floor plan included', '24-hour delivery'], qualifier: 'Additional fees above 3,200 sqft.', inquireOnly: false },
 { id: 'commercial', name: 'Commercial Photos', path: '/photos', price: 175, inclusions: ['Interior and exterior photos', '24-hour delivery'], qualifier: 'Up to 3,200 sqft.', inquireOnly: false },
 { id: 'drone', name: 'Aerial Drone Photos', path: '/drone', price: 160, inclusions: ['Aerial property photography'], qualifier: 'Additional fees above 20 acres.', inquireOnly: false },
 { id: 'tour', name: '3D Virtual Tour', path: '/3d-tours', price: 185, inclusions: ['Dollhouse view', '360° exterior'], qualifier: '', inquireOnly: false },
 { id: 'video', name: 'Video Walkthrough', path: '/videos', price: 210, inclusions: ['Property video walkthrough'], qualifier: '', inquireOnly: false },
 { id: 'floor', name: 'Floor Plan (standalone)', path: '/floor-plans', price: 50, inclusions: ['CubiCasa floor plan', 'Included free with Basic'], qualifier: 'Standalone price applies when ordered without photos.', inquireOnly: false },
 ...[
  ['staging', 'Virtual Staging', '/virtual-staging'], ['twilight', 'Twilight Shoots', '/contact'],
  ['multi', 'Multi-location', '/contact'], ['rush', 'Rush Turnaround', '/contact'],
  ['large', 'Properties well above the size thresholds', '/contact'],
 ].map(([id, name, path]) => ({ id, name, path, price: null, inclusions: [], qualifier: '', inquireOnly: true })),
];
export const rate = (id: string): ServiceRate => serviceRates.find(service => service.id === id)!;
export const priceLabel = (service: ServiceRate): string => service.inquireOnly || service.price === null ? 'Inquire for pricing' : `$${service.price}`;
