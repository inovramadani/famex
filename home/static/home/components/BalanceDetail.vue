var BalanceDetail = Vue.component('balance-detail', {
	props: {
		item: String,
		currency: String,
		balance: Object,
	},
	template: '\
	<div class="balance">\
		<span class="balance-item">{{ capitalizeFirstLetter(item) }}</span>\
		<span class="currency-sign">{{ currency }}</span>\
		<span class="balance-value">{{ balance[item] }}</span>\
	</div>\
	',
})