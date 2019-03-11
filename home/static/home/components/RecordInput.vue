var RecordInput = Vue.component('record-input', {
	props: {
		id: String,
		label: String,
		type: String,
		items: Array,
		currency: String,
		value: String,
	},
	template: '\
	<div class="col-12">\
		<template v-if="type === \'string\'">\
			<span class="label-input"><label :for="id">{{ label }}</label></span>\
			<span class="input-text">\
				<div class="input-group input-group-sm">\
					<input :id="id" type="text" class="form-control" :value="value" @input="$emit(\'input\', $event.target.value)">\
				</div>\
			</span>\
		</template>\
		<template v-else-if="type === \'currency\'">\
			<span class="label-input"><label :for="id">{{ label }}</label></span>\
			<span class="input-text">\
				<div class="input-group input-group-sm mb-3">\
				  <div class="input-group-prepend">\
				    <span class="input-group-text">{{ currency }}</span>\
				  </div>\
				  <input :id="id" type="text" class="form-control" :value="value" @input="$emit(\'input\', $event.target.value)">\
				</div>\
			</span>\
		</template>\
		<template v-else-if="type === \'dropdown\'">\
			<span class="label-input"><label :for="id">{{ label }}</label></span>\
			<span class="input-text">\
				<select class="custom-select custom-select-sm" :value="value" @input="$emit(\'input\', $event.target.value)">\
				  <option v-for="item in items">{{ item }}</option>\
				</select>\
			</span>\
		</template>\
	</div>\
	'
})