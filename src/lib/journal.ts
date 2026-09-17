import { floorPlanExample } from './media';

export type JournalLink = { label: string; href: string };
export type JournalImage = {
	src: string;
	alt: string;
	width: number;
	height: number;
	caption?: string;
};
export type JournalPost = {
	slug: string;
	title: string;
	description: string;
	excerpt: string;
	image: JournalImage;
	intro: string[];
	sections: {
		id: string;
		heading: string;
		paragraphs: string[];
		items?: string[];
		links?: JournalLink[];
	}[];
	related: JournalLink[];
};

// Keep article content, index cards, and sitemap entries tied to the same published pages.
// Publication dates are omitted until an actual publication date is recorded.
export const journalPosts: JournalPost[] = [
	{
		slug: 'how-to-prep-house-shoot',
		title: 'How to Prep a House for a Shoot',
		description: 'Prepare your home for real estate photography with a room-by-room checklist covering clutter, cleaning, lighting, exterior spaces, pets, and shoot-day access.',
		excerpt: 'A practical room-by-room checklist to get a property ready before the photographer arrives.',
		image: {
			src: 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&h=750&q=80&auto=format&fit=crop',
			alt: 'Illustration of a home for a real estate photography preparation guide',
			width: 1200,
			height: 750,
		},
		intro: [
			'A successful property shoot starts before the camera comes out. Clean surfaces, clear walkways, and a simple plan for access let the photographer concentrate on the home. They also help the finished gallery show the rooms consistently, without a different pile of belongings appearing in each view.',
			'Use this checklist with the agent and homeowner before a shoot in East Lansing, Lansing, Okemos, or elsewhere. Finish the larger jobs the day before, then use the final walkthrough to catch the details that are easy to miss when you live in a space.',
		],
		sections: [
			{
				id: 'plan-the-shoot',
				heading: '1. Agree on the spaces to photograph',
				paragraphs: [
					'Confirm which rooms, exterior areas, and outbuildings belong in the gallery. Tell the photographer about features that deserve attention, such as a renovated kitchen, a separate workspace, or access to an outdoor living area. Explain any access restrictions before the appointment.',
					'Choose one place for temporary storage that is outside the planned shots. Moving laundry baskets from the bedroom to the hallway only shifts the problem into the next photograph. If staging furniture is being delivered, schedule the installation and cleanup before the photography appointment.',
				],
			},
			{
				id: 'clean-and-declutter',
				heading: '2. Clean the surfaces the camera will see',
				paragraphs: [
					'Clean floors, mirrors, windows, appliance fronts, and shower glass. Fingerprints and streaks are especially visible where daylight crosses a reflective surface. Put away paperwork, charging cables, remotes, wastebaskets, and personal photographs you do not want included in listing images.',
					'Leave the rooms furnished and purposeful. A dining table, a reading chair, and neatly arranged shelves can explain how a room is used. The aim is to remove distractions while keeping the space understandable.',
				],
			},
			{
				id: 'kitchen-and-bathrooms',
				heading: '3. Reset the kitchen and bathrooms',
				paragraphs: ['These rooms have many small objects competing for attention. Work across each surface from one side to the other so that you do not miss the corners.'],
				items: [
					'Clear dishes, drying racks, cleaning supplies, and excess countertop appliances.',
					'Remove magnets, notes, and calendars from the refrigerator.',
					'Wipe the sink and faucet, and straighten stools and dining chairs.',
					'Put away toiletries, toothbrushes, bath mats that interrupt the floor, and shower products.',
					'Close toilet lids and hang clean towels neatly.',
				],
			},
			{
				id: 'bedrooms-and-living-spaces',
				heading: '4. Give bedrooms and living spaces a final pass',
				paragraphs: [
					'Make beds, smooth the bedding, and clear bedside tables. In living rooms, straighten cushions and furniture, switch off televisions, and store toys and pet bedding outside the planned views. Check under tables and beds for items visible from a lower camera position.',
					'Keep the route between rooms clear. Furniture that blocks a doorway makes the layout harder to read. Avoid making last-minute furniture moves that require dragging heavy pieces or risking damage; discuss significant rearrangements with the homeowner in advance.',
				],
			},
			{
				id: 'exterior',
				heading: '5. Prepare the exterior as carefully as the interior',
				paragraphs: [
					'Move vehicles out of the driveway when they would block the house. Store bins, hoses, tools, and loose outdoor items. Sweep the porch and arrange patio furniture so that outdoor spaces look ready to use.',
					'For a Michigan winter shoot, clear safe access to the entrance and the exterior areas being photographed. In other seasons, check for leaves, yard debris, or unfinished maintenance. Let the photographer know about weather or access concerns ahead of time so the exterior portion can be planned.',
				],
			},
			{
				id: 'shoot-day',
				heading: '6. Set up access, lighting, and a quiet workspace',
				paragraphs: [
					'Make sure the agent or photographer can enter every agreed space. Arrange for pets to be safely away from the shooting area and limit people moving through adjoining rooms. Mirrors and glass can reveal someone standing well outside the main view.',
					'Replace failed bulbs and make sure window coverings operate. Have lights ready and blinds or curtains arranged neatly; the photographer can adjust them to suit the light in each room. Share the important features at the start, then allow time for the photographer to work through the property.',
				],
			},
			{
				id: 'final-checklist',
				heading: 'The five-minute check before arrival',
				paragraphs: ['Walk from the front door through the home in the order a visitor would. Look at the whole room from each doorway before checking the details.'],
				items: [
					'Entryways and planned camera positions are clear.',
					'Beds, towels, chairs, and cushions are straight.',
					'Personal items, bins, and cleaning supplies are stored.',
					'Cars and outdoor clutter are out of the exterior views.',
					'Access is arranged and pets have a safe place to stay.',
				],
				links: [{ label: 'Book real estate photography with Full Scope Media', href: '/contact' }],
			},
		],
		related: [
			{ label: 'Real estate photography services', href: '/photos' },
			{ label: 'Photography packages and pricing', href: '/pricing' },
			{ label: 'Ten techniques for interior photography', href: '/journal/ten-techniques-photograph-interiors' },
		],
	},
	{
		slug: 'why-every-listing-needs-floorplan',
		title: 'Why Every Listing Needs a Floorplan',
		description: 'Learn how a real estate floor plan explains room connections, dimensions, and multiple levels, and what to check before adding one to a property listing.',
		excerpt: 'Show buyers how a home fits together, with clear room labels, dimensions, and an easy-to-read layout.',
		image: floorPlanExample,
		intro: [
			'A photograph shows what a room looks like. A floor plan helps explain where that room sits in the home. Together, they answer two different questions: can I picture myself here, and does the arrangement of the space work for me?',
			'A clear plan belongs alongside the photographs when you prepare a listing. It gives buyers a reference they can return to as they move through the gallery, especially when several rooms have similar finishes or the property has more than one level.',
		],
		sections: [
			{
				id: 'room-connections',
				heading: 'Show the connections that photographs leave out',
				paragraphs: [
					'Consider a gallery that shows a kitchen, a dining area, and a living room. Without a plan, a viewer may struggle to tell whether those spaces connect directly or sit on opposite sides of a hallway. A simple overhead layout makes the route between them visible.',
					'In the example above, the kitchen and dining area connect with the living room, while the primary bedroom sits beside its own bathroom and closet area. Doorways and stairs explain how someone moves through the space. Those relationships are useful context for the individual photographs.',
				],
			},
			{
				id: 'dimensions',
				heading: 'Give room dimensions a visual context',
				paragraphs: [
					'A dimension in a description is easier to understand when a buyer can see the room shape, door positions, and adjoining spaces. A large room may still have a limited uninterrupted wall for a desk or sofa. The drawing helps someone notice that before relying on floor area alone.',
					'Keep labels and measurements legible at the size the plan will appear online. If a buyer needs to confirm that a particular piece of furniture fits, encourage them to verify the relevant dimensions at the property. Preserve measurement notes that come with the plan instead of cropping them from the published image.',
				],
			},
			{
				id: 'multiple-levels',
				heading: 'Make multiple levels easy to follow',
				paragraphs: [
					'A multilevel home needs a clearly identified drawing for each included level. Label the levels consistently and make stair connections easy to find. Buyers should be able to tell where a bedroom, bathroom, laundry room, or separate living area is located without guessing from the order of the photos.',
					'Use the same room names in the plan, gallery captions, and listing description. If one calls a space a study and another calls it a dining room, check the intended label before publishing. Explain separate buildings or additional spaces clearly rather than making them appear to be part of the main house.',
				],
			},
			{
				id: 'review-before-publishing',
				heading: 'Review the plan before adding it to a listing',
				paragraphs: ['Treat the floor plan as part of the listing content review. Check it against the property and the other marketing material before sending the gallery live.'],
				items: [
					'Every intended room and level is present and labeled correctly.',
					'Doors, stairs, and connections between spaces are represented clearly.',
					'Measurements and any accompanying notes remain readable.',
					'The image is sharp when opened at full size and useful on a phone.',
					'Room names agree with the listing description and photo captions.',
				],
			},
			{
				id: 'publish-with-photography',
				heading: 'Use the floor plan alongside the photography',
				paragraphs: [
					'Place the plan where a buyer can find it while viewing the listing photos, and include a full-size version when the platform supports it. A small thumbnail can introduce the layout, but it should not be the only way to read the room labels.',
					'Keep the photographs responsible for showing condition, finishes, and the character of each room. Let the plan explain the arrangement. Neither needs to do the other’s job, and neither should promise a particular sale price or time on the market.',
				],
			},
			{
				id: 'floor-plans-with-full-scope',
				heading: 'Add a floor plan to your real estate media',
				paragraphs: [
					'Full Scope Media offers CubiCasa floor plans for listings in East Lansing and greater Michigan. Discuss the spaces you want covered when arranging your shoot so photography and the plan can be considered together.',
					'CubiCasa describes its schematic 2D plans as simple representations of a property’s layout and supplies downloadable image formats. The useful deliverable for a listing is a clear drawing that buyers can read, save, and compare with the gallery.',
				],
				links: [
					{ label: 'View my floor plan service and example', href: '/floor-plans' },
					{ label: 'CubiCasa: real estate floor plans', href: 'https://www.cubi.casa/products/real-estate-floor-plans/' },
				],
			},
		],
		related: [
			{ label: 'Floor plan pricing', href: '/pricing' },
			{ label: 'How to prepare a house for a shoot', href: '/journal/how-to-prep-house-shoot' },
			{ label: 'Discuss your property’s media package', href: '/contact' },
		],
	},
	{
		slug: 'ten-techniques-photograph-interiors',
		title: 'Ten Techniques to Best Photograph Interior Spaces',
		description: 'Ten practical interior photography techniques covering composition, camera position, vertical lines, light, exposure, focus, reflections, and consistent editing.',
		excerpt: 'Use thoughtful camera placement, controlled light, and consistent editing to make interior photographs clear and believable.',
		image: {
			src: 'https://images.unsplash.com/photo-1565182999561-18d7dc61c393?w=1200&h=750&q=80&auto=format&fit=crop',
			alt: 'Interior space illustrating a guide to photographing rooms',
			width: 1200,
			height: 750,
		},
		intro: [
			'An effective interior photograph makes the room easy to understand. The viewer should see its proportions, important features, and connection to the surrounding space without being distracted by tilted lines, inconsistent color, or exaggerated perspective.',
			'These ten techniques form a practical sequence: prepare the room, decide what the image needs to communicate, set the camera, manage the light, and review the result. Adjust each decision to the room rather than relying on one camera position or preset for every property.',
		],
		sections: [
			{
				id: 'prepare-the-frame',
				heading: '1. Prepare the whole frame',
				paragraphs: ['Look beyond the main piece of furniture. Check cords along the floor, objects on nearby counters, crooked cushions, and whatever appears through an open doorway. Remove temporary distractions before shooting. A tidy foreground is less useful if the adjoining room pulls attention away from the subject.'],
				links: [{ label: 'Use the room-by-room preparation checklist', href: '/journal/how-to-prep-house-shoot' }],
			},
			{
				id: 'choose-a-purpose',
				heading: '2. Give each composition a purpose',
				paragraphs: ['Decide whether the photograph explains the whole room, a connection between rooms, or a particular feature. A view through the kitchen toward the dining area serves a different purpose from a close view of cabinetry. Choose the frame that communicates that purpose instead of trying to include every object.'],
			},
			{
				id: 'camera-position',
				heading: '3. Choose camera position before widening the view',
				paragraphs: ['Move around the room and compare views before choosing the focal length. A very close foreground can dominate the image and make the background feel unusually distant. Step back where possible and use a field of view that includes the necessary context without stretching furniture at the edges.'],
				links: [{ label: 'Canon’s explanation of photographic perspective', href: 'https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/perspective/index.html' }],
			},
			{
				id: 'vertical-lines',
				heading: '4. Keep vertical lines under control',
				paragraphs: ['Use door frames, wall corners, and cabinets as visual references when leveling the camera. Tilting up or down can make vertical lines appear to converge. Leave enough space around the composition for modest correction later, but solve as much as possible through camera position first.'],
			},
			{
				id: 'stable-camera',
				heading: '5. Keep the camera stable',
				paragraphs: ['A stable tripod makes it easier to compare small composition changes and keep multiple exposures aligned. Recheck the frame after tightening the head. Use a release method that avoids nudging the camera, and inspect a sample image at a useful magnification before moving to the next position.'],
			},
			{
				id: 'lighting',
				heading: '6. Evaluate daylight and room lighting together',
				paragraphs: ['Check how window light falls across the room and whether lamps introduce noticeably different colors. Try a controlled arrangement of the available lights instead of assuming every fixture must remain on. The goal is a coherent, believable room with useful detail, not simply the brightest possible image.'],
			},
			{
				id: 'exposure',
				heading: '7. Balance the interior and bright windows',
				paragraphs: ['A bright window and a shaded room may need different exposures to retain detail. Inspect both parts of the scene. When using exposure bracketing, keep the camera fixed and review the merged result for ghosting, halos, and unnatural contrast. Additional exposures are useful only when the finished photograph still looks coherent.'],
			},
			{
				id: 'focus',
				heading: '8. Check focus across the important parts of the room',
				paragraphs: ['Choose a focus point and aperture for the depth of the actual composition. Review nearby furniture, midroom details, and the background rather than judging sharpness from a small preview alone. There is no single aperture that answers every room, lens, and camera position; verify the result before packing up.'],
			},
			{
				id: 'reflections',
				heading: '9. Inspect reflections and the edges of the image',
				paragraphs: ['Mirrors, windows, appliances, and glossy cabinetry can show the photographer or equipment. Check these areas deliberately, along with partly cropped furniture at the frame edges. A slight change in position may resolve a reflection, but confirm that the new angle still explains the room clearly.'],
			},
			{
				id: 'consistent-editing',
				heading: '10. Edit the gallery as a connected set',
				paragraphs: [
					'Compare adjoining rooms for consistent brightness and color. Apply suitable lens corrections, review perspective, and check the crop after geometric adjustments. Preserve the appearance of the property’s permanent features rather than using editing to invent a different space.',
					'Adobe’s Upright tools can correct horizontal and vertical perspective, with manual adjustment available when the automatic result needs refinement. Review each photograph after correction: straight walls are useful, but an awkward crop can still make the image harder to read.',
				],
				links: [{ label: 'Adobe: correcting perspective in Lightroom Classic', href: 'https://helpx.adobe.com/lightroom-classic/desktop/help/upright-automatic-perspective-correction.html' }],
			},
		],
		related: [
			{ label: 'View Full Scope Media’s property photography', href: '/portfolio' },
			{ label: 'Real estate photography services', href: '/photos' },
			{ label: 'Book a property shoot', href: '/contact' },
		],
	},
];

export const getJournalPost = (slug: string): JournalPost | undefined =>
	journalPosts.find((post) => post.slug === slug);
