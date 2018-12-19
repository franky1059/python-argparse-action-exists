



def initialize_args(parser_obj = None):
	parser_obj.add_argument("-t2o1", "--tier2_option1",
						dest="tier2_option1",
						default="",
						type=str,
						help="Option execution for this tier")
						
	parser_obj.add_argument("-t2o2", "--tier2_option2",
						dest="tier2_option2",
						default="",
						type=str,
						help="Option execution for this tier")