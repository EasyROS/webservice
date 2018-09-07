{
	"targets":[
		{
			"target_name": "adapter",
			"sources": ["./src/adapter.cc"],
			"link_setting":{
				"libraries":[
					"-lm"
				],
				'library_dirs': [
					'./lib',
				],
			},
			'test': 0,
		}
	]
	
}
