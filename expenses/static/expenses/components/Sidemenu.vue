const baseSidemenuStyle = {
	width: '250px',
	height: '100%',
	position: 'fixed',
	top: '0',
	'z-index': '100',
	background: 'white',
	'padding-top': '24px',
	transition: '0.2s',
	'box-shadow': '0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2)',
	overflow: 'hidden',
}

const sidemenu_left_style = {
	...baseSidemenuStyle,
	left: '0',
	transform: 'translateX(-105%)',
}

const sidemenu_right_style = {
	...baseSidemenuStyle,
	right: '0',
	transform: 'translateX(105%)',
}

const itemStyle = {
	display: 'block',
	color: 'unset',
	padding: '8px 24px',
}

const iconStyle = {
	display: 'inline-block',
	width: '24px',
	'margin-right': '24px',
	'text-align': 'center',
	'font-size': '16px',
}

const textStyle = {
	display: 'inline-block',
	'font-size': '16px',
}

function attachIcon (icon) {
	return `fas fa-fw fa-${icon}`
}

var Sidemenu = Vue.component('side-menu', {
	data: function () {
		return {
			
		}
	},
	computed: {
		sidemenuStyle () {return this.onright ? sidemenu_right_style : sidemenu_left_style },
	},
	props: {
		id: String,
		items: Array,
		onright: Boolean,
	},
	template: `
		<div :id="id"
			:style="sidemenuStyle"
		>
			<template v-for="item in items" >
				<a class="sidemenu-item" :href="item.link" :style="itemStyle">
					<span :style="iconStyle"><i :class="attachIcon(item.icon)"></i></span>
					<span :style="textStyle">{{ item.text }}</span>
				</a>
			</template>
		</div>
	`
})