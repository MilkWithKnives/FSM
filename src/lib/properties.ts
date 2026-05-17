export type Property = {
	slug: string;
	address: string;
	city: string;
	state: string;
	zip: string;
	tag: string;
	photoCount: number;
	selected: number[];
};

export const properties: Property[] = [
	{
		slug: '622-vine-st-st-joseph-mi-49085',
		address: '622 Vine St',
		city: 'St. Joseph',
		state: 'MI',
		zip: '49085',
		tag: 'Photos + Video + Floorplans',
		photoCount: 106,
		selected: [1, 9, 17, 25, 33, 41, 49, 58, 65, 73, 81, 89, 97, 105],
	},
	{
		slug: '4442-greenwood-dr-okemos-mi-48864',
		address: '4442 Greenwood Dr',
		city: 'Okemos',
		state: 'MI',
		zip: '48864',
		tag: 'Photos + Video',
		photoCount: 69,
		selected: [1, 6, 11, 16, 21, 29, 31, 36, 41, 48, 51, 56, 61, 66],
	},
	{
		slug: '3977-stirrup-st-east-lansing-mi-48823',
		address: '3977 Stirrup St',
		city: 'East Lansing',
		state: 'MI',
		zip: '48823',
		tag: 'Photos + Video',
		photoCount: 45,
		selected: [1, 4, 7, 10, 14, 16, 19, 22, 24, 28, 31, 34, 37, 40, 43],
	},
	{
		slug: '2877-bessemer-rd-coloma-mi-49038',
		address: '2877 Bessemer Rd',
		city: 'Coloma',
		state: 'MI',
		zip: '49038',
		tag: 'Photos + Video',
		photoCount: 38,
		selected: [1, 4, 7, 10, 14, 16, 19, 21, 25, 28, 31, 34, 38],
	},
	{
		slug: '1904-carvel-ct-lansing-mi-48910',
		address: '1904 Carvel Ct',
		city: 'Lansing',
		state: 'MI',
		zip: '48910',
		tag: 'Photos + Video',
		photoCount: 28,
		selected: [1, 4, 7, 10, 13, 16, 19, 21, 25, 27],
	},
];

export const getProperty = (slug: string): Property | undefined =>
	properties.find((p) => p.slug === slug);

export const propertyArea = (p: Property): string => `${p.city}, ${p.state}`;
export const propertyFullAddress = (p: Property): string =>
	`${p.address}, ${p.city}, ${p.state} ${p.zip}`;
