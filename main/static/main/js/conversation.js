window.onload = function() {
	var app = new Vue({
	  delimiters: ['[[', ']]'],
	  el: '#vue',
	  data: {
	    user1: '',
	    user2: '',
	    messages: '',
	    id: 0
	  },

	  mounted() {
	  	var url_string = window.location.href;
		var url = new URL(url_string);
		var id = url.searchParams.get("id");
		console.log(id);
		this.id = id;
	  }

	});
};