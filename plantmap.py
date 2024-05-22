import base64
import streamlit as st
import streamlit.components.v1 as components

tree_info_dictionary = {
	'Striped Maple':'Acer pensylvanicum L.|||Native|||Present on the Appalachian spine into New England but potentially extends into the lower Mississippi Valley|||5.1 (low negative)|||shade tolerance, seedling establishment|||drought|||Striped maple leaves are more shallowly lobed than Red maple',
	'Eastern White Pine':'Pinus strobus L.|||Native|||Widely distributed throughout the Northern and Eastern region of the US|||3.3 (very high negative)|||dispersal|||drought, fire topkill, insect pests|||Eastern white pine is the only pine tree in the East that has five needles per bunch and it has large banana-shaped cones',
	'Flowering Dogwood':'Cornus florida L.|||Native|||Flowering dogwood has been recently hit hard by anthracnose, but it is still widely distributed throughout the south central portion of the eastern US|||5 (low negative)|||shade tolerance||| |||It has large creamy-white flowers with 4 petals each and onion-shaped buds',
	'Sassafras':'Sassafras Nees & Eberm.|||Native|||Sassafras is widely distributed in the Northeastern and Southeastern side of the US, extending from Maine down to Florida|||4.2 (mid negative)||| |||shade tolerance, fire topkill|||Sassafras leaves have rounded edges and a lobed shape, looking smooth from afar',
	'American Beech':'Fagus grandifolia Ehrh.|||Native|||American Beech is widely distributed across the eastern half of the eastern US but is also found on the western side of the US|||3.6 (very high negative)|||shade tolerance|||insect pests, fire topkill|||American beech leaves have an ovate shape and serrated margins, they have no leaflets and are typically a dark green color that turn to a bronze/gold color in the fall',
	'Norway Maple':'Acer platanoides L.|||Introduced|||Norway Maple is a non-native, narrowly distributed tree species that is mostly found in Northeast states|||N/A|||tolerant of wide temperature range, tolerant to sulfur dioxide pollution and ozone||| |||Norway Maple leaves are simple, green, opposite, 5-lobed, coarsely toothed and pointed, the leaf is generally wider than they are tall',
	'Slippery Elm':'Ulmus rubra Muhl.|||Native|||Slippery Elm is widely distributed from Central to Eastern US|||4.8 (mid negative)|||shade tolerance|||fire topkill, disease|||Slippery Elm trees have a vase shape but often have branches higher than American Elms, its leaves are also have a pointed end and are serated',
	'White Oak':'Quercus alba L.|||Native|||Slippery Elm is densely distributed from Central to Eastern US, and has shifted northward over the years|||6.1 (very high positive)|||environment habitat specificity, edaphic specificity, temperature gradient, fire topkill|||insect pests, disease|||White Oak trees are large with a long, straight trunk and a broad, rounded crown, leaves are smooth and alternative with 6-10 lobes that are rounded at the tip',
	'Sugar Maple':'Acer saccharum Marshall|||Native|||Slippery Elm is densely distributed from Central to Eastern US, ranking 4th in overall abundance across the Eastern US due to its high adaptability|||5.8 (very high positive)|||environment habitat specificity, shade tolerance||| |||In the fall, Sugar Maples are likely to look multicolored, its leaves have 5 lobes and have sharp teeth, connected by shallow, U-shaped notches',
	'Red Spruce':'Picea rubens Sarg.|||Native|||Red Spruce is narrowly distributed and mostly concentrated in New England and Canada|||2.9 (very high negative)|||environment habitat specificity, shade tolerance|||fire topkill, seedling establishment|||Red Spruce trees have four-sided, short, yellowish green needles on woody pegs with cones of a wider diameter',
	'Red Oak':'Quercus rubra L.|||Native|||Red Oak is widely distributed, coming in 6th for overall distribution in New England, and is abundant throughout most of the Northern 2/3 of the Eastern US|||5.4 (very high positive)||| |||insect pests|||Red Oak trees have 7-11 pointed lobes that have bristle tips, which are its most distinguishable characteristic from White Oaks',
	'Tuliptree':'Liriodendron L.|||Native|||Red Oak is widely distributed in Eastern US and parts of Central-South US like Texas, however, its habitat has been shifting north with climate change|||5.3 (mid positive)|||seedling establishment, dispersal, environment habitat specificity||| |||Tuliptrees have alternative and simple leaves that are broad and V-shaped at the center, it usually has 2 lobes near the tip and 2 or 4 loves on the lower sides'
}

tree_images = {
	'Striped Maple':['stripedmapletree.png','stripedmapleleaf.jpeg'],
	'Eastern White Pine':['whitepinetree.jpeg','whitepineleaf.jpeg'],
	'Flowering Dogwood':['dogwoodtree.webp','dogwoodleaf.jpeg'],
	'Sassafras':['sassafrastree.jpeg','sassafrasleaf.jpeg'],
	'American Beech':['beechtree.png','beechleaf.jpeg'],
	'Norway Maple':['norwaymapletree.webp','norwaymapleleaf.jpeg'],
	'Slippery Elm':['elmtree.jpeg','elmleaf.jpeg'],
	'White Oak':['whiteoaktree.jpeg','whiteoakleaf.jpeg'],
	'Sugar Maple':['sugarmapletree.jpeg','sugarmapleleaf.jpeg'],
	'Red Spruce':['sprucetree.webp','spruceleaf.jpeg'],
	'Red Oak':['redoaktree.jpeg','redoakleaf.jpeg'],
	'Tuliptree':['tuliptree.jpeg','tuliptreeleaf.jpeg']
}

st.title("Exploring Tree Biodiversity at Choate!")
st.markdown("Created By Dana Tan")

st.header("Why is Biodiversity Important?")
st.write("Biodiversity is the variety and variability of life on Earth. As our society has progressed, it has come at the cost of the environment with the exploitation of resources, misuse of power, and the rise in consumerism. Protecting our biodiversity is crucial as it forms the basis of our natural world. Without a well-balanced ecosystem, we would have no planet to reside on. Biodiversity is also fundamental to human wellbeing and sustainable development.")

col1, col2 = st.columns(2)

with col1:
	st.header("Common Trees At Choate")
	st.caption("Click on the map to browse around the area and explore")

	choatemap_file = open('choatemap.html', 'r')
	raw_html = choatemap_file.read().encode("utf-8")
	raw_html = base64.b64encode(raw_html).decode()
	components.iframe(f"data:text/html;base64,{raw_html}", height=400)

with col2:
	st.header("Distribution of Trees in the US")
	st.caption("Click on the layers to see where the trees are found")

	usmap_file = open('usmap.html', 'r')
	raw_html = usmap_file.read().encode("utf-8")
	raw_html = base64.b64encode(raw_html).decode()
	components.iframe(f"data:text/html;base64,{raw_html}", height=400)

st.divider()

option = st.selectbox(
	"Select tree to learn more about",list(tree_info_dictionary.keys()))

col3, col4 = st.columns(2)

if option in tree_info_dictionary:
	tree_info = tree_info_dictionary[option].split('|||')
	scientific_name,native_status,region,adaptability_score,positive_traits,negative_traits,identification_factors = tree_info

	with col3:
		for image_path in tree_images[option]:
			st.image(image_path)

	with col4:
		st.header(option)
		st.subheader(scientific_name)
		st.write(f"Native status: {native_status}")
		st.write(f"Region: {region}")
		st.write(f"Adaptability score: {adaptability_score}")
		st.write(f"Primary positive traits: {positive_traits}")
		st.write(f"Primary negative traits: {negative_traits}")
		st.write(f"Identification factors: {identification_factors}")
